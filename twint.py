import tweepy
import csv
consumer_key = "ASRAGdCJdtmQ5bLWGBGZYd0oy"
consumer_key_secret = "x4zA9z6FOCwKtFVGRK3dtEZDuxyeQrNvTRzVSI4g83WFe4jirT"
access_token = "1368632915031040002-L98lPEecMSwK1J824JPDLN068VuafH"
access_token_secret = "zFg8F5hIIGmApVu52u8jkFIF7MseamgdiX7ZjCXIDWplI"
auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
api = tweepy.API(auth)
# Open/create a file to append data to
csvFile = open('xlHomeku.csv', 'w', encoding='utf-8')
#Use csv writer
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search, q='xl home -filter:retweets', tweet_mode='extended',lang="id").items(6000):
    text = tweet.full_text
    user = tweet.user.name
    created = tweet.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])
csvWriter = csv.writer(csvFile)
csvFile.close()