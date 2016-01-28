#!/usr/bin/env python
# encoding: utf-8

#this code is a mash of stuff collected from a bunch of different sources... plus a large amount of debugging and exception handling on my own. It collects up to 3500 tweets from each user contained in a csv list, and spits them into csv format...one file for each user. It uses the API credentials from Colin Conrad's own Twitter App: . If you want to use this code for your own application, you need to register an app and change the API credentials. The rest should work.
 
import tweepy #https://github.com/tweepy/tweepy
import csv, time
 
#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# this is used to collect the twitter names
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('users.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list

users = columns['x']

#skipped users go in this array
skipped =[""]
scanned = [] 

def get_all_tweets(screen_name):
	#Twitter only allows access to a users' most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify =True)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	#this has been changed to a while loop to handle exceptions related to people without tweets
	while True:	
		try:
			oldest = alltweets[-1].id - 1
			break
		except:
			oldest = 0
			break
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:

		print "getting tweets before %s" % (oldest)
	
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
	
		#save most recent tweets
		alltweets.extend(new_tweets)
	
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
	
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('tweets/%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


#the call goes here
if __name__ == '__main__':
	#declaring a variable for counting... this gets changed depending on whether we need to troubleshoot
	n = 0
	#pass in the username of the account you want to download. This also records errors and collects the error users in an array, printed when the program finishes.
	while n < 4:
		try:
			nm = users[n]
			print("Downloading tweets belonging to " + nm)
			get_all_tweets(nm)
			scanned.append(nm)
		except tweepy.TweepError as e:
			print e
			print type(e)
			print e.__dict__
			print e.reason
			print type(e.reason)
			print ("Something went wrong ...adding this user to the skipped users category. Beware!" )
			skipped.append(users[n])
			n+=1
			continue
		n += 1
print("The following is a list of users that were successfully copied " + str(scanned))
print("The following is a list of users for whom there were errors " + str(skipped))
print("Thanks for using the Tweet Dumper! I have a great day :)")
