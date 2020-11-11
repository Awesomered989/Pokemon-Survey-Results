import csv
import json
import os
from time import sleep as wait

def get_rank(r:int):
    print(r)
    if int(str(r)[-1])==1 and int(str(r)[-2:])!=11:
	    return f"{r}st"
    elif int(str(r)[-1])==2 and int(str(r)[-2:])!=12:
	    return f"{r}nd"
    elif int(str(r)[-1])==3 and int(str(r)[-2:])!=13:
	    return f"{r}rd"
    else:
	    return f"{r}th"

voters=[]
questions={}

#this code organizes each voters data into a json format
with open('Pokemon Survey.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    questions=set([n.split(" [")[0] for n in reader.fieldnames])
    questions.remove("Timestamp")
    questions={q:{n.split(" [")[1][:-1]:[] for n in reader.fieldnames if q in n} for q in questions}

    for row in reader:
        user_ranks={}
        for q, options in questions.items():
            user_ranks[q]={}
            ranks=[get_rank(x+1) for x in range(len(options))]
            for rank in ranks[:int(len(options)/2)]:
                for option in options:
                    if row[f"{q} [{option}]"]==rank:
                        user_ranks[q][rank]=option
                        questions[q][option].append(int(rank[:-2]))
        voters.append(user_ranks)

    json.dump(questions,open("questions.json","w"),indent=1)
    json.dump(voters,open("voters.json","w"),indent=3)
    csvfile.close()