from mistool.string_use import between
from mistool.os_use import PPath
from orpyste.clean import Clean
from orpyste.data import ReadBlock


# ----------- #
# -- TOOLS -- #
# ----------- #

def shortctxt(ctxt):
    if ctxt[-1] == "*":
        return ctxt[:-1]

    return ctxt


# --------------- #
# -- CONSTANTS -- #
# --------------- #

TAB = " "*4

THIS_DIR = PPath(__file__).parent

CONTEXTS_PEUF = THIS_DIR.parent.parent / "contexts.peuf"

CTXTS = []
with ReadBlock(
    content = CONTEXTS_PEUF,
    mode    = "verbatim"
) as data:
    for key, value in data.mydict("mini std").items():
        CTXTS += [shortctxt(v) for v in value]

CTXTS.sort()


# -------------------------- #
# -- UPDATE STY FOR LANGS -- #
# -------------------------- #

for ppath in THIS_DIR.walk("file::*.peuf"):
    with ppath.open(
        mode     = "r",
        encoding = "utf-8"
    ) as peufile:
        content = peufile.read()

    with ReadBlock(
        content = ppath,
        mode    = "keyval::="
    ) as data:
        dictdatas  = data.mydict("mini std")
        ctxtsfound = dictdatas["contexts"]

        before, _, after = between(
            text = content,
            seps = [
                "contexts::",
                "extra::"
            ],
            keepseps = True
        )

        inside = []


        for onectxt in CTXTS:
            translation = ctxtsfound.get(onectxt,  "?")

            inside.append(f"{TAB}{onectxt} = {translation}")

        inside = "\n".join(inside)

        content = f"""{before}
{inside}

{after}"""

    with Clean(
        content = content,
        layout  = "align",
        mode    = "keyval::="
    ) as datas:
        content = "\n".join(line for line in datas.view)

    with ppath.open(
        mode     = "w",
        encoding = "utf-8"
    ) as peufile:
        peufile.write(content)
