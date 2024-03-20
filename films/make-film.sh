#!/bin/bash

# OGV Variante
# video quality: Range is 0–10, where 10 is highest quality.
# 5–7 is a good range to try
# audio quality: Range is -1.0 to 10.0, where 10.0 is highest quality.
# Default is -q:a 3
MakeOGV(){
    ffmpeg -framerate ${FRAMERATE} -i "${BILD_MUSTER}" \
	   -c:v libtheora -q:v 9 -c:a libvorbis -q:a 5 \
	   ${FILM}.ogv
}

# MPEG Variante
MakeMPEG(){
    ffmpeg -framerate ${FRAMERATE} -i "${BILD_MUSTER}" \
	   -vcodec h264 -b:v 10485760 \
	   ${FILM}.mp4
}

# alte langsamen Variante mit convert
MakeWithConvert(){
    FORMAT='-f 9'
    RESCALE="-resize 720x576!"  # SD

    convert -monitor \
	    ${RESCALE} -depth 8 -alpha background ${BILD_MUSTER} \
	    -define registry:temporary-path=/tmp -limit area 0 \
	    ppm:- | \
	ppmtoy4m -S 420mpeg2 -F $((FRAMERATE+1)):1 | \
	mpeg2enc ${FORMAT} -o ${FILM}.mpeg 2>&1 | tee mk_ani.$$
}


BILD_MUSTER=frames/fig.%04d.png
FILM=film
FRAMERATE=4


# am besten für Webgerechte Animationen,
# mpeg wird nicht von jedem Browser gleich verstanden
MakeOGV
#MakeMPEG
