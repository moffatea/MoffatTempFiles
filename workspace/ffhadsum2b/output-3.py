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

#--setup for idis

conf['tmc']   = False
conf['ht']    = False
conf['nuc']=True
conf['sidis nuc smearing']=False
conf['hq']=False

#--grids

conf['path2idistab'] = '%s/grids/grids-idis/distab/'%os.environ['FITPACK']
conf['path2dytab']   = '%s/grids/grids-dy/'%os.environ['FITPACK']
conf['path2jettab']   = '%s/grids/grids-jets/'%os.environ['FITPACK']
conf['path2pidistab']   = '%s/grids/grids-pidis/'%os.environ['FITPACK']
conf['path2sidistab']   = '%s/grids/grids-sidis/'%os.environ['FITPACK']

#--datasets

conf['datasets']={}

#--SIA pion
conf['datasets']['sia']={}
conf['datasets']['sia']['filters']=[]
conf['datasets']['sia']['filters'].append('z>0.1')
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
conf['datasets']['sia']['norm'][1001]={'value':    1.10478e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1002]={'value':    9.82581e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1003]={'value':    1.03054e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1005]={'value':    1.03419e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1006]={'value':    9.79162e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1014]={'value':    9.97770e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1018]={'value':    1.02378e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1028]={'value':    9.76001e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1029]={'value':    8.68358e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1030]={'value':    1.01509e+00,'fixed':False,'min':0.5,'max':1.5}

##--SIA pion HQ
conf['datasets']['sia']['xlsx'][1010]='sia/expdata/1010.xlsx'  # hadron: pion exp: TPC(c)
conf['datasets']['sia']['xlsx'][1011]='sia/expdata/1011.xlsx'  # hadron: pion exp: TPC(b)
conf['datasets']['sia']['xlsx'][1016]='sia/expdata/1016.xlsx'  # hadron: pion exp: SLD(c)
conf['datasets']['sia']['xlsx'][1017]='sia/expdata/1017.xlsx'  # hadron: pion exp: SLD(b)
conf['datasets']['sia']['xlsx'][1023]='sia/expdata/1023.xlsx'  # hadron: pion exp: OPAL(c)
conf['datasets']['sia']['xlsx'][1024]='sia/expdata/1024.xlsx'  # hadron: pion exp: OPAL(b)
conf['datasets']['sia']['xlsx'][1027]='sia/expdata/1027.xlsx'  # hadron: pion exp: DELPHI(b)
conf['datasets']['sia']['norm'][1016]={'value':    1.18920e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1017]={'value':    1.00345e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1023]={'value':    1.33434e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][1024]={'value':    1.19151e+00,'fixed':False,'min':0.5,'max':1.5}

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
conf['datasets']['sia']['norm'][2030]={'value':    1.00482e+00,'fixed':False,'min':0.5,'max':1.5,'dN':0.1}
conf['datasets']['sia']['norm'][2028]={'value':    9.97435e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2029]={'value':    1.00000e+00,'fixed':True,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2002]={'value':    9.83394e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2003]={'value':    9.94421e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2005]={'value':    9.92876e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2014]={'value':    9.12186e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2018]={'value':    8.88453e-01,'fixed':False,'min':0.5,'max':1.5}

##--SIA kaon HQ
conf['datasets']['sia']['xlsx'][2016]='sia/expdata/2016.xlsx'  # hadron: kaon exp: SLD(c)
conf['datasets']['sia']['xlsx'][2017]='sia/expdata/2017.xlsx'  # hadron: kaon exp: SLD(b)
conf['datasets']['sia']['xlsx'][2023]='sia/expdata/2023.xlsx'  # hadron: kaon exp: OPAL(c)
conf['datasets']['sia']['xlsx'][2024]='sia/expdata/2024.xlsx'  # hadron: kaon exp: OPAL(b)
conf['datasets']['sia']['xlsx'][2027]='sia/expdata/2027.xlsx'  # hadron: kaon exp: DELPHI(b)
conf['datasets']['sia']['norm'][2016]={'value':    1.03996e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2017]={'value':    1.00015e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2023]={'value':    1.35922e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][2024]={'value':    1.38163e+00,'fixed':False,'min':0.5,'max':1.5}

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
conf['datasets']['sia']['norm'][4000]={'value':    1.07218e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4002]={'value':    1.06526e+00,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4003]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4008]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4009]={'value':    6.54559e-01,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4010]={'value':    9.00531e-01,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4011]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sia']['norm'][4012]={'value':    1.01288e+00,'fixed':False,'min':0.5,'max':1.5}
#conf['datasets']['sia']['norm'][4013]={'value':    1.00000e+00,'fixed':False,'min':0.5,'max':1.5}

#--lepton-hadron reactions

Q2cut=1.3**2
W2cut=4.0
pt_cut = 4.0

##--IDIS
conf['datasets']['idis']={}
conf['datasets']['idis']['filters']=[]
conf['datasets']['idis']['filters'].append("Q2>%f"%Q2cut)
conf['datasets']['idis']['filters'].append("W2>%f"%W2cut)
conf['datasets']['idis']['xlsx']={}
conf['datasets']['idis']['xlsx'][10010]='idis/expdata/10010.xlsx' # proton   | F2            | SLAC
conf['datasets']['idis']['xlsx'][10011]='idis/expdata/10011.xlsx' # deuteron | F2            | SLAC
conf['datasets']['idis']['xlsx'][10016]='idis/expdata/10016.xlsx' # proton   | F2            | BCDMS
conf['datasets']['idis']['xlsx'][10017]='idis/expdata/10017.xlsx' # deuteron | F2            | BCDMS
conf['datasets']['idis']['xlsx'][10020]='idis/expdata/10020.xlsx' # proton   | F2            | NMC
conf['datasets']['idis']['xlsx'][10021]='idis/expdata/10021.xlsx' # d/p      | F2d/F2p       | NMC
conf['datasets']['idis']['xlsx'][10026]='idis/expdata/10026.xlsx' # proton   | sigma red     | HERA II NC e+ (1)
conf['datasets']['idis']['xlsx'][10027]='idis/expdata/10027.xlsx' # proton   | sigma red     | HERA II NC e+ (2)
conf['datasets']['idis']['xlsx'][10028]='idis/expdata/10028.xlsx' # proton   | sigma red     | HERA II NC e+ (3)
conf['datasets']['idis']['xlsx'][10029]='idis/expdata/10029.xlsx' # proton   | sigma red     | HERA II NC e+ (4)
conf['datasets']['idis']['xlsx'][10030]='idis/expdata/10030.xlsx' # proton   | sigma red     | HERA II NC e-
conf['datasets']['idis']['xlsx'][10031]='idis/expdata/10031.xlsx' # proton   | sigma red     | HERA II CC e+
conf['datasets']['idis']['xlsx'][10032]='idis/expdata/10032.xlsx' # proton   | sigma red     | HERA II NC e-
conf['datasets']['idis']['norm']={}
conf['datasets']['idis']['norm'][10010]={'value':    1, 'min': 8.00000e-01, 'max': 1.20000e+00, 'fixed': False}
conf['datasets']['idis']['norm'][10011]={'value':    1, 'min': 8.00000e-01, 'max': 1.20000e+00, 'fixed': False}
conf['datasets']['idis']['norm'][10016]={'value':    1, 'min': 8.00000e-01, 'max': 1.20000e+00, 'fixed': False}
conf['datasets']['idis']['norm'][10017]={'value':    1, 'min': 8.00000e-01, 'max': 1.20000e+00, 'fixed': False}
conf['datasets']['idis']['norm'][10020]={'value':    1, 'min': 8.00000e-01, 'max': 1.20000e+00, 'fixed': False}

##--SIDIS
conf['datasets']['sidis']={}
conf['datasets']['sidis']['filters']=[]
conf['datasets']['sidis']['filters'].append("Q2>%f"%Q2cut)
conf['datasets']['sidis']['filters'].append("W2>%f"%W2cut)
conf['datasets']['sidis']['filters'].append('Z>0.2 and Z<0.9')
conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['xlsx'][1005]='sidis/expdata/1005.xlsx' # deuteron , mult , pi+ , COMPASS
conf['datasets']['sidis']['xlsx'][1006]='sidis/expdata/1006.xlsx' # deuteron , mult , pi- , COMPASS
conf['datasets']['sidis']['xlsx'][2005]='sidis/expdata/2005.xlsx' # deuteron , mult , K+  , COMPASS
conf['datasets']['sidis']['xlsx'][2006]='sidis/expdata/2006.xlsx' # deuteron , mult , K-  , COMPASS
conf['datasets']['sidis']['xlsx'][1007]='sidis/expdata/1007.xlsx' # proton   , mult , pi+ , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][1008]='sidis/expdata/1008.xlsx' # proton   , mult , pi- , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][1009]='sidis/expdata/1009.xlsx' # deuteron , mult , pi+ , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][1010]='sidis/expdata/1010.xlsx' # deuteron , mult , pi- , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][2007]='sidis/expdata/2007.xlsx' # proton   , mult , K+  , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][2008]='sidis/expdata/2008.xlsx' # proton   , mult , K-  , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][2009]='sidis/expdata/2009.xlsx' # deuteron , mult , K+  , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][2010]='sidis/expdata/2010.xlsx' # deuteron , mult , K-  , HERMES, Q2-z
conf['datasets']['sidis']['xlsx'][3000]='sidis/expdata/3000.xlsx' # deuteron , mult , h+  , COMPASS
conf['datasets']['sidis']['xlsx'][3001]='sidis/expdata/3001.xlsx' # deuteron , mult , h-  , COMPASS
conf['datasets']['sidis']['norm']={}
conf['datasets']['sidis']['norm'][1005]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][1006]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][1007]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][1008]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][1009]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][1010]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][2005]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][2006]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][2007]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][2008]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][2009]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}
conf['datasets']['sidis']['norm'][2010]={'value':    1.0000000,'fixed':False,'min':0.5,'max':1.5}

#--parameters
conf['params'] = {}

#--ff parameters

conf['ffpion parametrization']=0
conf['params']['ffpion']={}

conf['params']['ffpion']['g1 N']  ={'value':    1.33163e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['g1 a']  ={'value':    1.44992e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['g1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffpion']['g1 c']  ={'value':    6.90243e+00, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffpion']['g1 d']  ={'value':    1.82967e-01, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['u1 N']  ={'value':    7.08278e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['u1 a']  ={'value':   -1.51136e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['u1 b']  ={'value':    9.20008e-01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffpion']['u1 c']  ={'value':    3.22333e-27, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffpion']['u1 d']  ={'value':    1.18136e-33, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['d1 N']  ={'value':    1.27840e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['d1 a']  ={'value':    2.50613e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['d1 b']  ={'value':    7.20807e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffpion']['d1 c']  ={'value':    1.33273e-02, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffpion']['d1 d']  ={'value':    3.31850e+00, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['s1 N']  ={'value':    1.27840e-01, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffpion']['s1 a']  ={'value':    2.50613e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffpion']['s1 b']  ={'value':    7.20807e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffpion']['s1 c']  ={'value':    1.33273e-02, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffpion']['s1 d']  ={'value':    3.31850e+00, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffpion']['c1 N']  ={'value':    3.58168e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['c1 a']  ={'value':   -1.37435e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['c1 b']  ={'value':    3.26229e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffpion']['c1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffpion']['c1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['b1 N']  ={'value':    5.15544e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffpion']['b1 a']  ={'value':   -1.73110e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffpion']['b1 b']  ={'value':    3.63282e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffpion']['b1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffpion']['b1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffpion']['ub1 N'] ={'value':    1.27840e-01, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffpion']['ub1 a'] ={'value':    2.50613e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffpion']['ub1 b'] ={'value':    7.20807e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffpion']['ub1 c']  ={'value':    1.33273e-02, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffpion']['ub1 d']  ={'value':    3.31850e+00, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffpion']['db1 N'] ={'value':    7.08278e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffpion']['db1 a'] ={'value':   -1.51136e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffpion']['db1 b'] ={'value':    9.20008e-01, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffpion']['db1 c']  ={'value':    3.22333e-27, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffpion']['db1 d']  ={'value':    1.18136e-33, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffpion']['sb1 N'] ={'value':    1.27840e-01, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffpion']['sb1 a'] ={'value':    2.50613e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffpion']['sb1 b'] ={'value':    7.20807e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffpion']['sb1 c']  ={'value':    1.33273e-02, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffpion']['sb1 d']  ={'value':    3.31850e+00, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffpion']['cb1 N'] ={'value':    3.58168e-01, 'min':  0.0 , 'max':     1,'fixed':'c1 N'}
conf['params']['ffpion']['cb1 a'] ={'value':   -1.37435e+00, 'min': -1.8 , 'max':     2,'fixed':'c1 a'}
conf['params']['ffpion']['cb1 b'] ={'value':    3.26229e+00, 'min':  0   , 'max':    10,'fixed':'c1 b'}
#conf['params']['ffpion']['cb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 c'}
#conf['params']['ffpion']['cb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 d'}

conf['params']['ffpion']['bb1 N'] ={'value':    5.15544e-01, 'min':  0.0 , 'max':     1,'fixed':'b1 N'}
conf['params']['ffpion']['bb1 a'] ={'value':   -1.73110e+00, 'min': -1.8 , 'max':     2,'fixed':'b1 a'}
conf['params']['ffpion']['bb1 b'] ={'value':    3.63282e+00, 'min':  0   , 'max':    10,'fixed':'b1 b'}
#conf['params']['ffpion']['bb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 c'}
#conf['params']['ffpion']['bb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 d'}

conf['params']['ffkaon']={}
conf['ffkaon parametrization']=0

conf['params']['ffkaon']['g1 N']  ={'value':    5.79695e-02, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['g1 a']  ={'value':   -9.89326e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['g1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['g1 c']  ={'value':    6.11846e-35, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['g1 d']  ={'value':    3.17720e-27, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['u1 N']  ={'value':    1.02099e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['u1 a']  ={'value':   -4.35552e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['u1 b']  ={'value':    3.76130e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['u1 c']  ={'value':    5.44321e-20, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['u1 d']  ={'value':    1.12591e-28, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['d1 N']  ={'value':    9.60528e-02, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['d1 a']  ={'value':   -6.32787e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['d1 b']  ={'value':    1.09560e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['d1 c']  ={'value':    8.43911e-30, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['d1 d']  ={'value':    4.02954e-35, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['s1 N']  ={'value':    9.60528e-02, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffkaon']['s1 a']  ={'value':   -6.32787e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffkaon']['s1 b']  ={'value':    1.09560e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffkaon']['s1 c']  ={'value':    8.43911e-30, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffkaon']['s1 d']  ={'value':    4.02954e-35, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffkaon']['c1 N']  ={'value':    9.77856e-02, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['c1 a']  ={'value':   -3.73448e-01, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['c1 b']  ={'value':    3.46921e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffkaon']['c1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffkaon']['c1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['b1 N']  ={'value':    3.99833e-01, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['b1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['b1 b']  ={'value':    3.87332e+00, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffkaon']['b1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}
#conf['params']['ffkaon']['b1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['ub1 N'] ={'value':    9.60528e-02, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffkaon']['ub1 a'] ={'value':   -6.32787e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffkaon']['ub1 b'] ={'value':    1.09560e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffkaon']['ub1 c']  ={'value':    8.43911e-30, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffkaon']['ub1 d']  ={'value':    4.02954e-35, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffkaon']['db1 N'] ={'value':    9.60528e-02, 'min':  0.0 , 'max':     1,'fixed':'d1 N'}
conf['params']['ffkaon']['db1 a'] ={'value':   -6.32787e-01, 'min': -1.8 , 'max':     2,'fixed':'d1 a'}
conf['params']['ffkaon']['db1 b'] ={'value':    1.09560e+00, 'min':  0   , 'max':    10,'fixed':'d1 b'}
conf['params']['ffkaon']['db1 c']  ={'value':    8.43911e-30, 'min':  0   , 'max':    20,'fixed':'d1 c'}
conf['params']['ffkaon']['db1 d']  ={'value':    4.02954e-35, 'min':  0   , 'max':    20,'fixed':'d1 d'}

conf['params']['ffkaon']['sb1 N'] ={'value':    7.33164e-02, 'min':  0.0 , 'max':     1,'fixed':False}
conf['params']['ffkaon']['sb1 a'] ={'value':    1.79460e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffkaon']['sb1 b'] ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffkaon']['sb1 c']  ={'value':    1.03982e+01, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffkaon']['sb1 d']  ={'value':    1.55829e-03, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffkaon']['cb1 N'] ={'value':    9.77856e-02, 'min':  0.0 , 'max':     1,'fixed':'c1 N'}
conf['params']['ffkaon']['cb1 a'] ={'value':   -3.73448e-01, 'min': -1.8 , 'max':     2,'fixed':'c1 a'}
conf['params']['ffkaon']['cb1 b'] ={'value':    3.46921e+00, 'min':  0   , 'max':    10,'fixed':'c1 b'}
#conf['params']['ffkaon']['cb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 c'}
#conf['params']['ffkaon']['cb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'c1 d'}

conf['params']['ffkaon']['bb1 N'] ={'value':    3.99833e-01, 'min':  0.0 , 'max':     1,'fixed':'b1 N'}
conf['params']['ffkaon']['bb1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'b1 a'}
conf['params']['ffkaon']['bb1 b'] ={'value':    3.87332e+00, 'min':  0   , 'max':    10,'fixed':'b1 b'}
#conf['params']['ffkaon']['bb1 c']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 c'}
#conf['params']['ffkaon']['bb1 d']  ={'value':    0.0, 'min':  0   , 'max':    20,'fixed':'b1 d'}

conf['params']['ffhadron']={}
conf['ffhadron parametrization']='sum2'

conf['params']['ffhadron']['g1 N']  ={'value':    8.08867e-01, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['g1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['g1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffhadron']['g1 c']  ={'value':    7.91106e-15, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffhadron']['g1 d']  ={'value':    3.75367e-25, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffhadron']['u1 N']  ={'value':    1.89623e-01, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['u1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['u1 b']  ={'value':    2.25372e+00, 'min':  0   , 'max':    10,'fixed':False}
conf['params']['ffhadron']['u1 c']  ={'value':    2.56596e-23, 'min':  0   , 'max':    20,'fixed':False}
conf['params']['ffhadron']['u1 d']  ={'value':    1.58540e-22, 'min':  0   , 'max':    20,'fixed':False}

conf['params']['ffhadron']['d1 N']  ={'value':    1.89623e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['d1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['d1 b']  ={'value':    2.25372e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['d1 c']  ={'value':    2.56596e-23, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['d1 d']  ={'value':    1.58540e-22, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['s1 N']  ={'value':    7.76108e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['s1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['s1 b']  ={'value':    2.25372e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['s1 c']  ={'value':    2.56596e-23, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['s1 d']  ={'value':    1.58540e-22, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['c1 N']  ={'value':    5.44046e-01, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['c1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['c1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['c1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['c1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}

conf['params']['ffhadron']['b1 N']  ={'value':    8.46229e-02, 'min':  0.0 , 'max':     1,'fixed':True}
conf['params']['ffhadron']['b1 a']  ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':False}
conf['params']['ffhadron']['b1 b']  ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['b1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}
#conf['params']['ffhadron']['b1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':False}

conf['params']['ffhadron']['ub1 N'] ={'value':    7.76108e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['ub1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['ub1 b'] ={'value':    2.25372e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['ub1 c']  ={'value':    2.56596e-23, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['ub1 d']  ={'value':    1.58540e-22, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['db1 N'] ={'value':    1.95669e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['db1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['db1 b'] ={'value':    2.25372e+00, 'min':  0   , 'max':    20,'fixed':'u1 b'}
conf['params']['ffhadron']['db1 c']  ={'value':    2.56596e-23, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['db1 d']  ={'value':    1.58540e-22, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['sb1 N'] ={'value':    1.89623e-01, 'min':  0.0 , 'max':     1,'fixed':'u1 N'}
conf['params']['ffhadron']['sb1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'u1 a'}
conf['params']['ffhadron']['sb1 b'] ={'value':    2.25372e+00, 'min':  0   , 'max':    10,'fixed':'u1 b'}
conf['params']['ffhadron']['sb1 c']  ={'value':    2.56596e-23, 'min':  0   , 'max':    20,'fixed':'u1 c'}
conf['params']['ffhadron']['sb1 d']  ={'value':    1.58540e-22, 'min':  0   , 'max':    20,'fixed':'u1 d'}

conf['params']['ffhadron']['cb1 N'] ={'value':    5.44046e-01, 'min':  0.0 , 'max':     1,'fixed':'c1 N'}
conf['params']['ffhadron']['cb1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'c1 a'}
conf['params']['ffhadron']['cb1 b'] ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':'c1 b'}
#conf['params']['ffhadron']['cb1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'c1 c'}
#conf['params']['ffhadron']['cb1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'c1 d'}

conf['params']['ffhadron']['bb1 N'] ={'value':    8.46229e-02, 'min':  0.0 , 'max':     1,'fixed':'b1 N'}
conf['params']['ffhadron']['bb1 a'] ={'value':   -1.80000e+00, 'min': -1.8 , 'max':     2,'fixed':'b1 a'}
conf['params']['ffhadron']['bb1 b'] ={'value':    1.00000e+01, 'min':  0   , 'max':    10,'fixed':'b1 b'}
#conf['params']['ffhadron']['bb1 c']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'b1 c'}
#conf['params']['ffhadron']['bb1 d']  ={'value':    0.0, 'min':  0   , 'max':    10,'fixed':'b1 d'}

conf['pdf parametrization'] = 2
conf['params']['pdf'] = {}

conf['params']['pdf']['g1 N']    ={'value':    3.87592e-01, 'min':  None, 'max':  None, 'fixed': True }
conf['params']['pdf']['g1 a']    ={'value':   -6.60217e-01, 'min':  -1.9, 'max':     1, 'fixed': False}
conf['params']['pdf']['g1 b']    ={'value':    8.12091e+00, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['uv1 N']   ={'value':    3.47549e-01, 'min':  None, 'max':  None, 'fixed': True }
conf['params']['pdf']['uv1 a']   ={'value':   -1.14055e-01, 'min':  -0.5, 'max':     1, 'fixed': False}
conf['params']['pdf']['uv1 b']   ={'value':    3.21230e+00, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['dv1 N']   ={'value':    1.52089e-01, 'min':  None, 'max':  None, 'fixed': True }
conf['params']['pdf']['dv1 a']   ={'value':   -3.80099e-02, 'min':  -0.5, 'max':     1, 'fixed': False}
conf['params']['pdf']['dv1 b']   ={'value':    4.36319e+00, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['db1 N']   ={'value':    2.08640e-02, 'min':     0, 'max':     1, 'fixed': False}
conf['params']['pdf']['db1 a']   ={'value':   -4.05372e-01, 'min':    -1, 'max':     1, 'fixed': False}
conf['params']['pdf']['db1 b']   ={'value':    1.00000e+01, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['ub1 N']   ={'value':    1.64626e-02, 'min':     0, 'max':     1, 'fixed': False}
conf['params']['pdf']['ub1 a']   ={'value':    0.000000000, 'min':    -1, 'max':     1, 'fixed': False}
conf['params']['pdf']['ub1 b']   ={'value':    1.00000e+01, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['s1 N']    ={'value':    0.00000e+00, 'min':     0, 'max':     1, 'fixed': True }
conf['params']['pdf']['s1 a']    ={'value':   -0.19319e+00, 'min':  -0.5, 'max':     1, 'fixed': False}
conf['params']['pdf']['s1 b']    ={'value':    4.99999e+00, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['sb1 N']   ={'value':    0.00000e+00, 'min':     0, 'max':     1, 'fixed': False}
conf['params']['pdf']['sb1 a']   ={'value':   -0.19317e+00, 'min':  -0.5, 'max':     1, 'fixed': False}
conf['params']['pdf']['sb1 b']   ={'value':    4.99988e+00, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['sea1 N']  ={'value':    2.08640e-02, 'min':     0, 'max':     1, 'fixed': False}
conf['params']['pdf']['sea1 a']  ={'value':   -1.500000000, 'min':  -1.9, 'max':    -1, 'fixed': False}
conf['params']['pdf']['sea1 b']  ={'value':    1.00000e+01, 'min':     0, 'max':    10, 'fixed': False}

conf['params']['pdf']['sea2 N']  ={'value':    2.08640e-02, 'min':     0, 'max':     1, 'fixed': 'sea1 N'}
conf['params']['pdf']['sea2 a']  ={'value':   -1.500000000, 'min':  -1.9, 'max':    -1, 'fixed': 'sea1 a'}
conf['params']['pdf']['sea2 b']  ={'value':    1.00000e+01, 'min':     0, 'max':    10, 'fixed': 'sea1 b'}

#--steps
conf['steps']={}

#--ffpion sia
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

#--ffkaon sia
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

#--ffhadron sia
conf['steps'][3]={}
conf['steps'][3]['dep']=[1,2]
conf['steps'][3]['active distributions']=['ffhadron','ffpion','ffkaon']
conf['steps'][3]['passive distributions']=['ffpion','ffkaon']
conf['steps'][3]['datasets']={}
conf['steps'][3]['datasets']['sia']=[]
conf['steps'][3]['datasets']['sia'].append(4000)
conf['steps'][3]['datasets']['sia'].append(4001)
conf['steps'][3]['datasets']['sia'].append(4002)
conf['steps'][3]['datasets']['sia'].append(4004)
conf['steps'][3]['datasets']['sia'].append(4005)
conf['steps'][3]['datasets']['sia'].append(4006)
conf['steps'][3]['datasets']['sia'].append(4007)
conf['steps'][3]['datasets']['sia'].append(4009)
conf['steps'][3]['datasets']['sia'].append(4010)
conf['steps'][3]['datasets']['sia'].append(4012)

#--all ffs sia
#conf['steps'][4]={}
#conf['steps'][4]['dep']=[1,2,3]
#conf['steps'][4]['active distributions']=['ffhadron','ffpion','ffkaon']
#conf['steps'][4]['datasets']={}
#conf['steps'][4]['datasets']['sia']=[]
#conf['steps'][4]['datasets']['sia'].append(1001)
#conf['steps'][4]['datasets']['sia'].append(1002)
#conf['steps'][4]['datasets']['sia'].append(1003)
#conf['steps'][4]['datasets']['sia'].append(1004)
#conf['steps'][4]['datasets']['sia'].append(1005)
#conf['steps'][4]['datasets']['sia'].append(1006)
#conf['steps'][4]['datasets']['sia'].append(1007)
#conf['steps'][4]['datasets']['sia'].append(1008)
#conf['steps'][4]['datasets']['sia'].append(1010)
#conf['steps'][4]['datasets']['sia'].append(1011)
#conf['steps'][4]['datasets']['sia'].append(1012)
#conf['steps'][4]['datasets']['sia'].append(1013)
#conf['steps'][4]['datasets']['sia'].append(1014)
#conf['steps'][4]['datasets']['sia'].append(1016)
#conf['steps'][4]['datasets']['sia'].append(1017)
#conf['steps'][4]['datasets']['sia'].append(1018)
#conf['steps'][4]['datasets']['sia'].append(1019)
#conf['steps'][4]['datasets']['sia'].append(1023)
#conf['steps'][4]['datasets']['sia'].append(1024)
#conf['steps'][4]['datasets']['sia'].append(1025)
#conf['steps'][4]['datasets']['sia'].append(1027)
#conf['steps'][4]['datasets']['sia'].append(1028)
#conf['steps'][4]['datasets']['sia'].append(1029)
#conf['steps'][4]['datasets']['sia'].append(1030)
#conf['steps'][4]['datasets']['sia'].append(2030)
#conf['steps'][4]['datasets']['sia'].append(2028)
#conf['steps'][4]['datasets']['sia'].append(2029)
#conf['steps'][4]['datasets']['sia'].append(2001)
#conf['steps'][4]['datasets']['sia'].append(2002)
#conf['steps'][4]['datasets']['sia'].append(2003)
#conf['steps'][4]['datasets']['sia'].append(2004)
#conf['steps'][4]['datasets']['sia'].append(2005)
#conf['steps'][4]['datasets']['sia'].append(2006)
#conf['steps'][4]['datasets']['sia'].append(2007)
#conf['steps'][4]['datasets']['sia'].append(2008)
#conf['steps'][4]['datasets']['sia'].append(2012)
#conf['steps'][4]['datasets']['sia'].append(2013)
#conf['steps'][4]['datasets']['sia'].append(2014)
#conf['steps'][4]['datasets']['sia'].append(2018)
#conf['steps'][4]['datasets']['sia'].append(2019)
#conf['steps'][4]['datasets']['sia'].append(2025)
#conf['steps'][4]['datasets']['sia'].append(2031)
#conf['steps'][4]['datasets']['sia'].append(2016)
#conf['steps'][4]['datasets']['sia'].append(2017)
#conf['steps'][4]['datasets']['sia'].append(2023)
#conf['steps'][4]['datasets']['sia'].append(2024)
#conf['steps'][4]['datasets']['sia'].append(2027)
#conf['steps'][4]['datasets']['sia'].append(4000)
#conf['steps'][4]['datasets']['sia'].append(4001)
#conf['steps'][4]['datasets']['sia'].append(4002)
#conf['steps'][4]['datasets']['sia'].append(4004)
#conf['steps'][4]['datasets']['sia'].append(4005)
#conf['steps'][4]['datasets']['sia'].append(4006)
#conf['steps'][4]['datasets']['sia'].append(4007)
#conf['steps'][4]['datasets']['sia'].append(4009)
#conf['steps'][4]['datasets']['sia'].append(4010)
#conf['steps'][4]['datasets']['sia'].append(4012)

#--pdf idis and no hera
#conf['steps'][5]={}
#conf['steps'][5]['dep']=[1,2,3,4]
#conf['steps'][5]['active distributions']=['pdf','ffpion','ffkaon','ffhadron']
#conf['steps'][5]['passive distributions']=['ffpion','ffkaon','ffhadron']
#conf['steps'][5]['datasets']={}
#conf['steps'][5]['datasets']['idis']=[]
#conf['steps'][5]['datasets']['idis'].append(10010) # proton   | F2            | SLAC
#conf['steps'][5]['datasets']['idis'].append(10011) # deuteron | F2            | SLAC
#conf['steps'][5]['datasets']['idis'].append(10016) # proton   | F2            | BCDMS
#conf['steps'][5]['datasets']['idis'].append(10017) # deuteron | F2            | BCDMS
#conf['steps'][5]['datasets']['idis'].append(10020) # proton   | F2            | NMC
#conf['steps'][5]['datasets']['idis'].append(10021) # d/p      | F2d/F2p       | NMC

#--all ffs sidis
#conf['steps'][6]={}
#conf['steps'][6]['dep']=[4,5]
#conf['steps'][6]['active distributions']=['pdf','ffpion','ffkaon','ffhadron']
#conf['steps'][6]['passive distributions']=['pdf','ffkaon','ffhadron']
#conf['steps'][6]['datasets']={}
#conf['steps'][6]['datasets']['sidis']=[]
#conf['steps'][6]['datasets']['sidis'].append(1005) # deuteron , mult , pi+ , COMPASS
#conf['steps'][6]['datasets']['sidis'].append(1006) # deuteron , mult , pi- , COMPASS
#conf['steps'][6]['datasets']['sidis'].append(2005) # deuteron , mult , K+  , COMPASS
#conf['steps'][6]['datasets']['sidis'].append(2006) # deuteron , mult , K-  , COMPASS
#conf['steps'][6]['datasets']['sidis'].append(1007) # proton   , mult , pi+ , HERMES, Q2-z
#conf['steps'][6]['datasets']['sidis'].append(1008) # proton   , mult , pi- , HERMES, Q2-z
#conf['steps'][6]['datasets']['sidis'].append(1009) # deuteron , mult , pi+ , HERMES, Q2-z 
#conf['steps'][6]['datasets']['sidis'].append(1010) # deuteron , mult , pi- , HERMES, Q2-z
#conf['steps'][6]['datasets']['sidis'].append(2007) # proton   , mult , K+  , HERMES, Q2-z
#conf['steps'][6]['datasets']['sidis'].append(2008) # proton   , mult , K-  , HERMES, Q2-z
#conf['steps'][6]['datasets']['sidis'].append(2009) # deuteron , mult , K+  , HERMES, Q2-z
#conf['steps'][6]['datasets']['sidis'].append(2010) # deuteron , mult , K-  , HERMES, Q2-z
#conf['steps'][6]['datasets']['sidis'].append(3000) # deuteron , mult , h+  , COMPASS
#conf['steps'][6]['datasets']['sidis'].append(3001) # deuteron , mult , h-  , COMPASS

