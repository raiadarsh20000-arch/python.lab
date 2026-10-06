import json

with open('election_result.json','r',encoding='utf-8') as file_obj:
    elction_data=json.load(file_obj)

wining_vote=[0]
winner_info=None
for candiated_data in elction_data:
   if candiated_data["TotalVoteReceived"]>wining_vote:
       winning_vote=candiated_data["TotalVoteReceived"]
       winner_info=candiated_data
    
    
print(winner_info.get('candidateName'))