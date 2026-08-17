"""
LU1 activities — Customer's Needs and Feedback (Topics 1-6).

Each activity is a REAL-WORLD Singapore case study with:
  scenario   the situation, written as a case a learner could actually meet
  roles      who plays whom in the role play (RP-style, mirrors the assessment)
  flow       5 short chip labels for the PPT activity strip
  questions  the discussion questions learners work through
  debrief    the trainer's debrief points — what good looks like
  steps      the detailed step-by-step, for the Learner Guide ONLY (never the PPT)
  test       how the learner knows they succeeded
"""

DOMAIN1 = [
    dict(
        num=1, topic=1, minutes=20,
        title="Mapping the Service Chain at a Singapore Bank Branch",
        type="Case Study + Peer Sharing",
        objective="LO1 · K1 · Understand internal vs external customers and how the service chain shapes experience.",
        desc=("Learners map a real end-to-end service breakdown at a retail bank branch, identify every internal and "
              "external customer in the chain, and locate the point where the chain actually broke."),
        scenario=(
            "OCBC-style retail branch, Tampines. Mdm Rohani, 68, comes in to reactivate a dormant savings account so her "
            "CPF payout can be credited. The queue ticket says 12 minutes; she waits 47. At the counter, the teller, "
            "Wei Ming, finds the reactivation needs a signature-verification form that Operations must approve. "
            "Operations is understaffed and quotes 3 working days. Wei Ming has no authority to expedite and no way to "
            "see the Operations queue. Mdm Rohani has already made two trips. She says loudly that she will move her "
            "account to another bank, and other customers in the queue are listening.\n\n"
            "Behind the counter: the branch manager has a service-level dashboard showing counter wait times but not "
            "back-office turnaround. Operations measures forms processed per day, not customer trips avoided. "
            "The digital team launched an app-based reactivation two months ago that nobody told the branch about."
        ),
        roles="Groups of 4–5. Each group maps the chain; one member presents.",
        build="A service-chain map naming every internal and external customer, the broken link, and one fix per link.",
        services="Whiteboard / flip chart · Service chain worksheet",
        flow=["Read the case", "List the customers", "Map the chain", "Find the break", "Present one fix"],
        questions=[
            "Who are the EXTERNAL customers in this case, and who are the INTERNAL customers? List every one.",
            "Draw the service chain from Mdm Rohani's need to the outcome she actually got. Where exactly did it break?",
            "Wei Ming was polite and followed procedure, and the customer still left angry. Whose service failure is this?",
            "Operations measures 'forms processed per day'. What behaviour does that metric produce, and what does it miss?",
            "The app-based reactivation existed but the branch did not know. What internal service failure does that reveal?",
            "Name one change per link in the chain that would have prevented this outcome.",
        ],
        debrief=[
            "The frontline is where the failure BECOMES VISIBLE, not where it is caused. Wei Ming did nothing wrong — he was set up to fail by the links behind him.",
            "Internal customers here: Wei Ming is Operations' customer; the branch is the digital team's customer; Operations is the branch manager's customer. Every one of those relationships failed.",
            "'Forms processed per day' optimises throughput, not resolution. It is blind to Mdm Rohani's THREE trips — the metric would look healthy while the customer churns.",
            "The undisclosed app feature is a pure internal-communication failure. A capability the frontline does not know about does not exist.",
            "Expected fixes: give the teller visibility of the Operations queue; give SOMEONE authority to expedite; measure customer trips not forms; brief the branch on every new digital capability.",
            "Link back to Topic 1: excellent external service always begins with strong internal service. This case is the proof.",
        ],
        steps=[
            ("Form groups of 4–5. Read the case aloud once as a group so everyone shares the same facts.", ""),
            ("On a flip chart, draw two columns: EXTERNAL CUSTOMERS and INTERNAL CUSTOMERS. List every person or team in the case under the right column. Mdm Rohani is external — but so are the customers in the queue who overheard.", ""),
            ("Draw the service chain left to right as boxes: Mdm Rohani's need → queue system → Wei Ming (teller) → Operations → outcome. Add the branch manager and digital team as boxes that FEED the chain from above.", ""),
            ("On each arrow between boxes, write what is supposed to flow (information, authority, approval). Then mark with a red X every arrow where that flow failed.", ""),
            ("For each red X, write the internal customer whose need was not met. Example: the arrow from Operations to Wei Ming should carry 'queue visibility' — it carries nothing, so Wei Ming's need as an internal customer is unmet.", ""),
            ("Answer discussion question 4 explicitly: write the behaviour 'forms processed per day' rewards, and write what it makes invisible.", ""),
            ("Agree ONE fix per broken link. Write each fix as a specific action with an owner, not a slogan — 'give tellers read access to the Operations queue dashboard', not 'improve communication'.", ""),
            ("Nominate a presenter. Present the map in 2 minutes: the chain, the breaks, and your fixes.", ""),
        ],
        test="Your map names at least 3 internal customers, marks at least 3 broken links, and each fix is a specific action with an owner.",
    ),

    dict(
        num=2, topic=2, minutes=15,
        title="Attitude and Positive Language at a Changi Airport Service Counter",
        type="Role Play + Peer Sharing",
        objective="LO1 · K1 · Apply service attitude, body language and positive language under pressure.",
        desc=("Learners rewrite negative service language into positive language, then role play a high-pressure "
              "counter interaction where the answer to the customer's request is genuinely 'no'."),
        scenario=(
            "Changi Airport Terminal 3, airline transfer desk, 11:40pm. Mr Krishnan and his two children (aged 4 and 7) "
            "have missed their connecting flight to Chennai because the inbound flight was delayed by weather. The next "
            "available flight is 14 hours away. Company policy for weather delays: no hotel accommodation, no meal "
            "vouchers, rebooking only. The children are crying. Mr Krishnan has been queueing for 35 minutes and is the "
            "eleventh passenger you have seen with the same problem tonight. You are 90 minutes past the end of your "
            "shift.\n\n"
            "What you CAN do: rebook him on the 1:50pm flight; give him lounge access at your discretion; provide a "
            "transit hotel booking form at his own cost; escalate to the duty manager for a goodwill exception."
        ),
        roles="Pairs. Role A = Service Officer, Role B = Mr Krishnan. Swap after the first round. Observers score.",
        build="A rewritten positive-language script and a 5-minute role play that delivers a 'no' without losing the customer.",
        services="Positive language worksheet · Observer checklist",
        flow=["Rewrite the phrases", "Brief the roles", "Run the role play", "Observers score", "Swap and repeat"],
        questions=[
            "Rewrite each phrase in positive language: 'We don't cover weather delays.' / 'There's nothing I can do.' / 'You'll have to pay for that yourself.' / 'That's not our policy.' / 'I don't know.'",
            "You are 90 minutes past your shift end and this is the eleventh identical case. How does that show up in your body language and voice, even when your words are correct?",
            "The answer to 'will you pay for my hotel?' is genuinely no. How do you say no and still leave the customer feeling served?",
            "What can you offer that costs the company little but changes how Mr Krishnan experiences this? Name three things.",
            "At what point, if any, would you escalate to the duty manager — and what would you say to Mr Krishnan as you do it?",
            "The two crying children are not your customer, but they change the interaction. How?",
        ],
        debrief=[
            "Positive language does not mean saying yes. It means directing the customer to what IS available: 'I can get you on the 1:50pm and into the lounge now' beats 'we don't cover weather delays' with the same underlying answer.",
            "'I don't know' becomes 'let me find out' — the second is the same information plus ownership.",
            "Fatigue leaks through the non-verbal channel first. Words stay professional long after tone and posture have given up. Observers should watch for flat tone, no eye contact, and a sigh before speaking.",
            "The three low-cost offers most groups find: lounge access (comfort for the kids), a proactive rebooking done before he asks, and a printed confirmation so he does not have to re-explain at the next desk.",
            "Acknowledge the children explicitly — the customer's stress is mostly about them. Serving the parent means noticing the kids.",
            "Escalation here is not defeat: naming the duty manager and saying 'I want to ask if we can make an exception for you' shows the customer you are on their side of the counter.",
        ],
        steps=[
            ("Individually, rewrite the five negative phrases from discussion question 1 into positive language. Write both versions side by side so the contrast is visible.", ""),
            ("Compare with your partner. Keep the strongest rewrite of each pair. A good rewrite states what you CAN do and never begins with 'unfortunately' or 'we don't'.", ""),
            ("Assign roles: A = Service Officer, B = Mr Krishnan. B, read only the customer half of the brief — you are exhausted, your children are crying, and you believe the airline owes you a hotel.", ""),
            ("Before starting, A checks their own physical setup: shoulders back, hands visible, eye contact ready, a breath in before the first word. This is the attitude reset from Topic 2.", ""),
            ("Run the role play for 5 minutes. A must deliver the 'no' on hotel accommodation within the first 2 minutes — do not delay it to seem helpful, that is worse.", ""),
            ("Observers mark the checklist: Did A greet and acknowledge within seconds? Did A acknowledge the children? Did A use positive language? Did A offer alternatives before being asked? Did A state clear next steps?", ""),
            ("Debrief in the pair for 2 minutes: B says how the 'no' actually felt to receive, which is the only score that matters.", ""),
            ("Swap roles and run the scenario again. The second Officer must use at least two techniques they saw work in round one.", ""),
        ],
        test="You delivered a genuine 'no' inside 2 minutes, offered at least two alternatives unprompted, and your partner reports feeling served rather than dismissed.",
    ),

    dict(
        num=3, topic=3, minutes=20,
        title="Diagnosing Customer Needs at a Growing SME — TechNova Account Review",
        type="Case Study + Role Play",
        objective="LO1 · K1, A2 · Identify functional and emotional needs, and map them to the four levels of addressing needs.",
        desc=("Learners analyse a real account-at-risk case, separate what the customer SAYS from what they NEED, and "
              "run a needs-discovery conversation using open questioning and active listening."),
        scenario=(
            "TechNova Solutions (Singapore) supplies a cloud project-management platform. Mr Daniel Lim is Operations "
            "Director at Horizon Builders Pte Ltd, a Woodlands-based construction firm and a customer for 6 years. "
            "Horizon has grown from 12 to 50 employees. Daniel emails: 'Uploads are painfully slow, the reports are "
            "useless for what we need, and it took your support team 4 days to answer my last ticket. Competitors are "
            "offering us more for less. I need to justify this renewal to my MD by end of month.'\n\n"
            "What the account record shows: Horizon is on Team Pro (a 15-seat plan) with 50 users sharing logins. "
            "Upload slowness correlates with 200MB+ site photo batches — the plan caps concurrent uploads. The reporting "
            "Daniel wants (cost-per-project roll-up) exists in the Enterprise tier. The 4-day ticket was logged during "
            "the Chinese New Year holiday period. Daniel has never had a formal account review in 6 years."
        ),
        roles="Pairs. Role A = TechNova Account Manager, Role B = Daniel Lim. Assessor-style observer optional.",
        build="A needs analysis separating stated complaints from root needs, mapped to the four levels of addressing needs.",
        services="Needs analysis worksheet · Four-levels template",
        flow=["Read the account", "Split said vs needed", "Map four levels", "Run discovery call", "Recommend"],
        questions=[
            "Separate what Daniel SAID from what Daniel NEEDS. Write two columns. They are not the same list.",
            "Identify Daniel's FUNCTIONAL needs and his EMOTIONAL needs. Which one is driving the email's tone?",
            "'I need to justify this renewal to my MD by end of month.' What does this sentence tell you that the complaints do not?",
            "Map your findings to the four levels: understand the problem / meet basic needs / think outside the box / go the extra mile. What sits at each level?",
            "Horizon has 50 users on a 15-seat plan. This is a contract breach AND the cause of the slowness. How do you raise it without turning a save into a fight?",
            "Six years, no account review. What does that reveal about TechNova's own service process — and what should change?",
        ],
        debrief=[
            "Said vs needed: he SAYS slow uploads, useless reports, slow support. He NEEDS a defensible business case for his MD by month end. Solve only the first three and you still lose the account.",
            "The emotional need is dominant: Daniel is exposed in front of his MD. The functional fixes are the evidence he needs to not look foolish for having stayed 6 years.",
            "The last sentence is the actual brief. Everything before it is symptoms. Learners who spot this are doing genuine needs identification rather than complaint triage.",
            "Four levels — understand: the plan no longer fits a 50-person firm. Basic: fix the upload cap and the ticket SLA. Outside the box: the seat overage is leverage for a migration, not a penalty. Extra mile: build the cost-per-project report FOR his MD deck.",
            "The 15-seat breach must be raised as a discovery, not an accusation: 'your growth has outrun the plan we sold you six years ago — that's on us for not reviewing it.'",
            "The real service failure is TechNova's: no account review in 6 years means nobody was listening until the customer shouted. The process fix is a scheduled review cadence — this is a Topic 7 closed-loop point arriving early.",
        ],
        steps=[
            ("Read the case individually. Underline every sentence where Daniel states a problem, and circle every sentence that tells you about his SITUATION rather than his complaint.", ""),
            ("Draw two columns on your worksheet: WHAT HE SAID and WHAT HE NEEDS. Fill the left column first — it is quick, it is just his words. The right column takes longer because it requires inference.", ""),
            ("Under WHAT HE NEEDS, tag each item F (functional) or E (emotional). If you have no E items, you have not finished — re-read the last sentence of his email.", ""),
            ("On the four-levels template, place each need at the correct level. Level 1 (understand the problem) must be filled before you write anything at Level 2 — resist jumping to solutions.", ""),
            ("Prepare five OPEN questions for the discovery call. Open questions start with what, how, tell me, walk me through. If a question can be answered yes/no, rewrite it.", ""),
            ("Assign roles: A = Account Manager, B = Daniel Lim. B, you are frustrated but not abusive — you want to stay if given a reason.", ""),
            ("Run a 6-minute discovery call. A opens by acknowledging the 6-year relationship, then asks the open questions and PARAPHRASES each answer back before moving to the next.", ""),
            ("A must NOT propose an upgrade in the first 4 minutes. Diagnose before you prescribe — a plan upsell offered too early reads as a sales pitch and confirms Daniel's suspicion.", ""),
            ("In the last 2 minutes, A summarises the needs back to Daniel and proposes one action at each of the four levels, ending with the extra-mile offer to build the MD's report.", ""),
            ("Debrief: B rates whether A understood the real brief (the MD deadline) or only fixed the three complaints.", ""),
        ],
        test="Your needs analysis has at least one emotional need identified, all four levels populated, and your role-play partner confirms you surfaced the MD deadline as the real brief.",
    ),

    dict(
        num=4, topic=4, minutes=15,
        title="The Walk-In Interruption — Retail Service Counter, Bugis",
        type="Role Play",
        objective="LO1 · K1, A1 · Handle in-person and at-your-desk requests using body language and acknowledgement.",
        desc=("Learners run a layered in-person scenario where a walk-in customer, a ringing phone and an existing task "
              "compete for attention — and practise acknowledging without abandoning."),
        scenario=(
            "A telco retail store at Bugis Junction, Saturday 2pm. You are at the service counter finishing a SIM "
            "registration for a customer who is standing beside you waiting for the confirmation SMS. The store phone "
            "rings. At the same moment, Ms Chen walks up to your counter holding a phone with a cracked screen and says "
            "'Excuse me, I just need a quick answer' — she has been in the store for 20 minutes looking for someone. "
            "Two more customers are visibly waiting behind her.\n\n"
            "You cannot serve three people at once. Everything you do in the next 15 seconds is visible to all of them."
        ),
        roles="Groups of 4. Role A = Service Officer, B = SIM customer, C = Ms Chen, D = observer/phone caller.",
        build="A demonstrated acknowledgement sequence handling three competing demands without losing any of them.",
        services="Observer checklist · Timer",
        flow=["Set the scene", "Brief 4 roles", "Run 15-sec opening", "Full 6-min run", "Observer debrief"],
        questions=[
            "In the first 15 seconds, what do you do — and in what order? Be specific about words, eyes and hands.",
            "Ms Chen says 'I just need a quick answer'. Is it ever actually quick? What is the risk of treating it as quick?",
            "How do you acknowledge Ms Chen without abandoning the customer already at your counter?",
            "The phone is ringing and no one else can take it. What do you do, and what does the customer in front of you see you do?",
            "What body language keeps all three parties feeling attended to while you can only serve one?",
            "What is the 'park and return' method, and where exactly would you use it here?",
        ],
        debrief=[
            "Order matters: eye contact + a raised hand + 'I'll be right with you, about two minutes' to Ms Chen takes 3 seconds and buys 2 minutes. Being SEEN precedes being served.",
            "'Quick answer' is almost never quick — a cracked screen means warranty status, purchase date, insurance and a repair booking. Treating it as quick means starting something you cannot finish and now failing two customers.",
            "The customer in front of you keeps priority. State that openly to the room: it reassures the person you are serving AND tells the queue there is a fair rule.",
            "The phone: let it go to the queue or answer with 'may I take your number and call you back in five minutes?' Never leave a physical customer standing while you have a full phone conversation — the person present outranks the person calling.",
            "Body language: keep your torso oriented to the counter customer, turn only your head to Ms Chen, and use an open palm rather than a pointed finger. Turning your whole body away is the abandonment signal.",
            "Park and return: note where you were in the SIM registration before you turn away, so you resume without asking the first customer to repeat anything. Making a customer re-explain is the failure this method exists to prevent.",
        ],
        steps=[
            ("Set up the physical space: a counter, A behind it, B standing at the counter, C approaching from the side, D at a distance with a phone.", ""),
            ("Brief each role privately. C (Ms Chen) has already waited 20 minutes and believes her question is 30 seconds long. She is polite but firm.", ""),
            ("Run ONLY the first 15 seconds. Freeze on the trainer's call. Observers describe exactly what A did with eyes, hands, torso and words — in that order.", ""),
            ("Discuss the freeze-frame as a group for 2 minutes. Most first attempts either ignore Ms Chen entirely or abandon the SIM customer. Name which one happened.", ""),
            ("Reset and run the full scenario for 6 minutes with the phone ringing at the 20-second mark.", ""),
            ("A applies the sequence: acknowledge C within 3 seconds without leaving B; handle the phone with a callback offer; complete B's registration; note the park point; then turn fully to C.", ""),
            ("When A turns to C, A must NOT ask her to repeat why she is there — A should open with 'you mentioned a cracked screen' to prove she was heard the first time.", ""),
            ("Observer (D) scores the checklist and reports: acknowledgement time in seconds, whether any customer was made to repeat themselves, and whether A's torso ever fully turned away from the active customer.", ""),
            ("Rotate roles so at least two learners play the Service Officer.", ""),
        ],
        test="You acknowledged the walk-in within 5 seconds, no customer was asked to repeat themselves, and the observer confirms you never fully turned away from the customer you were actively serving.",
    ),

    dict(
        num=5, topic=5, minutes=15,
        title="The Angry Delivery Call — Logistics Hotline",
        type="Role Play",
        objective="LO1 · K1, A1 · Apply telephone etiquette, paraphrasing and hold technique with an angry caller.",
        desc=("Learners handle a live angry call end to end — greeting, listening without interrupting, paraphrasing, "
              "placing a proper hold, and closing with concrete next steps."),
        scenario=(
            "You work the customer hotline for a Singapore last-mile logistics firm. Mr Faisal calls at 4:15pm. His "
            "package — a replacement CPAP machine part his father needs — was due Monday. It is now Thursday. Tracking "
            "has said 'out for delivery' for three days. He has called twice before; both times he was told 'it will be "
            "delivered today'. He opens the call at volume: 'I've been lied to twice. Don't tell me it's out for "
            "delivery. Where is my package?'\n\n"
            "What you find while he is talking: the parcel was mis-sorted to the Jurong hub on Monday, scanned back out "
            "Wednesday, and is genuinely on a van today — but the van's route ends at 9pm and he is stop 61 of 68. "
            "You can request a priority re-route (needs hub supervisor approval, ~10 minutes) or offer next-morning "
            "guaranteed delivery before 10am."
        ),
        roles="Pairs, seated back to back so there is no visual channel. A = Hotline Officer, B = Mr Faisal.",
        build="A complete recorded-style call demonstrating the six-stage phone flow with a compliant hold.",
        services="Phone flow card · Observer checklist · Timer",
        flow=["Back-to-back setup", "Open and listen", "Paraphrase", "Proper hold", "Close with next steps"],
        questions=[
            "Mr Faisal opens by shouting. What are your first words, and how long do you let him talk before you speak?",
            "He says 'I've been lied to twice.' Is that true? How do you respond to it without blaming a colleague or defending the company?",
            "Write the exact sentence you would use to paraphrase his issue back to him.",
            "You need 10 minutes to get supervisor approval. How do you place him on hold correctly — what four things must you say?",
            "You have two options (priority re-route vs guaranteed next morning). Do you choose for him or offer both? Why?",
            "Why does the CPAP detail change how you handle this call, and what would you have missed if you had interrupted him?",
        ],
        debrief=[
            "Let him finish. The first 30–45 seconds are venting and contain the CPAP detail — the single most important fact in the call. An officer who interrupts to defend the tracking system never learns why this parcel matters.",
            "'I've been lied to twice' — do not defend and do not blame. 'You were given a delivery promise twice and it did not happen. That's on us.' Acknowledging the customer's EXPERIENCE is not admitting to a lie.",
            "Good paraphrase: 'So your father's CPAP part was promised Monday, you've called twice, been told it's out for delivery each time, and four days on you still have nothing.' Naming the father is what proves you listened.",
            "Correct hold has four parts: ask permission, state the reason, give a realistic duration, thank them on return. Missing any one of these makes the hold feel like being dumped.",
            "Offer both options with a recommendation. The CPAP context makes guaranteed 10am delivery likely better than stop 61 at 9pm — but it is his father and his call. Choosing FOR the customer removes the one piece of control he still has.",
            "This call is a Topic 7 case in disguise: the mis-sort is the fault, but the SERVICE failure is two false promises. Note it for the feedback loop — the fix is not promising a date the system cannot see.",
        ],
        steps=[
            ("Seat the pair back to back. This is not a gimmick — removing the visual channel is the entire point of practising phone service.", ""),
            ("B (Mr Faisal) reads the customer brief only. B must open at high volume and must mention the CPAP machine and his father within the first 40 seconds, unprompted.", ""),
            ("A answers within three rings with the full greeting: company, own name, offer of help. A smiles before speaking — it changes the voice even though nobody can see it.", ""),
            ("A does NOT speak again until B has finished venting. A may use minimal acknowledgement sounds ('mm-hm', 'I see') but no sentences and no interruptions.", ""),
            ("A acknowledges the experience first, then paraphrases the whole issue back including the father and the CPAP part. A waits for B to confirm the paraphrase is right before moving on.", ""),
            ("A places B on hold correctly: 'May I put you on hold for about three minutes while I get my hub supervisor to authorise a priority re-route? ... Thank you for waiting.' All four elements, in order.", ""),
            ("A returns and presents BOTH options with a recommendation and a reason tied to the father's need. A lets B choose.", ""),
            ("A closes with concrete next steps: what will happen, by when, who will call, and a reference number. Vague closes ('we'll look into it') fail this step.", ""),
            ("A commits to ONE proactive follow-up — a call tomorrow confirming delivery, made whether or not it succeeded.", ""),
            ("Observer scores: interruption count (target 0), paraphrase accuracy, all four hold elements present, and whether the close contained a time and an owner.", ""),
        ],
        test="You did not interrupt during the opening vent, your paraphrase included the father/CPAP detail, your hold had all four elements, and your close named a specific time and owner.",
    ),

    dict(
        num=6, topic=6, minutes=15,
        title="Rewriting the Refund Email — E-Commerce Support Inbox",
        type="Case Study + Practical Writing",
        objective="LO1 · K1, K2, A1 · Apply netiquette and the five-part email structure; choose email vs chat correctly.",
        desc=("Learners take a genuinely bad support email, diagnose every netiquette and structural failure in it, and "
              "rewrite it to the five-part structure — then decide which channel the case should have used."),
        scenario=(
            "A Singapore online fashion retailer. Ms Priya ordered a dress for her sister's wedding on 2 August, paid "
            "S$189, and received the wrong size. She returned it on 8 August using the prepaid label. It is now "
            "22 August, no refund has appeared, and the wedding is on 30 August. She has emailed twice.\n\n"
            "The agent's reply, sent as-is:\n\n"
            "  Subject: RE: RE: FW: order\n\n"
            "  Dear Customer,\n"
            "  As per our T&C section 7.3 refunds are processed within 14-21 WORKING DAYS from receipt at our "
            "  warehouse NOT from when you posted it. Your return was received 14/8. Therefore your refund is NOT "
            "  late and there is nothing further we can do at this time. Please do not email again as it does not "
            "  speed up the process.\n"
            "  Regards,\n"
            "  Support Team\n\n"
            "Every fact in that email is correct. It is still a service failure."
        ),
        roles="Individually, then compare in pairs.",
        build="A rewritten email following the five-part structure, plus a channel-choice justification.",
        services="Email structure template · Netiquette checklist",
        flow=["Diagnose the failures", "List what's correct", "Rewrite in 5 parts", "Choose the channel", "Peer review"],
        questions=[
            "List every netiquette failure in the agent's email. There are at least seven.",
            "Every fact in the email is accurate. Explain how an email can be 100% correct and still be a service failure.",
            "What is the customer's REAL deadline, and does the agent's reply acknowledge it at all?",
            "Rewrite the email using the five-part structure: greeting → acknowledge → solution → next steps → sign-off.",
            "'Please do not email again.' What does this sentence do to the relationship, and what should replace it?",
            "Should this have been email, live chat or a phone call? Justify your choice against the channel-selection rule.",
        ],
        debrief=[
            "Netiquette failures to find: 'RE: RE: FW: order' subject line, 'Dear Customer' not her name, ALL CAPS as shouting, policy-section jargon (T&C 7.3), no apology or acknowledgement, an instruction not to make contact, an unsigned 'Support Team' with no individual name, and no next step the customer can act on.",
            "Correct-but-failing is the key lesson: the agent answered the question the customer TYPED and ignored the question she MEANT — 'will I have this sorted before the wedding on the 30th?'",
            "The wedding date is the real deadline and the email never mentions it. This is the same 'said vs needed' distinction from Activity 3, in writing.",
            "A good rewrite names Priya, acknowledges two prior emails and the wedding, states the refund date with a specific day, offers something concrete (expedite request, or a replacement in the right size shipped now), and gives a named person and direct contact.",
            "'Please do not email again' tells the customer her only channel is closed. Replace with proactive ownership: 'You don't need to chase this — I'll email you the moment it clears, and here's my direct line.'",
            "Channel: email is right for the RECORD (money, dates, policy), but this case needed a phone call first because it is time-critical and emotional. Best practice is call, then confirm in writing — using both channels for what each does well.",
        ],
        steps=[
            ("Read the agent's email once at normal speed, then a second time slowly with the netiquette checklist beside you.", ""),
            ("Mark every failure directly on the email text. Aim for at least seven. Compare with your partner — most people miss the unsigned 'Support Team' and the dead subject line.", ""),
            ("In one sentence, write what the agent got RIGHT. There is something: the facts and the policy citation are accurate. This matters, because it shows accuracy is not the same as service.", ""),
            ("Write down the customer's real deadline (30 August, the wedding) and check whether it appears anywhere in the agent's reply. It does not. That absence is the core failure.", ""),
            ("Now rewrite. Part 1 — greeting: use her name. Part 2 — acknowledge: name the wait, the two prior emails and the wedding, and apologise for the experience without disputing the policy.", ""),
            ("Part 3 — the solution: state the actual refund date as a calendar date, not 'within 14–21 working days'. Add one concrete action you will take (raise an expedite request, or ship the correct size now against the pending refund).", ""),
            ("Part 4 — next steps: say exactly what happens next, when, and who does it. Make it clear she does not need to chase.", ""),
            ("Part 5 — sign-off: your real name, your role, and a direct contact channel. Never 'Support Team'.", ""),
            ("Fix the subject line last: make it specific and action-oriented, e.g. 'Your refund for order #48213 — resolution by 26 August'.", ""),
            ("Swap with your partner. Score their rewrite against the netiquette checklist and confirm all five parts are present and the wedding date is acknowledged.", ""),
            ("Finally, write two lines justifying the channel you would have used, referencing complexity, urgency, emotion and the need for a record.", ""),
        ],
        test="Your rewrite has all five parts, names the customer, acknowledges the 30 August wedding, gives a calendar date rather than a working-day range, and is signed by a named person.",
    ),
]
