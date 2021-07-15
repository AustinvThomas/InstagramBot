import tkinter as tk
import random
from instapy import InstaPy
from instapy import smart_run

# Top level window
frame = tk.Tk()
frame.title("InstaBot")
frame.geometry('700x450')
# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    lbl.config(text = "Bot Activated")
    #assigning the values received through GUI
    insta_username = inputtxt.get(1.0, "end-1c")
    
    insta_password = inputtxt1.get(1.0, "end-1c")
    account = inputtxt2.get(1.0, "end-1c")
    # Function for INSTAGRAM BOT
    instabot(insta_username,insta_password,account)

    

# TextBox Creation
label_0 = tk.Label(frame, text="Instagram Bot",width=20,font=("bold", 20),padx=20, pady=20)
label_0.pack()
label_1 = tk.Label(frame, text="Username",width=20,font=("bold", 10),padx=20, pady=20)
label_1.pack()
inputtxt = tk.Text(frame,
                height = 1,
                width = 20)
inputtxt.pack()
label_2 = tk.Label(frame, text="Password",width=20,font=("bold", 10),padx=20, pady=20)
label_2.pack()
inputtxt1 = tk.Text(frame,
                height = 1,
                width = 20)
inputtxt1.pack()
label_3 = tk.Label(frame, text="Simailar account you need to Target",width=30,font=("bold", 10),padx=20, pady=20)
label_3.pack()
inputtxt2 = tk.Text(frame,
                height = 1,
                width = 20)
inputtxt2.pack()
label_4 = tk.Label(frame, text="Click the below button to start!",width=30,font=("bold", 10),padx=20, pady=20)
label_4.pack()

# Button Creation
printButton = tk.Button(frame,
                        text = "Activate Bot",bg='brown',fg='white',
                        command = printInput)
printButton.pack()

# Label Creation
lbl = tk.Label(frame, text = "",font=("bold", 20))
lbl.pack()
def instabot(insta_username,insta_password,account):
    # login credentials
    insta_username = insta_username  
    insta_password = insta_password  


    # restriction data
    dont_likes = ['#exactmatch', '[startswith', ']endswith', 'broadmatch']
    ignore_users = []

    """ Prevent commenting on and unfollowing your good friends (the images will 
    still be liked)...
    """
    friends = []

    """ Prevent posts that contain...
    """
    ignore_list = []

    # TARGET data
    """ Set similar accounts and influencers from your niche to target...
    """
    targets = [account]

    """ Skip all business accounts, except from list given...
    """
    target_business_categories = ['category1', 'category2', 'category3']

    # COMMENT data
    comments = ['Nice shot! @{}',
            'I love your profile! @{}',
            'Your feed is an inspiration :thumbsup:',
            'Just incredible :open_mouth:',
            'What camera did you use @{}?',
            'Love your posts @{}',
            'Looks awesome @{}',
            'Getting inspired by you @{}',
            ':raised_hands: Yes!',
            'I can feel your passion @{} :muscle:']

    # get a session!
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False)

    # let's go! :>
    with smart_run(session):
        # HEY HO LETS GO
        # general settings
        session.set_dont_include(friends)
        session.set_dont_like(dont_likes)
        session.set_ignore_if_contains(ignore_list)
        session.set_ignore_users(ignore_users)
        session.set_simulation(enabled=True)
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=7500,
                                        max_following=3000,
                                        min_followers=25,
                                        min_following=25,
                                        min_posts=10)

        session.set_skip_users(skip_private=True,
                               skip_no_profile_pic=True,
                               skip_business=True,
                               dont_skip_business_categories=[
                                   target_business_categories])

        session.set_user_interact(amount=3, randomize=True, percentage=80,
                                  media='Photo')
        session.set_do_like(enabled=True, percentage=90)
        session.set_do_comment(enabled=True, percentage=15)
        session.set_comments(comments, media='Photo')
        session.set_do_follow(enabled=True, percentage=40, times=1)

        # activities

        # FOLLOW+INTERACTION on TARGETED accounts
        """ Select users form a list of a predefined targets...
        """
        number = random.randint(3, 5)
        random_targets = targets

        if len(targets) <= number:
            random_targets = targets

        else:
            random_targets = random.sample(targets, number)

        """ Interact with the chosen targets...
        """
        session.follow_user_followers(random_targets,
                                      amount=random.randint(30, 60),
                                      randomize=True, sleep_delay=600,
                                      interact=True)

        # UNFOLLOW activity
        """ Unfollow nonfollowers after one day...
        """
        session.unfollow_users(amount=random.randint(75, 100),
                               nonFollowers=True,
                               style="FIFO",
                               unfollow_after=24 * 60 * 60, sleep_delay=600)

        """ Unfollow all users followed by InstaPy after one week to keep the 
        following-level clean...
        """
        session.unfollow_users(amount=random.randint(75, 100),
                               allFollowing=True,
                               style="FIFO",
                               unfollow_after=168 * 60 * 60, sleep_delay=600)

        """ Joining Engagement Pods...
        """
        session.join_pods()


frame.mainloop()

