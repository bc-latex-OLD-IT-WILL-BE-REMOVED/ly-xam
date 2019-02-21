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
        "% Build all the contexts.",
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

inside = "\n".join(inside[1:])

content = f"""{before}
{inside}


{after.rstrip()}
"""


before, _, after = between(
    text = content,
    seps = [
        "% The counters for contexts.",
        "% Updating the counters for contexts."
    ],
    keepseps = True
)

inside = []

for level, (cntstyle, ctxs) in CTXTS.items():
    cntstyle = LATEX_CNT_STYLE[cntstyle]

    for c in ctxs:
        c, _ = parse_resetme(c)

        for suffix in [
            "",
            "@star",
            "@star@star"
        ]:
            inside += [
                f"\\newcounter{{lyxam@counter@{c}{suffix}}}",
                f"\\setcounter{{lyxam@counter@{c}{suffix}}}{{0}}"
            ]

        inside += [
            f"\\newcommand\lyxam@counter@{c}@style[1]{{{cntstyle}{{#1}}}}",
            ""
        ]


inside += [r"""% Auto-reset of counters.
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
                for c in CTXTS[parentlevel][1]:
                    for suffix in [
                        "",
                        "@star",
                        "@star@star"
                    ]:
                        parentctxts.append(
                            f"lyxam@counter@{parse_resetme(c)[0]}{suffix}"
                        )

            parentctxts = ",".join(parentctxts)

            inside.append(
                f"\@auto@reset@by{{lyxam@counter@{onectxt}}}{{{parentctxts}}}"
            )

    level += 1

inside = "\n".join(inside)

content = f"""{before}
{inside}

{after}
"""


before, _, after = between(
    text = content,
    seps = [
        "% Building and storing infos to print or not the counters.",
        "\AtEndDocument{%%"
    ],
    keepseps = True
)

allctxts = []

for level, (cntstyle, ctxs) in CTXTS.items():
    for c in ctxs:
        c, _ = parse_resetme(c)

        allctxts.append(c)

inside = "\n".join(inside[1:])

content = f"""{before}
\\setsepchar{{,}}
\\readlist\\@numbered@ctxts{{{",".join(allctxts)}}}
\\newcommand\\@code@to@print@counters{{}}

{after}
"""


before, _, after = between(
    text = content,
    seps = [
        "% Printing or not the counters for contexts.",
        "% Name, shorten or not, of the context with an number or an id."
    ],
    keepseps = True
)

inside = []

for level, (cntstyle, ctxs) in CTXTS.items():
    for c in ctxs:
        c, _ = parse_resetme(c)

        inside.append(f"""\\newcounter{{@cursor@{c}}}
\\setcounter{{@cursor@{c}}}{{1}}
\\@ifundefined{{@lyxam@print@{c}}}{{\\gdef\\@lyxam@print@{c}{{}}}}{{}}
""")

inside = "\n".join(inside)

content = f"""{before}
\setsepchar{{,}}

{inside}
{after}
"""


with EXERCISES_STY.open(
    mode     = "w",
    encoding = "utf-8"
) as STY_FILE:
    STY_FILE.write(content)
