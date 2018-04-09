import twitter
import io
import csv
api = twitter.Api(consumer_key="YMaRCwObPMfcEvcqDSMaEza4x",
	consumer_secret="qmawQuA8p6Rxvp9rrLREUkaLVRLRWpUdOE9GaI2BLpxntq8iat",
	access_token_key="961387368463781888-6NYJVeWtVhbXVU12qvRno4kuq43492N",
	access_token_secret="5DsU7UfhghntczyLNsijssrfZVpcsOe8Rbo24Ighjnzwo",
	sleep_on_rate_limit=True)
input_file1 = open("flu_annotations/RelatedVsNotRelated2009TweetIDs.txt", "r")
input_file2 = open("flu_annotations/RelatedVsNotRelated2012TweetIDs.txt", "r")
output_file = open("flu_annotations/retrivedTexts3.csv", "w")
i=0
writer = csv.writer(output_file)
for line in input_file2:
	v = str.split(line)
	#print v
	#print int(v[0])-1
	try:
		status = api.GetStatus(v[0], include_my_retweet=False, trim_user=True)
	except twitter.error.TwitterError as error:
		print error
		print v[0] + " was not found."
		
	else:
		#print status #is a 'twitter.models.Status'
		s = status.AsDict()
		text = s["text"]
		text = text.encode('ascii', 'replace')
		row = [v[0], text, v[1]]
		writer.writerow(row)
		

	