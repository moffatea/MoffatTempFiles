#!/usr/bin/env python
import sys,os
import numpy as np
import dssfpi1,dssfpi2,dssfk1,dssfk2,dssfh

class DSS:
  
  def __init__(self,conf):

    root=conf['path2DSS']
    if root.endswith('/')==False: root+='/'

    dssfpi1.root.root=root.ljust(255)
    dssfpi2.root.root=root.ljust(255)
    dssfk1.root.root=root.ljust(255)
    dssfk2.root.root=root.ljust(255)
    dssfh.root.root=root.ljust(255)
    
    self.pi={0:{},1:{},-1:{}}
    self.k={0:{},1:{},-1:{}}
    self.h={0:{},1:{},-1:{}}

  def _get_f(self,z,Q2,storage,func,s,ih,ic,io):
    if (z,Q2) not in storage[ic]:
      storage[ic][(z,Q2)]=np.array(func(s,ih,ic,io,z,Q2))/z
    return storage[ic][(z,Q2)]

  def get_f(self,z,Q2,hadron,setversion,order):
    """
    out: g,u,ub,d,db,s,sb,c,cb,b,bb
    """
    if   setversion=='DSS14' or setversion=='DSS17':
      if   hadron=='pi+':return self._get_f(z,Q2,self.pi,dssfpi2.fdss,2,1,1,1)
      elif hadron=='pi-':return self._get_f(z,Q2,self.pi,dssfpi2.fdss,2,1,-1,1)
      elif hadron=='pi0':return self._get_f(z,Q2,self.pi,dssfpi2.fdss,2,1,0,1)
      elif hadron=='k+':return self._get_f(z,Q2,self.k,dssfk2.fdss,2,2,1,1)
      elif hadron=='k-':return self._get_f(z,Q2,self.k,dssfk2.fdss,2,2,-1,1)
      elif hadron=='k0':return self._get_f(z,Q2,self.k,dssfk2.fdss,2,2,0,1)
    elif setversion=='DSS07' and order=='LO':
      if   hadron=='pi+':return self._get_f(z,Q2,self.pi,dssfpi1.fdss,1,1,1,0)
      elif hadron=='pi-':return self._get_f(z,Q2,self.pi,dssfpi1.fdss,1,1,-1,0)
      elif hadron=='pi0':return self._get_f(z,Q2,self.pi,dssfpi1.fdss,1,1,0,0)
      elif hadron=='k+':return self._get_f(z,Q2,self.k,dssfk1.fdss,1,2,1,0)
      elif hadron=='k-':return self._get_f(z,Q2,self.k,dssfk1.fdss,1,2,-1,0)
      elif hadron=='k0':return self._get_f(z,Q2,self.k,dssfk1.fdss,1,2,0,0)
      elif hadron=='h+':return self._get_f(z,Q2,self.h,dssfh.fdss,1,4,1,0)
      elif hadron=='h-':return self._get_f(z,Q2,self.h,dssfh.fdss,1,4,-1,0)
      elif hadron=='h0':return self._get_f(z,Q2,self.h,dssfh.fdss,1,4,0,0)
    else:
      if   hadron=='pi+':return self._get_f(z,Q2,self.pi,dssfpi1.fdss,1,1,1,1)
      elif hadron=='pi-':return self._get_f(z,Q2,self.pi,dssfpi1.fdss,1,1,-1,1)
      elif hadron=='pi0':return self._get_f(z,Q2,self.pi,dssfpi1.fdss,1,1,0,1)
      elif hadron=='k+':return self._get_f(z,Q2,self.k,dssfk1.fdss,1,2,1,1)
      elif hadron=='k-':return self._get_f(z,Q2,self.k,dssfk1.fdss,1,2,-1,1)
      elif hadron=='k0':return self._get_f(z,Q2,self.k,dssfk1.fdss,1,2,0,1)
      elif hadron=='h+':return self._get_f(z,Q2,self.h,dssfh.fdss,1,4,1,1)
      elif hadron=='h-':return self._get_f(z,Q2,self.h,dssfh.fdss,1,4,-1,1)
      elif hadron=='h0':return self._get_f(z,Q2,self.h,dssfh.fdss,1,4,0,1)

if __name__=='__main__':

  conf={}
  conf['path2DSS']='./'

  dss=DSS(conf)
  print dss.get_f(0.5,10,'pi+','DSS14','NLO')
  print dss.get_f(0.5,10,'pi+','DSS07','NLO')
  print dss.get_f(0.5,10,'pi+','DSS07','NLO')


