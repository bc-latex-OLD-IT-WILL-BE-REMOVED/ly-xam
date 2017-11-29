#! /usr/bin/env python3

from collections import defaultdict

from mistool.latex_use import Build, clean as latexclean
from mistool.os_use import cd, PPath, runthis

LYXAM_DIR = PPath( __file__ ).parent.parent / "lyxam"

STYLES_PATH   = LYXAM_DIR / "config" / "style"
EXAMPLES_PATH = LYXAM_DIR / "examples"


# ----------------------- #
# -- TOOLS & CONSTANTS -- #
# ----------------------- #

DECO = " "*4


# --------------------- #
# -- STYLES TO BUILD -- #
# --------------------- #

templates = {}

for suffix_1 in ["about-src", "noabout-nosrc"]:
    for suffix_2 in ["deliver", "no-deliver"]:
        suffix = f"{suffix_1}-{suffix_2}"

        templatefile = EXAMPLES_PATH / f"apmep-{suffix}.tex"

        if not templatefile.is_file():
            continue

        with templatefile.open(
            mode     = "r",
            encoding = "utf8"
        ) as f:
            template = "".join(f.readlines())

        for p in STYLES_PATH.walk("file::*.sty"):
            style = p.stem

            filetobuild = EXAMPLES_PATH / f"{style}-{suffix}.tex"

            if filetobuild.is_file():
                continue

            with filetobuild.open(
                mode     = "w",
                encoding = "utf8"
            ) as f:
                f.write(
                    template.replace("[apmep", f"[{style}")
                )


# ------------------------ #
# -- LATEX COMPILATIONS -- #
# ------------------------ #

nbrepeat = 3

for latexpath in EXAMPLES_PATH.walk(f"file::*.tex"):
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

latexclean(EXAMPLES_PATH)
