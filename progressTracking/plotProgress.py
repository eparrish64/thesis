from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
savedir = "/Users/tburch/Documents/gitDevelopment/thesis/progressTracking/"

df = pd.read_csv('/Users/tburch/Documents/gitDevelopment/thesis/progressTracking/progress.csv')
df['timestamp_fixed'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H:%M:%S")
df = df.set_index('timestamp_fixed')

current_pagecount = df["pagecount"].iloc[-1]
current_wordcount = df["wordcount"].iloc[-1]

wc_color="orangered"
pc_color="royalblue"

# Plot 1
df.plot(y='wordcount', legend=None, color=wc_color)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Word Count',fontsize=16)
sns.despine()
plt.tight_layout()
plt.savefig(savedir+'plots/wordcount.png')
plt.close()

# Plot 2
df.plot(y='pagecount',legend=None, color=pc_color)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Page Count',fontsize=16)
sns.despine()
plt.tight_layout()
plt.savefig(savedir+'plots/pagecount.png')
plt.close()

# Combined Plot
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator()  # every dat
date_fmt = mdates.DateFormatter('%m-%d')

fig, ax = plt.figure(), plt.gca()
ax2= ax.twinx()
df.plot(y='pagecount',legend=None, ax=ax, color=pc_color)
df.plot(y='wordcount', legend=None, ax=ax2, color=wc_color)

ax.set_ylabel("Page Count", fontsize=16, color=pc_color)
ax2.set_ylabel("Word Count", fontsize=16,color=wc_color)
ax.set_xlabel('Date',fontsize=16)

plt.annotate(str(current_pagecount)+" Pages", xy=(.05,.88), xycoords="axes fraction",color=pc_color, fontsize=14)
plt.annotate(str(current_wordcount)+" Words", xy=(.05,.8), xycoords="axes fraction",color=wc_color, fontsize=14)

#ax.xaxis.set_major_locator(months) Uncomment this after a month
ax.xaxis.set_minor_locator(days)
ax.xaxis.set_major_formatter(date_fmt)

ax.tick_params(labelsize=12)
ax2.tick_params(labelsize=12)
plt.tight_layout()
plt.savefig(savedir+"plots/combinedProgress.png")
