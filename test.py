from flask import Flask, render_template, request
from DB.base import *
import os
from Classe.Player import *
from Classe.Tournament import *
from Classe.Tour import *




rematch_list = []

for i in range (4):
    rematch_list.append("match"+str(i+1))

print(rematch_list)

