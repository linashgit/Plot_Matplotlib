# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:24:05 2020

@author: li.nash

"""
from LoadFinancialData import *
import talib # 指標套件
import pandas 
import numpy
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import mpl_finance as mpf
#import seaborn as sns


if __name__ == '__main__':
    #sns.set()
    # 取得資料
    tickers = ['^TWII']
    Load = LoadData()
    alldata = Load.loadYahooFinanceData(tickers=tickers, start='2019-01-01')
    df = alldata[tickers[0]]
    df.index = df.index.format(formatter = lambda x: x.strftime('%Y-%m-%d'))
    print(df)
    
    # 技術指標
    sma20 = talib.SMA(df['Close'], 20)
    
    # 設定風格
    stylelist = plt.style.available
    plt.style.use(stylelist[1])
    
    # 主圖---------------------------------------------------------------------
    
    # 定義子圖
    fig = plt.figure(figsize=(15, 8))
    '''gs = GridSpec(3, 1)
    ax = plt.subplot(gs[:2, :])
    ax2 = plt.subplot(gs[2, :])'''
    
    ax = fig.add_axes([0.1,0.2,0.8,0.7])
    ax2 = fig.add_axes([0.1,0.1,0.8,0.1])   
    
    
    # 繪圖
    #ax = fig.add_subplot(1, 1, 1)

    
    mpf.candlestick2_ochl(ax, 
                          df['Open'], 
                          df['Close'], 
                          df['High'], 
                          df['Low'], 
                          width=0.6, alpha=0.75, 
                          colorup='r', colordown='g')
    
    ax.set_xticks(range(0, len(df.index), 100))
    ax.set_xticklabels(df.index[::100])
    ax.set_xlim(0, len(df.index))
    ax.axes.xaxis.set_ticks([])
    
    ax.plot(sma20.index, sma20, label='ma20')
    ax.set_title('stock')
    ax.set_ylabel('price') 
    ax.legend(loc=2)
    
    # 量圖---------------------------------------------------------------------
    mpf.volume_overlay(ax2, 
                       df['Open'],
                       df['Close'], 
                       df['Volume'], 
                       width=0.6, 
                       colorup='r', colordown='g')
    
    ax2.set_xticks(range(0, len(df.index), 100))
    ax2.set_xticklabels(df.index[::100])
    ax2.set_xlim(0, len(df.index))
    
   #ax2.set_yticks(range(0, max(df['Volume']), max(df['Volume'])/4))
    
    
    