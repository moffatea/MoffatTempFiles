#!/usr/bin/env python
import os,sys
import numpy as np

import kmeanconf as kc
from analysis.corelib import core
from analysis.corelib import inspect
from analysis.corelib import predict
from analysis.corelib import classifier
from analysis.corelib import optpriors
from analysis.corelib import jar
from analysis.corelib import mlsamples
from analysis.corelib import summary
from analysis.qpdlib  import ff,pdf_proton#,lhapdf_data
from analysis.qpdlib  import ff_plot,pdf_proton_plot
from analysis.obslib  import sia,sidis,idis,dy_hadron,datakin
from analysis.parlib  import params

#--from tools
from tools.tools     import checkdir,save,load
from tools.config    import load_config, conf, options
from tools.inputmod  import INPUTMOD
from tools.randomstr import id_generator

#--from fitlib
from fitlib.resman import RESMAN

wdir='results/step10'

##--initial processeing 
#inspect.get_msr_inspected(wdir)
#predict.get_predictions(wdir)
#classifier.gen_labels(wdir,kc)
#jar.gen_jar_file(wdir,kc)
#summary.print_summary(wdir,kc)

##--optimal priors
#optpriors.gen_priors(wdir,kc,500)

####
######--parameters
#params.plot_params(wdir,'ffpion',kc)
#params.plot_params(wdir,'ffkaon',kc)
#params.plot_params(wdir,'ffhadron',kc)
#params.plot_params(wdir,'pdf',kc)

####
######--observables
sia.plot_xsec_offset(wdir,kc,'hadron')
#sia.plot_xsec_scaling(wdir,kc)
#sidis.plot_mult_scale(wdir,kc,'pion')
#sidis.plot_mult_scale(wdir,kc,'kaon')
#sidis.plot_mult_scale(wdir,kc,'hadron')
#datakin.plot_kin(wdir,kc)

####
#####--ffs
#ff.gen_xf(wdir,'pion',['u','ub','d','db','s','sb','c','b','g'])
#ff.gen_xf(wdir,'kaon',['u','ub','d','db','s','sb','c','b','g'])
#ff.gen_xf(wdir,'hadron',['u','ub','d','db','s','sb','c','b','g'])
#ff_plot.PLOTS(wdir,{'pion'},2)
#ff_plot.PLOTS(wdir,{'kaon'},2)
#ff_plot.PLOTS(wdir,{'pion','kaon'},2)
#ff_plot.PLOTS(wdir,{'pion','kaon','hadron'},2)
#ff_plot.PLOTS(wdir,{'pion','kaon','hadron'},3)

####
######--pdfs
#pdf_proton.gen_xf(wdir,['g', 'u', 'ub', 'd', 'db', 's', 'sb','uv','dv','d/u','db+ub','db-ub','s+sb','rs'])
#lhapdf_data.generate_xf(wdir,'JAM19PDF_proton_nlo',['g', 'u', 'ub', 'd', 'db', 's', 'sb','uv','dv','d/u','db+ub','db-ub','s+sb','rs'])
#pdf_proton_plot.PLOTS(1,wdir)
#pdf_proton_plot.PLOTS(2,wdir)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
