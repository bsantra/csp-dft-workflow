#!/bin/bash
INPUT_DIR=./
dft_input=../dft_input

method=$1
if [ -z $1 ]; then echo ./job_submit.sh method [pbed3light r2scan3light pbed3tight r2scan3tight]; exit 1 ; fi 
fmaegz=${method}-in.maegz
echo ... submit $method jobs using $fmaegz, $method.cfg

cp $dft_input/CFG/${method}.cfg . 

if [ $method == "pbed3light" ];    then cp $dft_input/PP_USPP/* . ; fi 
if [ $method == "r2scand3light" ]; then cp $dft_input/PP_ONCV/* . ; fi 

bash periodic_dft_driver.sh ${method}
