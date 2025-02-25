#!/bin/bash
SCHRODINGER=/opt/schrodinger/suite/suitefs/suites/suite2025-2-build053
export SCHRODINGER_ESPRESSO_ROOT=/personal-installations/santra/schrodinger_qe_2025-2
JOBNAME=$1
INPUT=${JOBNAME}-in.maegz
CORES=16
HOST=driver-4core-standard
SUBHOST=compute-16core-64gb-preemptible
NPOOL=1
MAX_RETRIES=5
MAX_SUBJOBS=100
"${SCHRODINGER}/run" periodic_dft_gui_dir/periodic_dft_driver.py -cfg_file ${JOBNAME}.cfg $INPUT -TPP $CORES -JOBNAME $JOBNAME -HOST $HOST -SUBHOST $SUBHOST:$MAX_SUBJOBS -max_retries $MAX_RETRIES -qargs=--no-requeue -save_failures -npools $NPOOL
