import twitter
import io
import csv
api = twitter.Api(consumer_key="YMaRCwObPMfcEvcqDSMaEza4x",
	consumer_secret="qmawQuA8p6Rxvp9rrLREUkaLVRLRWpUdOE9GaI2BLpxntq8iat",
	access_token_key="961387368463781888-6NYJVeWtVhbXVU12qvRno4kuq43492N",
	access_token_secret="5DsU7UfhghntczyLNsijssrfZVpcsOe8Rbo24Ighjnzwo",
	sleep_on_rate_limit=True)
i_stream = api.GetStreamFilter(
	track = ['flu', 'sick'],
	languages = ['en']
o_file = file('samp_data.csv', 'w')
csvwriter=csv.writer(o_file)
csvwriter.writerow(["user", "text"])
i=0
for result in i_stream:
	user = result["user"]
	scr_n= user["screen_name"]
	text = result["text"]
	text = text.encode('ascii', 'replace')
	#lat = result["geo"]["coordinates"][0]
	#lon = result["geo"]["coordinates"][1]
	row = [scr_n, text]
	csvwriter.writerow(row)
	
	i+=1
	
	print("Tweet "+str(i)+": " + scr_n +": "+text)
	
	if i > 20:
		break
