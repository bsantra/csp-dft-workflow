#!/bin/bash
INPUT_DIR=./
dft_input=../dft_input/scripts

method=$1
if [ -z $1 ]; then echo ./filter_structure.sh method [pbed3light r2scan3light pbed3tight r2scan3tight]; exit 1 ; fi 

fin=${method}.maegz
echo ... filter $fin 


script1=$dft_input/rename_title.py
script2=$dft_input/sort_energy.py

$SCHRODINGER/run $script1 ${fin}

if [ $fin == "pbed3light.maegz" ];     then ecut=4.0; ncap=200; fnext=r2scand3light-in.maegz; fi
if [ $fin == "r2scand3light.maegz" ];  then ecut=4.0; ncap=100; fnext=pbed3tight-in.maegz; fi
if [ $fin == "pbed3tight.maegz" ];     then ecut=3.0;  ncap=50; fnext=r2scand3tight-in.maegz; fi
if [ $fin == "r2scand3tight.maegz" ];  then ecut=3.0;  ncap=50; fi

fout=${fin/.maegz/-filtered.maegz}
$SCHRODINGER/run $script2 ${fin} -e $ecut -n $ncap -o ${fout} > ${fin/.maegz/.maegz.log}

cp $fout $fnext

