# Data-Science-Project--
CSCI183 Group 8 Project--
Haruto Nakai, Alma Niu, Jonathan Pak

--Contents:
-flu_annotations: folder containing source training data
	-RelatedVsNotRelated2009TweetIds.txt: collection of tweet IDs from 2009 and its relatedness to Influenza
	-RelatedVsNotRelated2012TweetIds.txt: collection of tweet IDs from 2012 and its relatedness to Influenza
	-retrievedTexts3.csv: tweets retrieved from IDs from 2009
	-retrievedTexts4.csv: tweets retrieved from IDs from 2012
-retrivedTexts2.csv: joining of 2 csvs above
-fetchFluTweets.py: Gets up to 5000 tweets from the last 7 days, in the SF Bay Area, with a certain keyword, and puts them into a csv file.
-fetchTextFromID.py: Uses tweet IDs from a text file and puts text from them into a csv file.
-fluTweets[1..6].csv: Tweets from last 7 days as of 3/11/18 with different flu related keywords 
-Group 8 Tweet Code.ipyb: Jupyter notebook code for project.
	-Runs tests on Naive Bayes and Logistic Regression sorting algorithm trained with data from retrievedTexts2.csv
	-Runs tests on Naive Bayes sorting algorithm from above with data from fluTweets[1..6]
