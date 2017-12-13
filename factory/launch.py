#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

import argparse

from mistool.os_use import PPath, runthis


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR  = PPath(__file__).parent
DOC_PDF   = THIS_DIR.parent / "lyxam" / "lyxam-doc[fr].pdf"

EXT_2_CMDS = {
    "py"  : 'python',
    "bash": 'bash'
}


# --------- #
# -- CLI -- #
# --------- #

parser = argparse.ArgumentParser()

for option, default in [
    ('--pdf' , False),
    ('--bash', False),
    ('--all' , False),
    ('--noex' , False)
]:
    parser.add_argument(
        option,
        action  = "store_true",
        default = default
    )

ARGS = parser.parse_args()

if ARGS.all:
    ARGS.pdf   = True
    ARGS.bash  = True
    ARGS.noex = False

# -------------------------------------- #
# -- LAUNCHING ALL THE BUILDING TOOLS -- #
# -------------------------------------- #

PATTERNS = ["file::**build_*.py"]

if ARGS.bash:
    PATTERNS.append("file::**build_*.bash")

PATTERNS.append("file::build_*.py")

for pattern in PATTERNS:
    cmd = EXT_2_CMDS[pattern.split('.')[-1]]

    allpaths = [onepath for onepath in THIS_DIR.walk(pattern)]
    allpaths.sort()

    for onepath in allpaths:
        if ARGS.noex and onepath.name == "build_03-examples.py":
            print(f'+ Ignoring "{onepath - THIS_DIR}"')
            continue

        print(f'+ Launching "{onepath - THIS_DIR}"')

        runthis(
            cmd        = f'{cmd} "{onepath}"',
            showoutput = True
        )


# ------------------- #
# -- SHOWING PDF ? -- #
# ------------------- #

if ARGS.pdf:
    print(f'+ Opening "{DOC_PDF.name}"')

    runthis(cmd = f'open "{DOC_PDF}"')
