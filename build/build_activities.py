#!/usr/bin/env python3
"""Per-activity handouts — Improve Your Business with Excellent Customer Service.

Writes ONE FOLDER PER ACTIVITY:

    courseware/activities/
        README.md                       index of all nine activities
        activity-01-.../
            activity-01-....md          the brief (scenario · questions · steps · debrief)
            activity-01-....pdf         the same brief rendered to PDF (handout)
        activity-02-.../
        ...

Content comes from data_domain1/2 — the same single source that drives the
slide deck, the Lesson Plan and the Learner Guide, so the four can never drift.

Markdown -> PDF is done with LibreOffice via an intermediate DOCX built with
python-docx, so the PDF carries the house fonts and a proper cover block
(pandoc/LaTeX are not assumed to be installed).
"""
import os, re, sys, subprocess, shutil

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
ACT = DOMAIN1 + DOMAIN2
import prodoc
from docx import Document
from docx.shared import Pt, RGBColor

REPO = os.path.dirname(HERE)                       # .../courseware
ASSETS = os.path.join(REPO, "assets")
OUT = os.path.join(REPO, "activities")

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
BRAND = RGBColor(0x1F, 0x6F, 0xEB); GREEN = RGBColor(0x16, 0x84, 0x5B)
GREY = RGBColor(0x55, 0x5B, 0x66)

TOPICS = {t["num"]: t for t in C.TOPICS}


def slug(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-+", "-", s)[:60]


# ---------------------------------------------------------------- markdown
def render_md(a):
    t = TOPICS[a["topic"]]
    L = []
    L.append(f"# Activity {a['num']} — {a['title']}")
    L.append("")
    L.append(f"**Course:** {C.TITLE} ({C.COURSE_CODE})  ")
    L.append(f"**Topic {t['num']}:** {t['title']}  ")
    L.append(f"**Mapping:** {a['objective']}  ")
    L.append(f"**Format:** {a['type']}  ·  **Duration:** {a['minutes']} minutes  ")
    L.append(f"**Roles:** {a['roles']}")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## The Scenario")
    L.append("")
    for para in [x.strip() for x in a["scenario"].split("\n\n") if x.strip()]:
        L.append(para)
        L.append("")
    L.append("## What You Will Produce")
    L.append("")
    L.append(a["build"])
    L.append("")
    L.append(f"*Materials: {a['services']}.*")
    L.append("")
    L.append("## Discussion Questions")
    L.append("")
    for i, q in enumerate(a["questions"], 1):
        L.append(f"{i}. {q}")
    L.append("")
    L.append("## Step-by-Step")
    L.append("")
    for i, (instr, _cmd) in enumerate(a["steps"], 1):
        L.append(f"{i}. {instr}")
    L.append("")
    L.append("## Debrief — What a Strong Answer Looks Like")
    L.append("")
    for d in a["debrief"]:
        L.append(f"- {d}")
    L.append("")
    L.append("## Check Your Work")
    L.append("")
    L.append(a["test"])
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"*{C.ORG} · {C.UEN} · {C.TITLE} ({C.COURSE_CODE}) · Version {C.VERSION}*")
    L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------- docx -> pdf
def render_docx(a, path):
    t = TOPICS[a["topic"]]
    doc = Document()
    n = doc.styles["Normal"]; n.font.name = "Arial"; n.font.size = Pt(11)
    prodoc.style_headings(doc)

    # header block
    p = doc.add_paragraph()
    r = p.add_run(f"{C.ORG}   ·   {C.UEN}")
    r.font.size = Pt(9); r.font.color.rgb = GREY
    p = doc.add_paragraph()
    r = p.add_run(f"{C.TITLE}   ·   {C.COURSE_CODE}")
    r.font.size = Pt(9); r.font.color.rgb = GREY

    doc.add_heading(f"Activity {a['num']} — {a['title']}", level=1)

    meta = doc.add_table(rows=0, cols=2); meta.style = "Table Grid"
    for k, v in [("Topic", f"{t['num']} — {t['title']}"),
                 ("Mapping", a["objective"]),
                 ("Format", a["type"]),
                 ("Duration", f"{a['minutes']} minutes"),
                 ("Roles", a["roles"])]:
        c = meta.add_row().cells
        c[0].text = ""; rr = c[0].paragraphs[0].add_run(k); rr.bold = True; rr.font.size = Pt(9.5)
        prodoc._shade_cell(c[0], "E8F0FE")
        c[1].text = ""; c[1].paragraphs[0].add_run(v).font.size = Pt(9.5)

    def head(txt, color=BRAND):
        pp = doc.add_paragraph()
        rr = pp.add_run(txt); rr.bold = True; rr.font.size = Pt(12); rr.font.color.rgb = color

    head("The Scenario")
    for para in [x.strip() for x in a["scenario"].split("\n\n") if x.strip()]:
        doc.add_paragraph(para)

    head("What You Will Produce")
    doc.add_paragraph(a["build"])
    pp = doc.add_paragraph(); rr = pp.add_run(f"Materials: {a['services']}.")
    rr.italic = True; rr.font.size = Pt(10); rr.font.color.rgb = GREY

    def numbered(items):
        """Explicit numbering — Word's List Number style continues across
        separate lists, which would make Step-by-Step start at 7."""
        for i, itxt in enumerate(items, 1):
            pp = doc.add_paragraph()
            pp.paragraph_format.left_indent = Pt(18)
            pp.paragraph_format.first_line_indent = Pt(-18)
            rr = pp.add_run(f"{i}.  "); rr.bold = True
            pp.add_run(itxt)

    head("Discussion Questions")
    numbered(a["questions"])

    head("Step-by-Step")
    numbered([instr for instr, _cmd in a["steps"]])

    head("Debrief — What a Strong Answer Looks Like", GREEN)
    for d in a["debrief"]:
        doc.add_paragraph(d, style="List Bullet")

    head("Check Your Work", GREEN)
    doc.add_paragraph(a["test"])

    prodoc.add_page_numbers(doc)
    doc.save(path)


def to_pdf(docx_path, outdir):
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", outdir, docx_path],
                   check=True, capture_output=True)


# ---------------------------------------------------------------- build
def main():
    os.makedirs(OUT, exist_ok=True)
    index = ["# Activities — " + C.TITLE, "",
             f"**Course code:** {C.COURSE_CODE}  ·  **Version:** {C.VERSION}  ·  {C.ORG}", "",
             "Nine real-world Singapore case-study activities. Each folder contains the activity "
             "brief in Markdown and the same brief as a printable PDF handout.", "",
             "| # | Activity | Topic | Format | Duration | Folder |",
             "|---|---|---|---|---|---|"]

    for a in ACT:
        t = TOPICS[a["topic"]]
        folder_name = f"activity-{a['num']:02d}-{slug(a['title'])}"
        folder = os.path.join(OUT, folder_name)
        os.makedirs(folder, exist_ok=True)
        base = folder_name

        md_path = os.path.join(folder, base + ".md")
        with open(md_path, "w") as f:
            f.write(render_md(a))

        docx_path = os.path.join(folder, base + ".docx")
        render_docx(a, docx_path)
        to_pdf(docx_path, folder)
        os.remove(docx_path)          # DOCX was only the PDF intermediate

        pdf_path = os.path.join(folder, base + ".pdf")
        ok = os.path.exists(pdf_path)
        print(f"  {'✓' if ok else '✗'} {folder_name}/  (md + pdf)")

        index.append(f"| {a['num']} | {a['title']} | T{t['num']} {t['title']} | {a['type']} | "
                     f"{a['minutes']} min | [`{folder_name}/`]({folder_name}/) |")

    index += ["", "## How the activities map to the assessment", "",
              "| Activity | Abilities practised | Assessment instrument |",
              "|---|---|---|"]
    for a in ACT:
        codes = [c for c in ("A1", "A2", "A3") if c in a["objective"]]
        ks = [c for c in ("K1", "K2", "K3") if c in a["objective"]]
        instr = "Role Play (RP)" if codes else "Oral Questioning (OQ)"
        if codes and ks:
            instr = "Role Play (RP) + Oral Questioning (OQ)"
        index.append(f"| {a['num']}. {a['title']} | {', '.join(codes + ks) or '—'} | {instr} |")
    index.append("")

    with open(os.path.join(OUT, "README.md"), "w") as f:
        f.write("\n".join(index))
    print("Saved", os.path.join(OUT, "README.md"))


if __name__ == "__main__":
    main()
