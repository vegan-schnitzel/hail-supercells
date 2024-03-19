#!/usr/bin/env bash

# process cm1-output with CDO operators to reduce file size
# Robert Wright
# 24.01.24

CDO=$(which cdo)
CDOFLGS="-L -O -f nc4"

SIMPATH=/daten/model-course/WS2023/rw0064fu/cm1
OUTPATH=/net/scratch/rw0064fu/fortran/belegarbeit/data

for mr in 21 #11 14 16
do
    IFILE=${SIMPATH}/MR${mr}/cm1out.nc
    
    # sounding in skew-t/log-p plot with hodograph
    # select first time step & single grid box &
    # potential temperature, pressure, mixing ratio,
    # horizontal wind components
    OFILE=${OUTPATH}/skewt-mr${mr}.nc
    $CDO $CDOFLGS -selname,th,prs,qv,u,v -seltimestep,1 \
                  -selindexbox,1,1,1,1 $IFILE $OFILE 
done    
