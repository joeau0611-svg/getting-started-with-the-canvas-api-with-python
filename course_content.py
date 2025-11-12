"""Structured content definitions for the WorldEd Canvas course builder."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class PageDefinition:
    key: str
    title: str
    body: str
    front_page: bool = False


@dataclass(frozen=True)
class AssignmentDefinition:
    key: str
    name: str
    group: str
    submission_types: List[str]
    grading_type: str
    points: float
    instructions: str
    allowed_extensions: Optional[List[str]] = None


@dataclass(frozen=True)
class DiscussionDefinition:
    key: str
    title: str
    message: str


@dataclass(frozen=True)
class QuizQuestion:
    question_name: str
    question_text: str
    question_type: str
    points_possible: float
    answers: List[Dict[str, object]]


@dataclass(frozen=True)
class QuizDefinition:
    key: str
    name: str
    description: str
    quiz_type: str
    group: Optional[str]
    allowed_attempts: int
    hide_correct_answers: bool
    questions: List[QuizQuestion]

    @property
    def points(self) -> float:
        return sum(question.points_possible for question in self.questions)


@dataclass(frozen=True)
class ModuleItemDefinition:
    item_type: str
    reference: str
    completion_type: str


@dataclass(frozen=True)
class ModuleDefinition:
    name: str
    prerequisite: Optional[str]
    require_sequential: bool
    items: List[ModuleItemDefinition]


ASSIGNMENT_GROUPS = [
    {"name": "Unit Activity", "weight": 20},
    {"name": "LCC", "weight": 10},
    {"name": "Post-Test", "weight": 10},
    {"name": "Debate", "weight": 20},
    {"name": "Final Exam", "weight": 30},
    {"name": "Engagement", "weight": 10},
]

HOME_PAGE_HTML = """
<section aria-label="Hero" style="background:#0F172A;color:#fff;padding:28px;border-radius:16px;box-shadow:0 10px 24px rgba(0,0,0,.12);max-width:900px;margin:0 auto;font-family:system-ui,-apple-system,'Segoe UI',Inter,Arial">
  <h1 style="margin:0 0 6px;font-size:2rem;line-height:1.2">WorldEd Tutor &amp; Coordinator Training</h1>
  <p style="margin:0 0 10px;color:#93c5fd">Set Up • Grow • Reflect &amp; Empower</p>
  <p style="margin:0 0 10px">You’re the protagonist. Build lessons that work, finish Chapter 3, and earn <strong>WICE</strong> + your <strong>WorldEd Training Certificate</strong>.</p>
  <a href="/courses/{{COURSE_ID}}/modules" style="display:inline-block;background:#3B82F6;color:#fff;text-decoration:none;padding:.6rem .9rem;border-radius:10px">Start in Chapter 1: Set Up</a>
</section>

<div role="list" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;max-width:900px;margin:16px auto">
  <article role="listitem" style="background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:16px"><h2 style="margin:0 0 6px;color:#0F172A">Set Up</h2><p style="margin:0">Hook &amp; Heart — connect your why to student outcomes.</p></article>
  <article role="listitem" style="background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:16px"><h2 style="margin:0 0 6px;color:#0F172A">Grow</h2><p style="margin:0">Skill &amp; Structure — PPP + backward design; artefacts you can reuse.</p></article>
  <article role="listitem" style="background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:16px"><h2 style="margin:0 0 6px;color:#0F172A">Reflect &amp; Empower</h2><p style="margin:0">Leadership &amp; Recognition — portfolio, WICE, certificate.</p></article>
</div>

<aside aria-label="Callout" style="border-left:6px solid #3B82F6;background:#F1F5F9;padding:12px 14px;border-radius:8px;max-width:900px;margin:0 auto">
  <p style="margin:0"><strong>Why it works:</strong> quick wins, peer support, and visible progress keep you moving.</p>
</aside>

<section aria-label="LinkedIn" style="max-width:900px;margin:12px auto">
  <h3 style="color:#0F172A;margin:0 0 6px">Add WICE to LinkedIn (after Chapter 3)</h3>
  <ol style="margin:.4rem 0 0;padding-left:1.2rem">
    <li>Profile → <em>Add profile section</em> → <em>Licenses &amp; Certifications</em>.</li>
    <li><strong>Name:</strong> WorldEd Innovative &amp; Certified Educator (WICE)</li>
    <li><strong>Issuing organization:</strong> WorldEd</li>
    <li><strong>Issue date:</strong> month/year • <strong>Credential URL:</strong> paste your badge share link</li>
    <li><strong>Credential ID:</strong> badge ID (optional)</li>
  </ol>
</section>
""".strip()

MODULE_PAGES = [
    PageDefinition(
        key="module_1_intro",
        title="Start Here — Set Up",
        body="""
<section style="max-width:900px;margin:0 auto;color:#0F172A">
  <h2 style="margin:0 0 6px">Set Up: Hook &amp; Heart</h2>
  <p style="margin:0 0 6px">Begin with <strong>your why</strong>. Name the student outcome you want to move this term. Then meet your buddy.</p>
  <ol style="margin:0;padding-left:1.2rem">
    <li>Write your <em>one-sentence intention</em>.</li>
    <li>Complete the PPP Draft Check (practice).</li>
    <li>Post and connect in <em>Find a Buddy</em>.</li>
  </ol>

  <section style="max-width:900px;margin:12px 0 0">
    <h3 style="margin:0 0 6px;color:#0F172A">Before you move on</h3>
    <ul style="list-style: '✓ ';padding-left:1rem;margin:0">
      <li>I posted my <strong>intention</strong>.</li>
      <li>I completed the <strong>PPP Draft Check</strong>.</li>
      <li>I connected with a peer in <strong>Find a Buddy</strong>.</li>
    </ul>
  </section>

  <aside style="border-left:6px solid #3B82F6;background:#F1F5F9;padding:12px;border-radius:8px;margin-top:12px">
    <p style="margin:0">Nice work — this chapter unlocks your next <strong>badge</strong>. Keep going.</p>
  </aside>
</section>
""".strip(),
    ),
    PageDefinition(
        key="module_2_intro",
        title="Grow — Skill & Structure",
        body="""
<section aria-label="Grow intro" style="max-width:900px;margin:0 auto;font-family:system-ui,-apple-system,'Segoe UI',Inter,Arial;color:#0F172A">
  <h2 style="margin:0 0 6px">Grow: Skill &amp; Structure</h2>
  <p style="margin:0 0 10px">This is the hands-on chapter. You’ll build from clear, measurable goals, run PPP with confidence, and produce artefacts you can use tomorrow.</p>

  <aside style="border-left:6px solid #3B82F6;background:#F1F5F9;padding:12px;border-radius:8px;margin:12px 0">
    <p style="margin:0"><strong>Why this matters:</strong> clearer goals → tighter lessons → calmer classrooms → better results.</p>
  </aside>

  <ol style="margin:0;padding-left:1.1rem">
    <li><strong>LCC PPT Upload</strong> — deck with 2–3 numbered goals + speaker notes for checks.</li>
    <li><strong>LCC — Proctored</strong> — short, goal-alignment confirmation (no time limit; one attempt).</li>
    <li><strong>Unit Activity — Draft</strong> — claim, evidence, reasoning tied to your goals.</li>
    <li><strong>Debate Sources</strong> — mind map + two credible sources per side; peer counter-source.</li>
  </ol>

  <details style="margin-top:12px"><summary style="cursor:pointer;color:#3B82F6">Audio (1 min)</summary>
    <p>Grow is your build phase. You’ll set measurable goals, test alignment in a quick proctored check, and finish with drafts you can teach from tomorrow. Keep it simple, aligned, and student-driven.</p>
  </details>

  <section style="margin:12px 0 0">
    <h3 style="margin:0 0 6px">Before you move on</h3>
    <ul style="list-style:'✓ ';padding-left:1rem;margin:0">
      <li>I uploaded my deck with numbered goals and speaker notes.</li>
      <li>I completed the proctored LCC check.</li>
      <li>I submitted my Unit Activity draft and posted Debate sources.</li>
    </ul>
  </section>
</section>
""".strip(),
    ),
    PageDefinition(
        key="module_3_intro",
        title="Reflect & Empower — Leadership & Recognition",
        body="""
<section aria-label="Reflect & Empower" style="max-width:900px;margin:0 auto;font-family:system-ui,-apple-system,'Segoe UI',Inter,Arial;color:#0F172A">
  <h2 style="margin:0 0 6px">Reflect &amp; Empower</h2>
  <p style="margin:0 0 8px">This is the launch. Pull together your best work, prove impact, and step into leadership with <strong>WICE</strong> and your certificate.</p>

  <aside style="border-left:6px solid #3B82F6;background:#F1F5F9;padding:12px;border-radius:8px;margin:12px 0">
    <p style="margin:0"><strong>Why this matters:</strong> Evidence → recognition → culture. Your growth lifts your students and your team.</p>
  </aside>

  <ol style="margin:0;padding-left:1.1rem">
    <li><strong>Post Test</strong> — a quick check of what’s now automatic.</li>
    <li><strong>Unit Activity — Final</strong> — polished artefact with revisions and goal alignment.</li>
    <li><strong>Debate Portfolio — Final</strong> — mind map, point cards, outline, bibliography, rebuttal notes.</li>
    <li><strong>Final Exam</strong> — capstone knowledge check.</li>
    <li><strong>Engagement Log — Final</strong> — the habits that kept you moving.</li>
  </ol>

  <details style="margin-top:12px"><summary style="cursor:pointer;color:#3B82F6">Audio (1 min)</summary>
    <p>Welcome to your launch chapter. You’ll demonstrate growth, submit your best work, and earn WICE. Add your badge and certificate to LinkedIn and carry this standard back to your classroom and team.</p>
  </details>

  <section style="margin:12px 0 0">
    <h3 style="margin:0 0 6px">Before you finish</h3>
    <ul style="list-style:'✓ ';padding-left:1rem;margin:0">
      <li>I completed the <strong>Post Test</strong> and <strong>Final Exam</strong>.</li>
      <li>I submitted <strong>Unit Activity — Final</strong> and <strong>Debate Portfolio — Final</strong>.</li>
      <li>I posted my <strong>Engagement Log — Final</strong>.</li>
    </ul>
  </section>

  <section style="margin:12px 0 0">
    <h3 style="margin:0 0 6px">Recognition</h3>
    <p style="margin:0">On completion, Canvas Credentials automatically awards <strong>WICE</strong> and your <strong>WorldEd Training Certificate</strong>. Add both to LinkedIn.</p>
  </section>
</section>
""".strip(),
    ),
]

ASSIGNMENTS = [
    AssignmentDefinition(
        key="intention",
        name="My One Sentence Intention",
        group="Engagement",
        submission_types=["online_text_entry"],
        grading_type="complete_incomplete",
        points=0,
        instructions="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">My One Sentence Intention</h3>
  <p style=\"margin:0 0 8px\">Start with “I intend to…” and link your teaching to a concrete student outcome (≤25 words).</p>
  <p style=\"margin:0 0 8px\"><strong>Example:</strong> “I intend to raise weekly reading minutes from 10→20 for my Level 2 group.”</p>
  <aside style=\"border-left:6px solid #3B82F6;background:#F1F5F9;padding:10px;border-radius:8px\">
    <p style=\"margin:0\"><strong>Rubric focus:</strong> Clarity &amp; Impact — the intention is specific and tied to learner outcomes.</p>
  </aside>
</section>
""".strip(),
    ),
    AssignmentDefinition(
        key="mission_draft",
        name="Educator Mission — Draft",
        group="Engagement",
        submission_types=["online_text_entry"],
        grading_type="complete_incomplete",
        points=0,
        instructions="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">Educator Mission — Draft</h3>
  <p style=\"margin:0 0 8px\">200–300 words. State your mission, name one WorldEd value, and add one weekly habit that keeps you aligned. Keep it human and practical.</p>
  <ul>
    <li><strong>Mission clarity</strong> — explain the impact you drive.</li>
    <li><strong>Values alignment</strong> — connect to Student-Driven or Excellence.</li>
    <li><strong>Weekly habit</strong> — show how you’ll stay on track.</li>
  </ul>
</section>
""".strip(),
    ),
    AssignmentDefinition(
        key="lcc_upload",
        name="LCC PPT Upload",
        group="LCC",
        submission_types=["online_upload"],
        grading_type="points",
        points=0,
        instructions="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">LCC PPT Upload</h3>
  <p style=\"margin:0 0 8px\">Upload a two-lesson deck. Keep it simple, aligned, and teachable tomorrow.</p>
  <ul>
    <li><strong>Slide 1:</strong> List 2–3 numbered learning goals (Verb + Condition + Criterion).</li>
    <li><strong>Speaker notes:</strong> Show quick checks for understanding during <em>Practice</em>.</li>
    <li><strong>Format:</strong> PPT or PDF. Use clear fonts, high contrast, and alt text for images.</li>
  </ul>
  <aside style=\"border-left:6px solid #3B82F6;background:#F1F5F9;padding:10px;border-radius:8px\">
    <p style=\"margin:0\"><strong>Tip:</strong> Teach from goals. Alignment reduces prep time and keeps classes calm.</p>
  </aside>
</section>
""".strip(),
        allowed_extensions=["ppt", "pptx", "pdf"],
    ),
    AssignmentDefinition(
        key="unit_activity_draft",
        name="Unit Activity — Draft",
        group="Unit Activity",
        submission_types=["online_upload", "online_text_entry"],
        grading_type="points",
        points=0,
        instructions="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">Unit Activity — Draft</h3>
  <p style=\"margin:0 0 8px\">Three short paragraphs. Keep it tight and goal-linked.</p>
  <ol>
    <li><strong>Claim &amp; insight</strong> — what learners should take away.</li>
    <li><strong>Evidence</strong> — quotes/data/media with proper citation.</li>
    <li><strong>Reasoning &amp; connection</strong> — explain how your evidence supports the claim and ties to your numbered goals.</li>
  </ol>
  <p style=\"margin:8px 0 0\">Add one sentence on how you’ll check understanding during <em>Practice</em>.</p>
</section>
""".strip(),
    ),
    AssignmentDefinition(
        key="unit_activity_final",
        name="Unit Activity — Final",
        group="Unit Activity",
        submission_types=["online_upload", "online_text_entry"],
        grading_type="points",
        points=100,
        instructions="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">Unit Activity — Final</h3>
  <p style=\"margin:0 0 8px\">Submit your polished artefact. Show revision from feedback and make goal alignment explicit.</p>
  <ul>
    <li><strong>Include:</strong> final artefact, a brief revision note (what changed &amp; why), and a line linking to your numbered goals.</li>
    <li><strong>Citations:</strong> credit sources (MLA/APA) and mark direct quotes.</li>
    <li><strong>Accessibility:</strong> use clear structure, high contrast, alt text, and captions/transcripts for media.</li>
  </ul>
  <aside style=\"border-left:6px solid #3B82F6;background:#F1F5F9;padding:10px;border-radius:8px\">
    <p style=\"margin:0\"><strong>Tip:</strong> Make the goal–evidence–reasoning chain obvious. You’re showing impact.</p>
  </aside>
</section>
""".strip(),
    ),
    AssignmentDefinition(
        key="debate_portfolio_final",
        name="Debate Portfolio — Final",
        group="Debate",
        submission_types=["online_upload"],
        grading_type="points",
        points=100,
        instructions="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">Debate Portfolio — Final</h3>
  <p style=\"margin:0 0 8px\">Upload the full set:</p>
  <ul>
    <li>Mind map (image/PDF)</li>
    <li>Three point cards (pro arguments with citations)</li>
    <li>One-page outline (structure and timing)</li>
    <li>Bibliography (credible sources)</li>
    <li>Rebuttal notes (anticipated counters + responses)</li>
  </ul>
  <p style=\"margin:8px 0 0\"><strong>Deliver for leadership:</strong> this is a model you can coach others with.</p>
</section>
""".strip(),
    ),
    AssignmentDefinition(
        key="engagement_log_final",
        name="Engagement Log — Final",
        group="Engagement",
        submission_types=["online_upload", "online_text_entry"],
        grading_type="points",
        points=100,
        instructions="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">Engagement Log — Final</h3>
  <p style=\"margin:0 0 8px\">Show the habits that sustained your progress and community.</p>
  <ul>
    <li><strong>Mini-engagers:</strong> brief activities you used to keep learners active.</li>
    <li><strong>Peer feedback:</strong> who you supported/learned from and how it changed your artefact.</li>
    <li><strong>Checkpoints met:</strong> note key deadlines and what unblocked you.</li>
  </ul>
</section>
""".strip(),
    ),
]

DISCUSSIONS = [
    DiscussionDefinition(
        key="buddy",
        title="Find a Buddy",
        message="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">Find a Buddy</h3>
  <p style=\"margin:0 0 8px\">Post one clear ask and one concrete offer. Then reply to a peer with a next step you’ll take together within 7 days.</p>
  <aside style=\"border-left:6px solid #3B82F6;background:#F1F5F9;padding:10px;border-radius:8px\">
    <p style=\"margin:0\"><strong>Community matters:</strong> build together, reduce prep time, and learn faster from each other.</p>
  </aside>
</section>
""".strip(),
    ),
    DiscussionDefinition(
        key="debate_sources",
        title="Debate Sources",
        message="""
<section style=\"max-width:900px;margin:0 auto;color:#0F172A\">
  <h3 style=\"margin:0 0 6px\">Debate Sources</h3>
  <p style=\"margin:0 0 8px\">Post your mind map and your two strongest sources for <em>each</em> side.</p>
  <ul>
    <li>Explain in 1–2 sentences why each source is credible and useful.</li>
    <li>Reply to a peer with <strong>one counter-source</strong> and a two-sentence rationale.</li>
  </ul>
  <aside style=\"border-left:6px solid #3B82F6;background:#F1F5F9;padding:10px;border-radius:8px\">
    <p style=\"margin:0\"><strong>Community matters:</strong> build together, reduce prep time, and learn faster from each other.</p>
  </aside>
</section>
""".strip(),
    ),
]

PPP_DRAFT_CHECK_QUESTIONS = [
    QuizQuestion(
        question_name="PPP stage identification",
        question_text="Which PPP stage focuses on introducing new content for the first time?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Present", "answer_weight": 100},
            {"answer_text": "Practice", "answer_weight": 0},
            {"answer_text": "Produce", "answer_weight": 0},
            {"answer_text": "Assess", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Practice check",
        question_text="During the Practice stage, which move best checks for understanding quickly?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Assign the final project", "answer_weight": 0},
            {"answer_text": "Give a two-question exit ticket", "answer_weight": 100},
            {"answer_text": "Introduce next week’s topic", "answer_weight": 0},
            {"answer_text": "Let students work independently without feedback", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Produce evidence",
        question_text="Which artefact best represents the Produce stage?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Students annotate a model paragraph with the teacher", "answer_weight": 0},
            {"answer_text": "Students complete guided practice with immediate feedback", "answer_weight": 0},
            {"answer_text": "Students create their own paragraph using the target structure", "answer_weight": 100},
            {"answer_text": "Students complete a diagnostic survey", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Alt text",
        question_text="Which alt text best describes the PPP cycle icon used in course materials?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "PPP graphic", "answer_weight": 0},
            {"answer_text": "Diagram showing Present → Practice → Produce arrows", "answer_weight": 100},
            {"answer_text": "Colorful picture", "answer_weight": 0},
            {"answer_text": "Teaching symbol", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Backward design",
        question_text="What is the first step in backward design when planning a PPP lesson?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Plan the activities", "answer_weight": 0},
            {"answer_text": "Identify desired student outcomes", "answer_weight": 100},
            {"answer_text": "Write homework instructions", "answer_weight": 0},
            {"answer_text": "Design the final exam", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Integrity scenario",
        question_text="Which action demonstrates academic honesty during Produce?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Copying an online paragraph without credit", "answer_weight": 0},
            {"answer_text": "Quoting a source with citation", "answer_weight": 100},
            {"answer_text": "Sharing someone else’s artefact as your own", "answer_weight": 0},
            {"answer_text": "Skipping the bibliography", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Transition move",
        question_text="What transition keeps momentum between Practice and Produce?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Restating the unit overview", "answer_weight": 0},
            {"answer_text": "Sharing feedback from the Practice exit ticket", "answer_weight": 100},
            {"answer_text": "Introducing a new unrelated topic", "answer_weight": 0},
            {"answer_text": "Collecting homework", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Evidence alignment",
        question_text="Which quick-check matches the goal “Identify three article uses in a short text with 80% accuracy”?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Ask students to list their favourite books", "answer_weight": 0},
            {"answer_text": "Have students highlight three article uses in a paragraph", "answer_weight": 100},
            {"answer_text": "Request a reflection on learning", "answer_weight": 0},
            {"answer_text": "Give extra homework for practice", "answer_weight": 0},
        ],
    ),
]

LCC_PROCTORED_QUESTIONS = [
    QuizQuestion(
        question_name="Measurable goal",
        question_text="Which learning goal follows the Verb + Condition + Criterion model?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Students will understand articles", "answer_weight": 0},
            {"answer_text": "Students will practice speaking", "answer_weight": 0},
            {"answer_text": "Identify three article uses in a 150-word text with 80% accuracy", "answer_weight": 100},
            {"answer_text": "Students will be confident", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Backward design order",
        question_text="Place the backward design steps in order.",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Identify desired results → Determine evidence → Plan learning experiences", "answer_weight": 100},
            {"answer_text": "Plan learning experiences → Identify desired results → Determine evidence", "answer_weight": 0},
            {"answer_text": "Determine evidence → Plan learning experiences → Identify desired results", "answer_weight": 0},
            {"answer_text": "Plan learning experiences → Determine evidence → Identify desired results", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Practice check",
        question_text="What should appear in speaker notes during Practice?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "A list of homework assignments", "answer_weight": 0},
            {"answer_text": "Specific prompts for checking understanding", "answer_weight": 100},
            {"answer_text": "A script for the final presentation", "answer_weight": 0},
            {"answer_text": "Personal reminders for the facilitator", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Alignment",
        question_text="Which activity best aligns with the goal “Cite two credible sources in a paragraph”?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Have students brainstorm discussion norms", "answer_weight": 0},
            {"answer_text": "Draft a paragraph that includes two citations", "answer_weight": 100},
            {"answer_text": "Memorise vocabulary", "answer_weight": 0},
            {"answer_text": "Create a poster", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Evidence of learning",
        question_text="Which option is the strongest evidence of learning for the Practice stage?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Students submit a blank worksheet", "answer_weight": 0},
            {"answer_text": "Students complete guided practice with annotated answers", "answer_weight": 100},
            {"answer_text": "Students share their feelings", "answer_weight": 0},
            {"answer_text": "Students read silently", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Accessibility move",
        question_text="How do you support accessibility in your deck?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Use 10pt fonts", "answer_weight": 0},
            {"answer_text": "Provide alt text for images and high contrast colours", "answer_weight": 100},
            {"answer_text": "Add decorative animations", "answer_weight": 0},
            {"answer_text": "Rely on color only for meaning", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Integrity",
        question_text="Which option protects academic honesty when using shared artefacts?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Reuse a colleague’s slide deck without credit", "answer_weight": 0},
            {"answer_text": "Credit the original creator and adapt for your learners", "answer_weight": 100},
            {"answer_text": "Share student data without permission", "answer_weight": 0},
            {"answer_text": "Omit citations to save time", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Goal clarity",
        question_text="Which statement best communicates measurable success criteria?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Students will improve quickly", "answer_weight": 0},
            {"answer_text": "Students will be excited", "answer_weight": 0},
            {"answer_text": "Students answer four comprehension questions with 90% accuracy", "answer_weight": 100},
            {"answer_text": "Students enjoy class", "answer_weight": 0},
        ],
    ),
]

POST_TEST_QUESTIONS = [
    QuizQuestion(
        question_name="PPP identify",
        question_text="A teacher models sentence frames while learners repeat. Which PPP stage is represented?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Present", "answer_weight": 100},
            {"answer_text": "Practice", "answer_weight": 0},
            {"answer_text": "Produce", "answer_weight": 0},
            {"answer_text": "Assess", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Backward design order",
        question_text="Arrange backward design in order: plan learning, identify results, determine evidence.",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Identify results → Determine evidence → Plan learning", "answer_weight": 100},
            {"answer_text": "Plan learning → Identify results → Determine evidence", "answer_weight": 0},
            {"answer_text": "Determine evidence → Plan learning → Identify results", "answer_weight": 0},
            {"answer_text": "Plan learning → Determine evidence → Identify results", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Exit ticket",
        question_text="Which exit ticket best matches a Practice goal on citing evidence?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Ask students to draw a comic", "answer_weight": 0},
            {"answer_text": "Have students cite two pieces of evidence in three sentences", "answer_weight": 100},
            {"answer_text": "Collect homework", "answer_weight": 0},
            {"answer_text": "Check attendance", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Evidence quality",
        question_text="Which source is most credible for a debate portfolio?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Anonymous blog post", "answer_weight": 0},
            {"answer_text": "Peer-reviewed journal article", "answer_weight": 100},
            {"answer_text": "Personal anecdote", "answer_weight": 0},
            {"answer_text": "Outdated statistics", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Accessibility",
        question_text="Which move supports UDL in slides?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Using color alone to show meaning", "answer_weight": 0},
            {"answer_text": "Adding captions to embedded videos", "answer_weight": 100},
            {"answer_text": "Using tiny fonts", "answer_weight": 0},
            {"answer_text": "Removing contrast", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Integrity",
        question_text="Which action models academic honesty?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Fabricating survey results", "answer_weight": 0},
            {"answer_text": "Paraphrasing with citation", "answer_weight": 100},
            {"answer_text": "Sharing student data publicly", "answer_weight": 0},
            {"answer_text": "Submitting uncredited images", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Goal alignment",
        question_text="Which activity best aligns to the goal “Write a persuasive paragraph with two cited sources”?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Brainstorm persuasive topics only", "answer_weight": 0},
            {"answer_text": "Draft a persuasive paragraph including two citations", "answer_weight": 100},
            {"answer_text": "Practice handwriting", "answer_weight": 0},
            {"answer_text": "Memorise vocabulary", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Feedback loop",
        question_text="After giving feedback on drafts, what closes the formative loop?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Assign more readings", "answer_weight": 0},
            {"answer_text": "Plan a revision activity using the feedback", "answer_weight": 100},
            {"answer_text": "Ignore the errors", "answer_weight": 0},
            {"answer_text": "Move to a new topic immediately", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Discussion move",
        question_text="Which reply deepens a peer discussion in Debate Sources?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Thanks!", "answer_weight": 0},
            {"answer_text": "Here’s a counter-source with two-sentence rationale", "answer_weight": 100},
            {"answer_text": "I disagree", "answer_weight": 0},
            {"answer_text": "Cool idea", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Portfolio evidence",
        question_text="Which artefact belongs in the Debate Portfolio?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Mind map + point cards + rebuttal notes", "answer_weight": 100},
            {"answer_text": "Class attendance list", "answer_weight": 0},
            {"answer_text": "Personal journal", "answer_weight": 0},
            {"answer_text": "Homework checklist", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Engagement habit",
        question_text="Which habit supports sustained engagement?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Documenting mini-engagers and peer feedback", "answer_weight": 100},
            {"answer_text": "Skipping reflection", "answer_weight": 0},
            {"answer_text": "Ignoring deadlines", "answer_weight": 0},
            {"answer_text": "Working alone", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Leadership",
        question_text="How do you extend impact after earning WICE?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Keep resources to yourself", "answer_weight": 0},
            {"answer_text": "Share artefacts in coordinator huddles", "answer_weight": 100},
            {"answer_text": "Avoid mentoring others", "answer_weight": 0},
            {"answer_text": "Skip celebrations", "answer_weight": 0},
        ],
    ),
]

FINAL_EXAM_QUESTIONS = [
    QuizQuestion(
        question_name="PPP scenario 1",
        question_text="Learners analyse mentor texts before drafting independently. Which PPP stage?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Present", "answer_weight": 0},
            {"answer_text": "Practice", "answer_weight": 0},
            {"answer_text": "Produce", "answer_weight": 100},
            {"answer_text": "Assess", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="PPP scenario 2",
        question_text="The facilitator demonstrates a think-aloud while highlighting context clues. Which stage?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Present", "answer_weight": 100},
            {"answer_text": "Practice", "answer_weight": 0},
            {"answer_text": "Produce", "answer_weight": 0},
            {"answer_text": "Assess", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="PPP scenario 3",
        question_text="Students complete guided partner work with immediate feedback. Which stage?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Present", "answer_weight": 0},
            {"answer_text": "Practice", "answer_weight": 100},
            {"answer_text": "Produce", "answer_weight": 0},
            {"answer_text": "Assess", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Backward design alignment",
        question_text="Which assessment best matches the goal “Summarise a news article in 5 sentences highlighting main idea and two supporting details”?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Learners design a poster", "answer_weight": 0},
            {"answer_text": "Learners write a five-sentence summary with two details", "answer_weight": 100},
            {"answer_text": "Learners memorise vocabulary", "answer_weight": 0},
            {"answer_text": "Learners complete a multiple-choice quiz", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Exit ticket alignment",
        question_text="Which exit ticket aligns to “Differentiate between fact and opinion in three statements”?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Ask for a reflection on effort", "answer_weight": 0},
            {"answer_text": "Have learners label three statements as fact or opinion", "answer_weight": 100},
            {"answer_text": "Collect homework", "answer_weight": 0},
            {"answer_text": "Assign extra credit", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Feedback plan",
        question_text="After reviewing exit tickets showing misconceptions, what is the next move?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Move on without changes", "answer_weight": 0},
            {"answer_text": "Design a reteach mini-lesson targeting the misconception", "answer_weight": 100},
            {"answer_text": "Assign extra homework without feedback", "answer_weight": 0},
            {"answer_text": "Skip Practice next time", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Accessibility captions",
        question_text="What accompanies every embedded video in this course?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Animated GIFs", "answer_weight": 0},
            {"answer_text": "Short transcript in a details block", "answer_weight": 100},
            {"answer_text": "Download requirement", "answer_weight": 0},
            {"answer_text": "No support", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Alt text practice",
        question_text="Which alt text best supports accessibility for a chart showing progress over time?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "chart", "answer_weight": 0},
            {"answer_text": "Line chart showing attendance rising from 60% to 90% across 8 weeks", "answer_weight": 100},
            {"answer_text": "Picture of data", "answer_weight": 0},
            {"answer_text": "Decorative", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Integrity citations",
        question_text="Which citation practice keeps debate work honest?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "List sources without URLs", "answer_weight": 0},
            {"answer_text": "Provide full citation details for every quote", "answer_weight": 100},
            {"answer_text": "Copy statistics without credit", "answer_weight": 0},
            {"answer_text": "Use Wikipedia as the only source", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Goal writing",
        question_text="Choose the goal that meets the house style.",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Learners will understand essays", "answer_weight": 0},
            {"answer_text": "Learners write a three-paragraph essay with thesis, two supports, and citations", "answer_weight": 100},
            {"answer_text": "Learners learn about essays", "answer_weight": 0},
            {"answer_text": "Learners enjoy writing", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Mentor leadership",
        question_text="How can coordinators extend Chapter 3 learning?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Host Friday micro-workshops featuring tutor artefacts", "answer_weight": 100},
            {"answer_text": "Keep practices private", "answer_weight": 0},
            {"answer_text": "Avoid referencing course language", "answer_weight": 0},
            {"answer_text": "Discourage peer mentoring", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Portfolio coaching",
        question_text="Which element makes a debate portfolio coachable?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Clear outline with timing and roles", "answer_weight": 100},
            {"answer_text": "Random notes", "answer_weight": 0},
            {"answer_text": "Uncited quotes", "answer_weight": 0},
            {"answer_text": "Single point card", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Engagement tracking",
        question_text="What belongs in the Engagement Log?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Notes on mini-engagers, peer feedback, and checkpoints", "answer_weight": 100},
            {"answer_text": "Personal diary", "answer_weight": 0},
            {"answer_text": "Budget data", "answer_weight": 0},
            {"answer_text": "Attendance only", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="WICE readiness",
        question_text="Which combination earns WICE?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Final artefacts submitted, quizzes ≥70%, engagement log submitted", "answer_weight": 100},
            {"answer_text": "Only the final exam completed", "answer_weight": 0},
            {"answer_text": "Mission statement only", "answer_weight": 0},
            {"answer_text": "Buddy post only", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Feedback culture",
        question_text="How do you model feedback culture post-course?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Share exemplars and invite peer review", "answer_weight": 100},
            {"answer_text": "Avoid discussing lessons", "answer_weight": 0},
            {"answer_text": "Limit feedback to coordinators", "answer_weight": 0},
            {"answer_text": "Skip celebrating wins", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Scenario formative",
        question_text="Learners struggle with a concept during Practice. What is the first move?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Collect data and plan a reteach", "answer_weight": 100},
            {"answer_text": "Proceed to Produce", "answer_weight": 0},
            {"answer_text": "Assign unrelated homework", "answer_weight": 0},
            {"answer_text": "Skip feedback", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Scenario SEL",
        question_text="Which move adds an SEL check without derailing pacing?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Opening mood meter with 60-second pair share", "answer_weight": 100},
            {"answer_text": "Removing Practice altogether", "answer_weight": 0},
            {"answer_text": "Extending Produce by 40 minutes", "answer_weight": 0},
            {"answer_text": "Skipping intention setting", "answer_weight": 0},
        ],
    ),
    QuizQuestion(
        question_name="Scenario leadership",
        question_text="How do you coach a peer using Module 2 language?",
        question_type="multiple_choice_question",
        points_possible=1,
        answers=[
            {"answer_text": "Reference PPP stages and numbered goals during feedback", "answer_weight": 100},
            {"answer_text": "Offer vague encouragement only", "answer_weight": 0},
            {"answer_text": "Avoid mentioning goals", "answer_weight": 0},
            {"answer_text": "Share unrelated anecdotes", "answer_weight": 0},
        ],
    ),
]

QUIZZES = [
    QuizDefinition(
        key="ppp_draft_check",
        name="PPP Draft Check",
        description="This is rehearsal. Try, check, and try again. Your goal: name the PPP stage with confidence and spot quick checks for understanding.",
        quiz_type="practice_quiz",
        group="Engagement",
        allowed_attempts=-1,
        hide_correct_answers=True,
        questions=PPP_DRAFT_CHECK_QUESTIONS,
    ),
    QuizDefinition(
        key="lcc_proctored",
        name="LCC — Proctored",
        description="Teach from goals. This quick check confirms that your goals are measurable and instruction is aligned.",
        quiz_type="graded_quiz",
        group="LCC",
        allowed_attempts=1,
        hide_correct_answers=True,
        questions=LCC_PROCTORED_QUESTIONS,
    ),
    QuizDefinition(
        key="post_test",
        name="Post Test",
        description="A snapshot of what’s now automatic. Read clearly; no time pressure.",
        quiz_type="graded_quiz",
        group="Post-Test",
        allowed_attempts=1,
        hide_correct_answers=True,
        questions=POST_TEST_QUESTIONS,
    ),
    QuizDefinition(
        key="final_exam",
        name="Final Exam",
        description="Your capstone check. Read carefully and apply the framework.",
        quiz_type="graded_quiz",
        group="Final Exam",
        allowed_attempts=1,
        hide_correct_answers=True,
        questions=FINAL_EXAM_QUESTIONS,
    ),
]

MODULES = [
    ModuleDefinition(
        name="Module 1 — Chapter 1: Set Up (The First Step)",
        prerequisite=None,
        require_sequential=True,
        items=[
            ModuleItemDefinition("page", "module_1_intro", "must_view"),
            ModuleItemDefinition("assignment", "intention", "must_submit"),
            ModuleItemDefinition("quiz", "ppp_draft_check", "must_submit"),
            ModuleItemDefinition("assignment", "mission_draft", "must_submit"),
            ModuleItemDefinition("discussion", "buddy", "must_contribute"),
        ],
    ),
    ModuleDefinition(
        name="Module 2 — Chapter 2: Grow (Skill & Structure)",
        prerequisite="Module 1 — Chapter 1: Set Up (The First Step)",
        require_sequential=True,
        items=[
            ModuleItemDefinition("page", "module_2_intro", "must_view"),
            ModuleItemDefinition("assignment", "lcc_upload", "must_submit"),
            ModuleItemDefinition("quiz", "lcc_proctored", "must_submit"),
            ModuleItemDefinition("assignment", "unit_activity_draft", "must_submit"),
            ModuleItemDefinition("discussion", "debate_sources", "must_contribute"),
        ],
    ),
    ModuleDefinition(
        name="Module 3 — Chapter 3: Reflect & Empower",
        prerequisite="Module 2 — Chapter 2: Grow (Skill & Structure)",
        require_sequential=True,
        items=[
            ModuleItemDefinition("page", "module_3_intro", "must_view"),
            ModuleItemDefinition("quiz", "post_test", "must_submit"),
            ModuleItemDefinition("assignment", "unit_activity_final", "must_submit"),
            ModuleItemDefinition("assignment", "debate_portfolio_final", "must_submit"),
            ModuleItemDefinition("quiz", "final_exam", "must_submit"),
            ModuleItemDefinition("assignment", "engagement_log_final", "must_submit"),
        ],
    ),
]

PAGE_LOOKUP: Dict[str, PageDefinition] = {page.key: page for page in MODULE_PAGES}
ASSIGNMENT_LOOKUP: Dict[str, AssignmentDefinition] = {assignment.key: assignment for assignment in ASSIGNMENTS}
DISCUSSION_LOOKUP: Dict[str, DiscussionDefinition] = {discussion.key: discussion for discussion in DISCUSSIONS}
QUIZ_LOOKUP: Dict[str, QuizDefinition] = {quiz.key: quiz for quiz in QUIZZES}

