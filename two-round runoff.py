import csv
import json
import os
from time import sleep as wait


questions=json.load(open("questions.json"))
voters=json.load(open("voters.json"))

#this code finds the winner of each catagory
finalR={}
for q, options in questions.items():
    print(q,options)