"""Provision the WorldEd Tutor & Coordinator Training Canvas course."""

from __future__ import annotations

import argparse
import logging
import os
from typing import Dict, Iterable

import dotenv
from canvasapi import Canvas
from canvasapi.course import Course
from canvasapi.module import Module

from course_content import (
    ASSIGNMENT_GROUPS,
    ASSIGNMENT_LOOKUP,
    ASSIGNMENTS,
    DISCUSSION_LOOKUP,
    DISCUSSIONS,
    HOME_PAGE_HTML,
    MODULES,
    MODULE_PAGES,
    QUIZ_LOOKUP,
    QUIZZES,
)

LOGGER = logging.getLogger(__name__)


def load_environment() -> None:
    dotenv.load_dotenv(dotenv.find_dotenv())


def configure_logging(verbose: bool) -> None:
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO, format="%(levelname)s %(message)s")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create or update the WorldEd Canvas course structure.")
    parser.add_argument("course_id", type=int, nargs="?", help="Canvas course ID to configure")
    parser.add_argument("--base-url", dest="base_url", help="Canvas base URL (defaults to CANVAS_BASE_URL)")
    parser.add_argument("--token", dest="token", help="Canvas API token (defaults to CANVAS_API_TOKEN)")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def find_by_name(collection: Iterable, name: str):
    for item in collection:
        if getattr(item, "name", None) == name:
            return item
    return None


def ensure_assignment_group(course: Course, name: str, weight: float) -> int:
    group = find_by_name(course.get_assignment_groups(), name)
    if group:
        if getattr(group, "group_weight", None) != weight:
            LOGGER.info("Updating assignment group weight for %s", name)
            group.edit(assignment_group={"group_weight": weight})
        return group.id

    LOGGER.info("Creating assignment group %s", name)
    created = course.create_assignment_group(assignment_group={"name": name, "group_weight": weight})
    return created.id


def ensure_page(course: Course, title: str, body: str, front_page: bool = False):
    existing = None
    for page in course.get_pages():
        if page.title == title:
            existing = page
            break

    payload = {"title": title, "body": body, "published": True}

    if existing:
        LOGGER.info("Updating page %s", title)
        page_obj = existing.edit(wiki_page=payload)
    else:
        LOGGER.info("Creating page %s", title)
        page_obj = course.create_page(wiki_page=payload)

    if front_page:
        LOGGER.info("Setting %s as front page", title)
        page_obj.edit(wiki_page={"front_page": True})

    return page_obj


def ensure_assignment(course: Course, assignment_def, group_id: int) -> int:
    assignment = find_by_name(course.get_assignments(), assignment_def.name)

    payload = {
        "name": assignment_def.name,
        "assignment_group_id": group_id,
        "submission_types": assignment_def.submission_types,
        "grading_type": assignment_def.grading_type,
        "points_possible": assignment_def.points,
        "description": assignment_def.instructions,
        "published": True,
    }

    if assignment_def.allowed_extensions:
        payload["allowed_extensions"] = assignment_def.allowed_extensions

    if assignment:
        LOGGER.info("Updating assignment %s", assignment_def.name)
        assignment.edit(assignment=payload)
        return assignment.id

    LOGGER.info("Creating assignment %s", assignment_def.name)
    created = course.create_assignment(assignment=payload)
    return created.id


def ensure_discussion(course: Course, discussion_def) -> int:
    discussion = find_by_name(course.get_discussion_topics(), discussion_def.title)
    payload = {
        "title": discussion_def.title,
        "message": discussion_def.message,
        "published": True,
        "discussion_type": "threaded",
        "require_initial_post": True,
    }
    if discussion:
        LOGGER.info("Updating discussion %s", discussion_def.title)
        discussion.edit(topic=payload)
        return discussion.id

    LOGGER.info("Creating discussion %s", discussion_def.title)
    created = course.create_discussion_topic(**payload)
    return created.id


def ensure_quiz(course: Course, quiz_def, group_id: int | None) -> int:
    quiz = find_by_name(course.get_quizzes(), quiz_def.name)

    payload = {
        "title": quiz_def.name,
        "description": quiz_def.description,
        "quiz_type": quiz_def.quiz_type,
        "allowed_attempts": quiz_def.allowed_attempts,
        "published": True,
        "points_possible": quiz_def.points,
        "show_correct_answers": not quiz_def.hide_correct_answers,
    }

    if group_id is not None:
        payload["assignment_group_id"] = group_id

    if quiz:
        LOGGER.info("Updating quiz %s", quiz_def.name)
        quiz.edit(quiz=payload)
        sync_quiz_questions(quiz, quiz_def)
        return quiz.id

    LOGGER.info("Creating quiz %s", quiz_def.name)
    created = course.create_quiz(quiz=payload)
    sync_quiz_questions(created, quiz_def)
    return created.id


def sync_quiz_questions(quiz, quiz_def) -> None:
    for question in quiz.get_questions():
        question.delete()
    for definition in quiz_def.questions:
        quiz.create_question(
            question={
                "question_name": definition.question_name,
                "question_text": definition.question_text,
                "question_type": definition.question_type,
                "points_possible": definition.points_possible,
                "answers": definition.answers,
            }
        )


def ensure_module(course: Course, module_def, resources: Dict[str, Dict[str, object]], module_lookup: Dict[str, Module]) -> Module:
    module = find_by_name(course.get_modules(), module_def.name)

    if module:
        LOGGER.info("Updating module shell %s", module_def.name)
    else:
        LOGGER.info("Creating module shell %s", module_def.name)
        module = course.create_module(module={"name": module_def.name, "published": True})

    update_payload = {"require_sequential_progress": module_def.require_sequential}
    if module_def.prerequisite:
        prereq = module_lookup[module_def.prerequisite]
        update_payload["prerequisite_module_ids"] = [prereq.id]

    module.edit_module(module=update_payload)

    for item in module.get_module_items():
        item.delete()

    for item_def in module_def.items:
        resource = resources[item_def.item_type][item_def.reference]
        payload = {"type": resource["type"], "published": True}
        if resource["type"] == "Page":
            payload["page_url"] = resource["url"]
        else:
            payload["content_id"] = resource["id"]
        if item_def.completion_type:
            payload["completion_requirement"] = {"type": item_def.completion_type}
        module.create_module_item(payload)

    module_lookup[module_def.name] = module
    return module


def build_course(course: Course) -> None:
    LOGGER.info("Building assignment groups")
    group_ids = {}
    for group in ASSIGNMENT_GROUPS:
        group_ids[group["name"]] = ensure_assignment_group(course, group["name"], group["weight"])

    LOGGER.info("Creating pages")
    ensure_page(course, "Home", HOME_PAGE_HTML, front_page=True)
    page_resources = {
        page.key: ensure_page(course, page.title, page.body) for page in MODULE_PAGES
    }

    LOGGER.info("Creating assignments")
    assignment_resources = {}
    for assignment in ASSIGNMENTS:
        assignment_resources[assignment.key] = ensure_assignment(
            course, assignment, group_ids[assignment.group]
        )

    LOGGER.info("Creating discussions")
    discussion_resources = {
        discussion.key: ensure_discussion(course, discussion) for discussion in DISCUSSIONS
    }

    LOGGER.info("Creating quizzes")
    quiz_resources = {}
    for quiz in QUIZZES:
        group_id = group_ids.get(quiz.group) if quiz.group else None
        quiz_resources[quiz.key] = ensure_quiz(course, quiz, group_id)

    resources = {
        "page": {key: {"type": "Page", "title": page.title, "url": page.url} for key, page in page_resources.items()},
        "assignment": {
            key: {"type": "Assignment", "title": ASSIGNMENT_LOOKUP[key].name, "id": assignment_id}
            for key, assignment_id in assignment_resources.items()
        },
        "discussion": {
            key: {"type": "Discussion", "title": DISCUSSION_LOOKUP[key].title, "id": discussion_id}
            for key, discussion_id in discussion_resources.items()
        },
        "quiz": {
            key: {"type": "Quiz", "title": QUIZ_LOOKUP[key].name, "id": quiz_id}
            for key, quiz_id in quiz_resources.items()
        },
    }

    module_lookup: Dict[str, Module] = {}
    LOGGER.info("Creating modules")
    for module_def in MODULES:
        ensure_module(course, module_def, resources, module_lookup)

    LOGGER.info("Course build completed")


def main() -> None:
    load_environment()
    args = parse_args()
    configure_logging(args.verbose)

    base_url = args.base_url or os.environ.get("CANVAS_BASE_URL")
    token = args.token or os.environ.get("CANVAS_API_TOKEN")
    course_id = args.course_id or os.environ.get("CANVAS_COURSE_ID")

    if not base_url or not token or not course_id:
        raise SystemExit(
            "Canvas base URL, API token, and course ID must be provided via arguments or environment variables."
        )

    if isinstance(course_id, str):
        try:
            course_id = int(course_id)
        except ValueError as err:
            raise SystemExit("CANVAS_COURSE_ID must be an integer") from err

    canvas = Canvas(base_url, token)
    course = canvas.get_course(course_id)
    build_course(course)


if __name__ == "__main__":
    main()

