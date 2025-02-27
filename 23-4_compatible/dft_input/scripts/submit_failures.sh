#!/bin/bash

method=$1

dir=${method}_failures

[ ! -d $dir ] && mkdir $dir

cp *UPF *.upf ${method}.cfg ${method}.sh $dir

cp ${method}_failures.maegz $dir/${method}-in.maegz 

cd $dir

./${method}.sh

cd ../
