from mistool.string_use import between
from mistool.os_use import PPath
from orpyste.data import ReadBlock


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAB = " "*4

THIS_DIR = PPath(__file__).parent

EXERCISES_DOC = THIS_DIR / "exercises-1-gene[fr].tex"

CTXTS = {}

with ReadBlock(
    content = THIS_DIR / "contexts.peuf",
    mode    = "verbatim"
) as data:
    for key, value in data.mydict("mini std").items():
        key = key.split("-")[0]

        CTXTS[int(key[1:])] = " ".join(value).split()


# ----------- #
# -- TOOLS -- #
# ----------- #

def parse_resetme(ctxt):
    if ctxt[-1] == "*":
        return ctxt[:-1], False

    return ctxt, True


# -------------------------- #
# -- UPDATE EXERCISES.TEX -- #
# -------------------------- #

with EXERCISES_DOC.open(
    mode     = "r",
    encoding = "utf-8"
) as STY_FILE:
    content = STY_FILE.read()

    before, _, after = between(
        text = content,
        seps = [
            "% All kind of level 2 contexts - START",
            "% All kind of level 2 contexts - END"
        ],
        keepseps = True
    )

inside = []

for c in CTXTS[2]:
    c, _ = parse_resetme(c)

    inside += [
        f'\\item \\verb+\\{c}+ correspond à "\\lyxam@text@{c}{{}}".',
        ''
    ]

inside = TAB + f"\n{TAB}".join(inside[:-1])

content = f"""{before}
\\begin{{itemize}}
\\makeatletter
{inside}
\\makeatother
\\end{{itemize}}
{after}
"""


for level in range(1, 4):
    before, _, after = between(
        text = content,
        seps = [
            f"% IDmacro - All kind of level {level} contexts - START",
            f"% IDmacro - All kind of level {level} contexts - END"
        ],
        keepseps = True
    )

    inside = []

    for c in CTXTS[level]:
        c, _ = parse_resetme(c)

        inside += [
            f"\\IDmacro{{{c}}}{{6}}{{}}", "",
            f"\\IDmacro{{{c}*}}{{6}}{{}}", "",
            f"\\IDmacro{{{c}**}}{{6}}{{}}", "",
            "\\vspace{0.7ex}"
        ]

    inside = "\n".join(inside[:-1])

    content = f"""{before}
{inside}
{after}
    """


before, _, after = between(
    text = content,
    seps = [
        "% IDmacro - All styles for counters - START",
        "% IDmacro - All styles for counters - END"
    ],
    keepseps = True
)

inside = []

for _, ctxts in CTXTS.items():
    for onectxt in ctxts:
        c, _ = parse_resetme(onectxt)

        inside.append(f"\\IDmacro{{lyxam@counter@{c}@style}}{{0}}{{1}}")

inside.sort()
inside = "\n\n".join(inside)

content = f"""{before}
{inside}
{after}
"""



content = content.strip()
content += "\n"

with EXERCISES_DOC.open(
    mode     = "w",
    encoding = "utf-8"
) as DOC_FILE:
    DOC_FILE.write(content)
