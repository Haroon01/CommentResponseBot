import configparser

config = configparser.ConfigParser()
config.read("config.ini")

a = config.get("SUBREDDIT", "NAME")

print(type(a))