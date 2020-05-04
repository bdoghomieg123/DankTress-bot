import praw
import time
from datetime import datetime
import pprint
import os
from common import *

reddit = praw.Reddit('bot1')


#Edit this line to the subreddit you want this bot to run on.
subreddit = ""

#This is what the bot will reply on a submission it removes.
removalComment = ""


removalComment2 = ""

#The Flair ID that you want the bot to search for (Note: Different from Flair Class and Flair Text)
#You can find the Flair ID by going to the submission Flair in your subreddit and clicking "Copy ID"
flairID = ""

#if you want to search more than one flairs, put the second one here.
flairID2 = ""


def flair2():
    if flairID2 != "":
        if submission.link_flair_template_id == flairID2:
            comment = submission.reply(removalComment)
            print(f"bot removed and replied to {submission.title}\n\n")
            posts_replied_to.append(submission.id)
            try:
                comment.mod.distinguish(sticky=True)
                submission.mod.remove()
                print("Task Completed Successfully\n\n")

            except Exception as e:
                print(e)

    else:
        main()

    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


"""DO NOT EDIT BELOW THIS LINE!"""
def main(subToScan):
    print("Bot Logged in")
    time.sleep(2)
    clear()
    subToScan = reddit.subreddit(subreddit)
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []

    else:
        with open("posts_replied_to.txt", "r") as f:
           posts_replied_to = f.read()
           posts_replied_to = posts_replied_to.split("\n")
           posts_replied_to = list(filter(None, posts_replied_to))

    while True:
        for submission in subToScan.new(limit=10):
            if submission.id not in posts_replied_to:
                if submission.link_flair_template_id == flairID:
                    comment = submission.reply(removalComment)
                    print(f"bot removed and replied to {submission.title}\n\n")
                    posts_replied_to.append(submission.id)
                    try:
                        comment.mod.distinguish(sticky=True)
                        submission.mod.remove()
                        print("Task Completed Successfully\n\n")
                        flair2()

                    except Exception as e:
                        print(e)

                else:
                    flair2()


                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")



print("Do you wish to delete the cache of posts replied to [Yes/No]?\n\n\n")
deleteCache = input("It is not reccomended to clear cache. Clearing the cache will create spam\n\n\n")
print("")
clear()

if deleteCache.lower() == "y" or "yes":
    if os.path.isfile("posts_replied_to.txt"):
        os.remove("posts_replied_to.txt")
        print("Cache deleted. Bot starting.")
        time.sleep(3)
        clear()

    elif not os.path.isfile("posts_replied_to.txt"):
        print("Cache is already clear or the bot has never been run.\n\nStarting bot.")
        time.sleep(3)
        clear()


elif deleteCache.lower() == "n" or "no":
    print("Ok. Keeping Cache and Starting Bot...")
    time.sleep(3)
    clear()


main(subreddit)
