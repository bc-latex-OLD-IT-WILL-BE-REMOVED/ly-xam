#! /usr/bin/env python3

from collections import defaultdict

from mistool.os_use import PPath
from mistool.string_use import between, joinand
from mistool.term_use import ALL_FRAMES, withframe
from orpyste.data import ReadBlock

THIS_DIR = PPath( __file__ ).parent

STY_PATH  = THIS_DIR.parent / "lyxam" / "lyxam.sty"
CONF_PATH = THIS_DIR.parent / "lyxam" / "config"


# ----------------------- #
# -- TOOLS & CONSTANTS -- #
# ----------------------- #

LANGS_STYLES = defaultdict(dict)

DECO = " "*4

MYFRAME = lambda x: withframe(
    text  = x,
    frame = ALL_FRAMES['latex_pretty']
)


def cleansource(text):
    if text.strip():
        text = text.split("\n")

        for i in [0, -1]:
            while not text[i].strip():
                text.pop(i)

    else:
        text = []

    return "\n".join(text)


def organize_packages(packages):
    global DECO

    packages_found = defaultdict(list)

    for texpackdef in packages:
        if texpackdef:
            options = between(
                text = texpackdef,
                seps = ["[", "]"]
            )

            if options:
                _, options, texpackdef = options

                options = [x.strip() for x in options.split(",")]

            else:
                options = []

            _, names, _ = between(
                text = texpackdef,
                seps = ["{", "}"]
            )

            for onename in names.split(","):
                packages_found[onename.strip()] += options

    allnames = sorted(packages_found.keys())

    packages_ok = []

    for onename in allnames:
        options = packages_found[onename]

        if options:
            options = f'[{", ".join(options)}]'

        else:
            options = ""

        packages_ok.append(f"\\RequirePackage{options}{{{onename}}}")


    print(f"{DECO}* Declaration of packages organized.")

    return packages_ok


# ---------------- #
# -- NEW THINGS -- #
# ---------------- #

ALL_PACKAGES       = []
ALL_MACROS         = []
ALL_LOCAL_SETTINGS = []

for subdir in THIS_DIR.walk("dir::"):
    subdir_name = str(subdir.name)

    if subdir_name in [
        "config",
    ] or subdir_name[:2] == "x-":
        continue

    for latexfile in subdir.walk("file::*.sty"):
        relative_path = latexfile - THIS_DIR
        relative_depth = latexfile.depth_in(THIS_DIR)

        print(f"{DECO}* Analyzing << {relative_path} >>")

        if relative_depth != 1:
            with open(
                file     = latexfile,
                encoding = "utf-8"
            ) as filetocopy:
                content = filetocopy.read()

            config = LANGS_STYLES[latexfile.parent.name]
            kind   = latexfile.stem

            if kind in config:
                config[kind] += ["\n", content]

            else:
                config[kind] = [content]


        else:  # TODO EVITER REPETITION et pb Process Option !!!!
            with open(
                file     = latexfile,
                encoding = "utf-8"
            ) as filetoupdate:
                _, packages, after = between(
                    text = filetoupdate.read(),
                    seps = [
                        "% == PACKAGES USED == %",
                        "% == GENERAL SETTINGS == %"
                    ],
                    keepseps = True
                )

            ALL_PACKAGES += [
                x.strip()
                for x in packages.strip().split("\n")
            ]


            _, general_settings, after = between(
                text = after,
                seps = [
                    "% == GENERAL SETTINGS == %",
                    "% == LOCAL SETTINGS == %"
                ],
                keepseps = True
            )

            general_settings = cleansource(general_settings)


            _, local_settings, after = between(
                text = after,
                seps = [
                    "% == LOCAL SETTINGS == %",
                    "% == PROCESSING OPTION - LOADING LANG == %"
                ],
                keepseps = True
            )

            local_settings = cleansource(local_settings)


            _, option_lang_load, after = between(
                text = after,
                seps = [
                    "% == PROCESSING OPTION - LOADING LANG == %",
                    "% == DEFINITIONS == %"
                ],
                keepseps = True
            )

            option_lang_load = cleansource(option_lang_load)


            _, definitions, after = between(
                text = after,
                seps = [
                    "% == DEFINITIONS == %",
                    "% == LOADING THE STYLE == %"
                ],
                keepseps = True
            )

            definitions = cleansource(definitions)


            _, style_load, _ = between(
                text = after,
                seps = [
                    "% == LOADING THE STYLE == %",
                    "% == END == %"
                ]
            )

            style_load = cleansource(style_load)


            if local_settings.strip():
                ALL_LOCAL_SETTINGS.append(local_settings)

            if definitions.strip():
                if ALL_MACROS:
                    ALL_MACROS.append("\n")

                ALL_MACROS += [
                    MYFRAME(relative_path.stem.replace('-', ' ').upper()),
                    "",
                    definitions
                ]


ALL_LOCAL_SETTINGS = "\n".join(ALL_LOCAL_SETTINGS)
ALL_MACROS         = "\n".join(ALL_MACROS)


# -------------------------------- #
# -- UPDATE LANG AN STYLE FILES -- #
# -------------------------------- #

for kind, configs in LANGS_STYLES.items():
    for subkind, lines in configs.items():
        confpath = CONF_PATH / kind / f"{subkind}.sty"
        confpath.create("file")

        with confpath.open(
            mode     = "w",
            encoding = "utf-8"
        ) as source:
            source.write("\n".join(lines) + "\n")


# --------------------------------- #
# -- ORGANIZING LIST OF PACKAGES -- #
# --------------------------------- #

ALL_PACKAGES = organize_packages(ALL_PACKAGES)
ALL_PACKAGES = "\n".join(ALL_PACKAGES)


# ------------------------------ #
# -- UPDATE THE MAIN STY FILE -- #
# ------------------------------ #

source = """{0}

{1}


{2}

{3}

{4}

{5}


{6}


{7}

{8}
""".format(
    MYFRAME("PACKAGES REQUIRED"),
    ALL_PACKAGES,
    MYFRAME("OPTIONS"),
    general_settings,
    local_settings,
    option_lang_load,
    ALL_MACROS,
    MYFRAME("OPTIONS"),
    style_load
)


STY_PATH.create("file")

with STY_PATH.open(
    mode     = "w",
    encoding = "utf-8"
) as lyxam:
    lyxam.write(source)

print(f"{DECO}* Update of << {STY_PATH.name} >> done.")
