# WSQ — Improve Your Business with Excellent Customer Service

**Course code:** TGS-2025056191 · **Version:** v2.0 · **Duration:** 1 day (8 hours)
**Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)

Courseware for the WSQ course *Improve Your Business with Excellent Customer Service*, mapped to
the Skills Framework TSC **Customer Service Innovation Management (EPW-CEX-3034-1.1)**.

📎 [Course page](https://www.tertiarycourses.com.sg/wsq-improve-your-business-with-excellent-customer-service.html)
· [LMS / TMS](https://lms-tms.tertiaryinfotech.com/)

---

## Learning outcomes

| | Outcome |
|---|---|
| **LO1** | Collect and analyse customer feedback to assess needs and expectations using effective communication principles. |
| **LO2** | Identify and recommend areas for improvement based on customer feedback and operational insights. |

## Skills Framework mapping

| Code | Ability | | Code | Knowledge |
|---|---|---|---|---|
| **A1** | Carry out collection of customer feedback on service | | **K1** | Principles of effective communication |
| **A2** | Determine customer's needs and expectations in relation to products and services | | **K2** | Customer feedback channels |
| **A3** | Determine areas of improvement as per customer feedback | | **K3** | Operation and process personnel feedback channels |

---

## Course structure

**LU1 — Customer's Needs and Feedback** (LO1 · K1, K2, A1, A2 · 4 h)

| Topic | Title |
|---|---|
| 1 | Understanding Customers & Customer Service |
| 2 | Establishing Your Service Attitude |
| 3 | Identifying and Addressing Customer Needs |
| 4 | In-Person Customer Service |
| 5 | Customer Service Over the Phone |
| 6 | Customer Service via Email and Chat |

**LU2 — Improving Customer's Needs Based on Feedback** (LO2 · K3, A3 · 3 h)

| Topic | Title |
|---|---|
| 7 | Generating Return Business from Feedback |
| 8 | Recovering Difficult Customers |
| 9 | Understanding When to Escalate |

---

## Repository layout

```
courseware/
├── courseware/          the deliverables
│   ├── Improve Your Business with Excellent Customer Service-v2.0.pptx   110-slide deck (+ PDF)
│   ├── LP-Improve Your Business with Excellent Customer Service.docx     Lesson Plan, 9 pp (+ PDF)
│   └── LG-Improve Your Business with Excellent Customer Service.docx     Learner Guide, 39 pp (+ PDF)
├── activities/          9 case-study activities — one folder each (.md + printable .pdf)
├── assets/              brand graphics (generated, matplotlib) + logo
├── build/               the single-source build pipeline
└── .env                 courseware + Drive links
```

> The `assessment/` folder (OQ + RP question papers and answer keys) is **trainer-only and
> deliberately excluded** from this repository.

---

## The activities

Nine real-world Singapore case studies. Each has a **scenario**, **discussion questions**, a
detailed **step-by-step**, a trainer **debrief** and a **self-check** standard.

| # | Activity | Topic | Format | Min |
|---|---|---|---|---|
| 1 | Mapping the Service Chain at a Singapore Bank Branch | 1 | Case Study + Peer Sharing | 20 |
| 2 | Attitude and Positive Language at a Changi Airport Service Counter | 2 | Role Play + Peer Sharing | 15 |
| 3 | Diagnosing Customer Needs at a Growing SME — TechNova Account Review | 3 | Case Study + Role Play | 20 |
| 4 | The Walk-In Interruption — Retail Service Counter, Bugis | 4 | Role Play | 15 |
| 5 | The Angry Delivery Call — Logistics Hotline | 5 | Role Play | 15 |
| 6 | Rewriting the Refund Email — E-Commerce Support Inbox | 6 | Case Study + Practical Writing | 15 |
| 7 | Closing the Loop — F&B Chain Losing Repeat Customers | 7 | Case Study + Group Presentation | 20 |
| 8 | Service Recovery Under Pressure — The Wedding Catering Failure | 8 | Role Play + Case Study | 15 |
| 9 | Drawing the Line — Escalation and Abuse at a Service Counter | 9 | Role Play + Decision Exercise | 15 |

See [`activities/README.md`](activities/README.md) for the full index and the activity → assessment mapping.

---

## Assessment

| Instrument | Format | Duration | Mapping |
|---|---|---|---|
| **Oral Questioning (OQ)** | 3 open-ended questions, individual, open book | 30 min | K1, K2, K3 |
| **Role Play (RP)** | 2 simulated customer interactions, individual, open book | 30 min | A1, A2, A3 |

A minimum of **75% attendance** is required, and the candidate must be assessed **Competent in both
instruments**, to be eligible for funding. Oral Clarification of up to 10 minutes may be conducted
1:1 to close minor performance gaps; it is not counted in the assessment duration.

---

## Building the courseware

Everything is generated from a **single source of truth** — `build/course_data.py` plus
`build/data_domain1.py` and `build/data_domain2.py` — so the deck, Lesson Plan, Learner Guide and
the activity handouts can never drift apart.

```bash
cd build
python3 make_graphics.py        # brand graphics  -> assets/*.png
python3 build_slides.py         # slide deck      -> courseware/*.pptx
python3 build_lesson_plan.py    # lesson plan     -> courseware/LP-*.docx
python3 build_learner_guide.py  # learner guide   -> courseware/LG-*.docx
python3 build_activities.py     # activities      -> activities/activity-NN-*/
python3 build_assessment.py     # assessment      -> assessment/  (trainer-only)
```

Render the DOCX/PPTX to PDF and inject page-numbered tables of contents:

```bash
soffice --headless --convert-to pdf --outdir ../courseware ../courseware/*.docx ../courseware/*.pptx
python3 inject_toc.py "../courseware/LP-….docx" "../courseware/LP-….pdf" 2
```

### Design rules encoded in the build

- All-white slides, Arial, brand palette; footer with course · code · © · slide number.
- **No step-by-step procedure on the slides** — each activity gets a case-study briefing,
  discussion questions and a debrief. The detailed procedure lives only in the Learner Guide
  and the activity handouts.
- Admin order: *Briefing for Assessment* → *Assessment* → *Assessment Flow*; TRAQOM digital
  attendance appears at the **front and again at the end**.
- Restrained motion: content slides fade, section dividers push. Applied in one pass.

---

## Content sources

The approved legacy deck (v1) was used as the coverage floor, then deepened from current industry
practice: [Zendesk](https://www.zendesk.com/sg/blog/important-customer-service-skills/),
[Help Scout](https://www.helpscout.com/blog/customer-service-skills/),
[Qualtrics](https://www.qualtrics.com/articles/customer-experience/customer-service-skills/),
[SurveyMonkey](https://www.surveymonkey.com/learn/customer-feedback/15-qualities-good-customer-service/),
[Coursera](https://www.coursera.org/articles/customer-service-skills),
[Tidio](https://www.tidio.com/blog/customer-service-skills/),
[Intercom](https://www.intercom.com/learning-center/customer-service-skills),
[Indeed SG](https://sg.indeed.com/career-advice/resumes-cover-letters/customer-service-skills) and
[Global Response](https://www.globalresponse.com/blog/customer-service-skills/).

---

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). All rights reserved.
enquiry@tertiaryinfotech.com · +65 6100 0613 · [www.tertiarycourses.com.sg](https://www.tertiarycourses.com.sg)
