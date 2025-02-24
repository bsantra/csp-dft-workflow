Periodic density functional theory DFT relaxation workflow using Schrodinger and Quantum espresso
To run csp-dft-workflow:
Download from https://github.com/bsantra/csp-dft-workflow

#file description
csp-df-workflow folder contains 
    csp-df-workflow/dft_input: contains configuration, pseudopotential, and analysis scripts
    csp-df-workflow/dft_jobs: your working directory, contains job submission scripts.

#to run
cd csp-df-workflow/dft_jobs
    Inside csp-df-workflow/dft_jobs DFT jobs are run with the following steps:
    -bash job_submit.sh pbed3light
        Launches pbed3light jobs using input as pbed3light-in.maegz
        Returns output as pbed3light.maegz
    -bash filter_structure.sh pbed3light
        Filter structures from pbed3light.maegz
        Returns pbed3light-filtered-relative-energy.csv and pbed3light-filetered.maegz, which is used as input for step 3.
    -bash job_submit.sh r2scand3light
        Launches r2scand3light jobs using input as r2scand3light-in.maegz
        Returns output as r2scand3light.maegz
    -bash filter_structure.sh r2scand3light
        Filter structures from r2scan3light.maegz
        Returns r2scand3light-filtered-relative-energy.csv and r2scand3light-filtered.maegz, which is used as input for step 5.
    -bash job_submit.sh pbed3tight
        Launches pbed3light jobs using input as pbed3tight-in.maegz
        Returns output as pbed3tight.maegz
    -bash filter_structure.sh pbed3tight
        Filter structures from pbed3tight.maegz
        Returns pbed3tight-filtered-relative-energy.csv and pbed3tight-filtered.maegz, which is used as input for step 7.
    -bash job_submit.sh r2scand3tight
        Launches r2scand3light jobs using input as r2scand3tight-in.maegz
        Returns output as r2scand3tight.maegz
    -bash filter_structure.sh r2scand3tight
        Filter structures from r2scan3tight.maegz
        Returns pbed3light-filtered-relative-energy.csv and r2scand3tight-filtered.maegz, the final sorted structure file.

