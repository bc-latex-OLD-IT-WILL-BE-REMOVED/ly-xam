# << WARNING >>
# Here we work with **two** initial pictures with the **same** size.

# Sources:
#     * https://stackoverflow.com/a/13717788/4589608
#     * https://stackoverflow.com/a/10415158/4589608
#     * https://stackoverflow.com/a/246128/4589608


# ----------- #
# -- TOOLS -- #
# ----------- #

# DIM is a global variable.
function onedim_img() {
    read DIM <<<$(convert $1 -format "%$2" info:)
}

function trim_grav() {
    if [ $1 = "South" ] || [ $1 = "North" ]
    then
        local dims="0x1"
    else
        local dims="1x0"
    fi

    convert $2 -gravity $1 -background white -splice $dims -background black -splice $dims -trim  +repage -chop $dims $3
}


# ---------------- #
# -- LET'S WORK -- #
# ---------------- #

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$THIS_DIR"

echo "    * Compilation of PDF"
python "bash-example-doc-pdf.py"

echo "    * ImageMagick's manipulations: be patient..."
convert -density 300 "example-nodoc[fr].pdf" -quality 100 "example-doc[fr].jpg"

for i in '0' '1'
do
# Original size : W x H
    for dir in 'w' 'h'
    do
        onedim_img "example-doc[fr]-$i.jpg" $dir
        printf -v $dir$i "$DIM"
    done

# Triming above : ... x HUP
    trim_grav "South" "example-doc[fr]-$i.jpg" "example-doc[fr]-$i-temp.jpg"

    onedim_img "example-doc[fr]-$i-temp.jpg" h
    printf -v "hup$i" "$DIM"

# Triming below : ... x HDOWN
    trim_grav "North" "example-doc[fr]-$i.jpg" "example-doc[fr]-$i-temp.jpg"

    onedim_img "example-doc[fr]-$i-temp.jpg" h
    printf -v "hdown$i" "$DIM"

# Triming left : WLEFT x ...
    trim_grav "East" "example-doc[fr]-$i.jpg" "example-doc[fr]-$i-temp.jpg"

    onedim_img "example-doc[fr]-$i-temp.jpg" w
    printf -v "wleft$i" "$DIM"

# Triming right : WRIGHT x ...
    trim_grav "West" "example-doc[fr]-$i.jpg" "example-doc[fr]-$i-temp.jpg"

    onedim_img "example-doc[fr]-$i-temp.jpg" w
    printf -v "wright$i" "$DIM"

# Remove the temporary file.
    rm "example-doc[fr]-$i-temp.jpg"
done

# Biggest HUP & HDOWN.
WRIGHT=$(($wright1>$wright0?$wright1:$wright0))
WLEFT=$(($wleft1>$wleft0?$wleft1:$wleft0))
HUP=$(($hup1>$hup0?$hup1:$hup0))
HDOWN=$(($hdown1>$hdown0?$hdown1:$hdown0))

# Conclusion: we have to crop...
#     ... ``w1 - WRIGHT`` left,
#     ... with a rectangle of width ``w1 - (w1 - WRIGHT) - (w1 - WLEFT)`` which
#         is ``WRIGHT + WLEFT - w1``.
#     ... and also ``h1 - HUP`` above,
#     ... with a rectangle of height ``HUP + HDOWN - h1``.
x=$(($w1 - $WRIGHT))
y=$(($h1 - $HUP))

wrect=$(($WRIGHT + $WLEFT - $w1))
hrect=$(($HUP + $HDOWN - $h1))

for i in '0' '1'
do
    convert "example-doc[fr]-$i.jpg" -crop "$wrect"x"$hrect"+$x+$y "example-doc[fr]-$i.jpg"
done
