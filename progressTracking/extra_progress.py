from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np
savedir = "/Users/tburch/Documents/gitDevelopment/thesis/progressTracking/"

df = pd.read_csv('/Users/tburch/Documents/gitDevelopment/thesis/progressTracking/progress.csv')
df['timestamp_fixed'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H:%M:%S")
df = df.set_index('timestamp_fixed')

current_pagecount = df["pagecount"].iloc[-1]
current_wordcount = df["wordcount"].iloc[-1]

pc_color="royalblue"

def make_pages_plot(axis):
    df.plot(y='pagecount',legend=None, color=pc_color, ax=axis,label="Raw Data")
    done_resample_df =  df.resample('w').max()
    done_resample_df['pagecount'].plot(figsize=(12,8), color='salmon',label="Rolling 7-day Max", ax=axis)
    slope = pd.Series(np.gradient(done_resample_df["pagecount"].values), done_resample_df.index, name='slope')
    plt.sca(axis)
    plt.plot(done_resample_df['pagecount'].diff(), color="forestgreen",label="Rolling 7-Day Change")
    plt.ylabel("Pages",fontsize=14)
    plt.annotate("{:,d} Pages".format(current_pagecount), xy=(.05,.88), xycoords="axes fraction", fontsize=16)

def make_words_plot(axis):
    df.plot(y='wordcount',legend=None, color=pc_color, ax=axis,label="Raw Data")
    done_resample_df =  df.resample('w').max()
    done_resample_df['wordcount'].plot(figsize=(12,8), color='salmon',label="Rolling 7-day Max",ax=axis)
    slope = pd.Series(np.gradient(done_resample_df["wordcount"].values), done_resample_df.index, name='slope')
    plt.sca(axis)
    plt.plot(done_resample_df['wordcount'].diff(), color="forestgreen",label="Rolling 7-Day Change")
    plt.ylabel("Words",fontsize=14)
    plt.annotate("{:,d} Words".format(current_wordcount), xy=(.05,.88), xycoords="axes fraction", fontsize=16)

def make_format():
    sns.despine()
    plt.ylim(bottom=0)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

fig, (ax1,ax2) = plt.subplots(ncols=1, nrows=2, sharex=True)
make_pages_plot(ax1)
make_format()
make_words_plot(ax2)
make_format()
plt.xlabel("Date",fontsize=14)
plt.legend(bbox_to_anchor=(1.2,1), loc="center",frameon=False,fontsize=14)

days = mdates.DayLocator()
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%b %Y')
ax2.xaxis.set_major_locator(months)
ax2.xaxis.set_major_formatter(years_fmt)
plt.minorticks_off()
plt.tight_layout()
plt.savefig('plots/page_with_delta')
