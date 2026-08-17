"""
LU2 activities — Improving Customer's Needs Based on Feedback (Topics 7-9).

Same contract as data_domain1.py: real Singapore case studies with scenario,
discussion questions, trainer debrief, LG-only step-by-step, and a test.
"""

DOMAIN2 = [
    dict(
        num=7, topic=7, minutes=20,
        title="Closing the Loop — F&B Chain Losing Repeat Customers",
        type="Case Study + Group Presentation",
        objective="LO2 · K2, K3, A1, A3 · Analyse multi-channel feedback, find root causes, and build a closed-loop improvement plan.",
        desc=("Learners work with a realistic mixed feedback set — reviews, survey scores, ticket data and staff "
              "comments — to identify root causes and build a retention plan with owners, timelines and measures."),
        scenario=(
            "Kopi & Co is a Singapore café chain with 9 outlets. Repeat-customer rate has fallen 15% this quarter. "
            "Management wants a recovery plan. Here is the feedback that exists:\n\n"
            "GOOGLE REVIEWS (rating fell 4.4 → 3.8): 'Waited 25 min for a flat white at Raffles Place, staff seemed "
            "overwhelmed.' · 'Ordered on the app, got the wrong drink twice.' · 'Nobody acknowledged me at the counter "
            "for 5 minutes.' · 'Food is still great, service has really slipped.'\n\n"
            "POST-VISIT SURVEY (CSAT 62%, down from 81%): lowest-scoring item is 'speed of service' (48%); highest is "
            "'product quality' (91%). Only 4% of visitors complete the survey.\n\n"
            "SUPPORT TICKETS: app order errors up 3x since the June app update. 70% of tickets are wrong-item.\n\n"
            "STAFF FEEDBACK (from a shift-leader WhatsApp group, never formally collected): 'The new app sends orders "
            "to the bar without the modifier field.' · 'We lost 2 baristas at Raffles Place in May, still not "
            "replaced.' · 'Nobody from HQ has asked us anything.'\n\n"
            "Nothing has been fed back to any customer who left a review or completed a survey."
        ),
        roles="Groups of 4–5. Each group presents a 3-minute plan to the class acting as management.",
        build="A closed-loop improvement plan: root causes, 3+ strategies, owners, timeline and success measures.",
        services="Feedback analysis grid · Closed-loop plan template",
        flow=["Sort the feedback", "Find root causes", "Separate cause from symptom", "Build the plan", "Present"],
        questions=[
            "Sort every piece of feedback by CHANNEL. What is each channel good at capturing, and what does each one miss?",
            "Only 4% complete the survey and CSAT is 62%. What is wrong with concluding '62% of our customers are satisfied'?",
            "Separate SYMPTOMS from ROOT CAUSES. The 25-minute wait is a symptom — what is causing it?",
            "The staff feedback identifies the app modifier bug that support tickets only show as 'wrong item'. What does that tell you about operational feedback channels?",
            "Not one customer who left feedback has heard anything back. What does that cost, beyond this quarter?",
            "Build the plan: at least 3 strategies, each with an owner, a timeline and a success measure. What will you measure, and when will you know it worked?",
        ],
        debrief=[
            "Channel biases: reviews capture the extremes (delighted and furious) and skew negative; surveys capture the compliant middle; tickets capture only what customers bothered to report; staff feedback captures CAUSES the other three only show as symptoms.",
            "4% response rate means severe non-response bias — and roughly 56% of unhappy customers never complain at all. 62% CSAT is the score of the 4% willing to answer, not of the customer base.",
            "Root causes are: (1) the June app update dropped the modifier field, (2) Raffles Place is 2 baristas short since May, (3) there is no closed loop so nothing gets fixed. The 25-minute wait and the wrong drinks are downstream of these.",
            "The staff channel had the highest-value diagnostic information in the whole case — and it was sitting in an informal WhatsApp group because no formal operational feedback channel exists. This is exactly K3.",
            "Silence costs the future: customers who give feedback and see nothing change stop giving feedback, and the early-warning system goes dark. The 15% drop is what you can see; the lost channel is what you cannot.",
            "A good plan is specific: 'Ops Manager fixes the modifier field by 5 Sept, measured by wrong-item tickets falling below 10/week' beats 'improve the app'. Push every group to name an owner, a date and a number.",
        ],
        steps=[
            ("Form groups of 4–5. On a flip chart, draw a four-column grid: REVIEWS · SURVEY · TICKETS · STAFF.", ""),
            ("Place every piece of feedback from the case into its column. Then, under each column, write one line on what that channel is GOOD at seeing and one line on what it is BLIND to.", ""),
            ("Discuss the 4% response rate. Write down explicitly why 62% CSAT cannot be read as '62% of customers are satisfied' — name the non-response bias and the silent-majority effect.", ""),
            ("Draw a second area: SYMPTOMS on the left, ROOT CAUSES on the right. Move each item across only when you can state the mechanism. '25-minute wait' moves to the right only as 'Raffles Place is 2 baristas short'.", ""),
            ("You should end with exactly three root causes. If you have more than five, you are still listing symptoms; if you have one, you have over-consolidated.", ""),
            ("For each root cause, write one strategy. A strategy must name WHO does WHAT by WHEN. Reject any strategy that is a slogan.", ""),
            ("Add a fourth strategy that fixes the MISSING closed loop itself — how will customers who gave feedback be told what changed? This is the strategy most groups forget.", ""),
            ("For every strategy, define a success measure with a number and a review date. 'Wrong-item tickets below 10/week by 30 Sept' is a measure; 'better service' is not.", ""),
            ("Add a fifth element: how will you collect STAFF feedback formally from now on, so the next modifier bug does not sit in WhatsApp for three months?", ""),
            ("Prepare a 3-minute presentation: the three root causes, your strategies with owners and dates, your measures, and your closed-loop mechanism. Nominate one presenter.", ""),
            ("Present to the class. The class acts as management and must ask one challenging question per group.", ""),
        ],
        test="Your plan names 3 root causes (not symptoms), has an owner and date for every strategy, includes a numeric success measure, and contains an explicit mechanism for telling customers what changed.",
    ),

    dict(
        num=8, topic=8, minutes=15,
        title="Service Recovery Under Pressure — The Wedding Catering Failure",
        type="Role Play + Case Study",
        objective="LO2 · K1, K3, A3 · Apply HEARD/LAST de-escalation, establish common ground and set limits professionally.",
        desc=("Learners handle a high-stakes recovery where the company is clearly at fault, the damage cannot be "
              "undone, and the customer is escalating — then design the process fix that prevents a recurrence."),
        scenario=(
            "You are the Duty Manager for a Singapore catering company. Yesterday you catered a 200-guest wedding at a "
            "hotel ballroom in Novena. Three failures occurred: the vegetarian main course (40 portions, pre-ordered and "
            "confirmed in writing) was never loaded onto the truck; service started 35 minutes late; and the wedding "
            "cake was delivered with visible damage to one side.\n\n"
            "The bride's father, Mr Wong, paid S$18,400. He is in your office now. He has photographs. He has already "
            "posted a one-star review naming your company. He is demanding a full refund and says he will 'make sure "
            "nobody in Singapore uses you again'.\n\n"
            "What you know internally: the vegetarian order WAS in the system — the kitchen printed the run sheet before "
            "the final amendment was saved, a known gap flagged twice by kitchen staff and never fixed. Your authority "
            "extends to a 40% refund; anything beyond that needs the Director, who is contactable.\n\n"
            "You cannot un-ruin the wedding. That is the constraint you are working inside."
        ),
        roles="Pairs or trios. A = Duty Manager, B = Mr Wong, C = observer scoring against HEARD.",
        build="A full recovery conversation applying HEARD, plus a written root-cause fix for the run-sheet gap.",
        services="HEARD framework card · LAST framework card · Observer scoring sheet",
        flow=["Brief the roles", "Run recovery", "Score against HEARD", "Set the limit", "Design the fix"],
        questions=[
            "Apply HEARD to this case. Write what you would actually SAY at each of the five stages.",
            "You cannot undo the wedding. What are you actually recovering, and is recovery even possible here?",
            "Mr Wong demands a full refund; you can authorise 40%. How do you set that limit without sounding like you are haggling over his daughter's wedding?",
            "The kitchen flagged the run-sheet gap twice and nothing was done. Do you tell Mr Wong that? Argue both sides.",
            "Perceived justice has three parts — outcome, process and treatment. Which of the three can you still influence here?",
            "Design the process fix. What exactly changes so this cannot happen to the next customer?",
        ],
        debrief=[
            "HEARD in practice — Hear: let him show the photographs and finish, however long it takes. Empathize: 'this was your daughter's wedding and we damaged it' — name the actual loss, not 'the inconvenience'. Apologize: unconditional, no 'if' and no 'but'. Resolve: a concrete offer, now. Diagnose: the run-sheet gap, named to him as a real fix.",
            "What you are recovering is not the wedding — it is Mr Wong's standing. He chose this vendor and it failed in front of 200 guests including his extended family. The dignity loss is larger than the money.",
            "Setting the limit: never haggle. State the 40% as immediate and unconditional, then say you are taking the rest to the Director TODAY with your own recommendation, and give a time you will call back. Being on his side of the table is the move.",
            "Disclosing the known gap: strong arguments both ways. Disclosing shows honesty and makes the fix credible; it also hands him evidence of negligence. Most groups land on acknowledging a 'known process gap we failed to close' without the detail that it was flagged twice — accurate, honest, not self-incriminating. There is no single right answer here and the discussion is the point.",
            "Outcome is largely fixed (money is all that is left). But PROCESS and TREATMENT are entirely still in your hands — and research on perceived justice says those two often matter more than the refund amount.",
            "The fix: lock the run sheet against the live order record at print time, or block printing until amendments are closed. Then close the loop — tell Mr Wong what changed, in writing, a week later. That last step is what converts a detractor.",
        ],
        steps=[
            ("Brief the roles separately. B (Mr Wong) must open by placing the photographs down and must NOT accept the first offer. B is devastated and angry, but not abusive — this is recovery practice, not escalation practice.", ""),
            ("A prepares for 2 minutes using the HEARD card. Write one opening sentence for each of the five stages before starting. Do not improvise the apology.", ""),
            ("Begin. A must let B speak completely — including the review threat — before saying anything beyond acknowledgement sounds. Observer times this; interrupting inside the first 90 seconds is the most common failure.", ""),
            ("A empathises by naming the specific loss: the vegetarian guests who had nothing to eat, the 35-minute delay in front of 200 people, the cake in the photographs. Generic phrases like 'I understand your frustration' score zero here.", ""),
            ("A apologises unconditionally. No 'if you were disappointed', no 'but the kitchen', no policy citation. One clean sentence taking ownership.", ""),
            ("A resolves: state the 40% refund as immediate and already authorised, and state that you are taking the balance to the Director today. Give a specific callback time.", ""),
            ("A establishes common ground before setting the limit: 'we both want this made right' — then set the limit calmly and once. Do not repeat or defend it if B pushes; restate the escalation path instead.", ""),
            ("A diagnoses aloud: explain that a process gap let the amended order miss the run sheet, and that it is being closed. Decide as a pair how much detail to disclose — you will defend that choice in the debrief.", ""),
            ("Observer scores each HEARD stage present/absent, times the first interruption, and notes whether the apology contained any conditional word ('if', 'but', 'however').", ""),
            ("After the role play, both partners write the process fix together: the specific system or procedural change, its owner, and how Mr Wong will be told about it.", ""),
            ("Swap roles and rerun with a different disclosure decision, so both learners experience receiving the recovery.", ""),
        ],
        test="All five HEARD stages were delivered, your apology contained no conditional words, you set the 40% limit once without haggling, and you produced a written process fix with an owner.",
    ),

    dict(
        num=9, topic=9, minutes=15,
        title="Drawing the Line — Escalation and Abuse at a Service Counter",
        type="Role Play + Decision Exercise",
        objective="LO2 · K3, A3 · Distinguish anger from abuse, apply the three-strike rule, escalate correctly and document.",
        desc=("Learners sort escalating behaviours against the escalation threshold, then run a scenario that crosses "
              "the line from anger into abuse and must be handled, escalated and documented."),
        scenario=(
            "You are a service officer at a telco flagship store on Orchard Road. Mr Douglas Teo is disputing a S$680 "
            "roaming bill from a trip to Australia. He says he was never told data roaming was not included. The account "
            "notes show a confirmation SMS was sent and opened. The charge is valid under the contract.\n\n"
            "The interaction escalates over 8 minutes:\n"
            "  0:00  He raises his voice: 'This is daylight robbery.'  \n"
            "  2:00  'Are you stupid? Can you even read English?'  \n"
            "  4:00  He calls you an offensive name related to your race.  \n"
            "  5:30  'I'm going to CASE, and I'll have your job. What's your full name and NRIC?'  \n"
            "  7:00  He steps behind the counter line, moves within arm's reach, and points a finger in your face.\n\n"
            "Other customers are present. Your supervisor is on the shop floor. There is a duress button under the "
            "counter and CCTV covering the area."
        ),
        roles="Trios. A = Service Officer, B = Mr Teo (trainer may play this role), C = supervisor/observer.",
        build="A completed escalation decision log and an incident report for the abusive interaction.",
        services="Escalation trigger checklist · Incident report template · Three-strike rule card",
        flow=["Sort the behaviours", "Mark the line", "Run to the trigger", "Escalate and hand over", "Write the report"],
        questions=[
            "Go through the timeline. At each timestamp, classify the behaviour as ANGRY or ABUSIVE. Where exactly is the line?",
            "Which timestamp is the point of no return — where continuing to serve is the wrong decision? Justify it.",
            "Apply the three-strike rule to this timeline. What are your two warnings, word for word?",
            "Is this functional escalation or hierarchical escalation? Would your answer change if the dispute were technical rather than behavioural?",
            "He demands your full name and NRIC. What are you obliged to give, and what are you not?",
            "At 7:00 he is within arm's reach and pointing at your face. What do you do in the next 5 seconds, in order?",
            "What must go into the incident report, and why does the exact wording he used need to be recorded verbatim?",
        ],
        debrief=[
            "The line: 0:00 and 2:00 are anger directed at the situation and then at your competence — unpleasant but serviceable. 4:00 is the crossing point: a racial slur is abuse of the PERSON and is a criminal matter under POHA, not a service problem.",
            "Point of no return is 4:00, not 7:00. Most learners wait for the physical proximity. Waiting until you feel physically unsafe means you served through the abuse — the threshold is the slur, and it is not negotiable or 'part of the job'.",
            "Warnings must be calm, specific and behavioural: 'Mr Teo, I want to help you with this bill, but I cannot continue if you speak to me that way.' Second: 'If that continues I will need to hand this to my supervisor and end our conversation.' Never sarcastic, never raised.",
            "This is HIERARCHICAL escalation — it needs authority, not expertise. A technical roaming dispute would be FUNCTIONAL escalation to a billing specialist. Same customer, same bill, entirely different escalation path.",
            "You give your first name or staff ID — that is standard and reasonable. You never give your NRIC or personal details. Deflect: 'my name is X and my staff ID is Y, and my supervisor will give you the complaint reference.'",
            "At 7:00, in order: step back to restore distance, keep hands visible and open, do not turn your back, say clearly 'please step back behind the counter', signal or press for the supervisor, and press the duress button if he does not comply. Do not attempt to win the exchange.",
            "The report needs date, time, location, the exact words used verbatim, witnesses present, CCTV reference, actions taken and who was notified. Verbatim matters because POHA and any police report turn on what was actually said — paraphrase destroys the evidence.",
        ],
        steps=[
            ("Individually, take the escalation trigger checklist and classify each of the five timestamps as ANGRY or ABUSIVE. Do this before any discussion so you commit to a personal threshold first.", ""),
            ("Compare in your trio. Where you disagree, argue it out. Most disagreement clusters around 2:00 ('are you stupid') — insulting your competence versus insulting you as a person.", ""),
            ("As a group, mark the single timestamp you consider the point of no return. Write one sentence justifying it. Be prepared to defend it to the class.", ""),
            ("Write your two warnings word for word on the three-strike card. Read them aloud to each other — if either sounds sarcastic or raised when spoken, rewrite it.", ""),
            ("Run the role play from 0:00. B escalates on the timeline; A responds. The trainer may play B for this activity because the racial slur is difficult to deliver as a peer.", ""),
            ("A issues warning one at the appropriate point, and warning two at 4:00 while simultaneously signalling the supervisor. A does NOT continue trying to resolve the bill after 4:00.", ""),
            ("A hands over to C (supervisor) with a clean, brief handover in front of the customer: the issue, what has been offered, and the behaviour that triggered the escalation. A then physically withdraws.", ""),
            ("Run the 7:00 physical-proximity moment separately as a freeze-frame exercise. A demonstrates the five-second sequence: step back, hands visible, verbal boundary, signal, duress button.", ""),
            ("A completes the incident report template: date, time, location, verbatim words, witnesses, CCTV reference, actions taken, notifications made. Verbatim means verbatim — do not sanitise it.", ""),
            ("As a group, add the POHA and TAFEP references to the report: harassment at work is a criminal matter, reportable to TAFEP or the police, and the employer has a legal duty to provide a safe workplace.", ""),
            ("Close with the wellbeing step most teams skip: what does the officer need AFTER this interaction — a break, a debrief with the supervisor, and a follow-up the next day.", ""),
        ],
        test="You identified 4:00 as the escalation threshold, delivered two calm behavioural warnings, handed over without continuing to serve, and produced an incident report containing the verbatim wording and a CCTV reference.",
    ),
]
