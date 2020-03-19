import os
conf={}

#--setup posterior sampling

conf['bootstrap']=False
conf['flat par']=False
conf['ftol']=1e-8

#--setup qcd evolution

conf['dglap mode']='truncated'
conf['alphaSmode']='backward'
conf['order'] = 'NLO'
conf['Q20']   = 1.0

#--datasets

conf['datasets']={}

#--SIA pion
conf['datasets']['sia']={}
conf['datasets']['sia']['filters']=[]
conf['datasets']['sia']['filters'].append('z>0.2 and z<0.9')
conf['datasets']['sia']['xlsx']={}
conf['datasets']['sia']['xlsx'][1001]='sia/expdata/1001.xlsx'  # hadron: pion exp: TASSO
conf['datasets']['sia']['xlsx'][1002]='sia/expdata/1002.xlsx'  # hadron: pion exp: TASSO
conf['datasets']['sia']['xlsx'][1003]='sia/expdata/1003.xlsx'  # hadron: pion exp: TASSO
conf['datasets']['sia']['xlsx'][1004]='sia/expdata/1004.xlsx'  # hadron: pion exp: TASSO
conf['datasets']['sia']['xlsx'][1005]='sia/expdata/1005.xlsx'  # hadron: pion exp: TASSO
conf['datasets']['sia']['xlsx'][1006]='sia/expdata/1006.xlsx'  # hadron: pion exp: TASSO
conf['datasets']['sia']['xlsx'][1007]='sia/expdata/1007.xlsx'  # hadron: pion exp: TPC
conf['datasets']['sia']['xlsx'][1008]='sia/expdata/1008.xlsx'  # hadron: pion exp: TPC
conf['datasets']['sia']['xlsx'][1012]='sia/expdata/1012.xlsx'  # hadron: pion exp: HRS
conf['datasets']['sia']['xlsx'][1013]='sia/expdata/1013.xlsx'  # hadron: pion exp: TOPAZ
conf['datasets']['sia']['xlsx'][1014]='sia/expdata/1014.xlsx'  # hadron: pion exp: SLD
conf['datasets']['sia']['xlsx'][1018]='sia/expdata/1018.xlsx'  # hadron: pion exp: ALEPH
conf['datasets']['sia']['xlsx'][1019]='sia/expdata/1019.xlsx'  # hadron: pion exp: OPAL
conf['datasets']['sia']['xlsx'][1025]='sia/expdata/1025.xlsx'  # hadron: pion exp: DELPHI
conf['datasets']['sia']['xlsx'][1028]='sia/expdata/1028.xlsx'  # hadron: pion exp: BABAR
conf['datasets']['sia']['xlsx'][1029]='sia/expdata/1029.xlsx'  # hadron: pion exp: BELL
conf['datasets']['sia']['xlsx'][1030]='sia/expdata/1030.xlsx'  # hadron: pion exp: ARGUS
conf['datasets']['sia']['norm']={}
conf['datasets']['sia']['norm'][1001]={'value':    1.12093e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1002]={'value':    1.00343e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1003]={'value':    1.02776e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1005]={'value':    1.02922e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1006]={'value':    9.93384e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1014]={'value':    9.91111e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1018]={'value':    9.87246e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1028]={'value':    9.97763e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1029]={'value':    8.95630e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1030]={'value':    1.02237e+00,'fixed':False,'min':0.5,'max':1.5}

##--SIA pion HQ
conf['datasets']['sia']['xlsx'][1010]='sia/expdata/1010.xlsx'  # hadron: pion exp: TPC(c)
conf['datasets']['sia']['xlsx'][1011]='sia/expdata/1011.xlsx'  # hadron: pion exp: TPC(b)
conf['datasets']['sia']['xlsx'][1016]='sia/expdata/1016.xlsx'  # hadron: pion exp: SLD(c)
conf['datasets']['sia']['xlsx'][1017]='sia/expdata/1017.xlsx'  # hadron: pion exp: SLD(b)
conf['datasets']['sia']['xlsx'][1023]='sia/expdata/1023.xlsx'  # hadron: pion exp: OPAL(c)
conf['datasets']['sia']['xlsx'][1024]='sia/expdata/1024.xlsx'  # hadron: pion exp: OPAL(b)
conf['datasets']['sia']['xlsx'][1027]='sia/expdata/1027.xlsx'  # hadron: pion exp: DELPHI(b)
conf['datasets']['sia']['norm'][1016]={'value':    9.98835e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1017]={'value':    1.00019e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1023]={'value':    1.27008e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1024]={'value':    1.26453e+00,'fixed':False,'min':0.5,'max':1.5}

##--SIA kaon
conf['datasets']['sia']['xlsx'][2030]='sia/expdata/2030.xlsx'  # hadron: kaon exp: ARGUS
conf['datasets']['sia']['xlsx'][2028]='sia/expdata/2028.xlsx'  # hadron: kaon exp: BABAR
conf['datasets']['sia']['xlsx'][2029]='sia/expdata/2029.xlsx'  # hadron: kaon exp: BELL
conf['datasets']['sia']['xlsx'][2001]='sia/expdata/2001.xlsx'  # hadron: kaon exp: TASSO
conf['datasets']['sia']['xlsx'][2002]='sia/expdata/2002.xlsx'  # hadron: kaon exp: TASSO
conf['datasets']['sia']['xlsx'][2003]='sia/expdata/2003.xlsx'  # hadron: kaon exp: TASSO
conf['datasets']['sia']['xlsx'][2004]='sia/expdata/2004.xlsx'  # hadron: kaon exp: TASSO
conf['datasets']['sia']['xlsx'][2005]='sia/expdata/2005.xlsx'  # hadron: kaon exp: TASSO
conf['datasets']['sia']['xlsx'][2006]='sia/expdata/2006.xlsx'  # hadron: kaon exp: TASSO
conf['datasets']['sia']['xlsx'][2007]='sia/expdata/2007.xlsx'  # hadron: kaon exp: TASSO
conf['datasets']['sia']['xlsx'][2008]='sia/expdata/2008.xlsx'  # hadron: kaon exp: TPC
conf['datasets']['sia']['xlsx'][2012]='sia/expdata/2012.xlsx'  # hadron: kaon exp: HRS
conf['datasets']['sia']['xlsx'][2013]='sia/expdata/2013.xlsx'  # hadron: kaon exp: TOPAZ
conf['datasets']['sia']['xlsx'][2014]='sia/expdata/2014.xlsx'  # hadron: kaon exp: SLD
conf['datasets']['sia']['xlsx'][2018]='sia/expdata/2018.xlsx'  # hadron: kaon exp: ALEPH
conf['datasets']['sia']['xlsx'][2019]='sia/expdata/2019.xlsx'  # hadron: kaon exp: OPAL
conf['datasets']['sia']['xlsx'][2025]='sia/expdata/2025.xlsx'  # hadron: kaon exp: DELPHI
conf['datasets']['sia']['xlsx'][2031]='sia/expdata/2031.xlsx'  # hadron: kaon exp: DELPHI
conf['datasets']['sia']['norm'][2030]={'value':    1.00968e+00,'fixed':False,'min':0.5,'max':1.5,'dN':0.1}
conf['datasets']['sia']['norm'][2028]={'value':    1.00213e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2029]={'value':    1.00000e+00,'fixed':True,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2002]={'value':    9.73464e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2003]={'value':    1.00359e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2005]={'value':    9.98737e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2014]={'value':    9.99114e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2018]={'value':    9.84694e-01,'fixed':False,'min':0.5,'max':1.5}

##--SIA kaon HQ
conf['datasets']['sia']['xlsx'][2016]='sia/expdata/2016.xlsx'  # hadron: kaon exp: SLD(c)
conf['datasets']['sia']['xlsx'][2017]='sia/expdata/2017.xlsx'  # hadron: kaon exp: SLD(b)
conf['datasets']['sia']['xlsx'][2023]='sia/expdata/2023.xlsx'  # hadron: kaon exp: OPAL(c)
conf['datasets']['sia']['xlsx'][2024]='sia/expdata/2024.xlsx'  # hadron: kaon exp: OPAL(b)
conf['datasets']['sia']['xlsx'][2027]='sia/expdata/2027.xlsx'  # hadron: kaon exp: DELPHI(b)
conf['datasets']['sia']['norm'][2016]={'value':    9.98084e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2017]={'value':    9.94084e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2023]={'value':    1.24299e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2024]={'value':    1.30788e+00,'fixed':False,'min':0.5,'max':1.5}

##--SIA hadrons
conf['datasets']['sia']['xlsx'][4000]='sia/expdata/4000.xlsx'  # hadron: hadrons exp: ALEPH
conf['datasets']['sia']['xlsx'][4001]='sia/expdata/4001.xlsx'  # hadron: hadrons exp: DELPHI
conf['datasets']['sia']['xlsx'][4002]='sia/expdata/4002.xlsx'  # hadron: hadrons exp: SLD
#conf['datasets']['sia']['xlsx'][4003]='sia/expdata/4003.xlsx'  # hadron: hadrons exp: TASSO
#conf['datasets']['sia']['xlsx'][4008]='sia/expdata/4008.xlsx'  # hadron: hadrons exp: TASSO
conf['datasets']['sia']['xlsx'][4009]='sia/expdata/4009.xlsx'  # hadron: hadrons exp: TASSO
conf['datasets']['sia']['xlsx'][4010]='sia/expdata/4010.xlsx'  # hadron: hadrons exp: TASSO
#conf['datasets']['sia']['xlsx'][4011]='sia/expdata/4011.xlsx'  # hadron: hadrons exp: TASSO
conf['datasets']['sia']['xlsx'][4012]='sia/expdata/4012.xlsx'  # hadron: hadrons exp: TASSO
#conf['datasets']['sia']['xlsx'][4013]='sia/expdata/4013.xlsx'  # hadron: hadrons exp: TASSO
conf['datasets']['sia']['xlsx'][4004]='sia/expdata/4004.xlsx'  # hadron: hadrons exp: TPC
conf['datasets']['sia']['xlsx'][4005]='sia/expdata/4005.xlsx'  # hadron: hadrons exp: OPAL(b)
conf['datasets']['sia']['xlsx'][4006]='sia/expdata/4006.xlsx'  # hadron: hadrons exp: OPAL(c)
conf['datasets']['sia']['xlsx'][4007]='sia/expdata/4007.xlsx'  # hadron: hadrons exp: OPAL
conf['datasets']['sia']['norm'][4000]={'value':    1.01654e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4002]={'value':    1.01415e+00,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4003]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4008]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4009]={'value':    8.34901e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4010]={'value':    1.00559e+00,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4011]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4012]={'value':    9.38135e-01,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4013]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}



#--parameters
conf['params'] = {}

#--ff parameters

conf['ffpion parametrization']=0
conf['params']['ffpion']={}

conf['params']['ffpion']['g1 N']  ={'value':    1.09200e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['g1 a']  ={'value':    7.64521e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['g1 b']  ={'value':    9.99050e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffpion']['g1 c']  ={'value':    6.43145e+00, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffpion']['g1 d']  ={'value':    2.86250e-02, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['u1 N']  ={'value':    7.66472e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['u1 a']  ={'value':   -1.55289e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['u1 b']  ={'value':    9.07228e-01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffpion']['u1 c']  ={'value':    2.54919e-05, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffpion']['u1 d']  ={'value':    4.11393e-06, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['d1 N']  ={'value':    1.24351e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['d1 a']  ={'value':    4.35135e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['d1 b']  ={'value':    7.39963e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffpion']['d1 c']  ={'value':    5.10711e-02, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffpion']['d1 d']  ={'value':    3.74425e+00, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['s1 N']  ={'value':    1.24351e-01, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffpion']['s1 a']  ={'value':    4.35135e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffpion']['s1 b']  ={'value':    7.39963e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffpion']['s1 c']  ={'value':    5.10711e-02, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffpion']['s1 d']  ={'value':    3.74425e+00, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffpion']['c1 N']  ={'value':    8.02996e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['c1 a']  ={'value':   -1.70922e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['c1 b']  ={'value':    2.92078e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffpion']['c1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffpion']['c1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['b1 N']  ={'value':    5.32428e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['b1 a']  ={'value':   -1.72912e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['b1 b']  ={'value':    3.69955e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffpion']['b1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffpion']['b1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['ub1 N'] ={'value':    1.24351e-01, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffpion']['ub1 a'] ={'value':    4.35135e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffpion']['ub1 b'] ={'value':    7.39963e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffpion']['ub1 c']  ={'value':    5.10711e-02, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffpion']['ub1 d']  ={'value':    3.74425e+00, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffpion']['db1 N'] ={'value':    7.66472e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffpion']['db1 a'] ={'value':   -1.55289e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffpion']['db1 b'] ={'value':    9.07228e-01, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffpion']['db1 c']  ={'value':    2.54919e-05, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffpion']['db1 d']  ={'value':    4.11393e-06, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffpion']['sb1 N'] ={'value':    1.24351e-01, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffpion']['sb1 a'] ={'value':    4.35135e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffpion']['sb1 b'] ={'value':    7.39963e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffpion']['sb1 c']  ={'value':    5.10711e-02, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffpion']['sb1 d']  ={'value':    3.74425e+00, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffpion']['cb1 N'] ={'value':    8.02996e-01, 'min':  0.0 , 'max':     1,'fixed':'c1 N'}
conf['params']['ffpion']['cb1 a'] ={'value':   -1.70922e+00, 'min': -1.8 , 'max':     2,'fixed':'c1 a'}
conf['params']['ffpion']['cb1 b'] ={'value':    2.92078e+00, 'min':  0   , 'max':    10,'fixed':'c1 b'}
#conf['params']['ffpion']['cb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 c'}
#conf['params']['ffpion']['cb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 d'}

conf['params']['ffpion']['bb1 N'] ={'value':    5.32428e-01, 'min':  0.0 , 'max':     1,'fixed':'b1 N'}
conf['params']['ffpion']['bb1 a'] ={'value':   -1.72912e+00, 'min': -1.8 , 'max':     2,'fixed':'b1 a'}
conf['params']['ffpion']['bb1 b'] ={'value':    3.69955e+00, 'min':  0   , 'max':    10,'fixed':'b1 b'}
#conf['params']['ffpion']['bb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 c'}
#conf['params']['ffpion']['bb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 d'}

conf['params']['ffkaon']={}
conf['ffkaon parametrization']=0

conf['params']['ffkaon']['g1 N']  ={'value':    5.51029e-02, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['g1 a']  ={'value':   -8.76860e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['g1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['g1 c']  ={'value':    2.24223e-07, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['g1 d']  ={'value':    7.63136e-07, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['u1 N']  ={'value':    1.46043e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['u1 a']  ={'value':   -4.88392e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['u1 b']  ={'value':    3.84111e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['u1 c']  ={'value':    2.76098e-04, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['u1 d']  ={'value':    6.06026e-03, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['d1 N']  ={'value':    5.91406e-02, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['d1 a']  ={'value':   -5.14846e-02, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['d1 b']  ={'value':    1.20621e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['d1 c']  ={'value':    2.45901e-01, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['d1 d']  ={'value':    2.42214e-02, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['s1 N']  ={'value':    5.91406e-02, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffkaon']['s1 a']  ={'value':   -5.14846e-02, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffkaon']['s1 b']  ={'value':    1.20621e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffkaon']['s1 c']  ={'value':    2.45901e-01, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffkaon']['s1 d']  ={'value':    2.42214e-02, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffkaon']['c1 N']  ={'value':    1.11382e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['c1 a']  ={'value':   -6.94542e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['c1 b']  ={'value':    2.99134e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffkaon']['c1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffkaon']['c1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['b1 N']  ={'value':    3.94740e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['b1 a']  ={'value':   -1.79685e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['b1 b']  ={'value':    3.89600e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffkaon']['b1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffkaon']['b1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['ub1 N'] ={'value':    5.91406e-02, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffkaon']['ub1 a'] ={'value':   -5.14846e-02, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffkaon']['ub1 b'] ={'value':    1.20621e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffkaon']['ub1 c']  ={'value':    2.45901e-01, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffkaon']['ub1 d']  ={'value':    2.42214e-02, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffkaon']['db1 N'] ={'value':    5.91406e-02, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffkaon']['db1 a'] ={'value':   -5.14846e-02, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffkaon']['db1 b'] ={'value':    1.20621e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffkaon']['db1 c']  ={'value':    2.45901e-01, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffkaon']['db1 d']  ={'value':    2.42214e-02, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffkaon']['sb1 N'] ={'value':    1.22065e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['sb1 a'] ={'value':    1.40642e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['sb1 b'] ={'value':    6.59185e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['sb1 c']  ={'value':    1.51472e+01, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['sb1 d']  ={'value':    3.66974e+00, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['cb1 N'] ={'value':    1.11382e-01, 'min':  0.0 , 'max':     1,'fixed':'c1 N'}
conf['params']['ffkaon']['cb1 a'] ={'value':   -6.94542e-01, 'min': -1.8 , 'max':     2,'fixed':'c1 a'}
conf['params']['ffkaon']['cb1 b'] ={'value':    2.99134e+00, 'min':  0   , 'max':    10,'fixed':'c1 b'}
#conf['params']['ffkaon']['cb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 c'}
#conf['params']['ffkaon']['cb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 d'}

conf['params']['ffkaon']['bb1 N'] ={'value':    3.94740e-01, 'min':  0.0 , 'max':     1,'fixed':'b1 N'}
conf['params']['ffkaon']['bb1 a'] ={'value':   -1.79685e+00, 'min': -1.8 , 'max':     2,'fixed':'b1 a'}
conf['params']['ffkaon']['bb1 b'] ={'value':    3.89600e+00, 'min':  0   , 'max':    10,'fixed':'b1 b'}
#conf['params']['ffkaon']['bb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 c'}
#conf['params']['ffkaon']['bb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 d'}

conf['params']['ffhadron']={}
conf['ffhadron parametrization']='sum2'

conf['params']['ffhadron']['g1 N']  ={'value':    8.35697e-01, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['g1 a']  ={'value':   -1.32356e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['g1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffhadron']['g1 c']  ={'value':    3.71236e-01, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffhadron']['g1 d']  ={'value':    1.28732e-06, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffhadron']['u1 N']  ={'value':    8.74858e-02, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['u1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['u1 b']  ={'value':    2.53505e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffhadron']['u1 c']  ={'value':    6.64169e-08, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffhadron']['u1 d']  ={'value':    7.39995e-05, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffhadron']['d1 N']  ={'value':    8.74858e-02, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['d1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['d1 b']  ={'value':    2.53505e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['d1 c']  ={'value':    6.64169e-08, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['d1 d']  ={'value':    7.39995e-05, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['s1 N']  ={'value':    8.16509e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['s1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['s1 b']  ={'value':    2.53505e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['s1 c']  ={'value':    6.64169e-08, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['s1 d']  ={'value':    7.39995e-05, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['c1 N']  ={'value':    8.56220e-02, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['c1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['c1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['c1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['c1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}

conf['params']['ffhadron']['b1 N']  ={'value':    7.28320e-02, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['b1 a']  ={'value':   -1.06166e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['b1 b']  ={'value':    2.56130e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['b1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['b1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}

conf['params']['ffhadron']['ub1 N'] ={'value':    8.16509e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['ub1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['ub1 b'] ={'value':    2.53505e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['ub1 c']  ={'value':    6.64169e-08, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['ub1 d']  ={'value':    7.39995e-05, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['db1 N'] ={'value':    1.74388e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['db1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['db1 b'] ={'value':    2.53505e+00, 'min':  0   , 'max':    20,'fixed':'u1 b'}
conf['params']['ffhadron']['db1 c']  ={'value':    6.64169e-08, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['db1 d']  ={'value':    7.39995e-05, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['sb1 N'] ={'value':    8.74858e-02, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['sb1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['sb1 b'] ={'value':    2.53505e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['sb1 c']  ={'value':    6.64169e-08, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['sb1 d']  ={'value':    7.39995e-05, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['cb1 N'] ={'value':    8.56220e-02, 'min':  0.0 , 'max':     1,'fixed':'c1 N'}
conf['params']['ffhadron']['cb1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'c1 a'}
conf['params']['ffhadron']['cb1 b'] ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':'c1 b'}
#conf['params']['ffhadron']['cb1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'c1 c'}
#conf['params']['ffhadron']['cb1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'c1 d'}

conf['params']['ffhadron']['bb1 N'] ={'value':    7.28320e-02, 'min':  0.0 , 'max':     1,'fixed':'b1 N'}
conf['params']['ffhadron']['bb1 a'] ={'value':   -1.06166e+00, 'min': -1.8 , 'max':     2,'fixed':'b1 a'}
conf['params']['ffhadron']['bb1 b'] ={'value':    2.56130e+00, 'min':  0   , 'max':    10,'fixed':'b1 b'}
#conf['params']['ffhadron']['bb1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'b1 c'}
#conf['params']['ffhadron']['bb1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'b1 d'}

#--steps
conf['steps']={}

#--sia
#conf['steps'][1]={}
#conf['steps'][1]['dep']=[]
#conf['steps'][1]['active distributions']=['ffpion']
#conf['steps'][1]['datasets']={}
#conf['steps'][1]['datasets']['sia']=[]
#conf['steps'][1]['datasets']['sia'].append(1001)
#conf['steps'][1]['datasets']['sia'].append(1002)
#conf['steps'][1]['datasets']['sia'].append(1003)
#conf['steps'][1]['datasets']['sia'].append(1004)
#conf['steps'][1]['datasets']['sia'].append(1005)
#conf['steps'][1]['datasets']['sia'].append(1006)
#conf['steps'][1]['datasets']['sia'].append(1007)
#conf['steps'][1]['datasets']['sia'].append(1008)
#conf['steps'][1]['datasets']['sia'].append(1010)
#conf['steps'][1]['datasets']['sia'].append(1011)
#conf['steps'][1]['datasets']['sia'].append(1012)
#conf['steps'][1]['datasets']['sia'].append(1013)
#conf['steps'][1]['datasets']['sia'].append(1014)
#conf['steps'][1]['datasets']['sia'].append(1016)
#conf['steps'][1]['datasets']['sia'].append(1017)
#conf['steps'][1]['datasets']['sia'].append(1018)
#conf['steps'][1]['datasets']['sia'].append(1019)
#conf['steps'][1]['datasets']['sia'].append(1023)
#conf['steps'][1]['datasets']['sia'].append(1024)
#conf['steps'][1]['datasets']['sia'].append(1025)
#conf['steps'][1]['datasets']['sia'].append(1027)
#conf['steps'][1]['datasets']['sia'].append(1028)
#conf['steps'][1]['datasets']['sia'].append(1029)
#conf['steps'][1]['datasets']['sia'].append(1030)

#conf['steps'][2]={}
#conf['steps'][2]['dep']=[1]
#conf['steps'][2]['active distributions']=['ffkaon','ffpion']
#conf['steps'][2]['passive distributions']=['ffpion']
#conf['steps'][2]['datasets']={}
#conf['steps'][2]['datasets']['sia']=[]
#conf['steps'][2]['datasets']['sia'].append(2030)
#conf['steps'][2]['datasets']['sia'].append(2028)
#conf['steps'][2]['datasets']['sia'].append(2029)
#conf['steps'][2]['datasets']['sia'].append(2001)
#conf['steps'][2]['datasets']['sia'].append(2002)
#conf['steps'][2]['datasets']['sia'].append(2003)
#conf['steps'][2]['datasets']['sia'].append(2004)
#conf['steps'][2]['datasets']['sia'].append(2005)
#conf['steps'][2]['datasets']['sia'].append(2006)
#conf['steps'][2]['datasets']['sia'].append(2007)
#conf['steps'][2]['datasets']['sia'].append(2008)
#conf['steps'][2]['datasets']['sia'].append(2012)
#conf['steps'][2]['datasets']['sia'].append(2013)
#conf['steps'][2]['datasets']['sia'].append(2014)
#conf['steps'][2]['datasets']['sia'].append(2018)
#conf['steps'][2]['datasets']['sia'].append(2019)
#conf['steps'][2]['datasets']['sia'].append(2025)
#conf['steps'][2]['datasets']['sia'].append(2031)
#conf['steps'][2]['datasets']['sia'].append(2016)
#conf['steps'][2]['datasets']['sia'].append(2017)
#conf['steps'][2]['datasets']['sia'].append(2023)
#conf['steps'][2]['datasets']['sia'].append(2024)
#conf['steps'][2]['datasets']['sia'].append(2027)

#conf['steps'][3]={}
#conf['steps'][3]['dep']=[1,2]
#conf['steps'][3]['active distributions']=['ffhadron','ffpion','ffkaon']
#conf['steps'][3]['passive distributions']=['ffpion','ffkaon']
#conf['steps'][3]['datasets']={}
#conf['steps'][3]['datasets']['sia']=[]
#conf['steps'][3]['datasets']['sia'].append(4000)
#conf['steps'][3]['datasets']['sia'].append(4001)
#conf['steps'][3]['datasets']['sia'].append(4002)
#conf['steps'][3]['datasets']['sia'].append(4004)
#conf['steps'][3]['datasets']['sia'].append(4005)
#conf['steps'][3]['datasets']['sia'].append(4006)
#conf['steps'][3]['datasets']['sia'].append(4007)
#conf['steps'][3]['datasets']['sia'].append(4009)
#conf['steps'][3]['datasets']['sia'].append(4010)
#conf['steps'][3]['datasets']['sia'].append(4012)

conf['steps'][4]={}
conf['steps'][4]['dep']=[1,2,3]
conf['steps'][4]['active distributions']=['ffhadron','ffpion','ffkaon']
conf['steps'][4]['datasets']={}
conf['steps'][4]['datasets']['sia']=[]
conf['steps'][4]['datasets']['sia'].append(1001)
conf['steps'][4]['datasets']['sia'].append(1002)
conf['steps'][4]['datasets']['sia'].append(1003)
conf['steps'][4]['datasets']['sia'].append(1004)
conf['steps'][4]['datasets']['sia'].append(1005)
conf['steps'][4]['datasets']['sia'].append(1006)
conf['steps'][4]['datasets']['sia'].append(1007)
conf['steps'][4]['datasets']['sia'].append(1008)
conf['steps'][4]['datasets']['sia'].append(1010)
conf['steps'][4]['datasets']['sia'].append(1011)
conf['steps'][4]['datasets']['sia'].append(1012)
conf['steps'][4]['datasets']['sia'].append(1013)
conf['steps'][4]['datasets']['sia'].append(1014)
conf['steps'][4]['datasets']['sia'].append(1016)
conf['steps'][4]['datasets']['sia'].append(1017)
conf['steps'][4]['datasets']['sia'].append(1018)
conf['steps'][4]['datasets']['sia'].append(1019)
conf['steps'][4]['datasets']['sia'].append(1023)
conf['steps'][4]['datasets']['sia'].append(1024)
conf['steps'][4]['datasets']['sia'].append(1025)
conf['steps'][4]['datasets']['sia'].append(1027)
conf['steps'][4]['datasets']['sia'].append(1028)
conf['steps'][4]['datasets']['sia'].append(1029)
conf['steps'][4]['datasets']['sia'].append(1030)
conf['steps'][4]['datasets']['sia'].append(2030)
conf['steps'][4]['datasets']['sia'].append(2028)
conf['steps'][4]['datasets']['sia'].append(2029)
conf['steps'][4]['datasets']['sia'].append(2001)
conf['steps'][4]['datasets']['sia'].append(2002)
conf['steps'][4]['datasets']['sia'].append(2003)
conf['steps'][4]['datasets']['sia'].append(2004)
conf['steps'][4]['datasets']['sia'].append(2005)
conf['steps'][4]['datasets']['sia'].append(2006)
conf['steps'][4]['datasets']['sia'].append(2007)
conf['steps'][4]['datasets']['sia'].append(2008)
conf['steps'][4]['datasets']['sia'].append(2012)
conf['steps'][4]['datasets']['sia'].append(2013)
conf['steps'][4]['datasets']['sia'].append(2014)
conf['steps'][4]['datasets']['sia'].append(2018)
conf['steps'][4]['datasets']['sia'].append(2019)
conf['steps'][4]['datasets']['sia'].append(2025)
conf['steps'][4]['datasets']['sia'].append(2031)
conf['steps'][4]['datasets']['sia'].append(2016)
conf['steps'][4]['datasets']['sia'].append(2017)
conf['steps'][4]['datasets']['sia'].append(2023)
conf['steps'][4]['datasets']['sia'].append(2024)
conf['steps'][4]['datasets']['sia'].append(2027)
conf['steps'][4]['datasets']['sia'].append(4000)
conf['steps'][4]['datasets']['sia'].append(4001)
conf['steps'][4]['datasets']['sia'].append(4002)
conf['steps'][4]['datasets']['sia'].append(4004)
conf['steps'][4]['datasets']['sia'].append(4005)
conf['steps'][4]['datasets']['sia'].append(4006)
conf['steps'][4]['datasets']['sia'].append(4007)
conf['steps'][4]['datasets']['sia'].append(4009)
conf['steps'][4]['datasets']['sia'].append(4010)
conf['steps'][4]['datasets']['sia'].append(4012)

