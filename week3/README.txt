====SHIFTKEY PY WEEK 3====

THE TWEET EXTRACTOR

Now that you know a bit about strings and lists, you should be able to do something pretty cool. Check out 
the Tweet Extractor, contained in this folder. When you open it up, you will notice that there are three python
files and a csv file. Open the file called tweet_dumper.py.

This is a simple script that uses the Twitter API to extract tweets from a users' profile, convert them into 
.csv format, and then save them in the tweets folder. It checks a csv file called users.csv to find a list of
Twitter profiles to extract from. Pretty cool, huh?

Try running the script in the command line (linux/Unix) or IDLE (Windows). It probably won't run. In all likelihood,
Python is telling you that there is an error on line 6, which says that it doesn't understand Tweepy. This is because
Tweepy is a python library, which needs to be installed before you can run this script.

To install libraries in Python, we can use a tool called pip. Pip is a nerdy recursive acronym "Pip Installs Python"
...these sorts of things are popular with open source advocates like Richard Stallman (see GNU/Linux). We are going to 
use pip to install the tweepy library. Fortunately, pip comes installed in newer versions of python, (2.7.9 and newer). 
If you are using Linux, this is very easy. Just run "pip install tweepy" and you should be good. Windows users, on the other hand, have it harder. Open op the command line by clicking on start => cmd. Get to the 
root (if you have to, use cd .. until it only says "C:\>"). When you get to the root go to the python folder (cd python)
and type "pip install tweepy".

Try running it again. It still won't run because it doesn't have a Twitter key. If we are going to access the Twitter api,
we will need access keys which are provided by Twitter. In order to make this work, you will need to get a developer key from
Twitter. You can read more about this here: https://dev.twitter.com/oauth/overview and from https://apps.twitter.com/

Once tweepy is installed, and you have keys, you should be good to run the script. Go back to the tweet_dumper.py and run the script. Ok,
it shouldn't take very long. Once it's done it will give you a happy message. Click on the tweets folder. You will notice
three csv files from three twitter users. These are the users that are listed in the users.csv file. Pretty neat, huh? You
can add any number of twitter users to that list and it should try to extract their tweets.

THE TWITTER API

So how does it work? As mentioned, we use the Twitter api to get the data from twitter. An API "Application Programming
Interface" is a series of programming protocols to access a web service provided by a company. Basically this means that
Twitter provices certian functions on the web that opens up their data for the whole world to use. API's follow a protocol
called REST ... it's a pretty important part of modern e-commerce. If you want to learn more, look up how RESTful API's work.

In our case, we use Twitter's web service in our program to do cool stuff. So far, we've only extracted tweets from users. 
However, we might use this technique to build a collection of tweets for analysis. For instance, if we wanted to build an 
app that tells the world about your personality, we might build a "psychographic mining application". There's a pretty cool
one developed by Leadsift here: http://fingerprint.leadsift.com/

It's important to note that though Twitter has opened this up to the world, it is by no means limitless. Twitter limits the 
number of calls to the API for each key to 180 search GET requests and 15 GET requests on dumps per 15 minute window. Basically
if you exceed this, Twitter will make you wait 15 minutes before resuming.