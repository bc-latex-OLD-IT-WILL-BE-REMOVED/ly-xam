#! /usr/bin/env python3

from mistool.latex_use import clean as latexclean
from mistool.os_use import PPath


# ----------------------- #
# -- TOOLS & CONSTANTS -- #
# ----------------------- #

FACTORY_DIR = PPath( __file__ ).parent
LYXAM_DIR   = FACTORY_DIR.parent / "lyxam"


# ----------------------- #
# -- CLEAN BEFORE PUSH -- #
# ----------------------- #

for onedir in [FACTORY_DIR, LYXAM_DIR]:
    for filetoremove in onedir.walk("file::**.macros-x.txt"):
        filetoremove.remove()

    for filetoremove in onedir.walk("file::**.scores"):
        filetoremove.remove()

for filetoremove in FACTORY_DIR.walk("file::**.pdf"):
    filetoremove.remove()

for filetoremove in FACTORY_DIR.walk("dir::*"):
    latexclean(filetoremove)
