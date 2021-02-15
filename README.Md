project-3-2-implementation-falcons
project-3-2-implementation-falcons created by GitHub Classroom 


To run server use command line for this ---
1. First cd to ddesai9 folder
2. Then run bin/python3 chart.py 
3. Then run bin/python3 hello.py

Once flask development server starts then --

To view the PROJECT graphs Need to open dashboard.html with X2GO client-

1. On desktop check for dashboard.html file and open it with browser.
2. Run all the queries in 'sequence'. 
3. plot_for_date will give you the datewise cdf.
4. sentiment_norm will provide you the normalized sentiment analysis 
where RED color denotes Negative, Green denotes Positive and Purple shows Neutral sentiments over the days.
5. sentiment will provide you the sentiment analysis (without normalized)
where RED color denotes Negative, Green denotes Positive and Purple shows Neutral sentiments over the days.
6. top_positive will provide you the most frequent hashtags used in the positive sentiments. There are total 8 hashtags.
7. top_negative will proived you the most frequent hashtags used in the negative sentiments. There are total 8 hashtags.

Note-- All queries must run in sequence.


----
If want to run utility files then - (Not needed to run)

--For tweet.py get config1.json in same file directory. 
--For tweet visualizer.py keep twitter.csv in same file.
--For sentimentwithtextblob.py keep train, test and twitter.csv in same file it will give you vader_labled_data.csv as output.
(We chose VADER over restof the algorithms due to accuracy of VADER is highest amongst all with 82%)
--For kappa_score_visual.py keep vader_labled_data_first100.csv and vader_labled_data.csv in the same file.
--To run data onto postgresql run dataforpostgresql.py with vader_labled_data.csv to keep data onto server.
--Can check templates used for the chart.js.
--chart.py used to create graphs and retrieve data from postgresql server.
--hello.py will run flask server.