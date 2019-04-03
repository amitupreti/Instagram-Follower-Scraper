""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run
import random

"""
This template is written by Amit Upreti
This is avery good strategy to get  followers from  various locations and tags.
with locations it is not very effective because people dont put locations most of the time. But wecan try generic locations
like us or new york.
"""



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





while True:
    with smart_run(session):
        """ Activity flow """
        # general settings
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



        # activity

        '''
        It defines how many posts of a user should our bot interact with. 
        Similarly percentage is for descision whether the bot should engage or not

        '''
        session.set_user_interact(amount=3, randomize=False, percentage=100, media='Photo')



        '''
        Here we define the percentage  whether the bot should follow,like the account or not
        '''
        session.set_do_follow(enabled=True, percentage=60)
        session.set_do_like(enabled=True, percentage=100)
        session.set_action_delays(enabled=True, like=5,comment=5,follow=5)


        #setting comments. Pleas include as much comments you can
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







        '''
        This is section where you make sure you account doesnot get blocked.
        It helps the bot to take rest after certain limits . For example- after certain amount of likes or follows or comments
            Here
                peak_likes=(50, 1000) -> 50 is hourly like limit and 1000 is daily like limit
                peak_comments=(31, 600) -> 21 is hourly comment limit and 500 is daily comment limit
                peak_follows=(50, None) -> 50 is houry follow limit and None means that there is no daily follow limit

            Please use it wisely and dont be greedy. I am not reponsible if you try to do high number of follows ,comments or likes per day.
            This will run 24/7 so dont worry and choose small numbers
        '''
        session.set_quota_supervisor(enabled=True,
                sleep_after=["likes", "follows","comments"],
                sleepyhead=True, stochastic_flow=True,
                notify_me=False,
                peak_likes=(50, None),
                peak_comments=(50, None),
                peak_follows=(30, 600))


        #percentage for whether the bot should comment on the post or not
        session.set_do_comment(enabled=True, percentage=100)



        session.set_delimit_liking(enabled=True, max=15000, min=0)
        session.set_delimit_commenting(enabled=True, max=3000, min=0)


        #here is where you put the instagram tags and locations
        #here amount means how many followers to go after 
        #find location data here
        #https://www.instagram.com/explore/locations/
        session.like_by_locations(locations = ["498124133/kathmandu-university/"
                                            ],
                                                amount = 300
                                                )



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
