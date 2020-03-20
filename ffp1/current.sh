#!/bin/csh

setenv FITPACK ~/fitpack
setenv PYTHONPATH ~/fitpack:${PYTHONPATH}
/Users/ericmoffat/opt/anaconda2/bin  ~/fitpack/fitlib/maxlike.py  -n 10 -v 1 input.py    

