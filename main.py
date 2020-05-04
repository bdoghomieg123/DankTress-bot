import praw
import time
import datetime
import pprint

reddit = praw.Reddit('bot1')


sub_to_scan = ""
removal_reason = ""

def remove(submission):
    print(submission.title)
    if (datetime.datetime.now() - datetime.datetime.fromtimestamp(submission.created_utc)).seconds >= 3600 and submission.score < 10:
            comment = submission.reply(removal_reason)
            try:
                comment.mod.distinguish(sticky=True)
                submission.mod.remove()
                print("Task Completed Successfully")
            except Exception as e:
                print(e)


def main(subreddit):
        while True:
                for submission in reddit.subreddit(str(subreddit)).new():
                    remove(submission)
                time.sleep(60) #waits a minute before re-sifting through posts

main(sub_to_scan) #put the name of the subreddit you want to operate on here
