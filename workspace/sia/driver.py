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
from analysis.qpdlib  import ff
from analysis.qpdlib  import ff_plot
from analysis.obslib  import sia
from qcdlib           import ff0

#--from tools
from tools.tools     import checkdir,save,load
from tools.config    import load_config, conf, options
from tools.inputmod  import INPUTMOD
from tools.randomstr import id_generator

#--from fitlib
from fitlib.resman import RESMAN

wdir='results2/step03'

##--initial processeing 
inspect.get_msr_inspected(wdir)
predict.get_predictions(wdir)
classifier.gen_labels(wdir,kc)
jar.gen_jar_file(wdir,kc)
summary.print_summary(wdir,kc)

####
######--observables
#sia.data_over_theory(wdir,1,kc,'pion')
#sia.data_over_theory(wdir,2,kc,'kaon')
sia.data_over_theory(wdir,3,kc,'hadron')
####
#####--ffs
ff.gen_xf(wdir,'pion',['u+ub','d+db','s+sb','c+cb','b+bb','g'])
ff.gen_xf(wdir,'kaon',['u+ub','d+db','s+sb','c+cb','b+bb','g'])
ff.gen_xf(wdir,'hadron',['u+ub','d+db','s+sb','c+cb','b+bb','g'])
ff_plot.PLOTS(wdir,{'pion','kaon','hadron'})
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
