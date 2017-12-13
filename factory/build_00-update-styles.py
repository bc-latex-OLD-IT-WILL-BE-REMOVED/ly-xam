#! /usr/bin/env python3

from mistool.os_use import PPath
from mistool.string_use import between


# ----------------------- #
# -- TOOLS & CONSTANTS -- #
# ----------------------- #

THIS_DIR = PPath( __file__ ).parent

EXAM_STYLE_DIR = THIS_DIR / "02-kind-of-exam" / "config" / "style"

STYLE_FILES = [
    THIS_DIR / "02-kind-of-exam" / "kind-of-exam.sty",
    THIS_DIR / "03-exercises" / "exercises.sty"
]

DEFAULT_STYLE = "mini"

OPTIONS_DOC = THIS_DIR / "01-options" / "options[fr].tex"


# ---------------- #
# -- NEW STYLES -- #
# ---------------- #

STYLES = [s.stem for s in EXAM_STYLE_DIR.walk("file::*.sty")]

OPTIONS = "\n".join([
    f"\DeclareOption{{{s}}}{{\\renewcommand{{\@style@choosen}}{{{s}}}}}"
    for s in STYLES if s != DEFAULT_STYLE
])

INPUTS = "\n".join([
    f"    {{{s}}}{{\input{{config/style/{s}.sty}}}}%%"
    for s in STYLES
])



# ------------------------------- #
# -- UPDATE THE MAIN STY FILES -- #
# ------------------------------- #

for onesty in STYLE_FILES:
    with onesty.open(
        mode     = "r",
        encoding = "utf-8"
    ) as filetomodify:
        content = filetomodify.read()


    before, _, after = between(
        text = content,
        seps = [
            "% Which style to use ?",
            "% Which language to use ?"
        ],
        keepseps = True
    )

    content = f"""{before}
\\newcommand{{\@style@choosen}}{{mini}}
\DeclareOption{{mini}}{{}}
{OPTIONS}

{after}"""


    before, _, after = between(
        text = content,
        seps = [
            "% Loading the good style",
            "% == END == %"
        ],
        keepseps = True
    )

    content = f"""{before}
\IfStrEqCase{{\@style@choosen}}{{%%
{INPUTS}
}}

{after}"""


    with onesty.open(
        mode     = "w",
        encoding = "utf-8"
    ) as filetomodify:
        filetomodify.write(content)


# -------------------- #
# -- UPDATE THE DOC -- #
# -------------------- #

with OPTIONS_DOC.open(
    mode     = "r",
    encoding = "utf-8"
) as filetomodify:
    content = filetomodify.read()


before, _, after = between(
    text = content,
    seps = [
        r"\begin{itemize}[label={\small\textbullet}]",
        r"\end{itemize}"
    ],
    keepseps = True
)

del STYLES[STYLES.index(DEFAULT_STYLE)]
STYLES = [DEFAULT_STYLE] + STYLES

newlines = []
TAB      = " "*8

for s in STYLES:
    with (EXAM_STYLE_DIR / f"{s}[fr].tex").open(
        mode     = "r",
        encoding = "utf-8"
    ) as filetomodify:
        desc = filetomodify.read().split("\n")

    while not desc[0].strip() or desc[0][0] == "%":
        desc.pop(0)

    if s == DEFAULT_STYLE:
        desc[0] = "Style par défaut, " + desc[0]

    desc = f"\n{TAB}".join(desc)

    newlines.append(f"{TAB}\\item {desc}")

newlines = "\n".join(newlines)


content = f"""{before}
{newlines.rstrip()}
    {after}"""

with OPTIONS_DOC.open(
    mode     = "w",
    encoding = "utf-8"
) as filetomodify:
    filetomodify.write(content)
