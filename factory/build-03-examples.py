#! /usr/bin/env python3

from collections import defaultdict

from mistool.latex_use import Build, clean as latexclean
from mistool.os_use import cd, PPath, runthis


# ----------------------- #
# -- TOOLS & CONSTANTS -- #
# ----------------------- #

LYXAM_DIR   = PPath( __file__ ).parent.parent / "lyxam"
STYLES_PATH = LYXAM_DIR / "config" / "style"

DECO = " "*4


# --------------------- #
# -- STYLES TO BUILD -- #
# --------------------- #

templates = {}

for p in STYLES_PATH.walk("file::*.sty"):
    style = p.stem

    for suffix_1 in ["about-src", "no-about-no-src"]:
        for suffix_2 in ["deliver", "no-deliver"]:
            if style == "book" and suffix_2 == "deliver":
                continue

            suffix = f"{suffix_1}-{suffix_2}"

            templatefile = LYXAM_DIR / f"examples-apmep-{suffix}.tex"

            if not templatefile.is_file():
                continue

            with templatefile.open(
                mode     = "r",
                encoding = "utf8"
            ) as f:
                template = "".join(f.readlines())

            filetobuild = LYXAM_DIR / f"examples-{style}-{suffix}.tex"

            if filetobuild.is_file():
                continue

            with filetobuild.open(
                mode     = "w",
                encoding = "utf8"
            ) as f:
                f.write(template.replace("apmep]", f"{style}]"))


# ------------------------ #
# -- LATEX COMPILATIONS -- #
# ------------------------ #

nbrepeat = 3

allexamples = [
    p for p in LYXAM_DIR.walk(f"file::examples-*.tex")
]

allexamples.sort()

for latexpath in allexamples:
    print(
        f"{DECO}* Compilations of << {latexpath.name} >> started : {nbrepeat} times."
    )

    builder = Build(
        ppath      = latexpath,
        repeat     = nbrepeat,
        showoutput = True
    )
    builder.pdf()

    print(
        f"{DECO}* Compilation of << {latexpath.name} >> finished.",
        f"{DECO}* Cleaning extra files.",
        sep = "\n"
    )

latexclean(LYXAM_DIR)
