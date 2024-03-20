#!/bin/bash
#
# Vorbereitung der Daten eines CM1 Experiments fuer PARAVIEW
# I.Kirchner Jan/2021

# WICHTIG!
# aktiviere 'test' environment in conda
# um xarray bug zu umgehen (ältere version benötigt)

# HIER PFAD ANPASSEN
TOOLDIR=/net/scratch/rw0064fu/fortran/cm1-ifm/exp/tools/
TOOL=${TOOLDIR}convert2pv.py

# Tool testen
#$TOOL -h ; exit

# Aufspaltung der Dateien bei Bedarf
CONVERT="${TOOL} --split"
# oder alle in einer Datei
#CONVERT="${TOOL}"

# Optionen für CDOs hier einbinden
CDO="$(which cdo) -s -r -L -w"

# ... erstellt eine Datei {EXP}_[VAR].nc
Convert(){
    VARS=${1}
    LABEL=${2:-_V}
    ${CONVERT} --input ${EXP}_${INFIX}.nc \
	       --output $$ \
	       --var-names ${VARS} && \
	( for FILE in $$*.nc
	  do
	      NEWFILE=${EXP}${LABEL}${FILE##$$}
	      ${CDO} ${TAXIS} \
		     $FILE ${NEWFILE} && echo "... $NEWFILE"
	  done
	) && rm -f $$*.nc
}

# die Liste der 3-D Variablen
VARS_3D="qc,qg,qi"

# die Liste der 2-D Variablen
VARS_2D="cref" # sgs,cape

# Zeitachseneinstellung
# ab min möglich ACHTUNG Zeitachse relativ 
TAXIS='-settaxis,0000-1-1,0:0:0,5min'

# der benutzte Infix des Outfiles
INFIX=cm1out
#
EXP=MR21
# der Name der CM1-Outputdatei wird ... erwartet
# ${EXP}_${INFIX}.nc
# das muss individuell verlinkt werden !!!

INPFILE=${EXP}_${INFIX}.nc
if [ -f ${INPFILE} ]
then
    Convert ${VARS_2D} _2D_
    Convert ${VARS_3D} _3D_
else
    echo "missing Inputfile ... $INPFILE"
fi

