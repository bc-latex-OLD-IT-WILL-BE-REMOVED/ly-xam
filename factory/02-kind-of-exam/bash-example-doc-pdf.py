#! /usr/bin/env python3

from mistool.latex_use import Build, clean as latexclean
from mistool.os_use import PPath


# ----------------------- #
# -- TOOLS & CONSTANTS -- #
# ----------------------- #

DECO = " "*4

THIS_DIR = PPath( __file__ ).parent


# ------------------------------- #
# -- COMPILE ALL THE DOCS FILE -- #
# ------------------------------- #

nbrepeat = 3

for latexpath in THIS_DIR.walk("file::*nodoc\[fr\].tex"):
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

latexclean(THIS_DIR)
