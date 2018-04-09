import twitter
import io
import csv
api = twitter.Api(consumer_key="YMaRCwObPMfcEvcqDSMaEza4x",
	consumer_secret="qmawQuA8p6Rxvp9rrLREUkaLVRLRWpUdOE9GaI2BLpxntq8iat",
	access_token_key="961387368463781888-6NYJVeWtVhbXVU12qvRno4kuq43492N",
	access_token_secret="5DsU7UfhghntczyLNsijssrfZVpcsOe8Rbo24Ighjnzwo",
	sleep_on_rate_limit=True)
output_file = open("flu_annotations/fluTweets6.csv", "w")
i=0
writer = csv.writer(output_file)
writer.writerow(["tw_id", "text", "location", "long", "lat"])

term = 'virus'
lang = 'en'
geocode = (37.80444444,-122.27083333, "100mi")
max_id = None

for i in range(0,50):
	tweet_list = api.GetSearch(term = term, lang = lang, geocode = geocode,
						   max_id = max_id, result_type = 'recent', count = 100)
	for tweet in tweet_list:
		#print tweet
		d = tweet.AsDict()
		tw_id = d["id"]
		if max_id == None or max_id > tw_id:
			max_id = tw_id-1
		text = d["text"]
		location = None
		long = None
		lat = None
		if "coordinates" in d:
			long = d["coordinates"]["coordinates"][0]
			lat = d["coordinates"]["coordinates"][1]
		try:
			location = d["user"]["location"]
		except KeyError:
			location = None
		row = tw_id, text.encode('ascii', 'replace'), location, long, lat
		try:
			writer.writerow(row)
		except UnicodeEncodeError:
			None
		