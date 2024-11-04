import ichimoku_04
import candles_data_creation_im
import dataframe_calculation
import indicators
import high_low
import high_low_week
import directory_crea
import peaks
import pivot_points
import swing_low_high
import sr



import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.orders as orders 
import oandapyV20.endpoints.pricing as pricing
import numpy as np
from mpl_finance import candlestick_ohlc
import mplfinance as mpf
import matplotlib.pyplot as plt

import datetime 
import time

import shutil as sh

from dotenv import load_dotenv
import os

load_dotenv()
access_token=os.getenv("access_token")
accountID=os.getenv("accountID")








granularity=['H1','M15','D']


dossiers=[['charts_m15_1h_d',['EUR_USD','GBP_USD','EUR_CAD','GBP_CAD','EUR_CHF','GBP_CHF','EUR_JPY','GBP_JPY','EUR_AUD','GBP_AUD','EUR_GBP',\
	 'EUR_NZD','GBP_NZD','USD_CAD','USD_CHF','USD_JPY','AUD_USD','NZD_USD','AUD_CAD','NZD_CAD','AUD_JPY', 'NZD_JPY','AUD_CHF','NZD_CHF','AUD_NZD',\
	 \
	'CHF_JPY','CAD_JPY','CAD_CHF','XAU_USD','FR40_EUR','DE30_EUR','US30_USD','NAS100_USD','SPX500_USD',]]]
count=1440




def fnc(doss):
	i=0
	for d in doss:
		dr=directory_crea.Directory_crea(d,1)
		paths=dr.crea()
		for elt in d[1]:
			for g in granularity:  # FIGURE
				fig = plt.figure(figsize=(18, 12))
				plt.style.use('tableau-colorblind10')

				ax1 = plt.subplot2grid((5, 1), (0, 0), rowspan=4)
				ax2 = plt.subplot2grid((5, 1), (4, 0))

				# Data
				d = candles_data_creation_im.Candles_data_crea(elt, g, count)
				d.request()

				df = d.data_crea()
				ohlc = d.ohlc_crea_imbalance('ax')

				# Operations: sma, ema, bollinger (1 seule classe)
				op = dataframe_calculation.Dataframe_calc(df)

				# Moyennes mobiles
				ema08 = op.ema(8)
				ema20 = op.ema(20)
				ema50 = op.ema(50)
				ema200 = df['c'].ewm(200).mean()

				bande = op.bollinger_band(20)
				bande2 = op.bollinger_band(100)

				# Levels
				o2 = high_low.High_low(elt, count, 'D')
				hld = o2.high_low()
				    
				o3 = high_low.High_low(elt, count, 'W')
				hlw = o3.high_low()

				p1 = pivot_points.Pivot(elt, count, 'M')
				pvp = p1.pivot_calculation()

				swhl = swing_low_high.Swing_low_high(df)
				swing = swhl.swing_low_high_calc()

				op1 = sr.SR(elt, 100, 'D')
				support_resistance1 = op1.sr()

				# Indicateurs (1 classe par indicateur)
				i1 = indicators.Rsi(df, count, 9)
				rsi = i1.rsi_calculation()

				i2 = indicators.Candles_size(df, count, 2)
				candlesize = i2.candles_size_calc()
				cdz1 = candlesize[1][count - 1]
				cdz2 = candlesize[1][count - 11]

				print("valeur candles sz",candlesize[1][count - 1])
				print(candlesize[1][count - 21])

				ind = indicators.Stochastic(df, count, 15)
				sto = ind.sto_calculation()

				# Display
				border_down = df.l.min()
				border_up = df.h.max()
				rg = (border_up - border_down) * 0.05

				ax1.set_ylim(border_down - rg, border_up + rg)
				ax1.plot(df.c, '-', linewidth=0.5, c='grey')
				candlestick_ohlc(ax1, ohlc[1], width=2.6, colorup='orange', colordown='red')
				ax1.plot(bande2[0],linewidth=0.8,color='green')
				ax1.plot(bande2[1],linewidth=0.4,color='green')
				ax1.plot(bande2[2],linewidth=0.4,color='green')

				# Display bas et haut du jour, semaine
				ax1.plot([hld[0]] * count, '-', linewidth=0.75, color='grey')
				ax1.plot([hld[1]] * count, '--', linewidth=0.05, color='grey')
				ax1.plot([hld[2]] * count, '--', linewidth=0.05, color='grey')
				ax1.plot([hld[3]] * count, '-', linewidth=0.75, color='pink')
				ax1.plot([hld[4]] * count, '--', linewidth=0.05, color='pink')
				ax1.plot([hld[5]] * count, '--', linewidth=0.05, color='pink')

				ax1.plot([hlw[0]] * count, '-', linewidth=0.75, color='yellow')
				ax1.plot([hlw[1]] * count, '--', linewidth=0.05, color='yellow')
				ax1.plot([hlw[2]] * count, '--', linewidth=0.05, color='yellow')
				ax1.plot([hlw[3]] * count, '-', linewidth=0.75, color='orange')
				ax1.plot([hlw[4]] * count, '--', linewidth=0.05, color='orange')
				ax1.plot([hlw[5]] * count, '--', linewidth=0.05, color='orange')
				print('candlesize[1]: '+str(candlesize[1][0]))
				ax2.plot(candlesize[1], '-', color='pink')
				ax2.plot(candlesize[2][0], candlesize[2][1], '-')

				# Save figure
				try:
				    fig.savefig("C:/MK_analytics/" + paths + '/' + elt + '_' + g + '.png')
				except Exception as e:
				    print(e)
				print("C:/MK_analytics/" + paths + '/' + elt + '_' + g + '.png')

				plt.close(fig)
				i += 1


fnc(dossiers)
