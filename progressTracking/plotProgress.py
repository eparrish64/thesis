from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/tburch/Documents/gitDevelopment/thesis/progressTracking/progress.csv')
df['timestamp_fixed'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H:%M:%S")
df = df.set_index('timestamp_fixed')

# Plot 1
df.plot(y='wordcount', legend=None)
plt.xlabel('Date')
plt.ylabel('Word Count')
plt.savefig('plots/wordcount.png')

# Plot 2
df.plot(y='pagecount',legend=None)
plt.xlabel('Date')
plt.ylabel('Page Count')
plt.savefig('plots/pagecount.png')
