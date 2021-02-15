
from flask import Flask, send_file, make_response
#from plot import plot_for_date
#from plot import sentiment_plot_norm
from chart import plot_for_date
from chart import sentiment_plot_norm
from chart import sentiment_plot
from chart import top_positive_plot
from chart import top_negative_plot
import pandas as pd
from sqlalchemy import create_engine
from flask import render_template
#from plot import sentiment_plot
engine = create_engine("postgresql://postgres:NFvpbWt78@128.226.28.177:5432/data")
df_visual = pd.read_sql_query('select * from "data"',con=engine)

app = Flask(__name__)

@app.route("/plot_for_date")
def get_plot():
  label, data = plot_for_date(df_visual)
  return render_template('first_chart.html' , title = 'Date Wise CDF', max = 4500, labels=label, values=data)
  
@app.route("/sentiment_norm")
def get_plot_norm():
  label, sentiment_norm, positive, negative = sentiment_plot_norm(df_visual)
  return render_template('second_chart.html' , title = 'Normalized Sentiment', max = 1, labels=label, values=sentiment_norm, values1=positive, values2=negative)
  

  
  
@app.route("/sentiment")
def get_plot_sentiment():
  label, sentiment, positive, negative = sentiment_plot(df_visual)
  return render_template('third_template.html' , title = 'Sentiments Without Normalized', max = 1, labels=label, values=sentiment, values1=positive, values2=negative)
  
@app.route("/top_positive")
def get_plot_for_top_positive():
  label, value = top_positive_plot(df_visual)
  return render_template('top_positive.html', title = 'Top Positive Hashtags', max = 1200, labels = label, values = value)
  

@app.route("/top_negative")
def get_plot_for_top_negative():
  label, value = top_negative_plot(df_visual)
  return render_template('top_negative.html', title = 'Top Negative Hashtags', max = 300, labels = label, values = value)
    
if __name__ =='__main__':
    app.run(port=8080)
    app.config['TEMPLATES_AUTO_RELOAD'] = True