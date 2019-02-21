from mistool.string_use import between
from mistool.os_use import PPath
from orpyste.data import ReadBlock


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAB = " "*4

THIS_DIR = PPath(__file__).parent

EXERCISES_DOC_1 = THIS_DIR / "exercises-1-gene[fr].tex"
EXERCISES_DOC_3 = THIS_DIR / "exercises-3-score[fr].tex"

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


# --------------------------------- #
# -- UPDATE EXERCISES-1-GENE.TEX -- #
# --------------------------------- #

with EXERCISES_DOC_1.open(
    mode     = "r",
    encoding = "utf-8"
) as TEX_FILE:
    content = TEX_FILE.read()

    before, _, after = between(
        text = content,
        seps = [
            "% All kinds of level 2 contexts - START",
            "% All kinds of level 2 contexts - END"
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
            f"% IDmacro - All kinds of level {level} contexts - START",
            f"% IDmacro - All kinds of level {level} contexts - END"
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

with EXERCISES_DOC_1.open(
    mode     = "w",
    encoding = "utf-8"
) as DOC_FILE:
    DOC_FILE.write(content)



# ---------------------------------- #
# -- UPDATE EXERCISES-3-SCORE.TEX -- #
# ---------------------------------- #

with EXERCISES_DOC_3.open(
    mode     = "r",
    encoding = "utf-8"
) as TEX_FILE:
    content = TEX_FILE.read()

    before, _, after = between(
        text = content,
        seps = [
            "% All kinds of contexts - START",
            "% All kinds of contexts - END"
        ],
        keepseps = True
    )

allctxts = []

for _, ctxts in CTXTS.items():
    for onectxt in ctxts:
        c, _ = parse_resetme(onectxt)

        allctxts.append(c)

allctxts.sort()

inside = []

imax = len(allctxts)
imid = imax // 2 + imax % 2

for ileft in range(imid):
    rule = [allctxts[ileft]]

    iright = ileft + imid
    if iright < imax:
        rule.append(allctxts[iright])

    else:
        rule.append("")

    rule = " &&& ".join(rule)

    inside.append(f"{TAB*4}\\hline {rule} \\\\")


inside = "\n".join(inside)

content = f"""{before}
{TAB*2}\\begin{{center}}
{TAB*3}\\begin{{tabular}}{{|ll@{{\\hskip 0.5ex}}|l@{{\\hskip 0.5ex}}l|}}
{inside}
{TAB*4}\\hline
{TAB*3}\\end{{tabular}}
{TAB*2}\\end{{center}}
{after}
"""

content = content.strip()
content += "\n"

with EXERCISES_DOC_3.open(
    mode     = "w",
    encoding = "utf-8"
) as DOC_FILE:
    DOC_FILE.write(content)
