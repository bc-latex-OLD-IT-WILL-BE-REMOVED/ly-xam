from mistool.string_use import between
from mistool.os_use import PPath
from orpyste.data import ReadBlock


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAB = " "*4

THIS_DIR = PPath(__file__).parent

EXERCISES_STY = THIS_DIR / "exercises.sty"

CTXTS = {}

LATEX_CNT_STYLE = {
    'I': r"\Roman",
    'i': r"\roman",
    'A': r"\Alph",
    'a': r"\alph",
    '1': r"\arabic"
}

with ReadBlock(
    content = THIS_DIR / "contexts.peuf",
    mode    = "verbatim"
) as data:
    for key, value in data.mydict("mini std").items():
        level, cntstyle = key[1:].split("-")

        CTXTS[int(level)] = (cntstyle, " ".join(value).split())


# ----------- #
# -- TOOLS -- #
# ----------- #

def parse_resetme(ctxt):
    if ctxt[-1] == "*":
        return ctxt[:-1], False

    return ctxt, True


# -------------------------- #
# -- UPDATE EXERCISES.STY -- #
# -------------------------- #

with EXERCISES_STY.open(
    mode     = "r",
    encoding = "utf-8"
) as STY_FILE:
    content = STY_FILE.read()

    before, _, after = between(
        text = content,
        seps = [
            "% Let's build our contexts.",
            "% == LOADING THE STYLE == %"
        ],
        keepseps = True
    )

inside = []

for level, (cntstyle, ctxs) in CTXTS.items():
    cntstyle = LATEX_CNT_STYLE[cntstyle]

    inside.append('')

    for c in ctxs:
        c, _ = parse_resetme(c)

        inside.append(f"\@add@context{{{c}}}")
        inside.append(f"\\newcommand\lyxam@counter@{c}@style[1]{{{cntstyle}{{#1}}}}")


inside += [r"""
% Reseting of counters.
\setsepchar{,}

\newcommand\@auto@reset@by[2]{
    \readlist\parentcounters{#2}%%
    \foreachitem\onecounter\in\parentcounters{%%
        \@addtoreset{#1}{\onecounter}%%
    }%%
}
"""]

level = 1

while level in CTXTS:
    for onectxt in CTXTS[level][1]:
        onectxt, resetme = parse_resetme(onectxt)

        if resetme:
            parentctxts = []

            for parentlevel in range(1, level):
                parentctxts += [
                    f"lyxam@counter@{parse_resetme(c)[0]}"
                    for c in CTXTS[parentlevel][1]
                ]

            parentctxts = ",".join(parentctxts)

            inside.append(
                f"\@auto@reset@by{{lyxam@counter@{onectxt}}}{{{parentctxts}}}"
            )

    level += 1

inside = "\n".join(inside[1:])

with EXERCISES_STY.open(
    mode     = "w",
    encoding = "utf-8"
) as STY_FILE:
    STY_FILE.write(
f"""{before}
{inside}


{after.rstrip()}
"""
    )
