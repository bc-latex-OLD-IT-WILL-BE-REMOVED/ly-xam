from mistool.string_use import between
from mistool.os_use import PPath
from orpyste.data import ReadBlock


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAB = " "*4

THIS_DIR = PPath(__file__).parent

EXERCISES_STY = THIS_DIR / "exercises.sty"

with ReadBlock(
    content = THIS_DIR / "contexts.peuf",
    mode    = "verbatim"
) as data:
    CTXTS = {
        int(key[1:]): " ".join(value).split()
        for key, value in data.mydict("mini std").items()
    }


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

for level, ctxs in CTXTS.items():
    inside.append('')

    for c in ctxs:
        c, _ = parse_resetme(c)

        inside.append(f"\@add@context{{{c}}}")


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
    for onectxt in CTXTS[level]:
        onectxt, resetme = parse_resetme(onectxt)

        if resetme:


            parentctxts = []

            for parentlevel in range(1, level):
                parentctxts += [
                    f"lyxam@counter@{parse_resetme(c)[0]}"
                    for c in CTXTS[parentlevel]
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
