import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib
import io
matplotlib.use('TkAgg')

engine = create_engine("postgresql://postgres:NFvpbWt78@128.226.28.177:5432/data")
df_visual = pd.read_sql_query('select * from "data"',con=engine)

def plot_for_date(df_visual):

  df_visual['Date'] = pd.to_datetime(df_visual['created_at']).dt.date
  df_visual['counter'] = 1
  date_time = df_visual.groupby('Date')['counter'].sum().reset_index()
  plt.figure(figsize=(10,6))
  plt.hist(date_time['Date'], bins =10, density=True, cumulative=True, histtype='stepfilled', alpha=0.4)
  plt.xticks(rotation=90)
  date_plot = io.BytesIO()
  plt.savefig(date_plot, format='png')
  date_plot.seek(0)
  return date_plot

def sentiment_plot_norm(df_visual):

  df_sent = df_visual.groupby(['sentiment','Date'])['counter'].sum().reset_index()
  p1 = df_sent[:33]
  p2 = df_sent[33:66]
  p3 = df_sent[66:]

  plt.figure(figsize=(12,8))
  def norm(data):
    return (data)/(max(data)-min(data))
  plt.plot(p1['Date'],norm(p1['counter']), marker='o',label='negative')
  plt.plot(p2['Date'],norm(p2['counter']), marker='o',label='neutral')
  plt.plot(p3['Date'],norm(p3['counter']), marker='o',label='positive')
  plt.legend()
  sent_norm_plot = io.BytesIO()
  plt.savefig(sent_norm_plot, format='png')
  sent_norm_plot.seek(0)
  return sent_norm_plot
  
def sentiment_plot(df_visual):

  df_sent = df_visual.groupby(['sentiment','Date'])['counter'].sum().reset_index()
  p1 = df_sent[:25]
  p2 = df_sent[25:50]
  p3 = df_sent[50:]
  plt.figure(figsize=(12,8))
  plt.plot(p1['Date'],(p1['counter']), marker='o',label='negative')
  plt.plot(p2['Date'],(p2['counter']), marker='o',label='neutral')
  plt.plot(p3['Date'],(p3['counter']), marker='o',label='positive')
  plt.legend()
  sent_plot = io.BytesIO()
  plt.savefig(sent_plot, format='png')
  sent_plot.seek(0)
  return sent_plot