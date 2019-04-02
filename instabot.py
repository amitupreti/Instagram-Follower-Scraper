import instaloader
import re
import csv
from time import sleep
import os
import sys
# Get instance
L = instaloader.Instaloader()

# Login or load session

# L.login('dslr.lover.nepal', 'kubhwifi')        # (login)
#L.interactive_login(USER)      # (ask password on terminal)
L.load_session_from_file('dslr.lover.nepal') # (load session created w/

import urllib3

http = urllib3.PoolManager()



def wait_for_internet_connection():
    while True:
        try:
        
            response = http.request('GET', 'http://ku.edu.np')
            return
        except:
            print('No internet connection.\nTrying after 5 seconds.\n')
            sleep(5)

p = sys.argv[1]
p=p.split(',')
print(p)
# input()

PROFILE = p

for pro in PROFILE:
    try:
        wait_for_internet_connection()
        print('\n\nGetting followers from',pro)
        filename = pro+'.csv'
        with open(filename,'a',newline='') as csvf:

            csv_writer = csv.writer(csvf)
            csv_writer.writerow(['user_id','username','fullname','is_verified','is_private','media_count','follower_count','following_count','bio','website','emails'])
            

    
        profile = instaloader.Profile.from_username(L.context, pro)
        count = 0
        total=0
        # Print list of followees
        for person in profile.get_followers():
            try:
                wait_for_internet_connection()
                total+=1
                user_id = person.userid
                username = person.username
                fullname  = person.full_name
                is_verified = person.is_verified
                is_private = person.is_private
                media_count  = person.mediacount
                follower_count = person.followers
                following_count = person.followees
                bio = person.biography
                emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", bio)
                website = person.external_url
                #last activity
                try:
                    follower_profile = instaloader.Profile.from_username(L.context, username)
                    for post in profile.get_posts():
                        last_activity = post.date_local
                        break
                except Exception as e:
                    print(e)
                    last_activity=''


                
                
                with open(filename,'a',newline='') as csvf:

                    csv_writer = csv.writer(csvf)
                    csv_writer.writerow([user_id,username,fullname,is_verified,is_private,media_count,follower_count,following_count,bio,website,emails])
                # os.system('clear')
                print('\nTotal:',total)
                print('Username:',username)
                print('Last Activity',last_activity)
            
            except Exception as e:
                print(e)
            


        # (likewise with profile.get_followers())
    except:
        print('Skipping',pro)
