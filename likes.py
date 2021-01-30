import instaloader
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO


L = instaloader.Instaloader()

USER = "talestheytell"
PROFILE = USER
L.interactive_login(USER)


profile = instaloader.Profile.from_username(L.context, PROFILE)
likes=[]
comments=[]
#url=[]
print("Fetching likes of all posts of profile {}.".format(profile.username))
for post in profile.get_posts():    
    likes.append(post.likes)
    comments.append(post.comments)
    #url.append(post.url)
    # response = requests.get(post.url)
    # img = Image.open(BytesIO(response.content))
    # img.show()
print(likes)
print(comments)
total_likes=sum(likes)
total_comments=sum(comments)
print(total_likes)
print(total_comments)
avg_likes=total_likes//len(likes)
print(avg_likes)
avg_comments=total_comments//len(comments)
print(avg_comments)

#     likes = likes+len(set(post.get_likes()))
# print(likes)

#print("Fetching followers of profile {}.".format(profile.username))
#followers = set(profile.get_followers())

# ghosts = followers - likes

# print("Storing ghosts into file.")
# with open("inactive-users.txt", 'w') as f:
#     for ghost in ghosts:
#         print(ghost.username, file=f)Vaani@787
