#! /usr/bin/env python3

from collections import defaultdict

from mistool.latex_use import install, PPath

DECO = " "*4

answer = input(f"{DECO}* Local installation ? [Y/N] ")

if answer.lower() == "y":
    THIS_DIR = PPath( __file__ ).parent

    install(
        ppath   = THIS_DIR.parent / "lyxam",
        regpath = "file not::**.macros-x.txt"
    )

    print(f"{DECO}* Installation has been done.")
