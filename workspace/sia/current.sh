#!/usr/bin/csh

setenv FITPACK /w/general-scifs17exp/JAM/moffatea/fitpack
setenv PYTHONPATH /w/general-scifs17exp/JAM/moffatea/fitpack:/work/JAM/apps/lhapdf2/lib/python2.7/site-packages/
/w/general-scifs17exp/JAM/apps/anaconda2/bin/python  /w/general-scifs17exp/JAM/moffatea/fitpack/fitlib/maxlike.py  -n 10 -v 1 input.py    -p results2/step02/msr-inspected/3QRIT1HVQ9NY.msr

