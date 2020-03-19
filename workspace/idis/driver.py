#!/usr/bin/env python
import os,sys

import kmeanconf as kc
from analysis.corelib import core
from analysis.corelib import inspect
from analysis.corelib import predict
from analysis.corelib import classifier
from analysis.corelib import optpriors
from analysis.corelib import jar
from analysis.corelib import mlsamples
from analysis.corelib import summary
from analysis.obslib  import idis
from analysis.qpdlib  import pdf_proton
from analysis.qpdlib  import pdf_proton_plot

wdir=sys.argv[1]

##--initial processeing 
#inspect.get_msr_inspected(wdir)
#predict.get_predictions(wdir)
#classifier.gen_labels(wdir,kc)
#jar.gen_jar_file(wdir,kc)
summary.print_summary(wdir,kc)
###
#####--observables
#idis.plot_obs(wdir,kc,False)
#dy_pion.plot_obs(wdir,kc)
##ln.plot_obs(wdir,kc)
##dy_pT_pion.plot_obs(wdir,kc)
###
####--pdfs
#pdf_proton.gen_xf(wdir,['g', 'u', 'ub', 'd', 'db', 's', 'sb','uv','dv','d/u','db+ub','db-ub','s+sb','rs'])
#pdf_proton_plot.PLOTS(1,wdir)
#pdf_pion.gen_xf(wdir,Q2=10.0)
#pdf_pion.plot3_xf(wdir,kc,Q2=10.0)
##pdf_pion.gen_xf(wdir,Q2=None)
##pdf_pion.plot3_xf(wdir,kc,Q2=None)
#pdf_pion.gen_moms(wdir,Q2=None)
#pdf_pion.plot1_mom1(wdir,kc,Q2=None)
#pdf_pion.print_mom1(wdir,kc,Q2=None)
#
#--pi2n
#pdf_pion.plot1_pi2n(wdir,kc)







