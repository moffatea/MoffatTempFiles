#!/bin/csh
#SBATCH --account=theory
#SBATCH --nodes 1
#SBATCH --partition=theory
#SBATCH --cpus-per-task 5
#SBATCH --mem=2G
#SBATCH --time=0-10:00:00
#SBATCH --constraint=centos7
#SBATCH --job-name="jam-40NW9OKEL7"
#SBATCH --output=/w/general-scifs17exp/JAM//moffatea/workspace/idis2/results/step01/out/jam-40NW9OKEL7.out
#SBATCH --error=/w/general-scifs17exp/JAM//moffatea/workspace/idis2/results/step01/out/jam-40NW9OKEL7.err

setenv FITPACK /w/general-scifs17exp/JAM//moffatea/fitpack
setenv PYTHONPATH /w/general-scifs17exp/JAM//moffatea/fitpack:/work/JAM/apps/lhapdf2/lib/python2.7/site-packages/
/w/general-scifs17exp/JAM//apps/anaconda2/bin/python  /w/general-scifs17exp/JAM//moffatea/fitpack/fitlib/maxlike.py  -n 5 -v 100 input.py -msrh "mv <<fname>> /w/general-scifs17exp/JAM//moffatea/workspace/idis2/results/step01/msr/"   

