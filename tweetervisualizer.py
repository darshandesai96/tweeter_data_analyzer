import pandas as pd
import operator
import matplotlib.pyplot as plt
import seaborn as sns
desired_width=320

pd.set_option('display.width', desired_width)
pd.set_option('max_colwidth',400)
pd.describe_option('max_colwidth')
pd.set_option('max_rows',9999)


pd.set_option('display.max_columns',20)
df1 = pd.read_csv("twitter.csv", names=['tweetid','created_at', 'user_name','text','favourite_count','retweet_count', 'location', 'hashtags'])

df1 = df1.replace(to_replace='NaN', value="Unknown")

print(df1.columns[df1.isna().any()])
print(df1['location'].isna().sum())
print(df1['hashtags'].isna().sum())

print(df1['text'].str.contains('share|stock|trade|tsla|Tsla|Share|Stock|invest|Invest|$TSLA|$Tsla|$tsla|split|Split|buy|reverse|fund|amazon|Amazon|Analysis' ).value_counts()[True])
print(df1['text'].str.contains('Car|car|Vehicle|Vehicle|Electric|electric|EV|ev|Motor|motor|Model|MODEL|model|CAR|SPEED|speed|Turck|truck|ElectricVehicles|EVs|pickup|Pickup|OEM|Control|Charge|charge|control|Driver|driver|capacity|Capacity|Brake|Coil|wire|Volatage|voltage|Volt|volt|Renewable|renewable|Drive|drive|Design|design|solar|science|patent|battery|Battery|cooling|charging|Charing' ).value_counts()[True])

dataframe = ""
dataframe = df1['text'].str.cat()

counts = dict()
words = dataframe.split()
for word in words:
  if word in counts:
    counts[word] += 1
  else:
    counts[word] = 1

sorting_dictionary = sorted(counts.items(), key = operator.itemgetter(1),reverse=True)
print(sorting_dictionary)

plt.figure()
plt.bar("Without Stocks",271)
plt.bar("With Stocks",86)
plt.legend()
plt.show()

print(df1['user_name'].duplicated().sum())
print(df1['user_name'].value_counts())

plt.figure()
df1['user_name'].value_counts().plot()

values = df1.user_name.value_counts()
print(values[values > 2])
df3 = values[values > 2]
plt.figure(figsize=(12,8))

df3.plot()

hasht = ""
counting_hashtags = dict()
hasht = df1['hashtags'].str.cat()
hasht = hasht.split()
for hashtags in hasht:
  if hashtags in counting_hashtags:
    counting_hashtags[hashtags] += 1
  else:
    counting_hashtags[hashtags] = 1

print(counting_hashtags)

lists = dict((k,v) for k,v in counting_hashtags.items() if v>= 5)
print(lists)
SMALL_SIZE = 11
keys = lists.keys()
values = lists.values()
plt.rc('xtick', labelsize=SMALL_SIZE, color='r')    
plt.rc('ytick', labelsize=SMALL_SIZE, color = 'r')    
plt.figure(figsize=(40,10))
plt.bar(keys, values)
plt.show()

sum_column_for_favourite_retweet_count = df1['favourite_count'] + df1['retweet_count']
df1['sum_column'] = sum_column_for_favourite_retweet_count
sorted_count = df1.sort_values('sum_column', ascending=False)
SMALL_SIZE = 9
keys = lists.keys()
values = lists.values()
plt.rc('xtick', labelsize=SMALL_SIZE, color='r')    
plt.rc('ytick', labelsize=SMALL_SIZE, color = 'r')  
ax = sorted_count[:70].plot.barh(x='tweetid',y='sum_column', figsize = (10,15))
plt.show()

plt.figure(figsize=(100,100))
plt.scatter(df1['tweetid'],df1['created_at'])
plt.show()

print(df1['text'].duplicated().sum())
df3 = df1['text'].value_counts()
print(df3[df3 > 1])
