from mistool.term_use import withframe, ALL_FRAMES
from mistool.os_use import PPath
from orpyste.data import ReadBlock


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

STY_HEADER = withframe(text = "CONTEXTS", frame = ALL_FRAMES["latex_pretty"])


# ----------- #
# -- TOOLS -- #
# ----------- #

def longshortversions(defs):
    longversion, *shortversion = defs.split("|")

    if shortversion:
        shortversion = "|".join(shortversion)

    else:
        shortversion = longversion

    return ("", longversion.strip()), ("short", shortversion.strip())


# -------------------------- #
# -- UPDATE STY FOR LANGS -- #
# -------------------------- #

for ppath in THIS_DIR.walk("file::*.peuf"):
    content = [STY_HEADER, ""]

    with ReadBlock(
        content = ppath,
        mode    = "keyval::="
    ) as data:
        for _, transtalions in data.mydict("mini std").items():
            for key, val in transtalions.items():
                for kind, name in longshortversions(val):
                    content.append(
                        f"\\newcommand\\lyxam@{kind}text@{key}{{{name}}}"
                    )

    with ppath.with_ext("sty").open(
        mode     = "w",
        encoding = "utf-8"
    ) as peufile:
        peufile.write("\n".join(content))
