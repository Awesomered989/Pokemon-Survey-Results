import csv
import json
import os
from time import sleep as wait



questions=json.load(open("questions.json"))
voters=json.load(open("voters.json"))

comp1,comp2=input("Option1:\n>>> ").title(),input("Option2:\n>>> ").title()
cat=[question for question,ops in questions.items() if comp1 in list(ops.keys())][0]
compscore1,compscore2=0,0
for voter in voters:
    try:
        comprank1,comprank2=list(voter[cat].values()).index(comp1),list(voter[cat].values()).index(comp2)
        compscore1+=comprank1<comprank2
        compscore2+=comprank1>comprank2
    except:
        if comp1 in list(voter[cat].values()) and not(comp2 in list(voter[cat].values())):
            compscore1+=1
        elif comp2 in list(voter[cat].values()):
            compscore2+=1

total=compscore1+compscore2

print(f'''╔{"╦":═>11}{"╤":═>11}{"╗":═>11}
║{"Option":<10}║{"Score":^10}│{"Percentage":^10}║
╠{"╬":═>11}{"╪":═>11}{"╣":═>11}
║{comp1[:10]:<10}║{compscore1:^10}│{str(int((compscore1/total)*100))+"%":^10}║
╟{"╫":─>11}{"┼":─>11}{"╢":─>11}
║{comp2[:10]:<10}║{compscore2:^10}│{str(int((compscore2/total)*100))+"%":^10}║
╟{"╫":─>11}{"┼":─>11}{"╢":─>11}
║{"Difference":<10}║{abs(compscore1-compscore2):^10}│{str(abs(int((compscore1/total)*100)-int((compscore2/total)*100)))+"%":^10}║
╟{"╫":─>11}{"┼":─>11}{"╢":─>11}
║{"Total":<10}║{total:^10}│{"100%":^10}║
╚{"╩":═>11}{"╧":═>11}{"╝":═>11}

█ = {comp1}
▒ = {comp2}

Winner: {max({comp1:compscore1,comp2:compscore2}, key={comp1:compscore1,comp2:compscore2}.get)}
{"█"*int((compscore1/total)*34):▒<34}''')