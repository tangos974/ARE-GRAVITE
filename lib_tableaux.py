import numpy as np

def inversion_vecteur(tableau):
"""Prend en entrée un vecteur (tableau de dimension 1) et renvoie le même inversé"""
  for k in range(len(tableau)//2):
    temp = tableau[k]
    tableau[k] = tableau[-k-1]
    tableau[-k-1] = temp
  return tableau
