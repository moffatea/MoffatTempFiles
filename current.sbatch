#!/bin/csh
#SBATCH --account=theory
#SBATCH --nodes 1
#SBATCH --partition=theory
#SBATCH --cpus-per-task 7
#SBATCH --mem=7G
#SBATCH --time=0-96:00:00
#SBATCH --constraint=general
#SBATCH --job-name="jam-2T1B95G83Q"
#SBATCH --output=/w/general-scifs17exp/JAM/moffatea/workspace/hadmc7/results/step11/out/jam-2T1B95G83Q.out
#SBATCH --error=/w/general-scifs17exp/JAM/moffatea/workspace/hadmc7/results/step11/out/jam-2T1B95G83Q.err

setenv FITPACK /w/general-scifs17exp/JAM/moffatea/fitpack
setenv PYTHONPATH /w/general-scifs17exp/JAM/moffatea/fitpack:/work/JAM/apps/lhapdf2/lib/python2.7/site-packages/
/w/general-scifs17exp/JAM/apps/anaconda2/bin/python  /w/general-scifs17exp/JAM/moffatea/fitpack/fitlib/maxlike.py  -n 7 -v 100 input.py -msrh "mv <<fname>> /w/general-scifs17exp/JAM/moffatea/workspace/hadmc7/results/step11/msr/"   -p /w/general-scifs17exp/JAM/moffatea/workspace/hadmc7/results/step10/msr-opt-priors/QOPTYSPKVQ5A.msr

