import pandas as pd
import numpy as np
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
  num_py = date_time.loc[:,'counter']
  dx = 0.01
  num_py /= (dx * num_py).sum()
  val = np.cumsum(num_py *dx)
  plt.figure(figsize=(10,6))
  plt.hist(date_time['Date'], bins =10, density=True, cumulative=True, histtype='stepfilled', alpha=0.4)
  plt.xticks(rotation=90)
  date_plot = io.BytesIO()
  plt.savefig(date_plot, format='png')
  date_plot.seek(0)
  return date_time['Date'], val

def sentiment_plot_norm(df_visual):

  df_sent = df_visual.groupby(['sentiment','Date'])['counter'].sum().reset_index()
  p1 = df_sent[:73]
  p4 = df_sent[:73]
  p2 = df_sent[73:148]
  p3 = df_sent[148:]

  

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
  p1 = norm(p1['counter']).values
  p2 = norm(p2['counter']).values
  p3 = norm(p3['counter']).values
  p4 = df_sent['Date'].unique()
  return p4,p1, p2, p3
  
def sentiment_plot(df_visual):

  df_sent = df_visual.groupby(['sentiment','Date'])['counter'].sum().reset_index()
  p1 = df_sent[:73]
  p2 = df_sent[73:148]
  p3 = df_sent[148:]
  p4 = df_sent[:73]
  plt.figure(figsize=(12,8))
  plt.plot(p1['Date'],(p1['counter']), marker='o',label='negative')
  plt.plot(p2['Date'],(p2['counter']), marker='o',label='neutral')
  plt.plot(p3['Date'],(p3['counter']), marker='o',label='positive')
  plt.legend()
  sent_plot = io.BytesIO()
  plt.savefig(sent_plot, format='png')
  
  
  sent_plot.seek(0)
  p1 = p1['counter'].values
  p2 = p2['counter'].values
  p3 = p3['counter'].values
  p4 = df_sent['Date'].unique()
  return p4, p1,p2, p3
  
def top_positive_plot(df_visual):
  df_highest = df_visual
  df_highest = df_highest.dropna(subset=['hashtags'])
  df_pos = df_highest.loc[df_highest['sentiment'] == 'positive']
  df_pos = df_pos['hashtags'].str.split(' ')
  positive = []
  for i in df_pos:
    positive.append(i)
  final_pos = []
  for i in positive:
    for j in i:
      final_pos.append(j)
  final_pos = list(filter(lambda a: a!= '', final_pos))
  dictionary_for_pos = {} 
  for i in final_pos:
    if i in dictionary_for_pos:
      dictionary_for_pos[i] += 1
    else:
      dictionary_for_pos[i] = 1
  final = sorted(dictionary_for_pos.items(), key=lambda x:x[1], reverse=True)
  list_of_pos = []
  for i in range(0,9):
    list_of_pos.append(final[i])
  hashtag_pos =  [i[0] for i in list_of_pos]
  hashtag_pos_counts =  [i[1] for i in list_of_pos]
  
  return hashtag_pos, hashtag_pos_counts
  
def top_negative_plot(df_visual):
  df_highest = df_visual
  df_highest = df_highest.dropna(subset=['hashtags'])
  df_neg = df_highest.loc[df_highest['sentiment'] == 'negative']
  df_neg = df_neg['hashtags'].str.split(' ')
  negative = []
  for i in df_neg:
    negative.append(i)
  final_neg = []
  for i in negative:
    for j in i:
      final_neg.append(j)
  final_neg = list(filter(lambda a: a!= '', final_neg))
  dictionary_for_neg = {} 
  for i in final_neg:
    if i in dictionary_for_neg:
      dictionary_for_neg[i] += 1
    else:
      dictionary_for_neg[i] = 1
  final_neg = sorted(dictionary_for_neg.items(), key=lambda x:x[1], reverse=True)
  list_of_neg = []
  for i in range(0,9):
    list_of_neg.append(final_neg[i])
  hashtag_neg =  [i[0] for i in list_of_neg]
  hashtag_neg_counts =  [i[1] for i in list_of_neg]
  
  return hashtag_neg, hashtag_neg_counts


  

  
  
  
  
  
