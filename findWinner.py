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

ranks=["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
voters=[]
questions={}

with open('Pokemon Survey.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    questions=set([n.split(" [")[0] for n in reader.fieldnames])
    questions.remove("Timestamp")
    questions={q:{n.split(" [")[1][:-1]:[] for n in reader.fieldnames if q in n} for q in questions}

    for row in reader:
        user_ranks={}
        for q, options in questions.items():
            user_ranks[q]={}
            for rank in ranks[:int(len(options)/2)]:
                for option in options:
                    if row[f"{q} [{option}]"]==rank:
                        user_ranks[q][rank]=option
                        questions[q][option].append(int(rank[:-2]))
        voters.append(user_ranks)

    json.dump(questions,open("questions.json","w"),indent=1)
    json.dump(voters,open("voters.json","w"),indent=3)
    csvfile.close()


finalR={}
for q, options in questions.items():
    #q="Favourite Type"
    #options=questions[q]
    winners={}
    vote_options=options
    for asdf in range(len(options)):
        winner=""
        results={}

        while len(vote_options)>1 and sum(x>50 for x in results.values())==0:
            results={}
            os.system("clear")
            for option,li in vote_options.items():
                results[option]=(li.count(1)/len(voters))*100
                print(f"{option}: {results[option]}%")

            lowest_Score=min(results.values())
            highest_Score=max(results.values())
            losers=[op for op,val in results.items() if val==lowest_Score]
            winner=[op for op,val in results.items() if val==highest_Score][0]
            vote_options={option:[] for option,re in vote_options.items() if not(option in losers)}
            
            for voter in voters:
                voterank=1
                for rank,option in voter[q].items():
                    if option in vote_options.keys():
                        vote_options[option].append(voterank)
                        voterank+=1
            
            print(vote_options)
            print(winner)

        
        if winner=="":
            winners[get_rank(len(winners)+1)]=([l for l in losers if not(l in winners.values())][0])
        else:
            winners[get_rank(len(winners)+1)]=winner
        vote_options=options
        vote_options={option:re for option,re in options.items() if not(option in winners.values())}
    print(winners,len(winners))
    finalR[q]=winners

print(finalR)
#json.dump(finalR,open("pokemon survey results/final results.js","w"),indent=3)
js=open("pokemon survey results/final results.js","w")
js.write("var results = "+json.dumps(finalR,indent=3))
js.close()
json.dump(finalR,open("pokemon survey results/final results.json","w"),indent=3)

