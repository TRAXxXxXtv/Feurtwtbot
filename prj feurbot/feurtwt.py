import re
import tweepy
import time
import json
import colorama
from colorama import Fore,Style
mot_de_passe ="tristan"

        

        


print(Fore.YELLOW+"lancement en cours")
time.sleep(5)
print(Style.RESET_ALL)
api_key = "Mz3f4aueWBVT5tblykvWUvlFo"
api_secrets = "KH2pmemtqbMVQWGnSJlHmBiYSXTO24hBV8Use4fL7taw9wyXAQ"
access_token = "1453336196042706948-GM16a7i91LpOVQ66sGaf1zevCS0GhM"
access_secret = "ZoOWV6yOy1NSpuBSbxppL0cjhbd2lGjAz2m6fr90Hp1El"
    
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)
    

#list of specific strings we want to check for in Tweets

rpd=0
djrpd=0
non=0
message = "quoi"
e=0
n=0
num_of_secs=120
search_results = api.search_tweets(q="quoi") 
while True:
    if n<500:
        if e <15:
        
   

            for i in search_results:
                nom=(f"{i.author.screen_name}")
                text=(f"{i.text}")
                
                    
                if(text.endswith("quoi") or text.endswith("quoi ?") or text.endswith("quoi !") or text.endswith("quoi?") or text.endswith("quoi!") ):
                    try:
                        
                        
                        api.update_status(status = "⚠️feur⚠️", in_reply_to_status_id=i.id , auto_populate_reply_metadata=True)
                        donne={
                            "nom":nom,
                            "contenu":text,
                            
                        }
                        time.sleep(3)
                        e=e+1
                        print(e)
                        api.like(tweet_id=i.id, user_auth=True)
                        

                        with open('data.json', 'w') as mon_fichier:
                            json.dump(donne, mon_fichier)
                    except:
                        n=n+1
                        continue
            else:
                print("attente antit ban")

                time.sleep(num_of_secs)                
    else:
        print("recherche")
        search_results = api.search_tweets(q="quoi", count=100)
        n=0
    
        
        


                            


    

        
            
                

        



