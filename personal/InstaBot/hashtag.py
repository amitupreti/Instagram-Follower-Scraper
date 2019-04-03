"""
This template is written by Amit Upreti
This is avery good strategy to get followers from hash tags
"""



# !/usr/bin/python2.7
import random
from instapy import InstaPy
from instapy.util import smart_run
from time import sleep




#new changes has been made inside this box for proxy setup
#########################################################################################################################################

from proxy_extension import create_proxy_extension
#this in case your proxy has username and password
proxy = 'lum-customer-hl_e5a0e1f6-zone-usa_instagram-ip-38.131.151.4:7j6kam84o78a@zproxy.lum-superproxy.io:22225'
proxy_chrome_extension = create_proxy_extension(proxy)

# login credentials
insta_username = 'wcc_model_scout'
insta_password = 'tanvir2k14'

# get a session!
# set headless_browser=True to run InstaPy in the background. You can set Up proxy here.
session = InstaPy(username=insta_username, 
                  password=insta_password,
                  headless_browser = True,
                #   proxy_address='202.79.34.115', #uncomment there if your proxy has no username and password
                #   proxy_port=8080   #uncomment there if your proxy has no username and password

                 proxy_chrome_extension=proxy_chrome_extension #remove this line if your proxy has no username and password
                  )

# let's go! :>
##########################################################################################################################################







with smart_run(session):
    #this is where you will put hash tags. I recommend you use as much as hashtags as you can.
    #the bot will select randomly 10 hashtags in every session
    #session-> session is like 1 complete cycle for the bot. once you run the bot. it will go forever on its own untill it receives error

    hashtags = ['gymsharkwomen']



    random.shuffle(hashtags)
    '''if you have lesss number of has tags or want to use feew hash tags in each session edit the number below.
    For example
        my_hashtags = hashtags[:5] The bot will go after 5 hash tags in each session
        my_hashtags = hashtags     The bit will go after all the hash tags in each session
    '''

    my_hashtags = hashtags



    # general settings

    '''
    Here you will define the tags or words that we should avoid while engaging with somebody's post.
    Use this section to avoid bot to comment on unrelavant users. This is very useful to get to right audience
    '''
    session.set_dont_like([
                        'rip', 
                        'R.I.P.', 
                        'rest', 
                        'cancer', 
                        'sexy', 
                        'boobs', 
                        'nude', 
                        'rape', 
                        'trump', 
                        'abortion',
                        'collegebabes', 
                        'sexyselfie', 
                        'wholesale', 
                        'manufacturer'
                        ])








    '''
    You only need to change the percentage value here.
    for example
        session.set_do_follow(enabled=True, percentage=50, times=1)
            This would mean that the bot has 50% chance that it will follow the current account it is engaging with.
        
        50 is a safe limit. you shouldnot get greedy and try to follow every account the bot interacts with.
        Our bot will run 24/7 everyday. so be patient and it will grow your instagram business 
    '''
    session.set_do_follow(enabled=True, percentage=60, times=1)
    session.set_action_delays(enabled=True , like=5,comment=5,follow=5)









    '''
    Same as above percentage of whether bot should comment or not. I would recommend not going over 70.
    If you want to do 70 wait at least 1 week after running the bot'''
    session.set_do_comment(enabled=True, percentage=100)










    '''
    This is where you set comments. Please put as many comments as you can. The bot will select randomly from these
    '''
    session.set_comments([
                        u'We think you"d be a great model! DM us for more info!:heart:',

                        u'We’d love to have you model for us!:heart:'
                        u'Message us for more information!',

                        u'You’d be a great model for our clothing line!'
                        u' DM us for more info!:heartbeat:',

                        u'This is awesome!! :heart_eyes:'
                        u'We’d love to have you model for us!:heart:Message us for more information!',

                        u'You are gorgeous ! We would love for you to model for our brand.'
                        u'DM us for more info! :love:',

                        u'You’d 😁 be a great model for our clothing line, DM us to learn more and get started!😁 😁',


                        u'Can we set you up as a model within our brand? DM us if you are interested!️😘❤️'
                        u'! We’d love to have you model for us! Message for more details !',


                        u'! Gorgeous ! ! We would LOVE to have you model for us! DM us for info !'
                        u'Love your work, DM us to join our modeling team!️😘❤️'
                            
                                ],
                            media='Photo')

    '''Same thing for likes. 60 is pretty solid'''
    session.set_do_like(True, percentage=100)





    '''
    This section is very important . This has helped me grow my followers.
    Here are the settings for whether our bot should interact with the posts. 
    it defines the max and min threshold of likes and comments the post should have.

        Maybe you donot want to go after girls with very high comments,likes on their posts because they might not notice or
        dont want to model for you becase they are alreday famous.
        I donot know if this will be useful to you but i included just in case.

        if you donot want to filter posts by likes and comments . set the "enabled=True" "to enabled=False"
    '''

    session.set_delimit_liking(enabled=True, max=15000, min=0)
    session.set_delimit_commenting(enabled=True, max=3000, min=0)









    '''
    This is where you define the max and min followers and following the account should have
    potency ratio helps you determine whether the account we are trying to interact with is good fit for us. You can calculate it with

        potency_ratio = followers count / following count 
    "None" means the bot will not filter by that parametetr Here i have set max_post to none. So the bot wont care if the account has zillion posts or zero posts

    '''
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=0.4,
                                    delimit_by_numbers=True,
                                    max_followers=100000,
                                    max_following=2000,
                                    min_followers=150,
                                    min_following=10,
                                    max_posts=None)







    '''
    This is section where you make sure you account doesnot get blocked.
    It helps the bot to take rest after certain limits . For example- after certain amount of likes or follows or comments
        Here
            peak_likes=(50, 1000) -> 50 is hourly like limit and 1000 is daily like limit
            peak_comments=(31, 600) -> 21 is hourly comment limit and 600 is daily comment limit
            peak_follows=(50, None) -> 50 is houry follow limit and None means that there is no daily follow limit

        Please use it wisely
    '''
    session.set_quota_supervisor(enabled=True,
                                    sleep_after=["likes", "follows","comments"],
                                    sleepyhead=True, stochastic_flow=True,
                                    notify_me=False,
                                    peak_likes=(50, None),
                                    peak_comments=(50, None),
                                    peak_follows=(30, 600))







    '''
    It defines how many posts of a user should our bot interact with. 
    Similarly percentage is for descision whether the bot should engage or not

    '''
    session.set_user_interact(amount=3, randomize=False, percentage=100, media='Photo')
    

    while True:


        # activity

        '''
        This section defines how many users should the bot interact per tags.
        '''
        session.like_by_tags(my_hashtags, amount=500, media=None,randomize=True)




        '''
        Here we unfollow users that we followed earlier by our bot. It wont unfollow people that you have followed manually

        As we target mainly active accounts, I use two unfollow methods. 
        The first will unfollow everyone who did not follow back within 12h.
        The second one will unfollow the followers within 24h.


        Bonus Tip: If you want to unfollow people who havenot followed you back.
        change InstapyFollowed=(True,"nonfollowers") to InstapyFollowed=(True,"nonfollowers")

            example:
                session.unfollow_users(amount=500, InstapyFollowed=(False, "nonfollowers"),
                                style="FIFO",
                                unfollow_after=12 * 60 * 60, sleep_delay=551)
        '''
        session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                                style="FIFO",
                                unfollow_after=12 * 60 * 60, sleep_delay=551)


        session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                                style="FIFO", unfollow_after=24 * 60 * 60,
                                sleep_delay=551)
