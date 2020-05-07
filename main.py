import praw
import time
from datetime import datetime
import pprint
import os
from common import *

reddit = praw.Reddit('bot1')


RESPONSES = {

        "<Flair ID>" : "Flair1 Removal Comment",
        "<FLair ID>" : "Flair2 Removal Comment",
        "<Flair ID>" : "Flair3 Removal Comment",


}

#Edit this line to the subreddit you want this bot to run on.
subreddit = ""

"""DO NOT EDIT BELOW THIS LINE!"""
def main(subToScan):
    print(f"Bot Logged in and searching r/{subreddit}")
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
                if submission.link_flair_text == None:
                    print("Flair Empty. Skipping post")
                    posts_replied_to.append(submission.id)

                else:
                    flair_id = submission.link_flair_template_id
                    response = RESPONSES.get(flair_id)
                    comment = submission.reply(response)
                    print(f"bot removed and replied to {submission.title}\n\n")
                    posts_replied_to.append(submission.id)
                    try:
                        comment.mod.distinguish(sticky=True)
                        submission.mod.remove()
                        print("Task Completed Successfully\n\n\n\n")

                    except Exception as e:
                        print(e)



                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")






main(subreddit)
