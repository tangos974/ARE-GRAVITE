import numpy as np

def inversion_tab_dim1(tableau):
"""Prend en entrée un tableau de dimension 1, renvoie le même inversé"""
  for k in range(len(tableau)//2):
    temp = tableau[k]
    tableau[k] = tableau[-k-1]
    tableau[-k-1] = temp
  return tableau
