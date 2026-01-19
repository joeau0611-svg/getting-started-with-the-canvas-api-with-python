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
<p>WorldEd Tutor &amp; Coordinator Training &ndash; Full Course</p>
<div style="max-width: 960px; margin: 0 auto; padding: 0 1rem 2.5rem 1rem;"><header id="top" style="background: linear-gradient(135deg,#0b3b6f,#1a4f8b); color: #ffffff; padding: 2rem 1.5rem 1.75rem 1.5rem; border-radius: 0 0 14px 14px; margin: 0 -1rem 1.75rem -1rem;">
<div style="font-size: 0.8rem; color: rgba(255,255,255,0.78); margin-bottom: 0.35rem;"><span style="font-size: 24pt;"><span style="text-decoration: underline; color: #ffffff;"><strong>WorldEd School: </strong></span>Tutor &amp; Coordinator Training</span></div>
<p style="margin: 0.25rem 0;"><strong><span style="text-decoration: underline;"><span style="font-size: 18pt;">Your path. Their diploma. Our support.</span></span></strong></p>
<p style="margin: 0.25rem 0;">You&rsquo;re here because your students are doing something big:</p>
<p style="margin: 0.25rem 0;">earning an International high school diploma alongside their local studies,</p>
<p style="margin: 0.25rem 0;">without leaving their families, schools, or lives behind.</p>
<p style="margin: 0.25rem 0;">&nbsp;</p>
<p style="margin: 0.25rem 0;">Between the platform and the student, there&rsquo;s you.</p>
<p style="margin: 0.25rem 0;">You are the bridge between your students and their International dual diploma,</p>
<p style="margin: 0.25rem 0;">between your school and a new curriculum,</p>
<p style="margin: 0.25rem 0;">between today&rsquo;s lesson and tomorrow&rsquo;s opportunities.</p>
<p style="margin: 0.25rem 0;">&nbsp;</p>
<p style="margin: 0.25rem 0;">This training walks with you while you build that bridge.</p>
<p style="margin: 0.25rem 0;">No one expects you to know everything already. We&rsquo;ll take it one clear step at a time.&nbsp;</p>
<p style="margin: 0.25rem 0;"><span style="font-size: 14pt;"><strong><span style="color: #c71f23;">Insert Youtube video.&nbsp;</span></strong></span></p>
<div style="margin-top: 0.75rem; display: flex; flex-wrap: wrap; gap: 0.5rem; font-size: 0.8rem;"><span style="border-radius: 999px; border: 1px solid rgba(255,255,255,0.4); padding: 0.25rem 0.75rem; background: rgba(0,0,0,0.1); white-space: nowrap;">Self-paced</span> <span style="border-radius: 999px; border: 1px solid rgba(255,255,255,0.4); padding: 0.25rem 0.75rem; background: rgba(0,0,0,0.1); white-space: nowrap;">PPP &amp; Backward Design</span> <span style="border-radius: 999px; border: 1px solid rgba(255,255,255,0.4); padding: 0.25rem 0.75rem; background: rgba(0,0,0,0.1); white-space: nowrap;">LCC, Unit Activities, Debates</span> <span style="border-radius: 999px; border: 1px solid rgba(255,255,255,0.4); padding: 0.25rem 0.75rem; background: rgba(0,0,0,0.1); white-space: nowrap;">Set Up &middot; Grow &middot; Empower &middot; WICE</span></div>
</header>
<section style="margin: 0 0 1.5rem 0; padding: 0.75rem 1rem; border-radius: 10px; background: #fffaf0; border: 1px solid #f6e05e; font-size: 0.92rem;"><strong>Already on the platform?</strong> Jump straight to confirm or update your reason for teaching (enrolment &amp; platform setup): <a style="color: #2b6cb0; text-decoration: none;" href="#we-1-6">Go to &ldquo;Why I currently teach&rdquo; &rarr;</a></section>
<section id="course-roadmap" style="padding: 1rem 1rem 1.1rem 1rem; border-radius: 12px; background: #e2edff; border: 1px solid #b3c7f5; margin-bottom: 1.75rem;">
<h2 style="margin: 0 0 0.75rem 0; font-size: 1.15rem; color: #1a4f8b;"><span style="font-size: 18pt;">Course Road Map: Jump to any section</span></h2>
<ul style="margin: 0.25rem 0 0.35rem 0; padding-left: 1.1rem; font-size: 0.92rem;">
<li><a style="color: #2b6cb0; text-decoration: none;" href="#home-overview">Home &ndash; What this journey offers you</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#home-language">Home &ndash; Key terms &amp; language</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#home-recognition">Home &ndash; How your work is recognised</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#home-start-why">Home &ndash; Start with your &ldquo;why&rdquo;</a></li>
</ul>
<ul style="margin: 0.25rem 0 0.35rem 0; padding-left: 1.1rem; font-size: 0.92rem;">
<li><span style="font-size: 14pt;"><strong><a style="color: #2b6cb0; text-decoration: none;" href="#chapter-1">Chapter 1 &ndash; Setting Up</a></strong></span>
<ul style="margin: 0.25rem 0 0.35rem 0; padding-left: 1.1rem;">
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-1">1.1 The question that started WorldEd</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-2">1.2 Mission, vision, where you fit</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-3">1.3 Standards without the jargon</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-4">1.4 PPP &amp; quick win</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-5">1.5 LCC &ndash; what it is and why it helps</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-6">1.6 Assignment &ndash; Why I currently teach</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-7">1.7 Assignment &ndash; PPP Rebuild</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-8">1.8 Assignment &ndash; My Educator Mission</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-9">1.9 Discussion &ndash; Buddy check-in</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-1-10">1.10 Chapter 1 wrap-up</a></li>
</ul>
</li>
</ul>
<ul style="margin: 0.25rem 0 0.35rem 0; padding-left: 1.1rem; font-size: 0.92rem;">
<li><span style="font-size: 14pt;"><strong><a style="color: #2b6cb0; text-decoration: none;" href="#chapter-2">Chapter 2 &ndash; Growing</a></strong></span>
<ul style="margin: 0.25rem 0 0.35rem 0; padding-left: 1.1rem;">
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-1">2.1 The &ldquo;Big Six&rdquo; student activities</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-2">2.2 Assignment &ndash; LCC Lesson Deck</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-3">2.3 Assignment &ndash; LCC Proctor &amp; Reflect</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-4">2.4 Unit Activities</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-5">2.5 Assignment &ndash; Unit Activity Draft</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-6">2.6 Debates</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-7">2.7 Assignment &ndash; Debate Source Builder</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-2-8">2.8 Chapter 2 wrap-up</a></li>
</ul>
</li>
</ul>
<ul style="margin: 0.25rem 0 0.35rem 0; padding-left: 1.1rem; font-size: 0.92rem;">
<li><span style="font-size: 14pt;"><strong><a style="color: #2b6cb0; text-decoration: none;" href="#chapter-3">Chapter 3 &ndash; Reflecting &amp; Empowering</a></strong></span>
<ul style="margin: 0.25rem 0 0.35rem 0; padding-left: 1.1rem;">
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-3-1">3.1 Quiz &ndash; Post-Test</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-3-2">3.2 Assignment &ndash; Unit Activity Final</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-3-3">3.3 Assignment &ndash; Debate Portfolio</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-3-4">3.4 Quiz &ndash; Final Exam</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-3-5">3.5 Assignment &ndash; Engagement Log</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-3-6">3.6 Assignment &ndash; Final Reflection</a></li>
<li><a style="color: #2b6cb0; text-decoration: none;" href="#we-3-7">3.7 Chapter 3 wrap-up &amp; closing words</a></li>
</ul>
</li>
</ul>
</section>
<section id="home-overview" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">Home: What This Journey Offers You</span></strong></h2>
<p>By the time you finish, you&rsquo;ll have:</p>
<ul>
<li><strong>Organised lessons</strong> &ndash; students know what today is for and what &ldquo;good work&rdquo; looks like. You&rsquo;ll know how to prep students using a structured methodology that brings consistency to planning and delivery.</li>
<li><strong>Less prep stress</strong> &ndash; simple patterns for lessons and activities you can reuse.</li>
<li><strong>Real proof of your work</strong> &ndash; showing you can plan and deliver lessons, activities, debates, learning content, post-tests, and exams using an International curriculum.</li>
<li><strong>Recognition you can show</strong> &ndash; WorldEd badges and a WICE Certificate with your name on it.</li>
</ul>
<p>Underneath all of that: a sense that you can guide students towards an International dual diploma with confidence, not uncertainty.</p>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">Three chapters, one gentle arc</h3>
<ul>
<li><strong>Chapter 1 &ndash; Setting Up</strong>: the &ldquo;why&rdquo;, your role, standards, PPP, LCC, Backward Design, and your personal mission.</li>
<li><strong>Chapter 2 &ndash; Growing</strong>: LCC decks, Unit Activities, Debates, and practical tools you can use tomorrow.</li>
<li><strong>Chapter 3 &ndash; Reflecting &amp; Empowering</strong>: portfolio pieces, final assessments, badges, and WICE recognition.</li>
</ul>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">Badges &amp; WICE Certificate</h3>
<ul>
<li><strong>Set Up badge</strong> &ndash; you can explain, in your own words, what WorldEd is doing and how you fit into the dual-diploma pathway.</li>
<li><strong>Grow badge</strong> &ndash; you can design clear lessons and activities based on the method.</li>
<li><strong>Empower badge</strong> &ndash; you can bring everything together: planning, assessment, reflection, and classroom culture.</li>
<li><strong>WICE Certificate</strong> &ndash; WorldEd Innovative &amp; Certified Educator (Tutor &amp; Coordinator Training).</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">You can move at your own pace. The platform remembers where you stopped. You&rsquo;re allowed to be tired, busy, and human.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="home-language" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">Home: A Quick Note on Language</span></strong></h2>
<p style="font-size: 0.9rem; color: #4a5568;">(No one expects you to know this yet.)</p>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">Backward Design</h3>
<ul>
<li>first decide what students should be able to do (outcomes/standards)</li>
<li>then decide what evidence will prove it (assessments)</li>
<li>only then plan the lessons and activities that lead there</li>
</ul>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">Standards</h3>
<p>What students should actually be able to do by the end of a unit.</p>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">PPP and LCC</h3>
<ul>
<li><strong>PPP</strong> &ndash; the rhythm of a lesson (Present &rarr; Practice &rarr; Produce).</li>
<li><strong>LCCs</strong> &ndash; short checks that show whether students understood the Learning Content.</li>
</ul>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">Unit Activities and Debates</h3>
<p>Larger tasks and structured speaking activities that show students&rsquo; deeper critical thinking and use of evidence.</p>
<p>In this training, we explain each of these before we ask you to work with them. You are not &ldquo;late&rdquo; or &ldquo;behind&rdquo; if they are new to you.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="home-recognition" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">Home: How Your Students&rsquo; Work Is Recognised</span></strong></h2>
<p style="font-size: 0.9rem; color: #4a5568;">(and the activities you&rsquo;ll complete throughout this)</p>
<p>The main graded pieces are:</p>
<ul>
<li>Unit Activity &ndash; 20%</li>
<li>LCC (deck + proctoring reflection) &ndash; 10%</li>
<li>Debate Portfolio &ndash; 20%</li>
<li>Post-Test &ndash; 10%</li>
<li>Final Exam &ndash; 30%</li>
<li>Engagement Log &ndash; 10%</li>
</ul>
<p>Most quizzes are untimed, with clear language. You&rsquo;re being invited to show how you think and teach, not to &ldquo;catch you out&rdquo;.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="home-start-why" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><span style="font-size: 18pt;"><strong>Home: Start Where All Good Stories Start: With Your &ldquo;Why&rdquo;</strong></span></h2>
<p>We begin with your reasons for teaching, not with rules.</p>
<p>Why did you become an educator?</p>
<ul>
<li>To inspire the desire to learn?</li>
<li>To ignite the torch your teachers once lit for you?</li>
<li>To plant seeds of liberation that brighten the future?</li>
<li>To be the shoulders your students stand on, so they can see further than they dreamed?</li>
<li>Or something else entirely?</li>
</ul>
<p>When you&rsquo;re ready, scroll to <a style="color: #2b6cb0; text-decoration: none;" href="#we-1-6">1.6 &ndash; &ldquo;Why I currently teach&rdquo;</a> to confirm your reason for teaching and your enrolment.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="chapter-1" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #cbd5e0; background: #edf2f7;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.3rem; color: #2d3748;"><strong><span style="font-size: 18pt;">Chapter 1 : Setting Up</span></strong></h2>
<p>This chapter is about the heart behind your work and the simple patterns underneath it: why WorldEd exists, why your role is central, and how standards, PPP, LCC, and Backward Design fit together.</p>
<p style="font-size: 0.9rem; color: #4a5568;">No exams here. Just understanding and gentle first moves.</p>
</section>
<section id="we-1-1" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><span style="font-size: 18pt;"><strong>1.1 The question that started WorldEd</strong></span></h2>
<p>WorldEd began with one simple question:</p>
<blockquote style="margin: 0.5rem 0; padding-left: 0.9rem; border-left: 3px solid #cbd5e0; color: #4a5568; font-size: 0.95rem;">&ldquo;How can more students, in more cities, in more countries earn a real International high school diploma without leaving their families, schools, and lives behind?&rdquo;</blockquote>
<p>The answer was not &ldquo;send everyone abroad&rdquo;. The answer was to bring the diploma to them:</p>
<ul>
<li>accredited International courses online</li>
<li>taken in parallel with their local schools</li>
<li>supported by local tutors and coordinators</li>
</ul>
<p>That&rsquo;s where you come in. You&rsquo;re not here to press buttons on a platform. You&rsquo;re here to make the program make sense to your students, in your classrooms, in your schools.</p>
<p>This chapter is about that bridge: why the program exists, how your work fits, and how simple patterns like PPP and tools like LCC can make your life easier instead of heavier.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-2" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><span style="font-size: 18pt;"><strong>1.2 Mission, vision, and where you fit</strong></span></h2>
<p>In simple language:</p>
<ul>
<li><strong>Mission</strong> &ndash; to give students supportive, flexible, personalized, high-quality education that leads to an International diploma.</li>
<li><strong>Vision</strong> &ndash; young people who can read closely, argue with evidence, reason with data, and move confidently across cultures.</li>
</ul>
<p>Some key values you&rsquo;ll recognise from your own work:</p>
<ul>
<li><strong>Excellence</strong> &ndash; clear goals, honest standards, and fair support</li>
<li><strong>Innovation</strong> &ndash; trying new tools when they help, not because they&rsquo;re trendy</li>
<li><strong>Global engagement</strong> &ndash; bringing in voices and issues from beyond the local bubble</li>
<li><strong>Student-driven learning</strong> &ndash; students producing work that shows thinking, not just filling in blanks</li>
</ul>
<p>Your classroom is one of the places this mission either feels real or doesn&rsquo;t. This course is here to support you in making it feel real, without burning you out.</p>
<p style="font-size: 0.9rem; color: #4a5568;">Optional short reflection (ungraded): In your own words, note: &ldquo;What makes a school excellent?&rdquo;, &ldquo;What do you believe the mission of your school to be?&rdquo;, and &ldquo;How could you feel more supported?&rdquo;</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-3" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">1.3 Standards without the jargon</span></strong></h2>
<p>You&rsquo;ll see references to International Core Curriculum standards (on the platform, you can click a link to see them in full).</p>
<p>In daily practice, standards boil down to one question:</p>
<blockquote style="margin: 0.5rem 0; padding-left: 0.9rem; border-left: 3px solid #cbd5e0; color: #4a5568; font-size: 0.95rem;">&ldquo;By the end of this unit, what should my students actually be able to do?&rdquo;</blockquote>
<p>Examples:</p>
<ul>
<li>&ldquo;Write a short argument using evidence from a text.&rdquo;</li>
<li>&ldquo;Explain a scientific process with a labelled diagram.&rdquo;</li>
<li>&ldquo;Compare two sources for reliability and explain why one is stronger.&rdquo;</li>
</ul>
<p>You are not expected to memorise standard codes. You are expected to keep this question in mind when you look at:</p>
<ul>
<li>the Learning Content in the course</li>
<li>the LCCs</li>
<li>Unit Activities</li>
<li>Debates</li>
<li>Post-Tests and the Final Exam</li>
</ul>
<p>We&rsquo;ll keep connecting back to this chain: <strong>Standards &rarr; What students do &rarr; How you plan &rarr; How you assess.</strong></p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-4" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">1.4 PPP:&nbsp; a simple pattern, and your first &ldquo;quick win&rdquo;</span></strong></h2>
<p>Before we go deep into tools, here&rsquo;s one simple pattern you probably already use:</p>
<p><strong>PPP = Present &rarr; Practice &rarr; Produce</strong></p>
<ul>
<li><strong>Present</strong> &ndash; you show a clear model and point out what matters.</li>
<li><strong>Practice</strong> &ndash; students try it with you; you support and shape.</li>
<li><strong>Produce</strong> &ndash; students do it alone; you see who is ready and who needs more help.</li>
</ul>
<p>We&rsquo;ll use PPP throughout this course because it lines up with standards (what students should do), assessments (what counts as proof), and your real lesson time (what actually happens in the room).</p>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;"><strong>1.4.1 Activity &ndash; Match the PPP step (ungraded quick win)</strong></h3>
<p>You&rsquo;ll see three short, unlabeled classroom examples, such as:</p>
<ul>
<li><strong>Example A</strong> &ndash; Teacher shows a model opinion paragraph and highlights the opinion, reasons, and linking words.</li>
<li><strong>Example B</strong> &ndash; Class and teacher build a new paragraph together. Students suggest ideas; the teacher helps form sentences.</li>
<li><strong>Example C</strong> &ndash; Each student writes their own 4&ndash;5 sentence opinion paragraph. Teacher collects or photographs them.</li>
</ul>
<p><strong>Your task:</strong> For each example, choose: Present, Practice, or Produce.</p>
<p style="font-size: 0.9rem; color: #4a5568;">This quick win does not count toward your grade. It gives you a small, early success and creates reference points we&rsquo;ll use later when you build your own PPP lessons.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-5" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">1.5 LCC &ndash; what it is and why it helps you</span></strong></h2>
<p>You&rsquo;ll hear LCC a lot. Let&rsquo;s slow it down.</p>
<p><strong>LCC = Learning Content Comprehension.</strong></p>
<p><strong>Learning Content (LC)</strong> is what students read or watch in the course: videos, texts, explanations.<br /><strong>LCC</strong> is a short check of whether they understood that content.</p>
<p>Think of LCCs like regular temperature checks:</p>
<ul>
<li>low pressure, high information</li>
<li>help you see quickly who is lost and who is fine</li>
<li>stop surprises at exam time</li>
</ul>
<p>You are not expected to write all LCC items yourself. Your main focus is:</p>
<ul>
<li>making sure students are prepared for LCCs (through PPP lessons), and</li>
<li>learning how to read the results so you can adjust next steps calmly.</li>
</ul>
<p>LCCs are on your side. They&rsquo;re a tool, not a threat.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-6" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><span style="font-size: 18pt;"><strong>1.6 Assignment:&nbsp; Your &ldquo;why&rdquo; as an educator</strong></span></h2>
<p>Before we talk methodology, we talk about you. This reflection connects your personal mission to WorldEd&rsquo;s mission and strengthens your buy-in.</p>
<p><strong>Goal:</strong> Capture &ldquo;Why I currently teach&rdquo;.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ul>
<li>Write <strong>100&ndash;150 words</strong> answering:</li>
</ul>
<ul>
<li>Why did you become an educator?</li>
<li>What do you hope changes in your students&rsquo; lives because of your work?</li>
<li>How does the idea of a dual diploma connect (or not connect) to that hope?</li>
</ul>
<p>You can reuse the answer you submitted when logging in. If your &ldquo;why&rdquo; has changed, paste the original in brackets and then write your updated answer.</p>
<p>Use simple language. This isn&rsquo;t an essay; it&rsquo;s your voice. We&rsquo;ll revisit this reflection when we talk about mission and values.</p>
<p style="font-size: 0.9rem; color: #4a5568;">In a live session, 1&ndash;2 tutors may share their &ldquo;why&rdquo; aloud. Hearing real stories often inspires others and deepens connection to the curriculum.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-7" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">1.7 Assignment: PPP in your own classroom (PPP Rebuild)</span></strong></h2>
<p><strong>Goal:</strong> Apply PPP consciously to a real lesson you already know.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ol>
<li><strong>Choose a real lesson</strong><br />A recent or favourite lesson that went reasonably well.</li>
<li><strong>Rebuild it using PPP in 2&ndash;3 bullet points:</strong>
<ul>
<li><strong>Present</strong> &ndash; What will you show or model first? (text, example answer, short demo, process on the board).</li>
<li><strong>Practice</strong> &ndash; What will you do together, with support? (guided questions, pair work, joint paragraph, worked example).</li>
<li><strong>Produce</strong> &ndash; What will students do alone so you can see what they can really do?</li>
</ul>
</li>
<li><strong>Add 1&ndash;2 LCC-style questions</strong><br />Gentle checks of understanding (e.g., &ldquo;According to the text, why did the character decide to leave?&rdquo;).</li>
</ol>
<p style="font-size: 0.9rem; color: #4a5568;">This can be ungraded or low-stakes. You&rsquo;re taking a lesson you&rsquo;re proud of and rebuilding it so it&rsquo;s clearer for you and for your students.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-8" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">1.8 Assignment &ndash; Mission, values, and your own sentence</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;My Educator Mission (Draft)&rdquo;</p>
<p><strong>Goal:</strong> Connect your personal &ldquo;why&rdquo; to WorldEd&rsquo;s mission in a short, usable mission statement.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ul>
<li>Re-read your &ldquo;Why I currently teach&rdquo; reflection.</li>
<li>Review WorldEd&rsquo;s mission, vision, and values from 1.2.</li>
<li>Think about your own mission and values as a teacher, in and beyond school.</li>
</ul>
<p>Write a <strong>75&ndash;120 word</strong> mission that includes:</p>
<ul>
<li>1&ndash;2 sentences about why you teach</li>
<li>a short description of your mission and values as an educator</li>
<li>one sentence about your future goal &ndash; the change you hope to see through your students</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">You don&rsquo;t need fancy language. A simple, honest mission is powerful. You&rsquo;ll refine this later in the course.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-9" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #4fd1c5; background: #e6fffa;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #285e61;"><strong><span style="font-size: 18pt;">1.9 Discussion: You are not alone: Buddy check-in</span></strong></h2>
<p><strong>Discussion:</strong> &ldquo;Find a Buddy&rdquo;</p>
<p>Learning something new is easier when someone walks beside you. This buddy can be your lifeline when you are planning PPP lessons, reading LCC results, or choosing which assessments to focus on.</p>
<p><strong>In this discussion, you will:</strong></p>
<ol>
<li><strong>Introduce yourself (100&ndash;150 words):</strong>
<ul>
<li>your name and where you teach</li>
<li>one thing you enjoy in your current work</li>
<li>one area where this training might help you move towards your goals</li>
</ul>
</li>
<li><strong>Share one small goal for the next two weeks</strong> related to this training (e.g., &ldquo;Try one PPP-rebuild lesson and one LCC-style question.&rdquo;).</li>
<li><strong>Reply to at least one colleague</strong>, offering:
<ul>
<li>one thing you see them already doing well</li>
<li>one small suggestion you think could support their goal</li>
</ul>
</li>
</ol>
<p>If you can, choose one person to be your buddy for the rest of the course. A quick check-in now and then can make a big difference when you&rsquo;re busy or stuck.</p>
<p style="font-size: 0.9rem; color: #4a5568;">Completing this discussion helps unlock your Set Up badge.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-1-10" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">1.10 Chapter 1 wrap-up</span></strong></h2>
<p>By the end of Chapter 1 you will have:</p>
<ul>
<li>a clear sense of why WorldEd exists</li>
<li>an understanding of where you fit in the dual-diploma story</li>
<li>simple, human language for standards, Backward Design, PPP, and LCC</li>
<li>a written &ldquo;Why I currently teach&rdquo; reflection</li>
<li>a first draft of your educator mission</li>
<li>a buddy (or at least a sense of community) for the journey ahead</li>
</ul>
<p>You&rsquo;ve planted seeds of clarity, language, purpose, and support.</p>
<p>In <strong>Chapter 2 &ndash; Growing</strong>, those seeds become tools: clear PPP lesson patterns, practical ways to use LCC, Unit Activities, and Debates, and calmer, more focused classes.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="chapter-2" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #cbd5e0; background: #edf2f7;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.3rem; color: #2d3748;"><span style="font-size: 18pt;"><strong>Chapter 2: Growing, Skill &amp; Structure</strong></span></h2>
<p>Now that you know why this work matters and where you fit, this chapter moves into the &ldquo;how&rdquo;: building LCC lessons, Unit Activities, and Debates using PPP and Backward Design.</p>
<p style="font-size: 0.9rem; color: #4a5568;">We keep the same rhythm: start from the outcome &rarr; decide what evidence would show it &rarr; build PPP lessons and tasks to get there. We&rsquo;re building muscles, not testing perfection.</p>
</section>
<section id="we-2-1" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><span style="font-size: 18pt;"><strong>2.1 The &ldquo;Big Six&rdquo; student activities</strong></span></h2>
<p>Across WorldEd courses, students tend to meet the same types of activities: Links to the platform for each activity, exapmles of quality work.&nbsp;</p>
<ul>
<li><strong>Learning Content (LC)</strong> &ndash; stories, texts, videos, explanations&nbsp;</li>
<li><strong>Learning Content Comprehension (LCC)</strong> &ndash; short quizzes checking understanding</li>
<li><strong>Unit Activities</strong> &ndash; bigger pieces of work (written, spoken, visual)</li>
<li><strong>Debates / discussions</strong> &ndash; structured speaking with evidence</li>
<li><strong>Post-Tests</strong> &ndash; checks at the end of units</li>
<li><strong>Final Exams</strong> &ndash; bigger summative checks at the end of the course</li>
</ul>
<p>This chapter focuses mainly on LCC, Unit Activities, and Debates. You&rsquo;ll touch Post-Tests and Final Exams in Chapter 3.</p>
<p style="font-size: 0.9rem; color: #4a5568;">Light task (ungraded): on the platform, click through short examples of each of the Big Six. In 1&ndash;2 short lines, note which type you feel most confident with right now and which one you&rsquo;d like the most support with.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-2-2" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">2.2 Assignment: Building an LCC lesson with PPP. <span style="color: #c71f23;">Tutors will not need to create LCCs</span></span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;LCC Lesson Deck&rdquo;</p>
<p><strong>Goal:</strong> Create a short slide deck that prepares students for a specific LCC using PPP.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ol>
<li>Choose one unit and one LCC from your course.</li>
<li>Identify, in simple language, what the LCC is trying to check, for example:
<ul>
<li>&ldquo;Can students identify the main idea?&rdquo;</li>
<li>&ldquo;Can students use the past simple in context?&rdquo;</li>
</ul>
</li>
<li>Build a minimum viable 4&ndash;5 slide deck:
<ul>
<li><strong>Slide 1 &ndash; Today&rsquo;s Goal</strong>: a clear &ldquo;By the end of today, you will be able to&hellip;&rdquo; + a tiny example of success.</li>
<li><strong>Slide 2 &ndash; Present (Model)</strong>: one worked example connected to the LCC skill, with key parts highlighted.</li>
<li><strong>Slide 3 &ndash; Practice</strong>: 2&ndash;3 short items done together, plus a quick understanding check (e.g., 1&ndash;3 fingers).</li>
<li><strong>Slide 4 &ndash; Produce</strong>: one short independent task that mirrors the LCC demands.</li>
<li><strong>Slide 5 (optional) &ndash; Next Steps</strong>: one support idea + one challenge idea.</li>
</ul>
</li>
<li>Upload your deck (PPT or link) with brief notes under each slide explaining what you&rsquo;ll say or do.</li>
</ol>
<p style="font-size: 0.9rem; color: #4a5568;">A clean 4-slide deck that works beats a 15-slide deck no one uses. This is about clarity and alignment: outcome &rarr; evidence &rarr; PPP lesson.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-2-3" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">2.3 Assignment: Running an LCC without panic.&nbsp;</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;LCC Proctor &amp; Reflect&rdquo;</p>
<p><strong>Goal:</strong> Practise proctoring an LCC in a calm, clear way and reading the results kindly.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">Before the LCC</h3>
<ul>
<li>Tell students what the LCC is and why it matters: &ldquo;This is to help us see what to review, not to punish anyone.&rdquo;</li>
<li>Remind them of the skill you focused on in your PPP lesson.</li>
</ul>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">During the LCC</h3>
<ul>
<li>Make sure everyone can access it.</li>
<li>Give enough time; the LCC is untimed.</li>
<li>Note one or two things you see (e.g., many students re-reading a certain question).</li>
</ul>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">After the LCC</h3>
<ul>
<li>Look at the basic data (overall scores or item difficulty, depending on your tools).</li>
<li>Write a short reflection (about <strong>150&ndash;200 words</strong>):
<ul>
<li>one thing that went well</li>
<li>one pattern you noticed (e.g., &ldquo;Most students struggled with inference questions&rdquo;)</li>
<li>one small adjustment you&rsquo;ll make in your next lesson</li>
</ul>
</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">If scores were low, that&rsquo;s the deck and timing talking, not your worth as a teacher. The purpose is to build a habit of using LCCs as information, not as a hammer.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-2-4" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">2.4 Unit Activities: where deeper thinking lives</span></strong></h2>
<p>A Unit Activity is one of the key places where students show deeper understanding. Often, these follow a Claim&ndash;Evidence&ndash;Reasoning (CER) pattern:</p>
<ul>
<li><strong>Claim</strong> &ndash; what the student thinks or concludes</li>
<li><strong>Evidence</strong> &ndash; information from texts, data, or experiences that support the claim</li>
<li><strong>Reasoning</strong> &ndash; explanation of how the evidence supports the claim</li>
</ul>
<p>Examples:</p>
<ul>
<li><strong>English:</strong> &ldquo;Is Character X truly brave? Make a claim, support it with two quotes, and explain your reasoning.&rdquo;</li>
<li><strong>Science:</strong> &ldquo;Explain how photosynthesis works using a diagram, labels, and a short explanation.&rdquo;</li>
<li><strong>History:</strong> &ldquo;Which source about the event is more reliable? Make a choice, use two details, and explain why.&rdquo;</li>
</ul>
<p>In this training, you&rsquo;ll build one Unit Activity with PPP in mind: what you&rsquo;ll show, how you&rsquo;ll practise, and how students will finally produce.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-2-5" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">2.5 Assignment: Unit Activity (Draft)</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;Unit Activity Draft&rdquo;</p>
<p><strong>Goal:</strong> Draft a clear Unit Activity task that matches a standard and can be tackled through PPP.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ol>
<li>Choose a unit and a key outcome in your own words (e.g., &ldquo;Students can compare two characters with evidence.&rdquo;).</li>
<li>Draft a student-friendly prompt that includes:
<ul>
<li>what they must do (Claim)</li>
<li>what they must use (Evidence)</li>
<li>how they should explain (Reasoning)</li>
</ul>
</li>
<li>Outline a simple PPP plan for this activity:
<ul>
<li><strong>Present</strong> &ndash; What model will you show?</li>
<li><strong>Practice</strong> &ndash; What guided practice will you lead?</li>
<li><strong>Produce</strong> &ndash; What will the final student product be?</li>
</ul>
</li>
</ol>
<p>You&rsquo;ll submit:</p>
<ul>
<li>the student-facing task (the instructions they see)</li>
<li>a short note for yourself describing your PPP steps</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">You&rsquo;ll refine this in Chapter 3, so it doesn&rsquo;t have to be perfect yet.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-2-6" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">2.6 Debates: helping students use their voices with evidence. Exapmple of student debate, Everest US His B&nbsp; Data Driven. Critical thinking, &amp; Active listening.&nbsp;</span></strong></h2>
<p>Debates in the WorldEd context are not about shouting or &ldquo;winning&rdquo;. They are about:</p>
<ul>
<li>forming clear opinions</li>
<li>listening to others</li>
<li>using evidence to support points</li>
<li>practising respect even when disagreeing</li>
</ul>
<p>As a tutor, you help:</p>
<ul>
<li>choose or adapt a motion</li>
<li>collect a few balanced sources</li>
<li>structure the speaking turns</li>
<li>guide students to prepare and respond thoughtfully</li>
</ul>
<p>This is not meant to be theatre. It&rsquo;s a structured way to teach critical thinking and global citizenship.<br /><br />Show Debate topic, History.&nbsp;</p>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;">Adaptations for mixed levels and shy students</h3>
<ul>
<li>Allow notes and sentence frames (e.g., &ldquo;I agree because&hellip;&rdquo;, &ldquo;According to&hellip;&rdquo;, &ldquo;One concern is&hellip;&rdquo;).</li>
<li>Let especially shy students take a smaller role (e.g., summarising a partner&rsquo;s point) or record a short statement instead of a live rebuttal, if your context allows.</li>
<li>Keep groups small so speaking turns feel safer and more manageable.</li>
</ul>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-2-7" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">2.7 Assignment: Debate Sources &amp; Map</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;Debate Source Builder&rdquo;</p>
<p><strong>Goal:</strong> Collect a small, balanced set of sources and map the argument in a clear way.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ol>
<li>Choose (or adapt) a simple motion connected to your course content, for example:
<ul>
<li>&ldquo;Homework should be limited to 30 minutes per night.&rdquo;</li>
<li>&ldquo;Social media does more harm than good for teenagers.&rdquo;</li>
</ul>
</li>
<li>Create a small mind map or outline showing:
<ul>
<li>the motion in the centre</li>
<li>2&ndash;3 arguments &ldquo;for&rdquo;</li>
<li>2&ndash;3 arguments &ldquo;against&rdquo;</li>
</ul>
</li>
<li>Find at least four sources (articles, data, short videos):
<ul>
<li>two that support &ldquo;for&rdquo;</li>
<li>two that support &ldquo;against&rdquo;</li>
</ul>
</li>
<li>For each source, write a short card:
<ul>
<li>title and link</li>
<li>what side it supports</li>
<li>one key idea you might use in the debate</li>
<li>a short note on why it&rsquo;s reasonably reliable (who wrote it, where it&rsquo;s from, how recent it is)</li>
</ul>
</li>
</ol>
<p>You&rsquo;ll upload your mind map and your source cards. You don&rsquo;t have to run the debate yet; we&rsquo;re building the foundation.</p>
<p style="font-size: 0.9rem; color: #4a5568;">Practising ......... LCC work, Unit Activity draft, and Debate Source Builder moves you toward your <strong>Grow</strong> badge.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-2-8" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">2.8 Chapter 2 wrap-up</span></strong></h2>
<p>By the end of Chapter 2 you will have:</p>
<ul>
<li>a have had real learning content, promts, debate promes, U.A prompts&nbsp; LCC&nbsp;&nbsp;</li>
<li>Given insite&nbsp; proctoring an LCC and using the results thoughtfully</li>
<li>a draft Unit Activity aligned with a clear outcome</li>
<li>a simple, balanced set of debate sources and a map of arguments</li>
</ul>
<p>You&rsquo;re not just reading about WorldEd&rsquo;s methodology; you&rsquo;re building real pieces you can use in your own teaching.</p>
<p>Next, Chapter 3 helps you gather these pieces, reflect on them, and connect them to recognition that travels with you.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="chapter-3" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #cbd5e0; background: #edf2f7;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.3rem; color: #2d3748;"><strong><span style="font-size: 18pt;">Chapter 3: Reflecting &amp; Empowering</span></strong></h2>
<p>This final chapter is about taking stock: looking back at what you&rsquo;ve built, checking your understanding in a fair way, polishing key artefacts, and making your growth visible to yourself and to others.</p>
<p style="font-size: 0.9rem; color: #4a5568;">You&rsquo;ve planted seeds and grown practical tools. Now you harvest: a clearer professional identity, a small real portfolio of work, badges and a WICE Certificate that mark what you&rsquo;ve achieved.</p>
</section>
<section id="we-3-1" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #ecc94b; background: #fffbea;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #744210;"><span style="font-size: 18pt;"><strong>3.1 Quiz: Post-Test: a quiet check-in</strong></span></h2>
<p><strong>Goal:</strong> Check your understanding of PPP, LCC, Unit Activities, and Debates in a low-pressure way before the final pieces.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ul>
<li>Take an untimed quiz that asks you to:
<ul>
<li>choose the next best PPP step in short scenarios</li>
<li>recognise clear vs unclear learning goals</li>
<li>spot where an LCC or Unit Activity is not aligned with its outcome</li>
<li>pick a small adjustment that would make a lesson <span style="color: #c71f23;">calmer </span>or clearer</li>
</ul>
</li>
</ul>
<p>After the quiz, you&rsquo;ll see your score and brief feedback. You&rsquo;ll be invited to write a short note for yourself:</p>
<ul>
<li>one strength you noticed</li>
<li>one thing you&rsquo;d like to keep working on</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">This is for your own growth, not to label you.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-3-2" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">3.2 Assignment: Unit Activity (Final)</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;Unit Activity Final Submission&rdquo;</p>
<p><strong>Goal:</strong> Polish and submit your Unit Activity as a clear example of your planning and alignment.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ol>
<li>Revisit your Unit Activity draft from Chapter 2.</li>
<li>Refine:
<ul>
<li>the student instructions (making them clearer and friendlier)</li>
<li>the link to the outcome (does this task really check the skill you care about?)</li>
</ul>
</li>
<li>Add a short teacher note explaining:
<ul>
<li>how you will Present (model)</li>
<li>how you will Practice with students</li>
<li>what the final Produce &gt;&gt;&gt;&gt;&gt;&gt; step looks like</li>
</ul>
</li>
<li>If you have already tried a version of this with students.&nbsp;</li>
</ol>
<p>You&rsquo;ll also write a<strong>&nbsp;reflection</strong>:</p>
<ul>
<li>what you changed and why</li>
<li>what you&rsquo;d like to try next time you run this activity</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">This piece is a key part of your final recognition. It shows not just what you plan, but how you think as an educator.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-3-3" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">3.3 Assignment: Debate Portfolio (Final)</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;Debate Portfolio&rdquo;</p>
<p><strong>Goal:</strong> Show that you can design a small debate that supports critical thinking and respectful dialogue.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<p>Submit a short portfolio including:</p>
<ul>
<li>your motion and mind map from Chapter 2 (updated if needed)</li>
<li>your revised source cards with any extra notes</li>
<li>a brief structure for the debate (who speaks when, for how long, and what they do)</li>
<li>a few sentence frames students can use (e.g., &ldquo;I agree because&hellip;&rdquo;, &ldquo;According to&hellip;&rdquo;, &ldquo;One concern is&hellip;&rdquo;)</li>
<li>a <strong>150&ndash;200 word reflection</strong> on how you would support students that find the debates challenging and keep the debate respectful</li>
</ul>
<p>If you have already tried a version of this in class, you may describe, in general terms, what you noticed and what you&rsquo;d change.</p>
<p style="font-size: 0.9rem; color: #4a5568;">This portfolio shows your ability to guide students through disagreement with care.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-3-4" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #ecc94b; background: #fffbea;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #744210;"><strong><span style="font-size: 18pt;">3.4 Quiz:&nbsp; Final Exam</span></strong></h2>
<p><strong>Goal:</strong> Bring the main ideas of the course together in one fair, structured assessment.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<ul>
<li>Sit an untimed, open-notes exam that asks you to:
<ul>
<li>design a brief PPP lesson from a given outcome</li>
<li>match activities to appropriate assessment types (LCC, Unit Activity, Debate, Post-Test, Final Exam)</li>
<li>identify where a plan needs clearer goals or a simpler product</li>
<li>choose supportive responses to LCC or exam data</li>
</ul>
</li>
</ul>
<p>You&rsquo;re allowed to use your notes from the course. The exam doesn&rsquo;t ask you to recite definitions; it asks you to make decisions like the ones you&rsquo;ll make in the classroom.&nbsp; real teaching.</p>
<p style="font-size: 0.9rem; color: #4a5568;">If you&rsquo;ve genuinely done the tasks in Chapters 1 and 2, you are already prepared for this exam.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-3-5" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">3.5 Assignment: Engagement Log</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;Engagement &amp; Culture Log&rdquo;</p>
<p><strong>Goal:</strong> Make visible the small decisions you make every day to keep students engaged and supported.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<p>Complete a simple log for a recent period (for example, the last 2&ndash;4 weeks):</p>
<ul>
<li>list 2&ndash;3 small engagement moves you tried (quick warm-ups, exit tickets, pair checks, etc.)</li>
<li>note what you saw:
<ul>
<li>how did students respond?</li>
<li>did it change the atmosphere or understanding?</li>
</ul>
</li>
<li>mention at least one time you supported a colleague (sharing a resource, co-planning, offering feedback)</li>
<li>end with one small, specific next step you want to take in your classroom culture</li>
<li>Sharing some of your personal ideas or resources with the group.&nbsp;</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">This is not about perfection. It&rsquo;s about recognising that engagement and care are things you build on purpose, not by accident. Even something as small as &ldquo;I switched from cold-calling to pair-checks once this week&rdquo; counts as evidence.</p>
<p style="font-size: 0.9rem; color: #4a5568;">Completing this log is part of earning your <strong>Empower</strong> badge and your WICE Certificate.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-3-6" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b794f4; background: #f5e9ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #553c9a;"><strong><span style="font-size: 18pt;">3.6 Assignment: Final reflection: your path forward</span></strong></h2>
<p><strong>Assignment:</strong> &ldquo;Looking Back, Looking Ahead, Your Future Why&rdquo;</p>
<p><strong>Goal:</strong> Close the loop on your learning and set a light but real intention for the future.</p>
<p><strong>You&rsquo;ll do:</strong></p>
<p>In up to <strong>100 words</strong>, respond in your own words:</p>
<ul>
<li>What part of the training changed how you see your role the most?</li>
<li>Which idea or tool (PPP, LCC, Unit Activity design, debates, data reflection) do you think will stay with you next term? Why?</li>
<li>What is one concrete action you will take in the next month to bring this method into your classroom more fully?</li>
</ul>
<p>You can write this as a letter to yourself if you prefer: <em>&ldquo;Dear future me, here&rsquo;s what I want you to remember&hellip;&rdquo;</em></p>
<p>Why will you continue to be an educator? And if you do not intend to continue, please give us your &ldquo;why not&rdquo;. Short, honest answers are welcome.</p>
<p>This reflection is for you. It&rsquo;s the moment where you place the seed in your own future. Your answers will help us understand:</p>
<ul>
<li>What first gave you that passion</li>
<li>What keeps you &ndash; what drives you to continue</li>
<li>What your vision of the future is</li>
</ul>
<p style="font-size: 0.9rem; color: #4a5568;">WorldEd is here to help you bring that vision to life.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#course-roadmap">&uarr; Back to course roadmap</a></p>
</section>
<section id="we-3-7" style="margin-bottom: 1.75rem; padding: 1rem 1.1rem; border-radius: 10px; border: 1px solid #b3c7f5; background: #f0f6ff;">
<h2 style="margin: 0 0 0.5rem 0; font-size: 1.25rem; color: #1a4f8b;"><strong><span style="font-size: 18pt;">3.7 Chapter 3 wrap-up and beyond</span></strong></h2>
<p>By the end of Chapter 3 you will have:</p>
<ul>
<li>a Post-Test and Final Exam showing your understanding</li>
<li>a polished Unit Activity</li>
<li>a thoughtful Debate portfolio</li>
<li>an Engagement Log that honours your daily work</li>
<li>a final reflection that ties together your purpose and your practice</li>
</ul>
<p>And you will hold:</p>
<ul>
<li>your Set Up badge</li>
<li>your Grow badge</li>
<li>your Empower badge</li>
<li>your WICE Certificate</li>
</ul>
<p>These are not magic pieces of paper. They are markers of the work you&rsquo;ve done and the work you&rsquo;re you will keep doing.</p>
<h3 style="margin-top: 0.75rem; margin-bottom: 0.35rem; color: #2b4365;"><strong>Closing words</strong></h3>
<p>You came into this as a tutor or coordinator juggling classes, exams, and real lives. You leave with:</p>
<ul>
<li>a clearer story about why you do this</li>
<li>a shared language with colleagues around the world</li>
<li>simple patterns you can rely on when things get messy</li>
<li>evidence of your craft that you can carry into new roles and new schools</li>
</ul>
<p>Your students will not remember all the acronyms. They will remember how you made the path feel: possible, structured, and human.</p>
<p>This training doesn&rsquo;t end with &ldquo;goodbye&rdquo;. It ends with something closer to:</p>
<blockquote style="margin: 0.5rem 0; padding-left: 0.9rem; border-left: 3px solid #cbd5e0; color: #4a5568; font-size: 0.95rem;">&ldquo;We&rsquo;ll see you again &mdash; every time you set a clear goal,<br />model a skill,<br />practise with patience,<br />and watch your students produce work they didn&rsquo;t think they could.&rdquo;</blockquote>
<p>You are the message in the bottle. The river is moving. We&rsquo;re still with you in every lesson you choose to bring this to life.<br /><br />Survey&nbsp;<br /><br /></p>
<p>Video guide.</p>
<p style="margin-top: 0.75rem; font-size: 0.85rem; color: #4a5568;"><a style="color: #2b6cb0; text-decoration: none;" href="#top">&uarr; Back to top</a></p>
</section>
</div>
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

