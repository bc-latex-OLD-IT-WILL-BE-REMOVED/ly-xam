#! /usr/bin/env python3

from mistool.latex_use import clean as latexclean
from mistool.os_use import PPath


# ----------------------- #
# -- TOOLS & CONSTANTS -- #
# ----------------------- #

THIS_DIR = PPath( __file__ ).parent
FACTORY_DIR = THIS_DIR.parent / "factory"


# ----------------------- #
# -- CLEAN BEFORE PUSH -- #
# ----------------------- #

for toremove in FACTORY_DIR.walk("file::**.macros-x.txt"):
    toremove.remove()

for toremove in FACTORY_DIR.walk("file::**.pdf"):
    toremove.remove()

for toremove in FACTORY_DIR.walk("dir::*"):
# Bug in mistool !!!!
    if toremove.depth_in(THIS_DIR) == 0 \
    and not toremove.name.startswith("x-"):
        latexclean(toremove)
