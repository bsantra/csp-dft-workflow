#!/bin/bash
SCHRODINGER=PATH_TO_SCHRODINGER
JOBNAME=$1
INPUT=${JOBNAME}-in.maegz
CORES=16 #use number of cores per subjob
HOST=HOST_NAME
SUBHOST=SUBHOST_NAME
NPOOL=1
MAX_SUBJOBS=4
"${SCHRODINGER}/run" periodic_dft_gui_dir/periodic_dft_driver.py -cfg_file ${JOBNAME}.cfg $INPUT -TPP $CORES -JOBNAME $JOBNAME -HOST $HOST -SUBHOST $SUBHOST:$MAX_SUBJOBS -save_failures -npools $NPOOL
