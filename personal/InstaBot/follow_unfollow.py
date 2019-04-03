"""
This template is written by Amit Upreti

What does this quickstart script aim to do?
- Basic follow/unfollow activity.
In case if you donot want to comment and  just want to follow and unfollow .
it will also like two posts per user
"""

# imports
from instapy import InstaPy
from instapy.util import smart_run



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
    """ Activity flow """
    # general settings
  
  
  #Make changes inside this box
  
  ##############################################################################################################
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "store"])
    session.set_user_interact(amount=2, randomize=True, percentage=100,media='Photo')
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_follow(enabled=True,percentage=100,times=1)
    session.set_action_delays(enabled=True, like=5,comment=5,follow=5)


    # activities
    session.set_quota_supervisor(enabled=True,
        sleep_after=["follows"],
        sleepyhead=True, stochastic_flow=True,
        notify_me=False,

        peak_follows=(20, None))
    """ Massive Follow of users followers (I suggest to follow not more than
    500-800 users  per day for better results)...I am not reponsible if you get blocked by being greedy on followers per day. 
    Please play safe


    """
    session.interact_user_followers(['indian_dslr_lover'], amount=1000,
                                  randomize=False)


############################################################################################################








    """ First step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Second step of Massive Follow...
    """
    session.follow_user_followers(['user1', 'user2', 'user3'], amount=800,
                                  randomize=False, interact=False)

    """ Second step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Clean all followed user - Unfollow all users followed by InstaPy...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=601)
