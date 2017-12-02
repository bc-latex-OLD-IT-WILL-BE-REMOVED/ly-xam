#! /usr/bin/env python3

from collections import defaultdict


from mistool.latex_use import install, PPath


THIS_DIR = PPath( __file__ ).parent

install(
    ppath   = THIS_DIR.parent / "lyxam",
    regpath = "file not::**.macros-x.txt"
)
