#!/usr/bin/env python3
"""
Brand-exact teaching graphics for the Customer Service deck.

All figures: Arial, white background, brand palette, 150 dpi, tight bbox.
Every number here is the SAME number used in the slides, LG and activities.

Run:  python3 make_graphics.py     -> courseware/assets/*.png
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge

plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 11

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "assets"))
os.makedirs(OUT, exist_ok=True)

BLUE = "#1F6FEB"; TEAL = "#10B981"; VIOLET = "#7C3AED"; AMBER = "#F59E0B"
RED = "#DC2626"; INK = "#161B26"; GREY = "#5B6372"; LIGHT = "#F5F8FC"
LINE = "#E2E8F0"; GREEN = "#16845B"


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ✓", name)


def rbox(ax, x, y, w, h, fc, ec=None, lw=1.6, r=0.045):
    b = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                       fc=fc, ec=ec or fc, lw=lw, zorder=2)
    ax.add_patch(b); return b


def ctext(ax, x, y, s, size=11, color=INK, weight="normal", ha="center", va="center"):
    ax.text(x, y, s, size=size, color=color, weight=weight, ha=ha, va=va, zorder=4)


def blank_ax(w, h):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.axis("off"); fig.patch.set_facecolor("white")
    return fig, ax


def arrow(ax, x1, y1, x2, y2, color=GREY, lw=2.0):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=16, lw=lw, color=color, zorder=3))


def tri(ax, x, y, color, size=1.5, ar=1.0):
    """Right-pointing triangle drawn as a real polygon (Arial has no U+25B6)."""
    ax.add_patch(mpatches.Polygon(
        [[x - size * 0.5, y + size * ar], [x - size * 0.5, y - size * ar], [x + size * 0.9, y]],
        closed=True, fc=color, ec=color, zorder=4))


# ---------------------------------------------------------------- 1. service chain
def service_chain():
    fig, ax = blank_ax(11, 4.0)
    stages = [("INTERNAL\nSUPPORT", "IT · HR · Ops\nenable the frontline", BLUE),
              ("FRONTLINE\nDELIVERY", "The moment the\ncustomer experiences", TEAL),
              ("CUSTOMER\nEXPERIENCE", "What the customer\nperceives and feels", VIOLET),
              ("LOYALTY &\nREVENUE", "Repeat business\nand referral", GREEN)]
    w, gap = 20.5, 5.8
    x0 = 3
    for i, (t, sub, c) in enumerate(stages):
        x = x0 + i * (w + gap)
        rbox(ax, x, 30, w, 44, LIGHT, LINE, 1.2)
        rbox(ax, x, 70, w, 4, c, c, 0)
        ctext(ax, x + w / 2, 60, t, 13, c, "bold")
        ctext(ax, x + w / 2, 42, sub, 10, GREY)
        if i < 3:
            arrow(ax, x + w + 0.8, 52, x + w + gap - 0.8, 52, c, 2.4)
    rbox(ax, 3, 3, 94, 19, LIGHT, LINE, 1.2)
    ctext(ax, 5, 18.0, "THE RULE", 10, BLUE, "bold", ha="left")
    ctext(ax, 5, 10.0,
          "Excellent external service always begins with strong internal service. A break in any link "
          "becomes visible at the frontline —\nbut it is rarely caused there.", 11, INK, ha="left")
    save(fig, "service_chain.png")


# ---------------------------------------------------------------- 2. four levels
def four_levels():
    fig, ax = blank_ax(10, 5.4)
    levels = [("LEVEL 1", "Understand the Problem", "Diagnose before you prescribe.\nAsk, listen, paraphrase.", BLUE),
              ("LEVEL 2", "Meet the Basic Need", "Deliver what was promised,\naccurately and on time.", TEAL),
              ("LEVEL 3", "Think Outside the Box", "Find a route when the\nstandard answer is 'no'.", VIOLET),
              ("LEVEL 4", "Go the Extra Mile", "Give what was never asked for\nbut is exactly what was needed.", AMBER)]
    for i, (lv, t, d, c) in enumerate(levels):
        y = 76 - i * 19
        wdt = 52 + i * 11
        rbox(ax, 6, y, wdt, 15.5, LIGHT, LINE, 1.2)
        rbox(ax, 6, y, 1.6, 15.5, c, c, 0)
        cir = Circle((13, y + 7.7), 4.3, fc=c, ec=c, zorder=4)
        ax.add_patch(cir)
        ctext(ax, 13, y + 7.7, str(i + 1), 15, "white", "bold")
        ctext(ax, 19.5, y + 10.6, t, 13, c, "bold", ha="left")
        ctext(ax, 19.5, y + 4.4, d, 10, GREY, ha="left", va="center")
    ctext(ax, 50, 3, "Each level is only available once the level below it is solid.",
          11, INK, "bold")
    save(fig, "four_levels.png")


# ---------------------------------------------------------------- 3. HEARD
def heard():
    fig, ax = blank_ax(11.5, 4.0)
    st = [("H", "HEAR", "Let them finish.\nDo not interrupt.", BLUE),
          ("E", "EMPATHIZE", "Name the actual loss,\nnot 'the inconvenience'.", TEAL),
          ("A", "APOLOGIZE", "Unconditional.\nNo 'if', no 'but'.", VIOLET),
          ("R", "RESOLVE", "A concrete offer,\nwith a time and an owner.", AMBER),
          ("D", "DIAGNOSE", "Fix the cause so the\nnext customer is spared.", GREEN)]
    w, gap = 16.4, 4.0
    for i, (ltr, t, d, c) in enumerate(st):
        x = 2 + i * (w + gap)
        rbox(ax, x, 26, w, 50, LIGHT, LINE, 1.2)
        rbox(ax, x, 72, w, 4, c, c, 0)
        cir = Circle((x + w / 2, 62), 5.2, fc=c, ec=c, zorder=4); ax.add_patch(cir)
        ctext(ax, x + w / 2, 62, ltr, 19, "white", "bold")
        ctext(ax, x + w / 2, 48, t, 12, c, "bold")
        ctext(ax, x + w / 2, 36, d, 9.5, GREY)
        if i < 4:
            tri(ax, x + w + gap / 2, 51, c, 1.5, 2.6)
    rbox(ax, 2, 2, 96, 18, LIGHT, LINE, 1.2)
    ctext(ax, 4, 16.0, "WHY IT WORKS", 9.5, BLUE, "bold", ha="left")
    ctext(ax, 4, 8.5,
          "Customers judge the outcome, the process AND how they were treated. HEARD is the only framework that "
          "addresses all three —\nwhich is why a well-recovered failure can leave a customer more loyal than one who never had a problem.",
          10.5, INK, ha="left")
    save(fig, "heard_framework.png")


# ---------------------------------------------------------------- 4. feedback channels
def feedback_channels():
    fig, ax = plt.subplots(figsize=(10, 5.2))
    fig.patch.set_facecolor("white")
    ch = ["Surveys\n(CSAT/NPS/CES)", "Online reviews", "Support tickets", "Social listening",
          "Direct interviews", "Frontline staff\nreports"]
    reach = [72, 55, 64, 48, 30, 26]
    depth = [40, 35, 55, 30, 92, 88]
    x = range(len(ch))
    ax.bar([i - 0.2 for i in x], reach, width=0.4, color=BLUE, label="Reach — how many customers it hears from")
    ax.bar([i + 0.2 for i in x], depth, width=0.4, color=TEAL, label="Diagnostic depth — how well it explains WHY")
    ax.set_xticks(list(x)); ax.set_xticklabels(ch, fontsize=10, color=INK)
    ax.set_ylabel("Relative strength", fontsize=11, color=INK)
    ax.set_ylim(0, 105)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(LINE)
    ax.tick_params(colors=GREY)
    ax.grid(axis="y", color=LINE, lw=0.8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=10, loc="upper right")
    ax.set_title("No single channel does both — triangulate or you will fix the wrong thing",
                 fontsize=12.5, color=INK, weight="bold", pad=14)
    fig.tight_layout()
    save(fig, "feedback_channels.png")


# ---------------------------------------------------------------- 5. iceberg
def complaint_iceberg():
    fig, ax = blank_ax(8.6, 5.4)
    ax.add_patch(mpatches.Rectangle((0, 62), 100, 1.1, fc=BLUE, ec=BLUE, zorder=3))
    ctext(ax, 99, 65, "waterline — what you can see", 10, BLUE, "bold", ha="right")
    ax.add_patch(mpatches.Polygon([[50, 96], [36, 63], [64, 63]], closed=True,
                                  fc=TEAL, ec=TEAL, zorder=2))
    ctext(ax, 50, 76, "≈ 4%", 17, "white", "bold")
    ctext(ax, 50, 69, "complain", 11, "white", "bold")
    ax.add_patch(mpatches.Polygon([[36, 62], [64, 62], [92, 6], [8, 6]], closed=True,
                                  fc="#BFD9F5", ec="#BFD9F5", zorder=2))
    ctext(ax, 50, 47, "≈ 56%", 26, BLUE, "bold")
    ctext(ax, 50, 38, "of unhappy customers say NOTHING", 12.5, INK, "bold")
    ctext(ax, 50, 29, "They do not complain. They do not fill in the survey.\nThey simply stop coming back.",
          11, INK)
    ctext(ax, 50, 15, "The absence of complaints is not evidence of satisfaction.", 11.5, BLUE, "bold")
    save(fig, "complaint_iceberg.png")


# ---------------------------------------------------------------- 6. escalation ladder
def escalation_ladder():
    fig, ax = blank_ax(10.4, 5.0)
    rows = [("Frustration with the situation", "'This is daylight robbery.'", "SERVE", TEAL),
            ("Criticism of your competence", "'Are you stupid?'", "SERVE + WARN", AMBER),
            ("Personal / discriminatory abuse", "A slur aimed at you as a person", "ESCALATE", RED),
            ("Legal threats", "'I'll have your job.'", "ESCALATE", RED),
            ("Physical intimidation", "Within arm's reach, finger in your face", "DURESS + EXIT", RED)]
    GAP = 11.0          # extra vertical space inserted for the threshold line
    for i, (b, ex, act, c) in enumerate(rows):
        y = 80 - i * 13.4 - (GAP if i >= 2 else 0)
        rbox(ax, 3, y, 62, 11.4, LIGHT, LINE, 1.2)
        rbox(ax, 3, y, 1.5, 11.4, c, c, 0)
        ctext(ax, 7, y + 7.7, b, 11.5, INK, "bold", ha="left")
        ctext(ax, 7, y + 3.1, ex, 10, GREY, ha="left")
        rbox(ax, 68, y + 1.5, 29, 8.4, c, c, 0)
        ctext(ax, 82.5, y + 5.7, act, 11, "white", "bold")
    row3_top = 80 - 2 * 13.4 - GAP + 11.4      # top edge of the first ABUSE row
    row2_bot = 80 - 1 * 13.4                    # bottom edge of the last ANGER row
    ly = row3_top + (row2_bot - row3_top) * 0.42
    ax.plot([2, 98], [ly, ly], color=RED, lw=2.2, ls="--", zorder=5)
    ctext(ax, 50, ly + 3.8, "THE LINE  —  anger attacks the problem, abuse attacks the person",
          10.5, RED, "bold")
    ctext(ax, 50, 3.0, "Waiting until you feel physically unsafe means you served through the abuse.",
          11, INK, "bold")
    save(fig, "escalation_ladder.png")


# ---------------------------------------------------------------- 7. closed loop
def closed_loop():
    fig, ax = blank_ax(7.6, 6.4)
    cx, cy, r = 50, 54, 30
    steps = [("COLLECT", "across every channel", BLUE),
             ("ANALYSE", "symptom vs root cause", TEAL),
             ("ACT", "owner · date · measure", VIOLET),
             ("TELL THEM", "close the loop visibly", AMBER)]
    for i, (t, d, c) in enumerate(steps):
        a = math.radians(90 - i * 90)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        cir = Circle((x, y), 15.5, fc=LIGHT, ec=c, lw=2.4, zorder=3); ax.add_patch(cir)
        ctext(ax, x, y + 4.4, t, 12.5, c, "bold")
        ctext(ax, x, y - 3.4, d, 9, GREY)
    for i in range(4):
        a1 = math.radians(90 - i * 90 - 26)
        a2 = math.radians(90 - (i + 1) * 90 + 26)
        ax.add_patch(FancyArrowPatch((cx + r * math.cos(a1), cy + r * math.sin(a1)),
                                     (cx + r * math.cos(a2), cy + r * math.sin(a2)),
                                     connectionstyle="arc3,rad=-0.32", arrowstyle="-|>",
                                     mutation_scale=17, lw=2.2, color=GREY, zorder=2))
    ctext(ax, 50, 56, "CLOSED", 12, INK, "bold")
    ctext(ax, 50, 50, "LOOP", 12, INK, "bold")
    ctext(ax, 50, 6,
          "Feedback with no visible action trains customers to stop giving it.\nThe loop is only closed at step 4.",
          11.5, INK, "bold")
    save(fig, "closed_loop.png")


# ---------------------------------------------------------------- 8. channel choice
def channel_matrix():
    fig, ax = plt.subplots(figsize=(8.4, 5.6))
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.axhline(5, color=LINE, lw=1.4); ax.axvline(5, color=LINE, lw=1.4)
    quad = [(2.5, 7.5, "LIVE CHAT", "Simple + urgent\nQuick single questions", TEAL),
            (7.5, 7.5, "PHONE", "Complex + urgent\nEmotional, needs a voice", RED),
            (2.5, 2.5, "SELF-SERVICE", "Simple + not urgent\nFAQ, help centre", BLUE),
            (7.5, 2.5, "EMAIL", "Complex + not urgent\nNeeds a written record", VIOLET)]
    for x, y, t, d, c in quad:
        ax.add_patch(FancyBboxPatch((x - 2.15, y - 1.7), 4.3, 3.4,
                                    boxstyle="round,pad=0,rounding_size=0.16",
                                    fc=LIGHT, ec=c, lw=2.2, zorder=2))
        ax.text(x, y + 0.75, t, size=13.5, color=c, weight="bold", ha="center", zorder=4)
        ax.text(x, y - 0.55, d, size=10, color=GREY, ha="center", zorder=4)
    ax.set_xticks([2.5, 7.5]); ax.set_xticklabels(["Simple issue", "Complex issue"], fontsize=11.5, color=INK)
    ax.set_yticks([2.5, 7.5]); ax.set_yticklabels(["Not urgent", "Urgent"], fontsize=11.5, color=INK)
    ax.tick_params(length=0, colors=INK)
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_title("Choose the channel from the issue — not from what is convenient for you",
                 fontsize=12.5, color=INK, weight="bold", pad=16)
    fig.tight_layout()
    save(fig, "channel_matrix.png")


# ---------------------------------------------------------------- 9. retention economics
def retention_economics():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.3))
    fig.patch.set_facecolor("white")
    a1.bar(["Retain an\nexisting customer", "Acquire a\nnew customer"], [1, 5],
           color=[TEAL, RED], width=0.55)
    a1.set_ylabel("Relative cost", fontsize=11, color=INK)
    a1.set_title("Acquisition costs ~5x retention", fontsize=12, color=INK, weight="bold", pad=12)
    for i, v in enumerate([1, 5]):
        a1.text(i, v + 0.15, f"{v}x", ha="center", fontsize=14, weight="bold",
                color=[TEAL, RED][i])
    a1.set_ylim(0, 6.2)

    x = list(range(0, 6))
    a2.plot(x, [100 * (1.05 ** i) for i in x], color=BLUE, lw=2.6, marker="o", label="+5% retention")
    a2.plot(x, [100] * 6, color=GREY, lw=2.0, ls="--", label="no change")
    a2.fill_between(x, [100] * 6, [100 * (1.05 ** i) for i in x], color=BLUE, alpha=0.12)
    a2.set_xlabel("Periods", fontsize=11, color=INK)
    a2.set_ylabel("Profit index", fontsize=11, color=INK)
    a2.set_title("A 5% retention lift compounds into 25–95% profit", fontsize=12,
                 color=INK, weight="bold", pad=12)
    a2.legend(frameon=False, fontsize=10)
    for a in (a1, a2):
        a.spines[["top", "right"]].set_visible(False)
        a.spines[["left", "bottom"]].set_color(LINE)
        a.tick_params(colors=GREY)
        a.grid(axis="y", color=LINE, lw=0.8); a.set_axisbelow(True)
    fig.tight_layout()
    save(fig, "retention_economics.png")


# ---------------------------------------------------------------- 10. listening funnel
def listening_funnel():
    fig, ax = blank_ax(9.2, 5.1)
    rows = [("ATTEND", "Full attention. Phone down, body turned, eyes up.", BLUE),
            ("ABSORB", "Let them finish. The vent carries the key fact.", TEAL),
            ("PARAPHRASE", "Say it back in your words. Prove you heard it.", VIOLET),
            ("CONFIRM", "'Have I got that right?' — let them correct you.", AMBER),
            ("ACT", "Only now propose a solution.", GREEN)]
    for i, (t, d, c) in enumerate(rows):
        y = 78 - i * 14.5
        inset = i * 4.2
        rbox(ax, 6 + inset, y, 88 - inset * 2, 12, LIGHT, LINE, 1.2)
        rbox(ax, 6 + inset, y, 1.5, 12, c, c, 0)
        ctext(ax, 11 + inset, y + 6, t, 12.5, c, "bold", ha="left")
        ctext(ax, 32 + inset, y + 6, d, 10.5, INK, ha="left")
    ctext(ax, 50, 4,
          "Only 17% of customers believe businesses actually listen to them. Paraphrasing is what makes listening visible.",
          11, INK, "bold")
    save(fig, "listening_funnel.png")


# ---------------------------------------------------------------- 11. email anatomy
def email_anatomy():
    fig, ax = blank_ax(9.6, 5.2)
    rbox(ax, 4, 8, 92, 84, "white", LINE, 1.6)
    rbox(ax, 4, 84, 92, 8, LIGHT, LINE, 1.2)
    ctext(ax, 6.5, 88, "Subject:  Your refund for order #48213 — resolved by 26 August",
          11, INK, "bold", ha="left")
    parts = [("1  GREETING", "Hi Priya,", "Use the name. Never 'Dear Customer'.", BLUE),
             ("2  ACKNOWLEDGE", "You've waited 3 weeks and emailed twice —\nand the wedding is on the 30th.",
              "Name the wait AND the real deadline.", TEAL),
             ("3  SOLUTION", "Your refund clears on 26 August. I've also\nraised an expedite request today.",
              "A calendar date, not '14–21 working days'.", VIOLET),
             ("4  NEXT STEPS", "You don't need to chase this. I'll email you\nthe moment it clears.",
              "Say who does what, by when.", AMBER),
             ("5  SIGN-OFF", "Sarah Tan · Customer Care · 6100 0613", "A real person and a real channel.", GREEN)]
    y = 74
    for tag, body, note, c in parts:
        h = 13 if "\n" in body else 9.5
        rbox(ax, 7, y - h, 55, h, LIGHT, LINE, 1.0)
        rbox(ax, 7, y - h, 1.3, h, c, c, 0)
        ctext(ax, 10, y - 3.6, tag, 8.8, c, "bold", ha="left")
        ctext(ax, 10, y - h + (h - 8.4) / 2 + 1.6, body, 10, INK, ha="left", va="center")
        ctext(ax, 65, y - h / 2, note, 9.5, GREY, ha="left", va="center")
        y -= h + 3.2
    save(fig, "email_anatomy.png")


# ---------------------------------------------------------------- 12. said vs needed
def said_vs_needed():
    fig, ax = blank_ax(10, 4.4)
    rbox(ax, 3, 16, 45, 66, "#FEF2F2", "#F3C6C6", 1.6)
    rbox(ax, 52, 16, 45, 66, "#E8F7EE", "#B7E3CA", 1.6)
    ctext(ax, 25.5, 75, "WHAT THE CUSTOMER SAID", 12, RED, "bold")
    ctext(ax, 74.5, 75, "WHAT THE CUSTOMER NEEDS", 12, GREEN, "bold")
    said = ["\"Uploads are painfully slow.\"", "\"The reports are useless.\"",
            "\"Support took 4 days to reply.\"", "\"Competitors offer more for less.\""]
    need = ["A plan that fits a 50-person firm", "Cost-per-project roll-up for the MD",
            "Confidence the vendor is reliable", "A defensible business case —\nby end of month"]
    for i, s in enumerate(said):
        ctext(ax, 6, 66 - i * 12, s, 10.5, INK, ha="left")
    for i, s in enumerate(need):
        ctext(ax, 55, 66 - i * 12, s, 10.5, INK, ha="left")
    arrow(ax, 48.6, 49, 51.4, 49, GREY, 2.4)
    ctext(ax, 50, 9,
          "The complaints are symptoms. The last line of the email is the actual brief.\nSolve only the left column and you still lose the account.",
          11, INK, "bold")
    save(fig, "said_vs_needed.png")


# ---------------------------------------------------------------- 13. first impression
def first_impression():
    fig, ax = plt.subplots(figsize=(7.4, 4.6), subplot_kw=dict(aspect="equal"))
    fig.patch.set_facecolor("white")
    vals = [55, 38, 7]
    labs = ["Appearance &\nbody language", "Tone of\nvoice", "The words\nthemselves"]
    cols = [BLUE, TEAL, AMBER]
    w, _, _ = ax.pie(vals, labels=None, colors=cols, startangle=90,
                     wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2.4),
                     autopct="%1.0f%%", pctdistance=0.79,
                     textprops=dict(color="white", fontsize=13, weight="bold"))
    ax.legend(labs, frameon=False, fontsize=10.5, loc="center left", bbox_to_anchor=(1.0, 0.5))
    ax.text(0, 0.12, "4–7 sec", ha="center", size=15, weight="bold", color=INK)
    ax.text(0, -0.16, "to form a first\nimpression", ha="center", size=10, color=GREY)
    ax.set_title("Your attitude is visible before you speak", fontsize=12.5,
                 color=INK, weight="bold", pad=14)
    fig.tight_layout()
    save(fig, "first_impression.png")


# ---------------------------------------------------------------- 14. phone flow
def phone_flow():
    fig, ax = blank_ax(11.4, 3.4)
    st = [("GREET", "within 3 rings\nsmile first"), ("LISTEN", "no interruption\nlet them vent"),
          ("PARAPHRASE", "say it back\nconfirm it"), ("HOLD", "ask · why · how long\nthank on return"),
          ("RESOLVE", "options + a\nrecommendation"), ("CLOSE", "time · owner\nreference no.")]
    cols = [BLUE, TEAL, VIOLET, AMBER, GREEN, BLUE]
    w, gap = 13.4, 3.3
    for i, ((t, d), c) in enumerate(zip(st, cols)):
        x = 2.4 + i * (w + gap)
        rbox(ax, x, 24, w, 54, LIGHT, LINE, 1.2)
        rbox(ax, x, 74, w, 4, c, c, 0)
        cir = Circle((x + w / 2, 62), 4.6, fc=c, ec=c, zorder=4); ax.add_patch(cir)
        ctext(ax, x + w / 2, 62, str(i + 1), 15, "white", "bold")
        ctext(ax, x + w / 2, 47, t, 11, c, "bold")
        ctext(ax, x + w / 2, 34, d, 9, GREY)
        if i < 5:
            tri(ax, x + w + gap / 2, 50, c, 1.5, 2.6)
    ctext(ax, 50, 8, "The four-part hold is where most calls are lost: ask permission · state the reason · give a duration · thank them on return.",
          10.5, INK, "bold")
    save(fig, "phone_flow.png")


if __name__ == "__main__":
    print("Generating brand graphics …")
    service_chain(); four_levels(); heard(); feedback_channels()
    complaint_iceberg(); escalation_ladder(); closed_loop(); channel_matrix()
    retention_economics(); listening_funnel(); email_anatomy(); said_vs_needed()
    first_impression(); phone_flow()
    print("Done →", OUT)
