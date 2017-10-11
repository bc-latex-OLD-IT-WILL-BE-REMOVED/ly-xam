#! /usr/bin/env python3

from mistool.os_use import PPath
from mistool.term_use import withframe, ALL_FRAMES
from orpyste.data import ReadBlock

THIS_DIR = PPath( __file__ ).parent

DECO = " "*4


# -------------- #
# -- TEMPLATE -- #
# -------------- #

TEMP = withframe(
    text  = "EXAM",
    frame =  ALL_FRAMES["latex_pretty"]
)


# ------------------ #
# -- TRANSLATIONS -- #
# ------------------ #

for ppath in THIS_DIR.walk("file::*.peuf"):
    lang = ppath.stem

    print(f"{DECO}* New lang ``{lang}`` found")

    with ReadBlock(
        content = ppath,
        mode    = "k::="
    ) as data:
        texcommands = {
            f"exam{k}": v.title()
            for k, v in data.mydict("std mini")["exam"].items()
        }

    texcommands = "\n".join([
        f"\\newcommand\\{k}{{{v}}}"
        for k, v in texcommands.items()
    ])


    with open(
        file     = ppath.with_ext("sty"),
        mode     = 'w',
        encoding = 'utf-8'
    ) as texfile:
        texfile.write(
            f"""{TEMP}

{texcommands}
            """.rstrip() + "\n"
        )

    print(f"{DECO}* ``{lang}.sty`` added")
