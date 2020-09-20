import praw
import time
import csv
import configparser
import random

config = configparser.ConfigParser()
config.read("config.ini")

reddit = praw.Reddit(client_id=config.get("ACCOUNT", "CLIENT_ID"),
                     client_secret=config.get("ACCOUNT", "CLIENT_SECRET"),
                     username=config.get("ACCOUNT", "USERNAME"),
                     password=config.get("ACCOUNT", "PASSWORD"),
                     user_agent="ItsTheRedditPolice")

name = reddit.user.me()


keywords = ["piers", "morgan"]


sillyComments = []


sub = config.get("SUBREDDIT", "NAME")


def wait(seconds):
    time.sleep(seconds)


def initialise():
    if name is None:
        print(f"** Error: Not logged in!")
        wait(1)
        print("Complete the account details in config.ini and try again.")
        wait(5)
        exit()
    print(f"Successfully logged in as: {reddit.user.me()}")
    wait(2)
    load_db()
    print("\nBot is now running!")
    wait(2)
    print("----------------------------------------------------\n")
    wait(1)
    scan_comments()


def load_db():
    db_name = config.get("DATABASE", "LOCATION")
    with open(db_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            str = "".join(row)
            sillyComments.append(str)
        f.close()
    wait(2)
    print(f"Using '{db_name}' for comments!")
    wait(3)


def scan_comments():
    for comment in reddit.subreddit(sub).stream.comments(skip_existing=True):
        try:
            author = comment.author
            if author != name:
                text = comment.body
                lst_text = text.split()
                response = random.choice(sillyComments)
                for word in keywords:
                    match = lst_text.count(word)
                    if match == 1:
                        comment.reply(response)
                        print(f"** Comment sent to u/{author}\n")
                        break
            wait(1)
        except praw.exceptions.RedditAPIException as e:
            print(f"** Failed to send a comment. ({e})\n")




initialise()
