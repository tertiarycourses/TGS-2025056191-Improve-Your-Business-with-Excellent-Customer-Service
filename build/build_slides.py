#!/usr/bin/env python3
"""
Slide deck — Improve Your Business with Excellent Customer Service (TGS-2025056191).

Built on the COMPACT v2/v3 component library (_engine.py, extracted verbatim from
the wsq-slides reference deck). Content comes from course_data.py +
data_domain1/2.py so the PPT, LP, LG and activities can never drift.

Design rules enforced here:
  - all-white, Arial, brand palette, footer on every slide
  - NO step-by-step procedure on slides (that lives ONLY in the Learner Guide);
    each activity gets a case-study briefing + discussion questions + debrief
  - admin order: ... Briefing for Assessment -> Assessment -> Assessment Flow
  - TRAQOM digital attendance at the FRONT and again at the END
  - restrained motion applied in one pass at the end (fade / push)
"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# The component library (cover/section/content/two_col/cards3/tile_grid/flow_h/
# trainer_slide/big_statement/brk/img_points/img_full/table_slide/formula_slide/
# activity_slide/lms_slide) — imported wholesale, never hand-rolled.
from _engine import *          # noqa: F401,F403
from _engine import (prs, slide, rect, oval, txt, bullets, head, footer, mark,
                     cover, section, content, two_col, cards3, big_statement,
                     tile_grid, flow_h, trainer_slide, brk, img_points, img_full,
                     table_slide, activity_slide, lms_slide,
                     BLUE, TEAL, AMBER, INK, GREY, LIGHT, WHITE, LINE, VIOLET,
                     RED, NAVY, PALETTE, SW, SH, PAGE, SLIDE_MAP, REPO,
                     Inches, Pt, RGBColor, PP_ALIGN, MSO_ANCHOR)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
ACTIVITIES = DOMAIN1 + DOMAIN2
GREEN = RGBColor(0x16, 0x84, 0x5B)


# ---------------------------------------------------------------- extra components
def case_slide(a, topic):
    """Case-study briefing: the scenario in full, with roles + time chips.
    Deliberately NOT a procedure — the steps live only in the Learner Guide."""
    s = head(slide(), f"Activity {a['num']} — {a['title']}",
             kicker=f"TOPIC {topic['code']} · CASE STUDY", kcolor=TEAL)
    rect(s, Inches(10.35), Inches(0.5), Inches(2.13), Inches(0.42), TEAL)
    txt(s, Inches(10.35), Inches(0.5), Inches(2.13), Inches(0.42),
        [[(f"ACTIVITY {a['num']}  ·  {a['minutes']} MIN", 12, WHITE, True)]],
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # scenario panel
    rect(s, Inches(0.85), Inches(1.95), Inches(11.63), Inches(3.62), LIGHT)
    rect(s, Inches(0.85), Inches(1.95), Inches(0.1), Inches(3.62), TEAL)
    txt(s, Inches(1.15), Inches(2.08), Inches(11.1), Inches(0.32),
        [[("THE SCENARIO", 11, TEAL, True)]])
    body = a["scenario"]
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    runs = []
    for p in paras[:3]:
        runs.append([(p, 11.5, INK, False)])
    txt(s, Inches(1.15), Inches(2.45), Inches(11.1), Inches(3.0), runs, space=7)
    # roles + type band
    rect(s, Inches(0.85), Inches(5.72), Inches(5.72), Inches(0.74), RGBColor(0xE8, 0xF0, 0xFE))
    txt(s, Inches(1.1), Inches(5.72), Inches(5.3), Inches(0.74),
        [[("FORMAT   ", 10.5, BLUE, True), (a["type"], 11.5, INK, False)]],
        anchor=MSO_ANCHOR.MIDDLE)
    rect(s, Inches(6.76), Inches(5.72), Inches(5.72), Inches(0.74), RGBColor(0xE8, 0xF7, 0xEE))
    txt(s, Inches(7.01), Inches(5.72), Inches(5.3), Inches(0.74),
        [[("ROLES   ", 10.5, GREEN, True), (a["roles"], 11.5, INK, False)]],
        anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(0.85), Inches(6.56), Inches(11.63), Inches(0.4),
        [[("Full step-by-step instructions: Learner Guide, Activity %d  ·  Activities folder: activities/activity-%02d/"
           % (a["num"], a["num"]), 11, GREY, False)]], align=PP_ALIGN.CENTER)
    footer(s)
    return s


def questions_slide(a, topic):
    """The discussion questions for a case study — numbered tiles."""
    qs = a["questions"]
    s = head(slide(), f"Activity {a['num']} — Discussion Questions",
             kicker=f"TOPIC {topic['code']} · WORK IN YOUR GROUP", kcolor=BLUE)
    n = len(qs)
    Y0 = Inches(1.95); AREA = Inches(4.78); gy = Inches(0.14)
    th = int((AREA - gy * (n - 1)) / n)
    for i, q in enumerate(qs):
        y = int(Y0 + (th + gy) * i); col = PALETTE[i % len(PALETTE)]
        rect(s, Inches(0.85), y, Inches(11.63), th, LIGHT)
        rect(s, Inches(0.85), y, Inches(0.09), th, col)
        bd = Inches(0.42)
        oval(s, Inches(1.1), int(y + th / 2 - bd / 2), bd, bd, col)
        txt(s, Inches(1.1), int(y + th / 2 - bd / 2), bd, bd,
            [[(str(i + 1), 13, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, Inches(1.72), y, Inches(10.6), th, [[(q, 12.5, INK, False)]],
            anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(0.85), Inches(6.86), Inches(11.63), Inches(0.28),
        [[(f"{a['minutes']} minutes  ·  {a['roles']}", 10.5, GREY, False)]], align=PP_ALIGN.CENTER)
    footer(s)
    return s


def debrief_slide(a, topic):
    """The trainer debrief — what good looks like. Green 'what we expect' theme."""
    pts = a["debrief"]
    s = head(slide(), f"Activity {a['num']} — Debrief",
             kicker=f"TOPIC {topic['code']} · WHAT GOOD LOOKS LIKE", kcolor=GREEN)
    n = len(pts)
    # Body must end above the TEST IT band, which itself must clear the
    # footer at y 7.05 — otherwise the band prints through the page number.
    BAND_Y = Inches(6.28); BAND_H = Inches(0.62)
    Y0 = Inches(1.95); gy = Inches(0.11)
    AREA = BAND_Y - Y0 - Inches(0.14)
    th = int((AREA - gy * (n - 1)) / n)
    for i, p in enumerate(pts):
        y = int(Y0 + (th + gy) * i)
        rect(s, Inches(0.85), y, Inches(11.63), th, RGBColor(0xE8, 0xF7, 0xEE))
        rect(s, Inches(0.85), y, Inches(0.09), th, GREEN)
        txt(s, Inches(1.15), y, Inches(11.15), th, [[(p, 11.5, INK, False)]],
            anchor=MSO_ANCHOR.MIDDLE)
    rect(s, Inches(0.85), BAND_Y, Inches(11.63), BAND_H, LIGHT)
    txt(s, Inches(1.1), BAND_Y, Inches(11.15), BAND_H,
        [[("TEST IT   ", 11, TEAL, True), (a["test"], 11.5, INK, False)]],
        anchor=MSO_ANCHOR.MIDDLE)
    footer(s)
    return s


def split_note(title, l_head, l_items, r_head, r_items, kicker=None, note=None):
    """Do/Don't — red panel vs green panel."""
    s = head(slide(), title, kicker, kcolor=BLUE)
    bh = Inches(4.3) if note else Inches(4.75)
    rect(s, Inches(0.85), Inches(1.95), Inches(5.72), bh, RGBColor(0xFE, 0xF2, 0xF2))
    rect(s, Inches(0.85), Inches(1.95), Inches(5.72), Inches(0.42), RED)
    txt(s, Inches(1.1), Inches(1.95), Inches(5.2), Inches(0.42),
        [[(l_head, 13.5, WHITE, True)]], anchor=MSO_ANCHOR.MIDDLE)
    rect(s, Inches(6.76), Inches(1.95), Inches(5.72), bh, RGBColor(0xE8, 0xF7, 0xEE))
    rect(s, Inches(6.76), Inches(1.95), Inches(5.72), Inches(0.42), GREEN)
    txt(s, Inches(7.01), Inches(1.95), Inches(5.2), Inches(0.42),
        [[(r_head, 13.5, WHITE, True)]], anchor=MSO_ANCHOR.MIDDLE)
    bullets(s, Inches(1.1), Inches(2.55), Inches(5.25), bh - Inches(0.75), l_items,
            size=13, gap=9, mcolor=RED)
    bullets(s, Inches(7.01), Inches(2.55), Inches(5.25), bh - Inches(0.75), r_items,
            size=13, gap=9, mcolor=GREEN)
    if note:
        rect(s, Inches(0.85), Inches(6.35), Inches(11.63), Inches(0.62), LIGHT)
        txt(s, Inches(1.1), Inches(6.35), Inches(11.15), Inches(0.62),
            [[(note, 12.5, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
    footer(s)
    return s


def stack_slide(title, items, kicker=None, accent=BLUE, note=None):
    """Vertical numbered stack — an ordered sequence (badge + bold + caption)."""
    s = head(slide(), title, kicker, kcolor=accent)
    n = len(items)
    Y0 = Inches(1.95); AREA = Inches(4.3) if note else Inches(4.85); gy = Inches(0.15)
    th = int((AREA - gy * (n - 1)) / n)
    for i, (t, d) in enumerate(items):
        y = int(Y0 + (th + gy) * i); col = PALETTE[i % len(PALETTE)]
        rect(s, Inches(0.85), y, Inches(11.63), th, LIGHT)
        rect(s, Inches(0.85), y, Inches(0.09), th, col)
        bd = Inches(0.5)
        oval(s, Inches(1.12), int(y + th / 2 - bd / 2), bd, bd, col)
        txt(s, Inches(1.12), int(y + th / 2 - bd / 2), bd, bd,
            [[(str(i + 1), 15, WHITE, True)]], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, Inches(1.85), y, Inches(10.5), th,
            [[(t, 14, col, True)], [(d, 11.5, INK, False)]],
            anchor=MSO_ANCHOR.MIDDLE, space=2)
    if note:
        rect(s, Inches(0.85), Inches(6.35), Inches(11.63), Inches(0.62), LIGHT)
        txt(s, Inches(1.1), Inches(6.35), Inches(11.15), Inches(0.62),
            [[(note, 12.5, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
    footer(s)
    return s


def cards4(title, cards, kicker=None, note=None):
    """Four-across concept cards — the reference deck's signature move."""
    s = head(slide(), title, kicker)
    xs = [Inches(0.85), Inches(3.85), Inches(6.85), Inches(9.85)]
    cw = Inches(2.72)
    ch = Inches(3.9) if note else Inches(4.5)
    for i, (t, body) in enumerate(cards[:4]):
        x = xs[i]; col = PALETTE[i % len(PALETTE)]
        rect(s, x, Inches(1.95), cw, ch, LIGHT)
        rect(s, x, Inches(1.95), Inches(0.09), ch, col)
        bd = Inches(0.46)
        oval(s, x + Inches(0.24), Inches(2.15), bd, bd, col)
        txt(s, x + Inches(0.24), Inches(2.15), bd, bd, [[(str(i + 1), 15, WHITE, True)]],
            align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, x + Inches(0.82), Inches(2.09), cw - Inches(0.95), Inches(0.6),
            [[(t, 13.5, col, True)]])
        txt(s, x + Inches(0.28), Inches(2.78), cw - Inches(0.54), ch - Inches(1.0),
            [[(body, 11.5, INK, False)]])
    if note:
        rect(s, Inches(0.85), Inches(6.05), Inches(11.63), Inches(0.9), LIGHT)
        txt(s, Inches(1.1), Inches(6.05), Inches(11.15), Inches(0.9),
            [[(note, 12.5, INK, False)]], anchor=MSO_ANCHOR.MIDDLE)
    footer(s)
    return s


def concept_slide(topic):
    """The topic's 6 concepts as a 2-col tile grid (title + caption tuples)."""
    return tile_grid(f"Topic {topic['num']} — Key Concepts", topic["concepts"],
                     kicker=f"TOPIC {topic['code']}  ·  {topic['weighting']}",
                     cols=2, size=13)



def attendance_slide():
    """TRAQOM / SSG digital attendance — visual, not a bullet wall."""
    return tile_grid("Digital Attendance (Mandatory)", [
        ("Three scans, every course day", "AM at the start, PM after lunch, and again before the assessment."),
        ("The trainer shows the QR", "Generated live from the SSG TRAQOM portal — it changes each session."),
        ("Scan with your phone camera", "Open the camera, point at the QR, tap the link and submit."),
        ("Use your registered details", "The NRIC/FIN you enrolled with, or the record will not match."),
        ("75% attendance minimum", "Below this you are not eligible for the assessment or for funding."),
        ("Tell the trainer immediately", "If your scan fails or you arrive late — it cannot be fixed after the day.")],
        kicker="TRAQOM · SSG DIGITAL ATTENDANCE", cols=2, size=13,
        note="Digital attendance is a mandatory SSG funding requirement — it is not the same thing as the TRAQOM feedback survey.")


def briefing_slide():
    return tile_grid("Briefing for Assessment", [
        ("Clear your workspace", "Phones and materials under the table or on the floor."),
        ("No photos or recording", "Assessment scripts must not be photographed or copied."),
        ("No discussion", "The assessment is individual, from the moment it starts."),
        ("Black or blue pen only", "For hard-copy scripts. No pencil."),
        ("No correction fluid or tape", "Strike through a mistake cleanly and write beside it."),
        ("Scripts collected on time", "When time is up, pens down and hand the script over.")],
        kicker="BEFORE THE ASSESSMENT", cols=2, size=13,
        note="Open book means the slides, the Learner Guide and approved materials only — not the internet, and not each other.")


def final_assessment_slide(kicker="FINAL ASSESSMENT"):
    return tile_grid("Final Assessment", [
        ("Oral Questioning (OQ) — 30 min", "3 open-ended questions covering K1, K2 and K3. Individual, open book."),
        ("Role Play (RP) — 30 min", "2 simulated customer interactions covering A1, A2 and A3. Individual, open book."),
        ("Open book", "Slides, Learner Guide and approved materials only."),
        ("Both must be Competent", "You must be assessed Competent in BOTH instruments to pass."),
        ("75% attendance required", "Attendance and a Competent result are both needed for funding."),
        ("Appeals available", "You may appeal if you disagree with the assessment outcome.")],
        kicker=kicker, cols=2, size=13,
        note="Oral Clarification of up to 10 minutes may be conducted 1:1 to close minor performance gaps — this is not counted in the assessment duration.")


def support_slide():
    return tile_grid("Support", [
        ("Email", "enquiry@tertiaryinfotech.com"),
        ("Telephone", "+65 6100 0613"),
        ("Website", "www.tertiarycourses.com.sg"),
        ("LMS / TMS portal", "lms-tms.tertiaryinfotech.com — courseware, assessment and certificates."),
        ("During the course", "Ask your trainer at any point — including during the activities."),
        ("After the course", "Contact us any time; we support learners after the class ends.")],
        kicker="WE'RE HERE TO HELP", cols=2, size=13)


def icebreaker_slide():
    return tile_grid("Let's Know Each Other", [
        ("Your name and organisation", "And the role you play day to day."),
        ("Who your customers are", "External, internal, or both — most people have both."),
        ("A recent interaction that went badly", "What happened, and what you think caused it."),
        ("One that went well", "What made the difference on that occasion?"),
        ("Your channels", "Counter, phone, email, chat — where do you spend most of your time?"),
        ("What you want from today", "One thing you want to do differently tomorrow.")],
        kicker="ICE-BREAKER", cols=2, size=13)


# ============================================================ BUILD
cover()

# ---------------------------------------------------------------- ADMIN
mark("admin")
section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")
attendance_slide()
trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
              "General Trainer template —\nto be completed by the trainer",
              [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
               ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
              initials="?", accent=GREY)
trainer_slide("YOUR TRAINER", C.TRAINER,
              "Principal Trainer\nTertiary Infotech Academy Pte Ltd",
              [("Role", "Principal Trainer, Tertiary Infotech Academy Pte Ltd"),
               ("Background", "PhD — 20+ years of industry and training experience across service quality, business operations and technology."),
               ("Delivers", "WSQ courses on customer service, service branding, business improvement and digital skills."),
               ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
              initials="AA", accent=BLUE)
icebreaker_slide()
tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required for funding."],
    kicker="HOUSEKEEPING", cols=2, size=15)
lms_slide()
two_col("Lesson Plan — 1 Day, 9:00am–6:00pm", [
    ("Morning (AM attendance)", 0, True),
    ("Welcome, introductions, learning outcomes", 1),
    ("Topic 1: Understanding Customers & Service + Activity 1", 1),
    ("Topic 2: Establishing Your Attitude + Activity 2", 1),
    ("Tea break (15 min)", 1),
    ("Topic 3: Identifying Customer Needs + Activity 3", 1),
    ("Topic 4: In-Person Service + Activity 4", 1),
    ("Lunch break 1:00–2:00pm", 1)],
    [("Afternoon (PM attendance)", 0, True),
     ("Topic 5: Phone Service + Activity 5", 1),
     ("Topic 6: Email & Chat Service + Activity 6", 1),
     ("Tea break (15 min)", 1),
     ("Topic 7: Return Business from Feedback + Activity 7", 1),
     ("Topic 8: Recovering Difficult Customers + Activity 8", 1),
     ("Topic 9: When to Escalate + Activity 9", 1),
     ("TRAQOM · Briefing · Assessment (OQ 30 min + RP 30 min)", 1)],
    kicker="SCHEDULE", lhead="Morning — LU1: needs & feedback",
    rhead="Afternoon — LU1 channels + LU2: improvement",
    note="8 hours: 7 h classroom facilitation + 1 h assessment · 1-hour lunch · tea breaks counted within training time.")
table_slide("Skills Framework — Customer Service Innovation Management",
            ["TSC element", "Detail"],
            [("TSC Title / Code", f"{C.TSC_TITLE}  ·  {C.TSC_CODE}")] +
            [(f"Ability {c}", d) for c, d in C.TSC_ABILITIES] +
            [(f"Knowledge {c}", d) for c, d in C.TSC_KNOWLEDGE],
            kicker="WSQ ALIGNMENT", widths=[0.30, 0.70],
            note="Every topic, activity and assessment item in this course maps to these TSC abilities and knowledge factors.")
tile_grid("Learning Outcomes",
          [(lo.split(": ")[0], lo.split(": ")[1]) for lo in C.LEARNING_OUTCOMES],
          kicker="BY THE END OF THIS COURSE", cols=1, size=14)
two_col("Course Outline — Two Learning Units, Nine Topics", [
    ("LU1 — Customer's Needs and Feedback  (LO1)", 0, True),
    ("T1 Understanding Customers & Customer Service", 1),
    ("T2 Establishing Your Service Attitude", 1),
    ("T3 Identifying and Addressing Customer Needs", 1),
    ("T4 In-Person Customer Service", 1),
    ("T5 Customer Service Over the Phone", 1),
    ("T6 Customer Service via Email and Chat", 1)],
    [("LU2 — Improving Needs Based on Feedback  (LO2)", 0, True),
     ("T7 Generating Return Business from Feedback", 1),
     ("T8 Recovering Difficult Customers", 1),
     ("T9 Understanding When to Escalate", 1),
     ("9 real-world case-study activities", 0, True),
     ("Every topic is practised on a realistic Singapore scenario", 1),
     ("Role plays mirror the Role Play assessment format", 1)],
    kicker="THE JOURNEY", lhead="Morning", rhead="Afternoon")
mark("briefing")
briefing_slide()
final_assessment_slide()
flow_h("Assessment Flow", C.ASSESSMENT_FLOW, kicker="ON ASSESSMENT DAY")

big_statement("Service is not a department.",
              "It is every interaction a customer has with your business — before, during and after the sale.",
              "WHY THIS COURSE MATTERS")

# ================================================================ LU1
section("LEARNING UNIT 1", "Customer's Needs and Feedback",
        "1", "LO1 · Collect and analyse customer feedback to assess needs and expectations")

# ---------------------------------------------------------------- TOPIC 1
T = C.TOPICS[0]; mark("topic1")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
cards4("What Customer Service Actually Covers", [
    ("BEFORE", "Pre-sales questions, product advice, quotations, expectation setting. Service starts before any money changes hands."),
    ("DURING", "The transaction itself — ordering, payment, delivery, installation, onboarding."),
    ("AFTER", "Support, returns, complaints, follow-up, renewal. Most loyalty is won or lost here."),
    ("BETWEEN", "Proactive contact when nothing is wrong: updates, check-ins, warnings about issues before they bite.")],
    kicker="THE FULL SERVICE LIFECYCLE",
    note="Most organisations resource the middle column well and the last two poorly — which is precisely where retention is decided.")
split_note("External and Internal Customers",
           "EXTERNAL CUSTOMERS", [
               "Buy your product or service and generate revenue.",
               "Judge you on the outcome AND on how they were treated.",
               "Can leave — and mostly leave silently, without complaining.",
               "Their experience is shaped by people they never meet."],
           "INTERNAL CUSTOMERS", [
               "Colleagues and departments who depend on your output.",
               "Cannot leave — so dissatisfaction shows up as friction, not churn.",
               "Enable (or block) the frontline's ability to serve.",
               "Treated as customers, they make external service possible."],
           kicker="WHO YOU SERVE",
           note="The rule that runs through this whole course: excellent external service always begins with strong internal service.")
img_points("How Service Quality Actually Flows", "service_chain.png", [
    ("Support enables delivery", "IT, HR and operations decide what the frontline is even able to offer."),
    ("Delivery shapes perception", "The customer only ever sees the last link — so that is where blame lands."),
    ("Perception drives loyalty", "Loyalty and referral are downstream of experience, not of product quality alone."),
    ("Break one link, break the chain", "A failure anywhere upstream surfaces as a frontline service failure.")],
    kicker="THE SERVICE CHAIN", img_w=7.0)
cards4("The Four Principles of Good Service", [
    ("PERSONALISED", "A human interaction that shows the organisation actually cares about this specific customer."),
    ("COMPETENT", "Strong product knowledge PLUS the authority to act on it. Knowledge without authority frustrates everyone."),
    ("CONVENIENT", "Available on the channel the customer prefers, not the one cheapest for you."),
    ("PROACTIVE", "You reach out about delays and issues before the customer has to ask.")],
    kicker="HELP SCOUT'S FOUR PRINCIPLES",
    note="All four must hold. Personalised but incompetent is charming and useless; competent but inconvenient still loses the customer.")
img_points("The Business Case for Service", "retention_economics.png", [
    ("Acquisition costs ~5x", "Winning a replacement customer costs far more than keeping the one you have."),
    ("Retention compounds", "A 5% retention improvement can move profit by 25–95% over time."),
    ("Poor service drives churn", "86% of customers stop buying after poor experiences."),
    ("Service is a growth centre", "Not a cost centre — the framing decides whether it gets resourced.")],
    kicker="WHY THE BUSINESS SHOULD CARE", img_w=7.2)
tile_grid("Who Delivers Customer Service", [
    ("Frontline staff", "The first — often only — human contact. They carry the entire perception."),
    ("Support and back office", "Never seen by the customer, but they determine what the frontline can promise."),
    ("Managers and leaders", "Set the standards, the metrics and the amount of authority the frontline has."),
    ("Self-service systems", "FAQ, chatbots, portals — service delivered without a person, and judged just as harshly."),
    ("Every other department", "Product, finance, logistics — each creates or removes friction the customer feels."),
    ("The customer themselves", "Reviews, referrals and word of mouth extend your service reputation beyond your control.")],
    kicker="SERVICE PROVIDERS", cols=2, size=13)
mark("act1"); a = ACTIVITIES[0]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

# ---------------------------------------------------------------- TOPIC 2
T = C.TOPICS[1]; mark("topic2")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
img_points("First Impressions Form Before You Speak", "first_impression.png", [
    ("4–7 seconds", "The window in which the customer decides how this is going to go."),
    ("55% is what they see", "Grooming, posture, expression — visible before a word is exchanged."),
    ("38% is how you sound", "Tone, pace and warmth carry more than the words themselves."),
    ("7% is what you say", "Correct words delivered badly still read as bad service.")],
    kicker="THE ATTITUDE MOMENT", img_w=6.6)
cards4("The Four Pillars of Service Attitude", [
    ("APPEARANCE", "Professional grooming signals competence and respect. It is the baseline expectation in Singapore hospitality and retail."),
    ("THE SMILE", "A genuine smile measurably raises trust. A forced one is detected instantly and costs more than none."),
    ("ENERGY", "Service quality decays with fatigue. Managed breaks protect the last customer of the day."),
    ("POSITIVITY", "Reframe the limit into what IS possible. Do not take the complaint personally.")],
    kicker="ESTABLISHING YOUR ATTITUDE",
    note="Attitude is not a personality trait you either have or lack — every one of these four pillars is a trainable, repeatable behaviour.")
split_note("Positive Language — Same Facts, Opposite Outcome",
           "NEGATIVE FRAMING", [
               "\"That product is back-ordered and unavailable.\"",
               "\"I don't know.\"",
               "\"You have to log out first.\"",
               "\"That's not our policy.\"",
               "\"You'll have to pay for that yourself.\"",
               "\"There's nothing I can do.\""],
           "POSITIVE FRAMING", [
               "\"That's available next month — I can reserve it now.\"",
               "\"Let me find out for you.\"",
               "\"Logging out should fix that quickly!\"",
               "\"Here's what I can do for you.\"",
               "\"I can book that for you at the member rate.\"",
               "\"Let me get someone who can authorise that.\""],
           kicker="THE HIGHEST-LEVERAGE HABIT IN THIS COURSE",
           note="Positive language does not mean saying yes. It means directing the customer to what IS available — with the same underlying answer.")
tile_grid("Managing Yourself Across a Shift", [
    ("Emotional contagion", "Your mood transfers to the customer within seconds — and theirs to you."),
    ("Reset between customers", "One breath and a deliberate posture reset stops case 11 inheriting case 10's frustration."),
    ("Micro-breaks work", "Short structured breaks measurably protect service quality later in the shift."),
    ("Depersonalise the complaint", "They are angry at the situation, at the company, at their day — not at you."),
    ("Resilience is trainable", "Absorb criticism, extract the useful part, discard the rest, start clean."),
    ("Know your own tells", "Flat tone, short answers, no eye contact — learn to catch your own fatigue signals.")],
    kicker="STAYING ENERGISED AND POSITIVE", cols=2, size=13)
mark("act2"); a = ACTIVITIES[1]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

brk("Tea Break", "15 minutes")

# ---------------------------------------------------------------- TOPIC 3
T = C.TOPICS[2]; mark("topic3")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
img_points("Active Listening — Making Listening Visible", "listening_funnel.png", [
    ("Attend", "Full attention. Phone down, body turned, eyes up. Half-attention is detected instantly."),
    ("Absorb", "Let them finish. The vent almost always contains the key fact."),
    ("Paraphrase", "Say it back in your own words — this is what makes listening visible."),
    ("Confirm, then act", "'Have I got that right?' Only after a yes do you propose a solution.")],
    kicker="THE CORE SERVICE SKILL", img_w=6.9,
    note="Only 17% of customers believe businesses actually listen to them — paraphrasing is the cheapest way to be in the other 83%.")
split_note("Questioning — Open to Explore, Closed to Confirm",
           "CLOSED QUESTIONS (confirm)", [
               "\"Is the account under your name?\"",
               "\"Did you receive the confirmation email?\"",
               "\"Would Tuesday work for delivery?\"",
               "Use to: pin down facts, confirm, close a decision.",
               "Risk: asking these first makes it an interrogation."],
           "OPEN QUESTIONS (explore)", [
               "\"Walk me through what happened.\"",
               "\"What were you expecting to see?\"",
               "\"How is this affecting your work?\"",
               "Use to: surface the real need and the emotion behind it.",
               "Rule: if it can be answered yes/no, rewrite it."],
           kicker="DIAGNOSE BEFORE YOU PRESCRIBE",
           note="Open first to understand, closed second to confirm. Reversing the order is the most common needs-identification failure.")
img_points("The Four Levels of Addressing Customer Needs", "four_levels.png", [
    ("1 · Understand", "Diagnose the actual problem before offering any solution."),
    ("2 · Meet the basic need", "Deliver what was promised, accurately and on time. Non-negotiable."),
    ("3 · Outside the box", "Find a route when the standard answer is 'no'."),
    ("4 · The extra mile", "Give what was never asked for but was exactly what was needed.")],
    kicker="A LADDER, NOT A MENU", img_w=6.7,
    note="Level 4 delivered while level 2 is failing reads as a distraction — you cannot skip the rungs.")
img_points("What They Said vs What They Need", "said_vs_needed.png", [
    ("Complaints are symptoms", "The stated problem is where they started, not where the need lives."),
    ("Functional vs emotional", "The product must work AND the customer must feel valued."),
    ("Listen for the deadline", "The real brief is often the last sentence, not the first."),
    ("Attentiveness reads patterns", "The same complaint from many customers is a defect report.")],
    kicker="THE INFERENCE THAT MATTERS", img_w=7.2)
mark("act3"); a = ACTIVITIES[2]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

# ---------------------------------------------------------------- TOPIC 4
T = C.TOPICS[3]; mark("topic4")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
split_note("In-Person Service — Strengths and Limits",
           "THE LIMITATIONS", [
               "No automatic record — if you don't write it down, it didn't happen.",
               "Queueing pressure: everyone waiting sees how long you take.",
               "You can only serve one person at a time.",
               "Scheduling conflicts and walk-in unpredictability.",
               "Harder to escalate discreetly with an audience present."],
           "THE ADVANTAGES", [
               "Immediate feedback — misunderstandings die in seconds.",
               "Full non-verbal bandwidth: posture, expression, timing.",
               "Strongest channel for building trust and rapport.",
               "Easiest channel on which to de-escalate genuine anger.",
               "You can show, demonstrate and hand over physically."],
           kicker="CHOOSING FACE-TO-FACE",
           note="The channel's great weakness is memory: always follow a face-to-face resolution with a written summary.")
cards4("Body Language You Control", [
    ("POSTURE", "Open and uncrossed, with a slight forward lean. Signals engagement and honesty."),
    ("EYE CONTACT", "Around 70% of the time. Constant staring intimidates; avoidance reads as dishonesty."),
    ("MIRRORING", "Subtly match their pace and energy. Builds rapport below conscious awareness."),
    ("THE SMILE", "Genuine and brief at greeting. It sets the emotional tone for everything after.")],
    kicker="THE NON-VERBAL CHANNEL",
    note="Signals that cost you trust: crossed arms, glancing at your phone, turning your torso away, or a fixed forced smile.")
stack_slide("Handling a Walk-In While You Are Already Busy", [
    ("Acknowledge within 3 seconds", "Eye contact, a raised hand, 'I'll be right with you.' Being SEEN precedes being served."),
    ("Give a realistic wait", "'About two minutes' buys you two minutes. A vague wait buys you nothing."),
    ("Protect the active customer", "The person you are serving keeps priority — say so openly so the queue hears the rule."),
    ("Note your park point", "Record where you stopped so you resume without making anyone repeat themselves."),
    ("Return and reference", "Open with what they told you: 'you mentioned a cracked screen' proves you were listening."),
    ("Close with next steps", "Summarise what happens now, so they leave with certainty rather than hope.")],
    kicker="THE PARK AND RETURN METHOD", accent=TEAL,
    note="Making a customer re-explain their problem is the single failure this method exists to prevent.")
mark("act4"); a = ACTIVITIES[3]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

brk("Lunch Break", "1:00pm – 2:00pm")

# ---------------------------------------------------------------- TOPIC 5
T = C.TOPICS[4]; mark("topic5")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
img_points("The Professional Call — Six Stages", "phone_flow.png", [
    ("Greet and listen", "Within three rings, smile first, then let them finish without interruption."),
    ("Paraphrase and confirm", "Say the whole issue back. Wait for their yes before moving on."),
    ("Hold properly", "Ask, explain, give a duration, thank them on return. All four, every time."),
    ("Resolve and close", "Options with a recommendation, then a time, an owner and a reference number.")],
    kicker="THE CALL STRUCTURE", img_w=7.4)
split_note("Telephone Service — What Loses and Wins Calls",
           "WHAT LOSES THE CALL", [
               "Interrupting to defend the company mid-vent.",
               "Silent hold with no reason and no time given.",
               "Reading a rigid script — it sounds robotic instantly.",
               "Jargon and internal system names.",
               "Vague closes: 'we'll look into it and get back to you.'",
               "Transferring without explaining or introducing."],
           "WHAT WINS THE CALL", [
               "Letting the first 30–45 seconds run — the key fact is in there.",
               "Smiling before you speak — it changes your voice audibly.",
               "Using their name naturally, two or three times.",
               "Paraphrasing before proposing anything.",
               "A specific time, a named owner and a reference number.",
               "One proactive follow-up call, made whether or not it worked."],
           kicker="TELEPHONE ETIQUETTE",
           note="With no visual channel, tone and pace do all the work that posture and expression do in person.")
stack_slide("Placing a Customer on Hold — the Four Parts", [
    ("Ask permission", "'May I put you on hold for a moment?' — then actually wait for the answer."),
    ("State the reason", "'…while I get my supervisor to authorise the re-route.' Reason converts waiting into progress."),
    ("Give a realistic duration", "'About three minutes.' Then beat it, or come back and re-contract."),
    ("Thank them on return", "'Thank you for waiting.' Missing this one part makes the whole hold feel like being dumped.")],
    kicker="WHERE MOST CALLS ARE LOST", accent=AMBER,
    note="A hold is a permission you are granted, not an action you perform on the customer.")
mark("act5"); a = ACTIVITIES[4]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

# ---------------------------------------------------------------- TOPIC 6
T = C.TOPICS[5]; mark("topic6")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
img_points("The Anatomy of a Service Email", "email_anatomy.png", [
    ("Greeting", "Their name, always. 'Dear Customer' announces that nobody read the file."),
    ("Acknowledge", "Name the wait, the prior contacts and the real deadline before anything else."),
    ("Solution", "A calendar date, not a working-day range. Ranges read as evasion."),
    ("Next steps + sign-off", "Who does what by when — signed by a real, named person.")],
    kicker="THE FIVE-PART STRUCTURE", img_w=7.0)
split_note("Netiquette — What Breaks a Service Email",
           "NEVER", [
               "ALL CAPS — it reads as shouting.",
               "'Dear Customer' when you have their name on file.",
               "Policy citations as an answer ('per T&C 7.3').",
               "'Please do not email again' — you just closed their only channel.",
               "Unsigned 'Support Team' with no human name.",
               "Dead subject lines: 'RE: RE: FW: order'."],
           "ALWAYS", [
               "A clear, action-oriented subject line.",
               "Their name, and a reference to their history with you.",
               "Plain language — explain the policy, don't cite it.",
               "A concrete date and a named owner.",
               "A real signature: name, role, direct contact.",
               "A proofread pass before you send."],
           kicker="WRITTEN TONE IS A SERVICE SKILL",
           note="An email can be 100% factually correct and still be a total service failure — accuracy is not the same as service.")
img_points("Choosing the Right Channel", "channel_matrix.png", [
    ("Phone", "Complex and urgent, or emotionally charged. Voice carries what text cannot."),
    ("Live chat", "Simple and urgent — one quick question, answered in real time."),
    ("Email", "Complex, not urgent, needs attachments and a durable written record."),
    ("Self-service", "Simple and not urgent — FAQ and help centre, available at 3am.")],
    kicker="MATCH THE CHANNEL TO THE ISSUE", img_w=6.8,
    note="Best practice for a time-critical emotional issue: call first, then confirm in writing — use each channel for what it does well.")
mark("act6"); a = ACTIVITIES[5]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

brk("Tea Break", "15 minutes")

# ================================================================ LU2
section("LEARNING UNIT 2", "Improving Customer's Needs Based on Feedback",
        "2", "LO2 · Identify and recommend areas for improvement from feedback and operational insight")

# ---------------------------------------------------------------- TOPIC 7
T = C.TOPICS[6]; mark("topic7")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
img_points("Feedback Channels — Reach vs Diagnostic Depth", "feedback_channels.png", [
    ("Surveys reach widest", "CSAT/NPS/CES cover many customers but rarely explain WHY."),
    ("Interviews go deepest", "Few customers, but they surface the mechanism behind the score."),
    ("Staff reports are gold", "Frontline staff see causes that customers only experience as symptoms."),
    ("Triangulate always", "No single channel does both — one channel alone fixes the wrong thing.")],
    kicker="K2 · CUSTOMER FEEDBACK CHANNELS", img_w=7.0)
table_slide("The Three Service Metrics — and What Each Actually Measures",
            ["Metric", "The question it asks", "What it is good for", "Its blind spot"],
            [("CSAT", "How satisfied were you with this interaction?",
              "A specific moment — one agent, one ticket, one visit.",
              "Says nothing about the overall relationship."),
             ("NPS", "How likely are you to recommend us?",
              "The whole relationship and word-of-mouth risk.",
              "One number; gives no reason without a follow-up question."),
             ("CES", "How much effort did you have to spend?",
              "Predicts disloyalty better than satisfaction does.",
              "Focuses on friction, not on delight or emotional loyalty.")],
            kicker="MEASURING SERVICE", widths=[0.11, 0.29, 0.32, 0.28], fsize=12,
            note="Use them together: CSAT for the moment, NPS for the relationship, CES for the friction.")
img_points("Most Unhappy Customers Never Complain", "complaint_iceberg.png", [
    ("~4% complain", "Only a small fraction ever tell you there is a problem."),
    ("~56% say nothing", "They do not complain, do not answer the survey — they just stop coming back."),
    ("Silence is not health", "The absence of complaints is not evidence of satisfaction."),
    ("Go and look", "If you only react to complaints, you are managing the visible 4%.")],
    kicker="THE SILENT MAJORITY", img_w=6.4)
img_points("Closing the Loop — the Only Cycle That Changes Anything", "closed_loop.png", [
    ("Collect", "Across every channel, deliberately — including from your own staff."),
    ("Analyse", "Separate symptoms from root causes. The wait is a symptom; the staffing gap is the cause."),
    ("Act", "An owner, a date and a measure. Anything less is an intention, not an action."),
    ("Tell them", "The step everyone forgets — and the only one the customer can see.")],
    kicker="K2 + A3 · FROM FEEDBACK TO IMPROVEMENT", img_w=6.4,
    note="Feedback with no visible action trains customers to stop giving it — and your early-warning system goes dark.")
tile_grid("Operational and Personnel Feedback Channels (K3)", [
    ("Shift huddles and briefings", "Short, daily, structured — the fastest route from frontline observation to action."),
    ("Frontline incident logs", "A written record of what actually happened, not what the system recorded."),
    ("Team retrospectives", "Regular review of what broke and why, with an owner assigned to each fix."),
    ("Internal escalation reports", "Patterns in what gets escalated reveal where authority is missing."),
    ("Quality assurance scorecards", "Reviewed interactions scored for tone, clarity and accuracy."),
    ("Suggestion and defect channels", "A formal route so a known bug never sits in a WhatsApp group for months.")],
    kicker="WHERE OPERATIONAL INSIGHT COMES FROM", cols=2, size=13,
    note="Customer channels tell you WHAT went wrong. Personnel channels are usually the only ones that tell you WHY.")
mark("act7"); a = ACTIVITIES[6]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

# ---------------------------------------------------------------- TOPIC 8
T = C.TOPICS[7]; mark("topic8")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
img_points("HEARD — the De-escalation Framework", "heard_framework.png", [
    ("Hear then Empathize", "Let them finish, then name the actual loss — not 'the inconvenience'."),
    ("Apologize unconditionally", "No 'if', no 'but'. A conditional apology is heard as a denial."),
    ("Resolve concretely", "An offer with a time and an owner, made now rather than promised later."),
    ("Diagnose the cause", "Fix the process so the next customer never meets this problem.")],
    kicker="THE RECOVERY SEQUENCE", img_w=7.4)
table_slide("Two Recovery Frameworks — HEARD and LAST",
            ["Stage", "HEARD", "LAST", "What it achieves"],
            [("1", "Hear", "Listen", "The customer gets to finish — and you get the real facts."),
             ("2", "Empathize", "Apologize", "The customer's experience is acknowledged as legitimate."),
             ("3", "Apologize", "Solve", "Ownership is taken and a concrete route forward appears."),
             ("4", "Resolve", "Thank", "The problem is fixed — and surfacing it is treated as a favour."),
             ("5", "Diagnose", "—", "The root cause is closed so it cannot recur.")],
            kicker="PICK ONE AND USE IT CONSISTENTLY", widths=[0.08, 0.17, 0.17, 0.58], fsize=12.5,
            note="LAST is faster for a live counter or call; HEARD adds the Diagnose step that prevents the recurrence.")
cards4("Perceived Justice — What the Customer Is Actually Judging", [
    ("OUTCOME", "Did I get a fair result? The refund, the replacement, the fix. Usually the only part organisations measure."),
    ("PROCESS", "Was it fair and reasonable to get there? How long, how many repeats, how many transfers."),
    ("TREATMENT", "Was I treated with respect and taken seriously? Often the part that decides whether they return."),
    ("THE TRAP", "Fix the outcome, fail the other two, and the customer still leaves — while your metrics show a resolved case.")],
    kicker="WHY A CORRECT FIX CAN STILL FAIL",
    note="When you cannot change the outcome, process and treatment are still entirely within your control.")
stack_slide("Managing Yourself in the Difficult Conversation", [
    ("Establish common ground first", "'We both want this resolved fairly today' turns an opponent into a co-problem-solver."),
    ("Depersonalise", "They are angry at the situation and the company. Absorbing it as a personal attack costs you the next customer too."),
    ("Control your physiology", "Slow the breath, slow the speech, drop the volume. Composure IS the de-escalation tool."),
    ("Set limits once, calmly", "State clearly what you can and cannot do. Repeating it or defending it invites haggling."),
    ("Never haggle over a loss", "Give the maximum you can authorise immediately, then escalate the rest openly and on their side."),
    ("Close the loop afterwards", "Tell them what changed a week later. That single follow-up converts detractors.")],
    kicker="COMMON GROUND · LIMITS · EMOTIONS", accent=VIOLET)
mark("act8"); a = ACTIVITIES[7]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

# ---------------------------------------------------------------- TOPIC 9
T = C.TOPICS[8]; mark("topic9")
section(f"TOPIC {T['code']}", T["title"], T["code"], T["subtitle"])
concept_slide(T)
img_points("Where the Line Is — Anger vs Abuse", "escalation_ladder.png", [
    ("Anger attacks the problem", "Loud, frustrated, even rude about the situation — still serviceable."),
    ("Abuse attacks the person", "Slurs, personal or discriminatory attacks. This is the threshold."),
    ("Threats escalate instantly", "Legal threats go to a manager; physical threats end the interaction."),
    ("Do not wait to feel unsafe", "If you wait for physical fear, you have already served through the abuse.")],
    kicker="THE ESCALATION THRESHOLD", img_w=7.2)
split_note("Two Kinds of Escalation — Know Which One You Need",
           "FUNCTIONAL (sideways)", [
               "The issue needs EXPERTISE you do not have.",
               "Technical faults, billing calculations, specialist products.",
               "Goes to a specialist team, not up the hierarchy.",
               "The customer is reasonable — the problem is hard.",
               "Introduce the specialist and hand over the context."],
           "HIERARCHICAL (upward)", [
               "The issue needs AUTHORITY you do not have.",
               "Goodwill beyond your limit, policy exceptions, abuse.",
               "Goes to a supervisor or duty manager.",
               "The problem may be simple — your mandate is the constraint.",
               "Brief your supervisor before they meet the customer."],
           kicker="K3 · THE ESCALATION DECISION",
           note="Same customer and same complaint can need either route — diagnose whether you are short of expertise or short of authority.")
stack_slide("The Three-Strike Rule in Practice", [
    ("Warning one — name the behaviour", "'I want to help you with this, but I can't continue if you speak to me that way.' Calm, specific, never sarcastic."),
    ("Warning two — state the consequence", "'If that continues I'll need to hand this to my supervisor and end our conversation.'"),
    ("Act on it", "Escalate or end. A warning you do not act on teaches the customer that the boundary is fictional."),
    ("Immediate escalation overrides", "Slurs, discriminatory abuse and any physical threat skip the warnings entirely."),
    ("Withdraw properly", "Hand over in front of the customer, then physically step away. Do not keep serving after escalating."),
    ("Document verbatim", "Date, time, exact words, witnesses, CCTV reference. Paraphrase destroys the evidence.")],
    kicker="SETTING AND HOLDING THE BOUNDARY", accent=RED)
tile_grid("Your Legal Protection in Singapore", [
    ("POHA 2014", "The Protection from Harassment Act criminalises harassment, including abuse of workers at work."),
    ("TAFEP", "The Tripartite Alliance for Fair & Progressive Employment Practices takes workplace harassment reports."),
    ("Police report", "Threats of violence and serious harassment are criminal matters, not service problems."),
    ("Employer duty", "Your employer is responsible for providing a workplace safe from harassment."),
    ("Documentation is evidence", "Verbatim wording, times and witnesses are what any report will turn on."),
    ("Aftercare is not optional", "A break, a supervisor debrief and a next-day follow-up after an abusive incident.")],
    kicker="YOU ARE NOT REQUIRED TO ABSORB ABUSE", cols=2, size=13,
    note="'It's part of the job' is not the standard. Singapore law explicitly protects public-facing workers.")
mark("act9"); a = ACTIVITIES[8]
case_slide(a, T); questions_slide(a, T); debrief_slide(a, T)

# ---------------------------------------------------------------- CLOSE
mark("close")
section("WRAP-UP", "Course Summary & Next Steps", "")
tile_grid("What You Achieved Today", [
    ("Understood the service chain", "External and internal customers, and why service quality is a chain not a department. (LO1)"),
    ("Built a service attitude", "Appearance, smile, energy, positivity and positive language under pressure. (LO1)"),
    ("Identified customer needs", "Active listening, open questioning, and the four levels of addressing needs. (LO1)"),
    ("Served across every channel", "In person, on the phone, and in writing — matching channel to issue. (LO1)"),
    ("Turned feedback into improvement", "Feedback channels, closing the loop, and root cause vs symptom. (LO2)"),
    ("Recovered and escalated safely", "HEARD and LAST, perceived justice, the three-strike rule and POHA. (LO2)")],
    kicker="LEARNING OUTCOMES DELIVERED", cols=1, size=12.5)
big_statement("The absence of complaints is not evidence of satisfaction.",
              "Go and look. Ask your customers, ask your frontline, and close the loop where it matters.",
              "THE ONE THING TO REMEMBER", color=TEAL)
support_slide()

mark("assessment")
final_assessment_slide(kicker="ASSESSMENT · REMINDER")
flow_h("Assessment Flow", C.ASSESSMENT_FLOW, kicker="ON ASSESSMENT DAY")
attendance_slide()
big_statement("Thank You!",
              "You can now collect customer feedback, read what it actually says, and turn it into service that keeps customers.",
              "SEE YOU AT THE COUNTER", color=TEAL)
mark("end")

# ---------------------------------------------------------------- MOTION
# One transition family for the whole deck: content = fade (fast),
# section dividers = push (medium). Applied in a single pass so every
# slide is covered exactly once.
from pptx.oxml.ns import qn
from lxml import etree

def _transition(s, kind="fade", speed="med"):
    sld = s._element
    for old in sld.findall(qn("p:transition")):
        sld.remove(old)
    tr = etree.SubElement(sld, qn("p:transition"))
    tr.set(qn("p14:dur") if False else "spd", speed)
    tr.set("advClick", "1")
    etree.SubElement(tr, qn(f"p:{kind}"))

DIVIDER_TITLES = set()
for i, s in enumerate(prs.slides):
    # a divider has the tall left bar and a big faint number; detect by shape count
    is_divider = len(s.shapes) <= 8
    _transition(s, "push" if is_divider else "fade", "med" if is_divider else "fast")

OUT = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
prs.save(OUT)
with open(os.path.join(HERE, "slide_map.json"), "w") as f:
    json.dump(SLIDE_MAP, f, indent=1)
print(f"Saved {OUT}  ({PAGE['n']} slides)")
print("Slide map:", json.dumps(SLIDE_MAP))
