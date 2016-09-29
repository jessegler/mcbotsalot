# These two lines let us use other people's code.  In this case, Twitter and random.
from twitter import *
import random

# These are like your user name and password. Fill them out with your own from Twitter
token = ''
token_key = ''
con_secret_key = ''
con_secret = ''

person = ["Ellen", "Lawrence", "Eric", "Jess", "Freswinn", "Xena the Warrior Princess", "David Brown", "Aarthi"]

verb = ["ate", "screamed in terror at", "fled from", "defeated", "discovered", "slipped on", "juggled", "danced with", "bamboozled", "dressed up like", "gazed upon", "sniffed", "serenaded"]

thing = ["the cat", "a sandwich", "everything", "all the bananas", "a mystical sword", "fantastic hair", "a shiny rock", "the literal moon", "a bear", "a rocketship to Mars", "Batman", "a robot", "seventeen ninjas", "a werewolf"]

sentence = "And then %s %s %s" % (random.choice(person), random.choice(verb), random.choice(thing))

t = Twitter(auth = OAuth(token, token_key, con_secret, con_secret_key))
t.statuses.update(status = sentence)

# print t.statuses.home_timeline()

# statusList = t.statuses.home_timeline()

# for status in statusList:
#   print status["text"]
