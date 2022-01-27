import twint
import schedule
import time

# you can change the name of each "job" after "def" if you'd like.
def jobone():
	print ("Fetching Tweets")
	c = twint.Config()
	# choose username (optional)
	c.Username = "irfankkhairullah"
	# choose search term (optional)
	c.Search = "xlhome"
	# choose beginning time (narrow results)
	c.Since = "2020-01-01"
	# set limit on total tweets
	c.Limit = 5000
	# no idea, but makes the csv format properly
	c.Store_csv = True
	# format of the csv
	c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
	# change the name of the csv file
	c.Output = "filename.csv"
	twint.run.Search(c)

def jobtwo():
	print ("Fetching Tweets")
	c = twint.Config()
	# choose username (optional)
	c.Username = "irfankkhairullah"
	# choose search term (optional)
	c.Search = "#xlhome"
	# choose beginning time (narrow results)
	c.Since = "2021-01-01"
	# set limit on total tweets
	c.Limit = 5000
	# no idea, but makes the csv format properly
	c.Store_csv = True
	# format of the csv
	c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
	# change the name of the csv file
	c.Output = "xlhome.csv"
	twint.run.Search(c)

# run once when you start the program

jobone()
jobtwo()

# run every minute(s), hour, day at, day of the week, day of the week and time. Use "#" to block out which ones you don't want to use.  Remove it to active. Also, replace "jobone" and "jobtwo" with your new function names (if applicable)

# schedule.every(1).minutes.do(jobone)
schedule.every().hour.do(jobone)
# schedule.every().day.at("10:30").do(jobone)
# schedule.every().monday.do(jobone)
# schedule.every().wednesday.at("13:15").do(jobone)

# schedule.every(1).minutes.do(jobtwo)
schedule.every().hour.do(jobtwo)
# schedule.every().day.at("10:30").do(jobtwo)
# schedule.every().monday.do(jobtwo)
# schedule.every().wednesday.at("13:15").do(jobtwo)

while True:
  schedule.run_pending()
  time.sleep(1)
