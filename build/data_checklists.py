"""
Per-activity ROLE-PLAY OBSERVER CHECKLISTS.

One entry per role-play activity (2, 3, 4, 5, 8, 9). Criteria are derived from
that activity's own debrief points and its `test` line, so what the observer
scores is exactly what the trainer debriefs and what the assessor looks for in
the Role Play (RP) assessment.

Each criterion is (code, criterion, "what good looks like"). The code ties the
row to the ability or knowledge factor it rehearses.

Activities 1, 6 and 7 are not role plays and get no checklist — they receive a
reflection worksheet only.
"""

CHECKLISTS = {

 2: dict(
    focus="Service attitude, body language and positive language under pressure",
    observing="Role A — the Service Officer",
    rows=[
      ("K1", "Greeted and acknowledged within seconds",
       "Made eye contact and greeted before the customer had to speak first."),
      ("K1", "Physical reset before the interaction",
       "Shoulders back, hands visible, a breath in before the first word — not visibly carrying the previous 10 customers."),
      ("K1", "Delivered the 'no' within the first 2 minutes",
       "Stated plainly that hotel accommodation is not covered, without stalling or burying it."),
      ("K1", "Used positive language throughout",
       "Framed on what IS available ('I can get you on the 1:50pm and into the lounge now'), never opened with 'unfortunately' or 'we don't'."),
      ("K1", "Offered alternatives unprompted",
       "Named at least two things they could do before the customer had to ask."),
      ("K1", "Acknowledged the children",
       "Noticed that the customer's stress is mostly about the two crying children and responded to it."),
      ("K1", "Tone and body language held under fatigue",
       "No flat tone, no sighing before speaking, no loss of eye contact as the interaction ran on."),
      ("K1", "Closed with clear next steps",
       "The customer left knowing exactly what happens next and by when."),
    ]),

 3: dict(
    focus="Needs discovery — open questioning, active listening and the four levels",
    observing="Role A — the TechNova Account Manager",
    rows=[
      ("A2", "Opened by acknowledging the relationship",
       "Referenced the six-year history before raising any problem or product."),
      ("K1", "Asked open questions first",
       "Used what / how / tell me / walk me through. Closed questions only to confirm specifics."),
      ("K1", "Paraphrased each answer before moving on",
       "Said the answer back in their own words and waited for confirmation."),
      ("A2", "Surfaced the REAL brief",
       "Got to the MD deadline at month end — not just the three stated complaints."),
      ("A2", "Identified an emotional need, not only functional ones",
       "Recognised that Daniel is exposed in front of his MD, not merely inconvenienced by slow uploads."),
      ("A2", "Did NOT propose an upgrade in the first 4 minutes",
       "Diagnosed before prescribing; no early sales pitch."),
      ("A2", "Raised the 15-seat breach as a discovery, not an accusation",
       "Framed it as 'your growth outran the plan we sold you' rather than a contract violation."),
      ("A2", "Proposed an action at each of the four levels",
       "Understand → meet the basic need → outside the box → extra mile (the MD's report)."),
    ]),

 4: dict(
    focus="In-person service — acknowledgement, body language and park-and-return",
    observing="Role A — the Service Officer",
    rows=[
      ("A1", "Acknowledged the walk-in within 5 seconds",
       "Eye contact plus a raised hand or a short verbal hold — before finishing the current task."),
      ("K1", "Gave a realistic wait time",
       "'About two minutes', not a vague 'in a moment'."),
      ("K1", "Protected the customer already at the counter",
       "Stated the priority rule openly so the queue could hear it was fair."),
      ("K1", "Torso stayed oriented to the active customer",
       "Turned only the head to the walk-in; never turned the whole body away."),
      ("K1", "Handled the phone without abandoning the person present",
       "Let it queue or offered a callback — did not hold a full phone conversation with a customer standing there."),
      ("A1", "Nobody was asked to repeat themselves",
       "Resumed the SIM registration and opened with Ms Chen's own words ('you mentioned a cracked screen')."),
      ("K1", "Open, non-defensive gestures",
       "Open palm rather than a pointed finger; no arms crossed; no glancing at a phone."),
      ("K1", "Closed each interaction with next steps",
       "Both customers left knowing what happens now."),
    ]),

 5: dict(
    focus="Telephone service — listening, paraphrasing, hold technique and the close",
    observing="Role A — the Hotline Officer (seated back to back)",
    rows=[
      ("K1", "Full greeting within three rings",
       "Company, own name, offer of help — and smiled before speaking."),
      ("K1", "Zero interruptions during the opening vent",
       "Used only minimal acknowledgement sounds until the customer had finished. Count interruptions: target 0."),
      ("A1", "Captured the key fact from the vent",
       "Heard and used the CPAP machine / father detail — the single most important fact in the call."),
      ("K1", "Acknowledged the experience without blaming",
       "'You were given a delivery promise twice and it did not happen' — no defending the system, no blaming a colleague."),
      ("K1", "Paraphrased the whole issue and waited for confirmation",
       "Included the father and the CPAP part, then checked 'have I got that right?'."),
      ("K1", "Hold had all FOUR parts",
       "Asked permission · stated the reason · gave a realistic duration · thanked them on return."),
      ("A1", "Offered both options with a recommendation",
       "Presented priority re-route AND guaranteed next-morning, recommended one with a reason, and let the customer choose."),
      ("K1", "Close named a specific time, an owner and a reference",
       "No vague 'we'll look into it'. Committed to one proactive follow-up."),
    ]),

 8: dict(
    focus="Service recovery — HEARD, unconditional apology, limits and root-cause fix",
    observing="Role A — the Duty Manager",
    rows=[
      ("A3", "HEAR — let the customer finish",
       "Allowed the photographs and the full account, however long. Note the time of the first interruption; inside 90 seconds is the common failure."),
      ("A3", "EMPATHIZE — named the actual loss",
       "The vegetarian guests with nothing to eat, the 35-minute delay in front of 200 people, the damaged cake. Generic 'I understand your frustration' scores zero."),
      ("A3", "APOLOGIZE — unconditional",
       "No 'if', no 'but', no 'however', no blaming the kitchen. Circle any conditional word used."),
      ("A3", "RESOLVE — concrete and immediate",
       "Stated the 40% refund as already authorised, and committed to taking the balance to the Director today with a callback time."),
      ("A3", "DIAGNOSE — explained the cause and the fix",
       "Named the run-sheet process gap and that it is being closed."),
      ("K1", "Established common ground before setting the limit",
       "'We both want this made right' — turned an adversarial exchange into a shared problem."),
      ("K1", "Set the limit once, without haggling",
       "Did not repeat or defend the 40%; restated the escalation path instead."),
      ("A3", "Produced a written process fix with an owner",
       "A specific system or procedural change, owned, plus how Mr Wong will be told what changed."),
    ]),

 9: dict(
    focus="Escalation — the anger/abuse threshold, warnings, handover and documentation",
    observing="Role A — the Service Officer",
    rows=[
      ("K3", "Identified 4:00 as the escalation threshold",
       "Recognised the racial slur as the crossing point — NOT the physical proximity at 7:00."),
      ("K3", "Warning one named the behaviour",
       "Calm, specific and behavioural: 'I want to help you with this bill, but I cannot continue if you speak to me that way.' Never sarcastic or raised."),
      ("K3", "Warning two stated the consequence",
       "'If that continues I will need to hand this to my supervisor and end our conversation.'"),
      ("A3", "Stopped serving after the threshold",
       "Did not keep trying to resolve the bill dispute after 4:00."),
      ("K3", "Protected personal information",
       "Gave first name or staff ID only. Never the NRIC or personal details."),
      ("K3", "Clean handover to the supervisor",
       "Briefly stated the issue, what was offered and the triggering behaviour — in front of the customer — then physically withdrew."),
      ("A3", "Correct five-second sequence at 7:00",
       "Step back · hands visible and open · do not turn your back · clear verbal boundary · signal or press duress."),
      ("A3", "Incident report is complete and verbatim",
       "Date, time, location, EXACT words used, witnesses, CCTV reference, actions taken, who was notified. Paraphrase destroys the evidence."),
    ]),
}


# ---------------------------------------------------------------- reflection
# One reflection worksheet per activity. The prompts are generic enough to work
# for every activity but each carries one activity-specific question so the
# sheet is not interchangeable filler.
REFLECTION_PROMPT = {
 1: "Which link in your own workplace's service chain is the one most likely to break — and who owns it?",
 2: "Think of a time you had to tell a customer 'no'. Rewrite what you actually said, in positive language.",
 3: "Name one customer of yours whose stated complaint is probably not their real need. What might the real need be?",
 4: "How long does a walk-in currently wait to be ACKNOWLEDGED at your workplace? How would you know?",
 5: "Recall your last difficult phone call. At what point did you first interrupt — and what might you have missed?",
 6: "Find one email you sent this month. Which of the five parts was missing?",
 7: "Which feedback channel does your organisation rely on most — and what is it structurally blind to?",
 8: "Recall a service failure you could not undo. Which of the three parts of perceived justice were still in your control?",
 9: "Where exactly is your own line between an angry customer and an abusive one? Would your supervisor draw it in the same place?",
}
