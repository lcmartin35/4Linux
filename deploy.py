#!/usr/bin/python3

import os,sys

path = '/home/developer/520/'
dirs = os.listdir(path)
for indice, arq in enumerate (dirs):
    print(indice,arq)
    