from mistool.term_use import withframe, ALL_FRAMES
from mistool.os_use import PPath
from orpyste.data import ReadBlock


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

STY_HEADER = withframe(text = "EXAM", frame = ALL_FRAMES["latex_pretty"])


# --------------- #
# -- CONSTANTS -- #
# --------------- #

def normalize(translation):
    return translation


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
                content.append(
                    f"\\newcommand\\lyxam@text@{key}{{{val.title()}}}"
                )


    with ppath.with_ext("sty").open(
        mode     = "w",
        encoding = "utf-8"
    ) as peufile:
        peufile.write("\n".join(content))
