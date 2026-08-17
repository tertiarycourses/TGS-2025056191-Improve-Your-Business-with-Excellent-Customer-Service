"""
SINGLE SOURCE OF TRUTH — Improve Your Business with Excellent Customer Service.

Every artifact (PPT, Lesson Plan, Learner Guide, activities/) is generated from
this module plus data_domain1.py + data_domain2.py so they stay 100% aligned
with the approved Course Proposal (TPG-2025092324) and the assessment set
(OQ 30 min + RP 30 min).

Course design: 1 training day = 7 h classroom facilitation + 1 h assessment.
TSC: Customer Service Innovation Management (EPW-CEX-3034-1.1).

Content is sourced from the approved legacy deck (v1, 85 slides) and deepened
from current industry practice: Zendesk, Help Scout, Qualtrics, SurveyMonkey,
Coursera, Tidio, Intercom, Indeed SG and Global Response.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Improve Your Business with Excellent Customer Service"
SHORT_TITLE  = "Improve Your Business with Excellent Customer Service"
COURSE_CODE  = "TGS-2025056191"
VERSION      = "v2.0"
VERSION_DATE = "17 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1

# Skills Framework alignment
TSC_TITLE = "Customer Service Innovation Management"
TSC_CODE  = "EPW-CEX-3034-1.1"
TSC_ABILITIES = [
    ("A1", "Carry out collection of customer feedback on service"),
    ("A2", "Determine customer's needs and expectations in relation to products and services"),
    ("A3", "Determine areas of improvement as per customer feedback"),
]
TSC_KNOWLEDGE = [
    ("K1", "Principles of effective communication"),
    ("K2", "Customer feedback channels"),
    ("K3", "Operation and process personnel feedback channels"),
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Collect and analyse customer feedback to assess needs and expectations using effective communication principles.",
    "LO2: Identify and recommend areas for improvement based on customer feedback and operational insights.",
]

# ------------------------------------------------------------------ learning units
LEARNING_UNITS = [
    dict(num=1, title="Customer's Needs and Feedback",
         lo="LO1", ka="K1, K2, A1, A2", hours="4 hrs",
         topics="Topics 1–6"),
    dict(num=2, title="Improving Customer's Needs Based on Feedback",
         lo="LO2", ka="K3, A3", hours="3 hrs",
         topics="Topics 7–9"),
]

# ------------------------------------------------------------------ topics
# num, code, title, subtitle, weighting, concepts [(title, caption) tuples]
TOPICS = [
    dict(num=1, code="01", lu=1,
         title="Understanding Customers & Customer Service",
         subtitle="Who customers are · what service is · who provides it · the service-profit chain",
         weighting="LU1 · K1 · 40 min",
         concepts=[
            ("Service is every interaction", "Customer service is the whole of the support a customer receives before, during and after a purchase — not just the complaint desk."),
            ("External and internal customers", "External customers buy from you; internal customers are colleagues who depend on your output. Both are served."),
            ("Service quality is a chain", "Internal support enables frontline delivery, which shapes customer experience, which drives loyalty and revenue."),
            ("Service is a growth centre", "Help Scout: great service is a growth centre, not a cost centre — retention, referral and lifetime value all flow from it."),
            ("The cost of getting it wrong", "86% of customers stop buying after poor experiences; US firms lose over US$62 billion a year to bad service (Help Scout)."),
            ("Four principles of good service", "Help Scout: service must be personalised, competent, convenient and proactive — all four, or the experience breaks."),
         ]),
    dict(num=2, code="02", lu=1,
         title="Establishing Your Service Attitude",
         subtitle="Appearance · the power of a smile · staying energised · staying positive · positive language",
         weighting="LU1 · K1 · 40 min",
         concepts=[
            ("Attitude is visible instantly", "First impressions form in 4–7 seconds; roughly 55% of that impression comes from appearance and body language."),
            ("Emotions are contagious", "Your mood transfers to the customer. A genuine smile measurably raises trust and how welcome a guest feels."),
            ("Positive language reframes limits", "'That's back-ordered' becomes 'That's available next month — I can reserve it now.' Same fact, different outcome."),
            ("Energy must be managed", "Service quality decays with fatigue. Structured micro-breaks and shift resets protect the last customer of the day."),
            ("Resilience is a trained skill", "Zendesk lists resilience as core: absorbing criticism without letting it degrade the next interaction."),
            ("Professionalism is the baseline", "Respectful tone, accuracy and appropriate boundaries held consistently — regardless of how the customer behaves."),
         ]),
    dict(num=3, code="03", lu=1,
         title="Identifying and Addressing Customer Needs",
         subtitle="Active listening · questioning · the four levels of need · going the extra mile",
         weighting="LU1 · K1, A2 · 50 min",
         concepts=[
            ("Needs are functional and emotional", "The product must work (functional) and the customer must feel valued (emotional). Missing either loses the customer."),
            ("Active listening is the core skill", "Attend fully, paraphrase back, read the cues, then confirm. Only 17% of customers believe businesses actually listen (Tidio)."),
            ("Ask before you prescribe", "Open questions surface the real need; closed questions confirm it. Diagnosing before solving prevents the wrong fix."),
            ("Attentiveness reads the unsaid", "Repeated 'I couldn't find it' across customers is a UX defect report, not a series of individual questions."),
            ("Four levels of addressing needs", "Understand the problem → meet the basic need → think outside the box → go the extra mile."),
            ("Personalisation drives loyalty", "Use history and context; 35% would rather deal with an AI than repeat themselves to a human (Salesforce)."),
         ]),
    dict(num=4, code="04", lu=1,
         title="In-Person Customer Service",
         subtitle="Walk-ins and at-your-desk requests · body language · advantages and limits of face-to-face",
         weighting="LU1 · K1, A1 · 45 min",
         concepts=[
            ("Face-to-face is highest bandwidth", "Tone, posture, expression and timing all carry meaning that text channels strip away."),
            ("Immediate feedback loop", "Misunderstandings surface and are corrected within seconds — the strongest advantage over email or chat."),
            ("Body language you control", "Open posture, ~70% eye contact, a slight forward lean and subtle mirroring build rapport without a word."),
            ("Signals that cost you trust", "Crossed arms, glancing at a phone, turning away or a fixed forced smile all read as disengagement."),
            ("Acknowledge within seconds", "Greet a walk-in within about 3 seconds even when occupied; being seen matters before being served."),
            ("The limits of in-person", "No automatic record, queueing pressure and scheduling conflicts — document afterwards or it never happened."),
         ]),
    dict(num=5, code="05", lu=1,
         title="Customer Service Over the Phone",
         subtitle="Telephone etiquette · voice as the whole channel · hold and transfer · call structure",
         weighting="LU1 · K1, A1 · 45 min",
         concepts=[
            ("Voice carries everything", "With no visual channel, tone, pace and warmth do all the work that body language does in person."),
            ("Phone still dominates complex issues", "When an issue needs back-and-forth clarification, customers still reach for the phone over text channels."),
            ("Etiquette is measurable", "Answer within three rings, smile while speaking, never interrupt, avoid jargon, always close with next steps."),
            ("Hold is a permission, not an action", "Ask before holding, explain why, give a time, thank them on return — otherwise it reads as being dumped."),
            ("Paraphrase to prove you listened", "'So the order was due Monday and hasn't arrived' converts a vent into a defined, solvable problem."),
            ("Scripts guide, they don't speak", "Rigid scripts sound robotic. Use them as a spine and personalise the words to the caller in front of you."),
         ]),
    dict(num=6, code="06", lu=1,
         title="Customer Service via Email and Chat",
         subtitle="Netiquette · email structure · written tone · choosing between email and live chat",
         weighting="LU1 · K1, K2, A1 · 40 min",
         concepts=[
            ("Writing is a service skill", "'You have to log out first' and 'Logging out should fix that quickly!' carry identical information and opposite tone."),
            ("Email creates the record", "The written trail is the channel's real advantage: the customer can re-read it and you can prove what was agreed."),
            ("Netiquette rules are not optional", "No ALL CAPS, no unexplained jargon, a clear action-oriented subject line and a real signature block."),
            ("A five-part email structure", "Personalised greeting → acknowledge the issue → give the solution → state next steps → professional sign-off."),
            ("Email vs live chat", "Email suits complex, documented, attachment-bearing issues; chat suits short, real-time, single-question issues."),
            ("Proofread before you send", "Grammar and spelling errors read as carelessness and quietly transfer to how the customer rates your competence."),
         ]),
    dict(num=7, code="07", lu=2,
         title="Generating Return Business from Feedback",
         subtitle="Feedback channels · closing the loop · complaint handling · retention economics",
         weighting="LU2 · K2, A1, A3 · 55 min",
         concepts=[
            ("Retention beats acquisition", "Keeping a customer costs far less than winning a new one; a 5% retention lift can move profit 25–95%."),
            ("Feedback channels are a portfolio", "Surveys, reviews, interviews, social listening, support tickets and staff reports — each has a bias, so triangulate."),
            ("CSAT, NPS and CES measure differently", "CSAT rates a moment, NPS rates the relationship, CES rates the effort the customer had to spend."),
            ("Most unhappy customers say nothing", "Roughly 56% leave silently. The absence of complaints is not evidence of satisfaction."),
            ("Closing the loop is the point", "Collect → analyse → act → tell the customer what changed. Feedback with no visible action trains people to stop giving it."),
            ("Recovery can beat no failure at all", "A well-recovered failure often leaves the customer more loyal than a customer who never had a problem."),
         ]),
    dict(num=8, code="08", lu=2,
         title="Recovering Difficult Customers",
         subtitle="De-escalation · HEARD and LAST · common ground · limits · managing your own emotions",
         weighting="LU2 · K1, K3, A3 · 50 min",
         concepts=[
            ("Recovery restores the relationship", "The goal is not only to fix the fault but to rebuild the trust the fault destroyed."),
            ("HEARD framework", "Hear · Empathize · Apologize · Resolve · Diagnose — let them finish, then act, then prevent the recurrence."),
            ("LAST framework", "Listen · Apologize · Solve · Thank — thank them for surfacing a problem you would otherwise not have seen."),
            ("Perceived justice has three parts", "Customers judge the outcome, the process and how they were treated. Fix the fault and still fail on the last two."),
            ("Establish common ground", "'We both want this resolved fairly today' converts an adversarial exchange into a shared problem."),
            ("Manage yourself first", "Detach from the personal, control breathing and pace, keep language neutral. Composure is the de-escalation tool."),
         ]),
    dict(num=9, code="09", lu=2,
         title="Understanding When to Escalate",
         subtitle="Functional vs hierarchical escalation · triggers · the three-strike rule · documentation · POHA",
         weighting="LU2 · K3, A3 · 45 min",
         concepts=[
            ("Escalation is a decision, not a failure", "Handing over to the right authority or expertise faster is better service than struggling on alone."),
            ("Functional vs hierarchical", "Functional escalation goes sideways to expertise; hierarchical escalation goes upward to authority."),
            ("Angry is not the same as abusive", "An angry customer attacks the problem. An abusive customer attacks you — that line is the escalation trigger."),
            ("Know the trigger behaviours", "Vulgarity, personal insults, discriminatory remarks, legal threats and any threat of physical harm."),
            ("The three-strike rule", "Two clear, calm warnings that the behaviour must stop, then escalate or end the interaction."),
            ("Singapore protects service staff", "POHA 2014 criminalises workplace harassment; incidents can go to TAFEP or the police. Document everything."),
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Understanding customers, collecting feedback, and turning it into service improvement",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Oral Questioning (OQ) — 3 open-ended questions covering K1, K2 and K3. 30 minutes, individual, open book.",
    practical="Role Play (RP) — 2 simulated customer interactions covering A1, A2 and A3. 30 minutes, individual, open book.",
    note="A minimum of 75% attendance is required, and the candidate must be assessed Competent in both instruments, to be eligible for funding.",
)

ASSESSMENT_FLOW = [
    "TRAQOM Survey",
    "Assessment Digital Attendance",
    "Assessment (OQ then RP)",
    "Submit on the LMS",
    "Sign the Assessment Summary Record",
]
