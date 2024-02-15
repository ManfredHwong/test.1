import pandas as pd 
import numpy as np

# load excel data and convert to dataframe
trading_log = pd.read_csv("trading_log.csv")

# find out if there are any discrepancies between the fill size and the order size
trading_log['Discrepancy'] = np.where(trading_log['Order Size'] != trading_log['Fill Size'], 
              trading_log['Order Size'] - trading_log['Fill Size'], np.nan)

# find price difference between actual price and average price
trading_log['Price Difference'] =  np.select([ 
    (trading_log['Symbol'] == 'AAPL'),
    (trading_log['Symbol'] == 'MSFT'), 
    (trading_log['Symbol'] == 'GOOGL'), 
    (trading_log['Symbol'] == 'AMZN'), 
    (trading_log['Symbol'] == 'TSLA'), 
    (trading_log['Symbol'] == 'FB'), 
    (trading_log['Symbol'] == 'BRK.A'), 
    (trading_log['Symbol'] == 'V'), 
    (trading_log['Symbol'] == 'JPM'), 
    (trading_log['Symbol'] == 'JNJ')
], [(150 - trading_log['Price']), 
    (250 - trading_log['Price']), 
    (2700 - trading_log['Price']),
    (3100 - trading_log['Price']), 
    (700 - trading_log['Price']), 
    (200 - trading_log['Price']), 
    (350000 - trading_log['Price']), 
    (210 - trading_log['Price']), 
    (130 - trading_log['Price']), 
    (160 - trading_log['Price'])])

#############################################################################

# price discrepancy between traders & specific securities bought

# Trader A & AAPL
tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_aapl1 = tradera_aapl[~np.isnan(tradera_aapl)]
(np.average(tradera_aapl1))
# print(tradera_aapl1)

# Trader B & AAPL 
traderb_aapl = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_aapl1 = traderb_aapl[~np.isnan(traderb_aapl)]
(np.average(traderb_aapl1))

# Trader C & AAPL 
traderc_aapl = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_aapl1 = traderc_aapl[~np.isnan(traderc_aapl)]
(np.average(traderc_aapl1))

# Trader D & AAPL
traderd_aapl = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_aapl1 = traderd_aapl[~np.isnan(traderd_aapl)]
(np.average(traderd_aapl1))

# Trader A & MSFT 
tradera_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_msft1 = tradera_msft[~np.isnan(tradera_msft)]
(np.average(tradera_msft1))

# Trader B & MSFT 
traderb_msft = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_msft1 = traderb_msft[~np.isnan(traderb_msft)]
(np.average(traderb_msft1))

# Trader C & MSFT
traderc_msft = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_msft1 = traderc_msft[~np.isnan(traderc_msft)]
(np.average(traderc_msft1))

# Trader D & MSFT 
traderd_msft = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_msft1 = traderd_msft[~np.isnan(traderd_msft)]
(np.average(traderd_msft1))

# Trader A & GOOGL 
tradera_googl = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'GOOGL') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_googl1 = tradera_googl[~np.isnan(tradera_googl)]
(np.average(tradera_googl1)) 

# Trader B & GOOGL 
traderb_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'GOOGL')& 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_googl1 = traderb_googl[~np.isnan(traderb_googl)]
(np.average(traderb_googl1)) 

# Trader C & GOOGL 
traderc_googl = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'GOOGL') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_googl1 = traderc_googl[~np.isnan(traderc_googl)]
(np.average(traderc_googl1)) 

# Trader D & GOOGL 
traderd_googl = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'GOOGL') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_googl1 = traderd_googl[~np.isnan(traderd_googl)]
(np.average(traderd_googl1)) 

# Trader A & AMZN
tradera_amzn = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_amzn1 = tradera_amzn[~np.isnan(tradera_amzn)]
(np.average(tradera_amzn1)) 

# Trader B & AMZN
traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_amzn1 = traderb_amzn[~np.isnan(traderb_amzn)]
(np.average(traderb_amzn1)) 

# Trader C & AMZN
traderc_amzn = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_amzn1 = traderc_amzn[~np.isnan(traderc_amzn)]
(np.average(traderc_amzn1)) 

# Trader D & AMZN
traderd_amzn = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_amzn1 = traderd_amzn[~np.isnan(traderd_amzn)]
(np.average(traderd_amzn1)) 

# Trader A & TSLA
tradera_tsla = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_tsla1 = tradera_tsla[~np.isnan(tradera_tsla)]
(np.average(tradera_tsla1)) 

# Trader B & TSLA
traderb_tsla = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_tsla1 = traderb_tsla[~np.isnan(traderb_tsla)]
(np.average(traderb_tsla1)) 

# Trader C & TSLA
traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_tsla1 = traderc_tsla[~np.isnan(traderc_tsla)]
(np.average(traderc_tsla1)) 

# Trader D & TSLA
traderd_tsla = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_tsla1 = traderd_tsla[~np.isnan(traderd_tsla)]
(np.average(traderd_tsla1)) 

# Trader A & FB
tradera_fb = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_fb1 = tradera_fb[~np.isnan(tradera_fb)]
(np.average(tradera_fb1)) 

# Trader B & FB
traderb_fb = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_fb1 = traderb_fb[~np.isnan(traderb_fb)]
(np.average(traderb_fb1)) 

# Trader C & FB
traderc_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_fb1 = traderc_fb[~np.isnan(traderc_fb)]
(np.average(traderc_fb1)) 

# Trader D & FB
traderd_fb = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_fb1 = traderd_fb[~np.isnan(traderd_fb)]
(np.average(traderd_fb1)) 

# Trader A & BRK.A
tradera_brka = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_brka1 = tradera_brka[~np.isnan(tradera_brka)]
(np.average(tradera_brka1)) 

# Trader B & BRK.A
traderb_brka = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_brka1 = traderb_brka[~np.isnan(traderb_brka)]
(np.average(traderb_brka1)) 

# Trader C & BRK.A
traderc_brka = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_brka1 = traderc_brka[~np.isnan(traderc_brka)]
(np.average(traderc_brka1)) 

# Trader D & BRK.A
traderd_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_brka1 = traderd_brka[~np.isnan(traderd_brka)]
(np.average(traderd_brka1))  

# Trader A & V
tradera_v = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_v1 = tradera_v[~np.isnan(tradera_v)]
(np.average(tradera_v1)) 

# Trader B & V
traderb_v = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_v1 = traderb_v[~np.isnan(traderb_v)]
(np.average(traderb_v1)) 

# Trader C & V
traderc_v = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_v1 = traderc_v[~np.isnan(traderc_v)]
(np.average(traderc_v1)) 

# Trader D & V
traderd_v = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_v1 = traderd_v[~np.isnan(traderd_v)]
(np.average(traderd_v1)) 

# Trader A & JPM
tradera_jpm = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_jpm1 = tradera_jpm[~np.isnan(tradera_jpm)]
(np.average(tradera_jpm1)) 

# Trader B & JPM
traderb_jpm = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_jpm1 = traderb_jpm[~np.isnan(traderb_jpm)]
(np.average(traderb_jpm1)) 

# Trader C & JPM
traderc_jpm = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_jpm1 = traderc_jpm[~np.isnan(traderc_jpm)]
(np.average(traderc_jpm1)) 

# Trader D & JPM
traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_jpm1 = traderd_jpm[~np.isnan(traderd_jpm)]
(np.average(traderd_jpm1)) 

# Trader A & JNJ
tradera_jnj = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
tradera_jnj1 = tradera_jnj[~np.isnan(tradera_jnj)]
(np.average(tradera_jnj1)) 

# Trader B & JNJ
traderb_jnj = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderb_jnj1 = traderb_jnj[~np.isnan(traderb_jnj)]
(np.average(traderb_jnj1)) 

# Trader C & JNJ
traderc_jnj = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderc_jnj1 = traderc_jnj[~np.isnan(traderc_jnj)]
(np.average(traderc_jnj1)) 

# Trader D & JNJ
traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Buy'),
                        trading_log['Price'], np.nan)
traderd_jnj1 = traderd_jnj[~np.isnan(traderd_jnj)]
(np.average(traderd_jnj1)) 

# create dataframe of all average prices grouped by security & trader 
trader_security_buy = pd.DataFrame(np.array([[np.average(tradera_aapl1), np.average(traderb_aapl1), np.average(traderc_aapl1), np.average(traderd_aapl1)],
                                        [np.average(tradera_msft1), np.average(traderb_msft1), np.average(traderc_msft1), np.average(traderd_msft1)],
                                        [np.average(tradera_googl1), np.average(traderb_googl1), np.average(traderc_googl1), np.average(traderd_googl1)],
                                        [np.average(tradera_amzn1), np.average(traderb_amzn1), np.average(traderc_amzn1), np.average(traderd_amzn1)],
                                        [np.average(tradera_tsla1), np.average(traderb_tsla1), np.average(traderc_tsla1), np.average(traderd_tsla1)],
                                        [np.average(tradera_fb1), np.average(traderb_fb1), np.average(traderc_fb1), np.average(traderd_fb1)],
                                        [np.average(tradera_brka1), np.average(traderb_brka1), np.average(traderc_brka1), np.average(traderd_brka1)], 
                                        [np.average(tradera_v1), np.average(traderb_v1), np.average(traderc_v1), np.average(traderd_v1)], 
                                        [np.average(tradera_jpm1), np.average(traderb_jpm1), np.average(traderc_jpm1), np.average(traderd_jpm1)], 
                                        [np.average(tradera_jnj1), np.average(traderb_jnj1), np.average(traderc_jnj1), np.average(traderd_jnj1)]]),
                                        index=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.A', 'V', 'JPM', 'JNJ'], 
                                        columns=['Trader A', 'Trader B', 'Trader C', 'Trader D'])
# print(trader_security_buy)

#############################################################################

# price discrepancy between traders & specific securities sold

# Trader A & AAPL
s_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_aapl1 = s_tradera_aapl[~np.isnan(s_tradera_aapl)]
(np.average(s_tradera_aapl1))

# Trader B & AAPL 
s_traderb_aapl = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_aapl1 = s_traderb_aapl[~np.isnan(s_traderb_aapl)]
(np.average(s_traderb_aapl1))

# Trader C & AAPL 
s_traderc_aapl = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_aapl1 = s_traderc_aapl[~np.isnan(s_traderc_aapl)]
(np.average(s_traderc_aapl1))

# Trader D & AAPL
s_traderd_aapl = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'AAPL') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_aapl1 = s_traderd_aapl[~np.isnan(s_traderd_aapl)]
(np.average(s_traderd_aapl1))

# Trader A & MSFT 
s_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_msft1 = s_tradera_msft[~np.isnan(s_tradera_msft)]
(np.average(s_tradera_msft1))

# Trader B & MSFT 
s_traderb_msft = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_msft1 = s_traderb_msft[~np.isnan(s_traderb_msft)]
(np.average(s_traderb_msft1))

# Trader C & MSFT
s_traderc_msft = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_msft1 = s_traderc_msft[~np.isnan(s_traderc_msft)]
(np.average(s_traderc_msft1))

# Trader D & MSFT 
s_traderd_msft = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'MSFT') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_msft1 = s_traderd_msft[~np.isnan(s_traderd_msft)]
(np.average(s_traderd_msft1))

# Trader A & GOOGL 
s_tradera_googl = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'GOOGL') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_googl1 = s_tradera_googl[~np.isnan(s_tradera_googl)]
(np.average(s_tradera_googl1)) 

# Trader B & GOOGL 
s_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'GOOGL')& 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_googl1 = s_traderb_googl[~np.isnan(s_traderb_googl)]
(np.average(s_traderb_googl1)) 

# Trader C & GOOGL 
s_traderc_googl = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'GOOGL') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_googl1 = s_traderc_googl[~np.isnan(s_traderc_googl)]
(np.average(s_traderc_googl1)) 

# Trader D & GOOGL 
s_traderd_googl = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'GOOGL') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_googl1 = s_traderd_googl[~np.isnan(s_traderd_googl)]
(np.average(s_traderd_googl1)) 

# Trader A & AMZN
s_tradera_amzn = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_amzn1 = s_tradera_amzn[~np.isnan(s_tradera_amzn)]
(np.average(s_tradera_amzn1)) 

# Trader B & AMZN
s_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_amzn1 = s_traderb_amzn[~np.isnan(s_traderb_amzn)]
(np.average(s_traderb_amzn1)) 

# Trader C & AMZN
s_traderc_amzn = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_amzn1 = s_traderc_amzn[~np.isnan(s_traderc_amzn)]
(np.average(s_traderc_amzn1)) 

# Trader D & AMZN
s_traderd_amzn = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'AMZN') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_amzn1 = s_traderd_amzn[~np.isnan(s_traderd_amzn)]
(np.average(s_traderd_amzn1)) 

# Trader A & TSLA
s_tradera_tsla = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_tsla1 = s_tradera_tsla[~np.isnan(s_tradera_tsla)]
(np.average(s_tradera_tsla1)) 

# Trader B & TSLA
s_traderb_tsla = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_tsla1 = s_traderb_tsla[~np.isnan(s_traderb_tsla)]
(np.average(s_traderb_tsla1)) 

# Trader C & TSLA
s_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_tsla1 = s_traderc_tsla[~np.isnan(s_traderc_tsla)]
(np.average(s_traderc_tsla1)) 

# Trader D & TSLA
s_traderd_tsla = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'TSLA') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_tsla1 = s_traderd_tsla[~np.isnan(s_traderd_tsla)]
(np.average(s_traderd_tsla1)) 

# Trader A & FB
s_tradera_fb = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_fb1 = s_tradera_fb[~np.isnan(s_tradera_fb)]
(np.average(s_tradera_fb1)) 

# Trader B & FB
s_traderb_fb = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_fb1 = s_traderb_fb[~np.isnan(s_traderb_fb)]
(np.average(s_traderb_fb1)) 

# Trader C & FB
s_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_fb1 = s_traderc_fb[~np.isnan(s_traderc_fb)]
(np.average(s_traderc_fb1)) 

# Trader D & FB
s_traderd_fb = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'FB') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_fb1 = s_traderd_fb[~np.isnan(s_traderd_fb)]
(np.average(s_traderd_fb1)) 

# Trader A & BRK.A
s_tradera_brka = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_brka1 = s_tradera_brka[~np.isnan(s_tradera_brka)]
(np.average(s_tradera_brka1)) 

# Trader B & BRK.A
s_traderb_brka = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_brka1 = s_traderb_brka[~np.isnan(s_traderb_brka)]
(np.average(s_traderb_brka1)) 

# Trader C & BRK.A
s_traderc_brka = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_brka1 = s_traderc_brka[~np.isnan(s_traderc_brka)]
(np.average(s_traderc_brka1)) 

# Trader D & BRK.A
s_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'BRK.A') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_brka1 = s_traderd_brka[~np.isnan(s_traderd_brka)]
(np.average(s_traderd_brka1))  

# Trader A & V
s_tradera_v = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_v1 = s_tradera_v[~np.isnan(s_tradera_v)]
(np.average(s_tradera_v1)) 

# Trader B & V
s_traderb_v = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_v1 = s_traderb_v[~np.isnan(s_traderb_v)]
(np.average(s_traderb_v1)) 

# Trader C & V
s_traderc_v = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_v1 = s_traderc_v[~np.isnan(s_traderc_v)]
(np.average(s_traderc_v1)) 

# Trader D & V
s_traderd_v = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'V') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_v1 = s_traderd_v[~np.isnan(s_traderd_v)]
(np.average(s_traderd_v1)) 

# Trader A & JPM
s_tradera_jpm = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_jpm1 = s_tradera_jpm[~np.isnan(s_tradera_jpm)]
(np.average(s_tradera_jpm1)) 

# Trader B & JPM
s_traderb_jpm = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_jpm1 = s_traderb_jpm[~np.isnan(s_traderb_jpm)]
(np.average(s_traderb_jpm1)) 

# Trader C & JPM
s_traderc_jpm = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_jpm1 = s_traderc_jpm[~np.isnan(s_traderc_jpm)]
(np.average(s_traderc_jpm1)) 

# Trader D & JPM
s_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'JPM') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_jpm1 = s_traderd_jpm[~np.isnan(s_traderd_jpm)]
(np.average(s_traderd_jpm1)) 

# Trader A & JNJ
s_tradera_jnj = np.where((trading_log['Trader'] == 'Trader A') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_tradera_jnj1 = s_tradera_jnj[~np.isnan(s_tradera_jnj)]
(np.average(s_tradera_jnj1)) 

# Trader B & JNJ
s_traderb_jnj = np.where((trading_log['Trader'] == 'Trader B') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderb_jnj1 = s_traderb_jnj[~np.isnan(s_traderb_jnj)]
(np.average(s_traderb_jnj1)) 

# Trader C & JNJ
s_traderc_jnj = np.where((trading_log['Trader'] == 'Trader C') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderc_jnj1 = s_traderc_jnj[~np.isnan(s_traderc_jnj)]
(np.average(s_traderc_jnj1)) 

# Trader D & JNJ
s_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                        (trading_log['Symbol'] == 'JNJ') & 
                        (trading_log['Order Type'] == 'Sell'),
                        trading_log['Price'], np.nan)
s_traderd_jnj1 = s_traderd_jnj[~np.isnan(s_traderd_jnj)]
(np.average(s_traderd_jnj1)) 

# create dataframe of all average prices grouped by security & trader 
trader_security_sell = pd.DataFrame(np.array([[np.average(s_tradera_aapl1), np.average(s_traderb_aapl1), np.average(s_traderc_aapl1), np.average(s_traderd_aapl1)],
                                        [np.average(s_tradera_msft1), np.average(s_traderb_msft1), np.average(s_traderc_msft1), np.average(s_traderd_msft1)],
                                        [np.average(s_tradera_googl1), np.average(s_traderb_googl1), np.average(s_traderc_googl1), np.average(s_traderd_googl1)],
                                        [np.average(s_tradera_amzn1), np.average(s_traderb_amzn1), np.average(s_traderc_amzn1), np.average(s_traderd_amzn1)],
                                        [np.average(s_tradera_tsla1), np.average(s_traderb_tsla1), np.average(s_traderc_tsla1), np.average(s_traderd_tsla1)],
                                        [np.average(s_tradera_fb1), np.average(s_traderb_fb1), np.average(s_traderc_fb1), np.average(s_traderd_fb1)],
                                        [np.average(s_tradera_brka1), np.average(s_traderb_brka1), np.average(s_traderc_brka1), np.average(s_traderd_brka1)], 
                                        [np.average(s_tradera_v1), np.average(s_traderb_v1), np.average(s_traderc_v1), np.average(s_traderd_v1)], 
                                        [np.average(s_tradera_jpm1), np.average(s_traderb_jpm1), np.average(s_traderc_jpm1), np.average(s_traderd_jpm1)], 
                                        [np.average(s_tradera_jnj1), np.average(s_traderb_jnj1), np.average(s_traderc_jnj1), np.average(s_traderd_jnj1)]]),
                                        index=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.A', 'V', 'JPM', 'JNJ'], 
                                        columns=['Trader A', 'Trader B', 'Trader C', 'Trader D'])
# print(trader_security_sell)

##############################################################################

# Analyze trader total fill sizes per day grouped by security 

# Trader A & AAPL
f_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'AAPL'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_aapl1 = f_tradera_aapl[~np.isnan(f_tradera_aapl)]
(np.sum(f_tradera_aapl1))

# Trader B & AAPL
f_traderb_aapl = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'AAPL'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_aapl1 = f_traderb_aapl[~np.isnan(f_traderb_aapl)]
(np.sum(f_traderb_aapl1))

# Trader C & AAPL
f_traderc_aapl = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'AAPL'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_aapl1 = f_traderc_aapl[~np.isnan(f_traderc_aapl)]
(np.sum(f_traderc_aapl1))

# Trader D & AAPL
f_traderd_aapl = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'AAPL'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_aapl1 = f_traderd_aapl[~np.isnan(f_traderd_aapl)]
(np.sum(f_traderd_aapl1))

# Trader A & MSFT
f_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'MSFT'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_msft1 = f_tradera_msft[~np.isnan(f_tradera_msft)]
(np.sum(f_tradera_msft1))

# Trader B & MSFT
f_traderb_msft = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'MSFT'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_msft1 = f_traderb_msft[~np.isnan(f_traderb_msft)]
(np.sum(f_traderb_msft1)) 

# Trader C & MSFT
f_traderc_msft = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'MSFT'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_msft1 = f_traderc_msft[~np.isnan(f_traderc_msft)]
(np.sum(f_traderc_msft1)) 

# Trader D & MSFT
f_traderd_msft = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'MSFT'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_msft1 = f_traderd_msft[~np.isnan(f_traderd_msft)]
(np.sum(f_traderd_msft1)) 

# Trader A & GOOGL
f_tradera_googl = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'GOOGL'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_googl1 = f_tradera_googl[~np.isnan(f_tradera_googl)]
(np.sum(f_tradera_googl1))

# Trader B & GOOGL
f_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'GOOGL'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_googl1 = f_traderb_googl[~np.isnan(f_traderb_googl)]
(np.sum(f_traderb_googl1))

# Trader C & GOOGL
f_traderc_googl = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'GOOGL'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_googl1 = f_traderc_googl[~np.isnan(f_traderc_googl)]
(np.sum(f_traderc_googl1)) 

# Trader D & GOOGL
f_traderd_googl = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'GOOGL'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_googl1 = f_traderd_googl[~np.isnan(f_traderd_googl)]
(np.sum(f_traderd_googl1))

# Trader A & AMZN
f_tradera_amzn = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'AMZN'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_amzn1 = f_tradera_amzn[~np.isnan(f_tradera_amzn)]
(np.sum(f_tradera_amzn1))

# Trader B & AMZN
f_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'AMZN'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_amzn1 = f_traderb_amzn[~np.isnan(f_traderb_amzn)]
(np.sum(f_traderb_amzn1))

# Trader C & AMZN
f_traderc_amzn = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'AMZN'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_amzn1 = f_traderc_amzn[~np.isnan(f_traderc_amzn)]
(np.sum(f_traderc_amzn1))

# Trader D & AMZN
f_traderd_amzn = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'AMZN'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_amzn1 = f_traderd_amzn[~np.isnan(f_traderd_amzn)]
(np.sum(f_traderd_amzn1))

# Trader A & TSLA
f_tradera_tsla = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'TSLA'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_tsla1 = f_tradera_tsla[~np.isnan(f_tradera_tsla)]
(np.sum(f_tradera_tsla1)) 

# Trader B & TSLA
f_traderb_tsla = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'TSLA'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_tsla1 = f_traderb_tsla[~np.isnan(f_traderb_tsla)]
(np.sum(f_traderb_tsla1))

# Trader C & TSLA
f_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'TSLA'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_tsla1 = f_traderc_tsla[~np.isnan(f_traderc_tsla)]
(np.sum(f_traderc_tsla1))

# Trader D & TSLA
f_traderd_tsla = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'TSLA'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_tsla1 = f_traderd_tsla[~np.isnan(f_traderd_tsla)]
(np.sum(f_traderd_tsla1))

# Trader A & FB
f_tradera_fb = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'FB'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_fb1 = f_tradera_fb[~np.isnan(f_tradera_fb)]
(np.sum(f_tradera_fb1)) 

# Trader B & FB
f_traderb_fb = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'FB'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_fb1 = f_traderb_fb[~np.isnan(f_traderb_fb)]
(np.sum(f_traderb_fb1))

# Trader C & FB
f_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'FB'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_fb1 = f_traderc_fb[~np.isnan(f_traderc_fb)]
(np.sum(f_traderc_fb1))

# Trader D & FB
f_traderd_fb = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'FB'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_fb1 = f_traderd_fb[~np.isnan(f_traderd_fb)]
(np.sum(f_traderd_fb1)) 

# Trader A & BRK.A
f_tradera_brka = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'BRK.A'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_brka1 = f_tradera_brka[~np.isnan(f_tradera_brka)]
(np.sum(f_tradera_brka1)) 

# Trader B & BRK.A
f_traderb_brka = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'BRK.A'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_brka1 = f_traderb_brka[~np.isnan(f_traderb_brka)]
(np.sum(f_traderb_brka1))

# Trader C & BRK.A
f_traderc_brka = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'BRK.A'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_brka1 = f_traderc_brka[~np.isnan(f_traderc_brka)]
(np.sum(f_traderc_brka1))

# Trader D & BRK.A
f_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'BRK.A'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_brka1 = f_traderd_brka[~np.isnan(f_traderd_brka)]
(np.sum(f_traderd_brka1))

# Trader A & V
f_tradera_v = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'V'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_v1 = f_tradera_v[~np.isnan(f_tradera_v)]
(np.sum(f_tradera_v1))

# Trader B & V
f_traderb_v = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'V'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_v1 = f_traderb_v[~np.isnan(f_traderb_v)]
(np.sum(f_traderb_v1))

# Trader C & V
f_traderc_v = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'V'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_v1 = f_traderc_v[~np.isnan(f_traderc_v)]
(np.sum(f_traderc_v1)) 

# Trader D & V
f_traderd_v = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'V'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_v1 = f_traderd_v[~np.isnan(f_traderd_v)]
(np.sum(f_traderd_v1)) 

# Trader A & JPM
f_tradera_jpm = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'JPM'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_jpm1 = f_tradera_jpm[~np.isnan(f_tradera_jpm)]
(np.sum(f_tradera_jpm1)) 

# Trader B & JPM
f_traderb_jpm = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'JPM'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_jpm1 = f_traderb_jpm[~np.isnan(f_traderb_jpm)]
(np.sum(f_traderb_jpm1)) 

# Trader C & JPM
f_traderc_jpm = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'JPM'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_jpm1 = f_traderc_jpm[~np.isnan(f_traderc_jpm)]
(np.sum(f_traderc_jpm1)) 

# Trader D & JPM
f_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'JPM'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_jpm1 = f_traderd_jpm[~np.isnan(f_traderd_jpm)]
(np.sum(f_traderd_jpm1)) 

# Trader A & JNJ
f_tradera_jnj = np.where((trading_log['Trader'] == 'Trader A') & 
                          (trading_log['Symbol'] == 'JNJ'), 
                            trading_log['Fill Size'], np.nan)
f_tradera_jnj1 = f_tradera_jnj[~np.isnan(f_tradera_jnj)]
(np.sum(f_tradera_jnj1)) 

# Trader B & JNJ
f_traderb_jnj = np.where((trading_log['Trader'] == 'Trader B') & 
                          (trading_log['Symbol'] == 'JNJ'), 
                            trading_log['Fill Size'], np.nan)
f_traderb_jnj1 = f_traderb_jnj[~np.isnan(f_traderb_jnj)]
(np.sum(f_traderb_jnj1)) 

# Trader C & JNJ
f_traderc_jnj = np.where((trading_log['Trader'] == 'Trader C') & 
                          (trading_log['Symbol'] == 'JNJ'), 
                            trading_log['Fill Size'], np.nan)
f_traderc_jnj1 = f_traderc_jnj[~np.isnan(f_traderc_jnj)]
(np.sum(f_traderc_jnj1)) 

# Trader D & JNJ
f_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                          (trading_log['Symbol'] == 'JNJ'), 
                            trading_log['Fill Size'], np.nan)
f_traderd_jnj1 = f_traderd_jnj[~np.isnan(f_traderd_jnj)]
(np.sum(f_traderd_jnj1))

# create dataframe of sum of filled amount grouped by security & trader 
trader_security_fill = pd.DataFrame(np.array([[np.sum(f_tradera_aapl1), np.sum(f_traderb_aapl1), np.sum(f_traderc_aapl1), np.sum(f_traderd_aapl1)],
                                        [np.sum(f_tradera_msft1), np.sum(f_traderb_msft1), np.sum(f_traderc_msft1), np.sum(f_traderd_msft1)],
                                        [np.sum(f_tradera_googl1), np.sum(f_traderb_googl1), np.sum(f_traderc_googl1), np.sum(f_traderd_googl1)],
                                        [np.sum(f_tradera_amzn1), np.sum(f_traderb_amzn1), np.sum(f_traderc_amzn1), np.sum(f_traderd_amzn1)],
                                        [np.sum(f_tradera_tsla1), np.sum(f_traderb_tsla1), np.sum(f_traderc_tsla1), np.sum(f_traderd_tsla1)],
                                        [np.sum(f_tradera_fb1), np.sum(f_traderb_fb1), np.sum(f_traderc_fb1), np.sum(f_traderd_fb1)],
                                        [np.sum(f_tradera_brka1), np.sum(f_traderb_brka1), np.sum(f_traderc_brka1), np.sum(f_traderd_brka1)], 
                                        [np.sum(f_tradera_v1), np.sum(f_traderb_v1), np.sum(f_traderc_v1), np.sum(f_traderd_v1)], 
                                        [np.sum(f_tradera_jpm1), np.sum(f_traderb_jpm1), np.sum(f_traderc_jpm1), np.sum(f_traderd_jpm1)], 
                                        [np.sum(f_tradera_jnj1), np.sum(f_traderb_jnj1), np.sum(f_traderc_jnj1), np.sum(f_traderd_jnj1)]]),
                                        index=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.A', 'V', 'JPM', 'JNJ'], 
                                        columns=['Trader A', 'Trader B', 'Trader C', 'Trader D'])
# print(trader_security_fill)

############################################################################################################################################# 

# Exchange & Security vs Price (Buys)

# CME & AAPL
b_cme_aapl = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_aapl1 = b_cme_aapl[~np.isnan(b_cme_aapl)]
(np.average(b_cme_aapl1)) 

# LSE & AAPL
b_lse_aapl = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_aapl1 = b_lse_aapl[~np.isnan(b_lse_aapl)]
(np.average(b_lse_aapl1)) 

# NYSE & AAPL
b_nyse_aapl = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_aapl1 = b_nyse_aapl[~np.isnan(b_nyse_aapl)]
(np.average(b_nyse_aapl1)) 

# NASDAQ & AAPL
b_nasdaq_aapl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_aapl1 = b_nasdaq_aapl[~np.isnan(b_nasdaq_aapl)]
(np.average(b_nasdaq_aapl1)) 

# CME & MSFT
b_cme_msft = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_msft1 = b_cme_msft[~np.isnan(b_cme_msft)]
(np.average(b_cme_msft1)) 

# LSE & MSFT
b_lse_msft = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_msft1 = b_lse_msft[~np.isnan(b_lse_msft)]
(np.average(b_lse_msft1)) 

# NYSE & MSFT 
b_nyse_msft = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_msft1 = b_nyse_msft[~np.isnan(b_nyse_msft)]
(np.average(b_nyse_msft1)) 

# NASDAQ & MSFT
b_nasdaq_msft = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_msft1 = b_nasdaq_msft[~np.isnan(b_nasdaq_msft)]
(np.average(b_nasdaq_msft1))

# CME & GOOGL
b_cme_googl = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_googl1 = b_cme_googl[~np.isnan(b_cme_googl)]
(np.average(b_cme_googl1)) 

# LSE & GOOGL
b_lse_googl = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_googl1 = b_lse_googl[~np.isnan(b_lse_googl)]
(np.average(b_lse_googl1)) 

# NYSE & GOOGL
b_nyse_googl = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_googl1 = b_nyse_googl[~np.isnan(b_nyse_googl)]
(np.average(b_nyse_googl1)) 

# NASDAQ & GOOGL
b_nasdaq_googl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_googl1 = b_nasdaq_googl[~np.isnan(b_nasdaq_googl)]
(np.average(b_nasdaq_googl1)) 

# CME & AMZN
b_cme_amzn = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_amzn1 = b_cme_amzn[~np.isnan(b_cme_amzn)]
(np.average(b_cme_amzn1)) 

# LSE & AMZN
b_lse_amzn = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_amzn1 = b_lse_amzn[~np.isnan(b_lse_amzn)]
(np.average(b_lse_amzn1)) 

# NYSE & AMZN
b_nyse_amzn = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_amzn1 = b_nyse_amzn[~np.isnan(b_nyse_amzn)]
(np.average(b_nyse_amzn1)) 

# NASDAQ & AMZN
b_nasdaq_amzn = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_amzn1 = b_nasdaq_amzn[~np.isnan(b_nasdaq_amzn)]
(np.average(b_nasdaq_amzn1)) 

# CME & TSLA
b_cme_tsla = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_tsla1 = b_cme_tsla[~np.isnan(b_cme_tsla)]
(np.average(b_cme_tsla1)) 

# LSE & TSLA
b_lse_tsla = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_tsla1 = b_lse_tsla[~np.isnan(b_lse_tsla)]
(np.average(b_lse_tsla1)) 

# NYSE & TSLA
b_nyse_tsla = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_tsla1 = b_nyse_tsla[~np.isnan(b_nyse_tsla)]
(np.average(b_nyse_tsla1)) 

# NASDAQ & TSLA
b_nasdaq_tsla = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_tsla1 = b_nasdaq_tsla[~np.isnan(b_nasdaq_tsla)]
(np.average(b_nasdaq_tsla1))

# CME & FB
b_cme_fb = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_fb1 = b_cme_fb[~np.isnan(b_cme_fb)]
(np.average(b_cme_fb1)) 

# LSE & FB
b_lse_fb = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_fb1 = b_lse_fb[~np.isnan(b_lse_fb)]
(np.average(b_lse_fb1)) 

# NYSE & FB
b_nyse_fb = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_fb1 = b_nyse_fb[~np.isnan(b_nyse_fb)]
(np.average(b_nyse_fb1)) 

# NASDAQ & FB
b_nasdaq_fb = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_fb1 = b_nasdaq_fb[~np.isnan(b_nasdaq_fb)]
(np.average(b_nasdaq_fb1)) 

# CME & BRK.A
b_cme_brka = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_brka1 = b_cme_brka[~np.isnan(b_cme_brka)]
(np.average(b_cme_brka1)) 

# LSE & BRK.A
b_lse_brka = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_brka1 = b_lse_brka[~np.isnan(b_lse_brka)]
(np.average(b_lse_brka1)) 

# NYSE & BRK.A
b_nyse_brka = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_brka1 = b_nyse_brka[~np.isnan(b_nyse_brka)]
(np.average(b_nyse_brka1)) 

# NASDAQ & BRK.A
b_nasdaq_brka = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_brka1 = b_nasdaq_brka[~np.isnan(b_nasdaq_brka)]
(np.average(b_nasdaq_brka1))

# CME & V
b_cme_v = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_v1 = b_cme_v[~np.isnan(b_cme_v)]
(np.average(b_cme_v1)) 

# LSE & V
b_lse_v = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_v1 = b_lse_v[~np.isnan(b_lse_v)]
(np.average(b_lse_v1)) 

# NYSE & V
b_nyse_v = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_v1 = b_nyse_v[~np.isnan(b_nyse_v)]
(np.average(b_nyse_v1)) 

# NASDAQ & V
b_nasdaq_v = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_v1 = b_nasdaq_v[~np.isnan(b_nasdaq_v)]
(np.average(b_nasdaq_v1)) 

# CME & JPM
b_cme_jpm = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_jpm1 = b_cme_jpm[~np.isnan(b_cme_jpm)]
(np.average(b_cme_jpm1)) 

# LSE & JPM
b_lse_jpm = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_jpm1 = b_lse_jpm[~np.isnan(b_lse_jpm)]
(np.average(b_lse_jpm1)) 

# NYSE & JPM
b_nyse_jpm = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_jpm1 = b_nyse_jpm[~np.isnan(b_nyse_jpm)]
(np.average(b_nyse_jpm1)) 

# NASDAQ & JPM
b_nasdaq_jpm = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_jpm1 = b_nasdaq_jpm[~np.isnan(b_nasdaq_jpm)]
(np.average(b_nasdaq_jpm1))

# CME & JNJ
b_cme_jnj = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_cme_jnj1 = b_cme_jnj[~np.isnan(b_cme_jnj)]
(np.average(b_cme_jnj1)) 

# LSE & JNJ
b_lse_jnj = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_lse_jnj1 = b_lse_jnj[~np.isnan(b_lse_jnj)]
(np.average(b_lse_jnj1)) 

# NYSE & JNJ
b_nyse_jnj = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nyse_jnj1 = b_nyse_jnj[~np.isnan(b_nyse_jnj)]
(np.average(b_nyse_jnj1)) 

# NASDAQ & JNJ
b_nasdaq_jnj = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Buy'), 
                      trading_log['Price'], np.nan) 
b_nasdaq_jnj1 = b_nasdaq_jnj[~np.isnan(b_nasdaq_jnj)]
(np.average(b_nasdaq_jnj1))

exchange_security_buy = pd.DataFrame(np.array([[np.average(b_cme_aapl1), np.average(b_lse_aapl1), np.average(b_nyse_aapl1), np.average(b_nasdaq_aapl1)],
                                        [np.average(b_cme_msft1), np.average(b_lse_msft1), np.average(b_nyse_msft1), np.average(b_nasdaq_msft1)],
                                        [np.average(b_cme_googl1), np.average(b_lse_googl1), np.average(b_nyse_googl1), np.average(b_nasdaq_googl1)],
                                        [np.average(b_cme_amzn1), np.average(b_lse_amzn1), np.average(b_nyse_amzn1), np.average(b_nasdaq_amzn1)],
                                        [np.average(b_cme_tsla1), np.average(b_lse_tsla1), np.average(b_nyse_tsla1), np.average(b_nasdaq_tsla1)],
                                        [np.average(b_cme_fb1), np.average(b_lse_fb1), np.average(b_nyse_fb1), np.average(b_nasdaq_fb1)],
                                        [np.average(b_cme_brka1), np.average(b_lse_brka1), np.average(b_nyse_brka1), np.average(b_nasdaq_brka1)], 
                                        [np.average(b_cme_v1), np.average(b_lse_v1), np.average(b_nyse_v1), np.average(b_nasdaq_v1)], 
                                        [np.average(b_cme_jpm1), np.average(b_lse_jpm1), np.average(b_nyse_jpm1), np.average(b_nasdaq_jpm1)], 
                                        [np.average(b_cme_jnj1), np.average(b_lse_jnj1), np.average(b_nyse_jnj1), np.average(b_nasdaq_jnj1)]]),
                                        index=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.A', 'V', 'JPM', 'JNJ'], 
                                        columns=['CME', 'LSE', 'NYSE', 'NASDAQ'])
# print(exchange_security_buy)

###################################################################################################################################################

# Exchange & Security vs Price (Sells)

# CME & AAPL
s_cme_aapl = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_aapl1 = s_cme_aapl[~np.isnan(s_cme_aapl)]
(np.average(s_cme_aapl1)) 

# LSE & AAPL
s_lse_aapl = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_aapl1 = s_lse_aapl[~np.isnan(s_lse_aapl)]
(np.average(s_lse_aapl1)) 

# NYSE & AAPL
s_nyse_aapl = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_aapl1 = s_nyse_aapl[~np.isnan(s_nyse_aapl)]
(np.average(s_nyse_aapl1)) 

# NASDAQ & AAPL
s_nasdaq_aapl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'AAPL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_aapl1 = s_nasdaq_aapl[~np.isnan(s_nasdaq_aapl)]
(np.average(s_nasdaq_aapl1)) 

# CME & MSFT
s_cme_msft = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_msft1 = s_cme_msft[~np.isnan(s_cme_msft)]
(np.average(s_cme_msft1)) 

# LSE & MSFT
s_lse_msft = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_msft1 = s_lse_msft[~np.isnan(s_lse_msft)]
(np.average(s_lse_msft1)) 

# NYSE & MSFT 
s_nyse_msft = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_msft1 = s_nyse_msft[~np.isnan(s_nyse_msft)]
(np.average(s_nyse_msft1)) 

# NASDAQ & MSFT
s_nasdaq_msft = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'MSFT') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_msft1 = s_nasdaq_msft[~np.isnan(s_nasdaq_msft)]
(np.average(s_nasdaq_msft1))

# CME & GOOGL
s_cme_googl = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_googl1 = s_cme_googl[~np.isnan(s_cme_googl)]
(np.average(s_cme_googl1)) 

# LSE & GOOGL
s_lse_googl = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_googl1 = s_lse_googl[~np.isnan(s_lse_googl)]
(np.average(s_lse_googl1)) 

# NYSE & GOOGL
s_nyse_googl = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_googl1 = s_nyse_googl[~np.isnan(s_nyse_googl)]
(np.average(s_nyse_googl1)) 

# NASDAQ & GOOGL
s_nasdaq_googl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'GOOGL') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_googl1 = s_nasdaq_googl[~np.isnan(s_nasdaq_googl)]
(np.average(s_nasdaq_googl1)) 

# CME & AMZN
s_cme_amzn = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_amzn1 = s_cme_amzn[~np.isnan(s_cme_amzn)]
(np.average(s_cme_amzn1)) 

# LSE & AMZN
s_lse_amzn = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_amzn1 = s_lse_amzn[~np.isnan(s_lse_amzn)]
(np.average(s_lse_amzn1)) 

# NYSE & AMZN
s_nyse_amzn = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_amzn1 = s_nyse_amzn[~np.isnan(s_nyse_amzn)]
(np.average(s_nyse_amzn1)) 

# NASDAQ & AMZN
s_nasdaq_amzn = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'AMZN') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_amzn1 = s_nasdaq_amzn[~np.isnan(s_nasdaq_amzn)]
(np.average(s_nasdaq_amzn1)) 

# CME & TSLA
s_cme_tsla = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_tsla1 = s_cme_tsla[~np.isnan(s_cme_tsla)]
(np.average(s_cme_tsla1)) 

# LSE & TSLA
s_lse_tsla = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_tsla1 = s_lse_tsla[~np.isnan(s_lse_tsla)]
(np.average(s_lse_tsla1)) 

# NYSE & TSLA
s_nyse_tsla = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_tsla1 = s_nyse_tsla[~np.isnan(s_nyse_tsla)]
(np.average(s_nyse_tsla1)) 

# NASDAQ & TSLA
s_nasdaq_tsla = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'TSLA') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_tsla1 = s_nasdaq_tsla[~np.isnan(s_nasdaq_tsla)]
(np.average(s_nasdaq_tsla1))

# CME & FB
s_cme_fb = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_fb1 = s_cme_fb[~np.isnan(s_cme_fb)]
(np.average(s_cme_fb1)) 

# LSE & FB
s_lse_fb = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_fb1 = s_lse_fb[~np.isnan(s_lse_fb)]
(np.average(s_lse_fb1)) 

# NYSE & FB
s_nyse_fb = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_fb1 = s_nyse_fb[~np.isnan(s_nyse_fb)]
(np.average(s_nyse_fb1)) 

# NASDAQ & FB
s_nasdaq_fb = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'FB') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_fb1 = s_nasdaq_fb[~np.isnan(s_nasdaq_fb)]
(np.average(s_nasdaq_fb1)) 

# CME & BRK.A
s_cme_brka = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_brka1 = s_cme_brka[~np.isnan(s_cme_brka)]
(np.average(s_cme_brka1)) 

# LSE & BRK.A
s_lse_brka = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_brka1 = s_lse_brka[~np.isnan(s_lse_brka)]
(np.average(s_lse_brka1)) 

# NYSE & BRK.A
s_nyse_brka = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_brka1 = s_nyse_brka[~np.isnan(s_nyse_brka)]
(np.average(s_nyse_brka1)) 

# NASDAQ & BRK.A
s_nasdaq_brka = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'BRK.A') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_brka1 = s_nasdaq_brka[~np.isnan(s_nasdaq_brka)]
(np.average(s_nasdaq_brka1))

# CME & V
s_cme_v = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_v1 = s_cme_v[~np.isnan(s_cme_v)]
(np.average(s_cme_v1)) 

# LSE & V
s_lse_v = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_v1 = s_lse_v[~np.isnan(s_lse_v)]
(np.average(s_lse_v1)) 

# NYSE & V
s_nyse_v = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_v1 = s_nyse_v[~np.isnan(s_nyse_v)]
(np.average(s_nyse_v1)) 

# NASDAQ & V
s_nasdaq_v = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'V') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_v1 = s_nasdaq_v[~np.isnan(s_nasdaq_v)]
(np.average(s_nasdaq_v1)) 

# CME & JPM
s_cme_jpm = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_jpm1 = s_cme_jpm[~np.isnan(s_cme_jpm)]
(np.average(s_cme_jpm1)) 

# LSE & JPM
s_lse_jpm = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_jpm1 = s_lse_jpm[~np.isnan(s_lse_jpm)]
(np.average(s_lse_jpm1)) 

# NYSE & JPM
s_nyse_jpm = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_jpm1 = s_nyse_jpm[~np.isnan(s_nyse_jpm)]
(np.average(s_nyse_jpm1)) 

# NASDAQ & JPM
s_nasdaq_jpm = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'JPM') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_jpm1 = s_nasdaq_jpm[~np.isnan(s_nasdaq_jpm)]
(np.average(s_nasdaq_jpm1))

# CME & JNJ
s_cme_jnj = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_cme_jnj1 = s_cme_jnj[~np.isnan(s_cme_jnj)]
(np.average(s_cme_jnj1)) 

# LSE & JNJ
s_lse_jnj = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_lse_jnj1 = s_lse_jnj[~np.isnan(s_lse_jnj)]
(np.average(s_lse_jnj1)) 

# NYSE & JNJ
s_nyse_jnj = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nyse_jnj1 = s_nyse_jnj[~np.isnan(s_nyse_jnj)]
(np.average(s_nyse_jnj1)) 

# NASDAQ & JNJ
s_nasdaq_jnj = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'JNJ') & 
                      (trading_log['Order Type'] == 'Sell'), 
                      trading_log['Price'], np.nan) 
s_nasdaq_jnj1 = s_nasdaq_jnj[~np.isnan(s_nasdaq_jnj)]
(np.average(s_nasdaq_jnj1))

exchange_security_sell = pd.DataFrame(np.array([[np.average(s_cme_aapl1), np.average(s_lse_aapl1), np.average(s_nyse_aapl1), np.average(s_nasdaq_aapl1)],
                                        [np.average(s_cme_msft1), np.average(s_lse_msft1), np.average(s_nyse_msft1), np.average(s_nasdaq_msft1)],
                                        [np.average(s_cme_googl1), np.average(s_lse_googl1), np.average(s_nyse_googl1), np.average(s_nasdaq_googl1)],
                                        [np.average(s_cme_amzn1), np.average(s_lse_amzn1), np.average(s_nyse_amzn1), np.average(s_nasdaq_amzn1)],
                                        [np.average(s_cme_tsla1), np.average(s_lse_tsla1), np.average(s_nyse_tsla1), np.average(s_nasdaq_tsla1)],
                                        [np.average(s_cme_fb1), np.average(s_lse_fb1), np.average(s_nyse_fb1), np.average(s_nasdaq_fb1)],
                                        [np.average(s_cme_brka1), np.average(s_lse_brka1), np.average(s_nyse_brka1), np.average(s_nasdaq_brka1)], 
                                        [np.average(s_cme_v1), np.average(s_lse_v1), np.average(s_nyse_v1), np.average(s_nasdaq_v1)], 
                                        [np.average(s_cme_jpm1), np.average(s_lse_jpm1), np.average(s_nyse_jpm1), np.average(s_nasdaq_jpm1)], 
                                        [np.average(s_cme_jnj1), np.average(s_lse_jnj1), np.average(s_nyse_jnj1), np.average(s_nasdaq_jnj1)]]),
                                        index=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.A', 'V', 'JPM', 'JNJ'], 
                                        columns=['CME', 'LSE', 'NYSE', 'NASDAQ'])
# print(exchange_security_sell)

########################################################################################################################################################## 

# Exchange & Security vs Volume (Fills)

# CME & AAPL
v_cme_aapl = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'AAPL'), 
                      trading_log['Fill Size'], np.nan) 
v_cme_aapl1 = v_cme_aapl[~np.isnan(v_cme_aapl)]
(np.sum(v_cme_aapl1)) 

# LSE & AAPL
v_lse_aapl = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'AAPL'),
                      trading_log['Fill Size'], np.nan) 
v_lse_aapl1 = v_lse_aapl[~np.isnan(v_lse_aapl)]
(np.sum(v_lse_aapl1)) 

# NYSE & AAPL
v_nyse_aapl = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'AAPL'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_aapl1 = v_nyse_aapl[~np.isnan(v_nyse_aapl)]
(np.sum(v_nyse_aapl1)) 

# NASDAQ & AAPL
v_nasdaq_aapl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'AAPL'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_aapl1 = v_nasdaq_aapl[~np.isnan(v_nasdaq_aapl)]
(np.sum(v_nasdaq_aapl1)) 

# CME & MSFT
v_cme_msft = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'MSFT'),
                      trading_log['Fill Size'], np.nan) 
v_cme_msft1 = v_cme_msft[~np.isnan(v_cme_msft)]
(np.sum(v_cme_msft1)) 

# LSE & MSFT
v_lse_msft = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'MSFT'),
                      trading_log['Fill Size'], np.nan) 
v_lse_msft1 = v_lse_msft[~np.isnan(v_lse_msft)]
(np.sum(v_lse_msft1)) 

# NYSE & MSFT 
v_nyse_msft = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'MSFT'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_msft1 = v_nyse_msft[~np.isnan(v_nyse_msft)]
(np.sum(v_nyse_msft1)) 

# NASDAQ & MSFT
v_nasdaq_msft = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'MSFT'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_msft1 = v_nasdaq_msft[~np.isnan(v_nasdaq_msft)]
(np.sum(v_nasdaq_msft1))

# CME & GOOGL
v_cme_googl = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'GOOGL'),
                      trading_log['Fill Size'], np.nan) 
v_cme_googl1 = v_cme_googl[~np.isnan(v_cme_googl)]
(np.sum(v_cme_googl1)) 

# LSE & GOOGL
v_lse_googl = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'GOOGL'),
                      trading_log['Fill Size'], np.nan) 
v_lse_googl1 = v_lse_googl[~np.isnan(v_lse_googl)]
(np.sum(v_lse_googl1)) 

# NYSE & GOOGL
v_nyse_googl = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'GOOGL'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_googl1 = v_nyse_googl[~np.isnan(v_nyse_googl)]
(np.sum(v_nyse_googl1)) 

# NASDAQ & GOOGL
v_nasdaq_googl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'GOOGL'), 
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_googl1 = v_nasdaq_googl[~np.isnan(v_nasdaq_googl)]
(np.sum(v_nasdaq_googl1)) 

# CME & AMZN
v_cme_amzn = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'AMZN'),
                      trading_log['Fill Size'], np.nan) 
v_cme_amzn1 = v_cme_amzn[~np.isnan(v_cme_amzn)]
(np.sum(v_cme_amzn1)) 

# LSE & AMZN
v_lse_amzn = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'AMZN'),
                      trading_log['Fill Size'], np.nan) 
v_lse_amzn1 = v_lse_amzn[~np.isnan(v_lse_amzn)]
(np.sum(v_lse_amzn1)) 

# NYSE & AMZN
v_nyse_amzn = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'AMZN'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_amzn1 = v_nyse_amzn[~np.isnan(v_nyse_amzn)]
(np.sum(v_nyse_amzn1)) 

# NASDAQ & AMZN
v_nasdaq_amzn = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'AMZN'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_amzn1 = v_nasdaq_amzn[~np.isnan(v_nasdaq_amzn)]
(np.sum(v_nasdaq_amzn1)) 

# CME & TSLA
v_cme_tsla = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'TSLA'),
                      trading_log['Fill Size'], np.nan) 
v_cme_tsla1 = v_cme_tsla[~np.isnan(v_cme_tsla)]
(np.sum(v_cme_tsla1)) 

# LSE & TSLA
v_lse_tsla = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'TSLA'), 
                      trading_log['Fill Size'], np.nan) 
v_lse_tsla1 = v_lse_tsla[~np.isnan(v_lse_tsla)]
(np.sum(v_lse_tsla1)) 

# NYSE & TSLA
v_nyse_tsla = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'TSLA'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_tsla1 = v_nyse_tsla[~np.isnan(v_nyse_tsla)]
(np.sum(v_nyse_tsla1)) 

# NASDAQ & TSLA
v_nasdaq_tsla = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'TSLA'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_tsla1 = v_nasdaq_tsla[~np.isnan(v_nasdaq_tsla)]
(np.sum(v_nasdaq_tsla1))

# CME & FB
v_cme_fb = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'FB'),
                      trading_log['Fill Size'], np.nan) 
v_cme_fb1 = v_cme_fb[~np.isnan(v_cme_fb)]
(np.sum(v_cme_fb1)) 

# LSE & FB
v_lse_fb = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'FB'),
                      trading_log['Fill Size'], np.nan) 
v_lse_fb1 = v_lse_fb[~np.isnan(v_lse_fb)]
(np.sum(v_lse_fb1)) 

# NYSE & FB
v_nyse_fb = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'FB'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_fb1 = v_nyse_fb[~np.isnan(v_nyse_fb)]
(np.sum(v_nyse_fb1)) 

# NASDAQ & FB
v_nasdaq_fb = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'FB'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_fb1 = v_nasdaq_fb[~np.isnan(v_nasdaq_fb)]
(np.sum(v_nasdaq_fb1)) 

# CME & BRK.A
v_cme_brka = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'BRK.A'), 
                      trading_log['Fill Size'], np.nan) 
v_cme_brka1 = v_cme_brka[~np.isnan(v_cme_brka)]
(np.sum(v_cme_brka1)) 

# LSE & BRK.A
v_lse_brka = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'BRK.A'),
                      trading_log['Fill Size'], np.nan) 
v_lse_brka1 = v_lse_brka[~np.isnan(v_lse_brka)]
(np.sum(v_lse_brka1)) 

# NYSE & BRK.A
v_nyse_brka = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'BRK.A'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_brka1 = v_nyse_brka[~np.isnan(v_nyse_brka)]
(np.sum(v_nyse_brka1)) 

# NASDAQ & BRK.A
v_nasdaq_brka = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'BRK.A'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_brka1 = v_nasdaq_brka[~np.isnan(v_nasdaq_brka)]
(np.sum(v_nasdaq_brka1))

# CME & V
v_cme_v = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'V'),
                      trading_log['Fill Size'], np.nan) 
v_cme_v1 = v_cme_v[~np.isnan(v_cme_v)]
(np.sum(v_cme_v1)) 

# LSE & V
v_lse_v = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'V'),
                      trading_log['Fill Size'], np.nan) 
v_lse_v1 = v_lse_v[~np.isnan(v_lse_v)]
(np.sum(v_lse_v1)) 

# NYSE & V
v_nyse_v = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'V'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_v1 = v_nyse_v[~np.isnan(v_nyse_v)]
(np.sum(v_nyse_v1)) 

# NASDAQ & V
v_nasdaq_v = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'V'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_v1 = v_nasdaq_v[~np.isnan(v_nasdaq_v)]
(np.sum(v_nasdaq_v1)) 

# CME & JPM
v_cme_jpm = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'JPM'),
                      trading_log['Fill Size'], np.nan) 
v_cme_jpm1 = v_cme_jpm[~np.isnan(v_cme_jpm)]
(np.sum(v_cme_jpm1)) 

# LSE & JPM
v_lse_jpm = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'JPM'),
                      trading_log['Fill Size'], np.nan) 
v_lse_jpm1 = v_lse_jpm[~np.isnan(v_lse_jpm)]
(np.sum(v_lse_jpm1)) 

# NYSE & JPM
v_nyse_jpm = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'JPM'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_jpm1 = v_nyse_jpm[~np.isnan(v_nyse_jpm)]
(np.sum(v_nyse_jpm1)) 

# NASDAQ & JPM
v_nasdaq_jpm = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'JPM'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_jpm1 = v_nasdaq_jpm[~np.isnan(v_nasdaq_jpm)]
(np.sum(v_nasdaq_jpm1))

# CME & JNJ
v_cme_jnj = np.where((trading_log['Exchange'] == 'CME') & 
                      (trading_log['Symbol'] == 'JNJ'),
                      trading_log['Fill Size'], np.nan) 
v_cme_jnj1 = v_cme_jnj[~np.isnan(v_cme_jnj)]
(np.sum(v_cme_jnj1)) 

# LSE & JNJ
v_lse_jnj = np.where((trading_log['Exchange'] == 'LSE') & 
                      (trading_log['Symbol'] == 'JNJ'),
                      trading_log['Fill Size'], np.nan) 
v_lse_jnj1 = v_lse_jnj[~np.isnan(v_lse_jnj)]
(np.sum(v_lse_jnj1)) 

# NYSE & JNJ
v_nyse_jnj = np.where((trading_log['Exchange'] == 'NYSE') & 
                      (trading_log['Symbol'] == 'JNJ'),
                      trading_log['Fill Size'], np.nan) 
v_nyse_jnj1 = v_nyse_jnj[~np.isnan(v_nyse_jnj)]
(np.sum(v_nyse_jnj1)) 

# NASDAQ & JNJ
v_nasdaq_jnj = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                      (trading_log['Symbol'] == 'JNJ'),
                      trading_log['Fill Size'], np.nan) 
v_nasdaq_jnj1 = v_nasdaq_jnj[~np.isnan(v_nasdaq_jnj)]
(np.sum(v_nasdaq_jnj1))

exchange_security_volume = pd.DataFrame(np.array([[np.sum(v_cme_aapl1), np.sum(v_lse_aapl1), np.sum(v_nyse_aapl1), np.sum(v_nasdaq_aapl1)],
                                        [np.sum(v_cme_msft1), np.sum(v_lse_msft1), np.sum(v_nyse_msft1), np.sum(v_nasdaq_msft1)],
                                        [np.sum(v_cme_googl1), np.sum(v_lse_googl1), np.sum(v_nyse_googl1), np.sum(v_nasdaq_googl1)],
                                        [np.sum(v_cme_amzn1), np.sum(v_lse_amzn1), np.sum(v_nyse_amzn1), np.sum(v_nasdaq_amzn1)],
                                        [np.sum(v_cme_tsla1), np.sum(v_lse_tsla1), np.sum(v_nyse_tsla1), np.sum(v_nasdaq_tsla1)],
                                        [np.sum(v_cme_fb1), np.sum(v_lse_fb1), np.sum(v_nyse_fb1), np.sum(v_nasdaq_fb1)],
                                        [np.sum(v_cme_brka1), np.sum(v_lse_brka1), np.sum(v_nyse_brka1), np.sum(v_nasdaq_brka1)], 
                                        [np.sum(v_cme_v1), np.sum(v_lse_v1), np.sum(v_nyse_v1), np.sum(v_nasdaq_v1)], 
                                        [np.sum(v_cme_jpm1), np.sum(v_lse_jpm1), np.sum(v_nyse_jpm1), np.sum(v_nasdaq_jpm1)], 
                                        [np.sum(v_cme_jnj1), np.sum(v_lse_jnj1), np.sum(v_nyse_jnj1), np.sum(v_nasdaq_jnj1)]]),
                                        index=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.A', 'V', 'JPM', 'JNJ'], 
                                        columns=['CME', 'LSE', 'NYSE', 'NASDAQ'])
# print(exchange_security_volume)

###############################################################################################################################

# Analyze trades when in preferred security & volume vs not in preferred volume

# Trader A, AAPL, >= 100 & <= 500 (Buys)
b_pref_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'AAPL') & 
                             (trading_log['Order Size'] >= 100) & 
                             (trading_log['Order Size'] <= 500) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_tradera_aapl1 = b_pref_tradera_aapl[~np.isnan(b_pref_tradera_aapl)]
# print(np.average(b_pref_tradera_aapl1))

# Trader A, AAPL, < 100 OR > 500 (Buys)
b_npref_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'AAPL') & 
                             ((trading_log['Order Size'] < 100) |
                             (trading_log['Order Size'] > 500)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_tradera_aapl1 = b_npref_tradera_aapl[~np.isnan(b_npref_tradera_aapl)]
# print(np.average(b_npref_tradera_aapl1))

# Trader A, AAPL, >= 100 & <= 500 (Sells)
s_pref_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'AAPL') & 
                             (trading_log['Order Size'] >= 100) & 
                             (trading_log['Order Size'] <= 500) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_tradera_aapl1 = s_pref_tradera_aapl[~np.isnan(s_pref_tradera_aapl)]
# print(np.average(s_pref_tradera_aapl1))

# Trader A, AAPL, < 100 OR > 500 (Sells)
s_npref_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'AAPL') & 
                             ((trading_log['Order Size'] < 100) |
                             (trading_log['Order Size'] > 500)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_tradera_aapl1 = s_npref_tradera_aapl[~np.isnan(s_npref_tradera_aapl)]
# print(np.average(s_npref_tradera_aapl1))

###

# Trader A, MSFT, >= 100 & <= 500 (Buys)
b_pref_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'MSFT') & 
                             (trading_log['Order Size'] >= 100) & 
                             (trading_log['Order Size'] <= 500) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_tradera_msft1 = b_pref_tradera_msft[~np.isnan(b_pref_tradera_msft)]
# print(np.average(b_pref_tradera_msft1))

# Trader A, MSFT, < 100 OR > 500 (Buys)
b_npref_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'MSFT') & 
                             ((trading_log['Order Size'] < 100) |
                             (trading_log['Order Size'] > 500)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_tradera_msft1 = b_npref_tradera_msft[~np.isnan(b_npref_tradera_msft)]
# print(np.average(b_npref_tradera_msft1))

# Trader A, MSFT, >= 100 & <= 500 (Sells)
s_pref_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'MSFT') & 
                             (trading_log['Order Size'] >= 100) & 
                             (trading_log['Order Size'] <= 500) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_tradera_msft1 = s_pref_tradera_msft[~np.isnan(s_pref_tradera_msft)]
# print(np.average(s_pref_tradera_msft1))

# Trader A, MSFT, < 100 OR > 500 (Sells)
s_npref_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') &
                             (trading_log['Symbol'] == 'MSFT') & 
                             ((trading_log['Order Size'] < 100) |
                             (trading_log['Order Size'] > 500)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_tradera_msft1 = s_npref_tradera_msft[~np.isnan(s_npref_tradera_msft)]
# print(np.average(s_npref_tradera_msft1))

### 

# Trader B, GOOGL, >= 50 & <= 300 (Buys)
b_pref_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'GOOGL') & 
                             (trading_log['Order Size'] >= 50) & 
                             (trading_log['Order Size'] <= 300) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderb_googl1 = b_pref_traderb_googl[~np.isnan(b_pref_traderb_googl)]
# print(np.average(b_pref_traderb_googl1))

# Trader B, GOOGL, < 50 OR > 300 (Buys)
b_npref_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'GOOGL') & 
                             ((trading_log['Order Size'] < 50) |
                             (trading_log['Order Size'] > 300)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderb_googl1 = b_npref_traderb_googl[~np.isnan(b_npref_traderb_googl)]
# print(np.average(b_npref_traderb_googl1))

# Trader B, GOOGL, >= 50 & <= 300 (Sells)
s_pref_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'GOOGL') & 
                             (trading_log['Order Size'] >= 50) & 
                             (trading_log['Order Size'] <= 300) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderb_googl1 = s_pref_traderb_googl[~np.isnan(s_pref_traderb_googl)]
# print(np.average(s_pref_traderb_googl1))

# Trader B, GOOGL, < 50 OR > 300 (Sells)
s_npref_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'GOOGL') & 
                             ((trading_log['Order Size'] < 50) |
                             (trading_log['Order Size'] > 300)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderb_googl1 = s_npref_traderb_googl[~np.isnan(s_npref_traderb_googl)]
# print(np.average(s_npref_traderb_googl1)) 

###

# Trader B, AMZN, >= 50 & <= 300 (Buys)
b_pref_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'AMZN') & 
                             (trading_log['Order Size'] >= 50) & 
                             (trading_log['Order Size'] <= 300) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderb_amzn1 = b_pref_traderb_amzn[~np.isnan(b_pref_traderb_amzn)]
# print(np.average(b_pref_traderb_amzn1))

# Trader B, AMZN, < 50 OR > 300 (Buys)
b_npref_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'AMZN') & 
                             ((trading_log['Order Size'] < 50) |
                             (trading_log['Order Size'] > 300)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderb_amzn1 = b_npref_traderb_amzn[~np.isnan(b_npref_traderb_amzn)]
# print(np.average(b_npref_traderb_amzn1))

# Trader B, AMZN, >= 50 & <= 300 (Sells)
s_pref_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'AMZN') & 
                             (trading_log['Order Size'] >= 50) & 
                             (trading_log['Order Size'] <= 300) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderb_amzn1 = s_pref_traderb_amzn[~np.isnan(s_pref_traderb_amzn)]
# print(np.average(s_pref_traderb_amzn1))

# Trader B, AMZN, < 50 OR > 300 (Sells)
s_npref_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') &
                             (trading_log['Symbol'] == 'AMZN') & 
                             ((trading_log['Order Size'] < 50) |
                             (trading_log['Order Size'] > 300)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderb_amzn1 = s_npref_traderb_amzn[~np.isnan(s_npref_traderb_amzn)]
# print(np.average(s_npref_traderb_amzn1)) 

### 

# Trader C, TSLA, >= 200 & <= 1000 (Buys)
b_pref_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'TSLA') & 
                             (trading_log['Order Size'] >= 200) & 
                             (trading_log['Order Size'] <= 1000) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderc_tsla1 = b_pref_traderc_tsla[~np.isnan(b_pref_traderc_tsla)]
# print(np.average(b_pref_traderc_tsla1))

# Trader C, TSLA, < 200 OR > 1000 (Buys)
b_npref_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'TSLA') & 
                             ((trading_log['Order Size'] < 200) |
                             (trading_log['Order Size'] > 1000)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderc_tsla1 = b_npref_traderc_tsla[~np.isnan(b_npref_traderc_tsla)]
# print(np.average(b_npref_traderc_tsla1))

# Trader C, TSLA, >= 200 & <= 1000 (Sells)
s_pref_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'TSLA') & 
                             (trading_log['Order Size'] >= 200) & 
                             (trading_log['Order Size'] <= 1000) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderc_tsla1 = s_pref_traderc_tsla[~np.isnan(s_pref_traderc_tsla)]
# print(np.average(s_pref_traderc_tsla1))

# Trader C, TSLA, < 200 OR > 1000 (Sells)
s_npref_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'TSLA') & 
                             ((trading_log['Order Size'] < 200) |
                             (trading_log['Order Size'] > 1000)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderc_tsla1 = s_npref_traderc_tsla[~np.isnan(s_npref_traderc_tsla)]
# print(np.average(s_npref_traderc_tsla1)) 

### 

# Trader C, FB, >= 200 & <= 1000 (Buys)
b_pref_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'FB') & 
                             (trading_log['Order Size'] >= 200) & 
                             (trading_log['Order Size'] <= 1000) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderc_fb1 = b_pref_traderc_fb[~np.isnan(b_pref_traderc_fb)]
# print(np.average(b_pref_traderc_fb1))

# Trader C, FB, < 200 OR > 1000 (Buys)
b_npref_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'FB') & 
                             ((trading_log['Order Size'] < 200) |
                             (trading_log['Order Size'] > 1000)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderc_fb1 = b_npref_traderc_fb[~np.isnan(b_npref_traderc_fb)]
# print(np.average(b_npref_traderc_fb1))

# Trader C, FB, >= 200 & <= 1000 (Sells)
s_pref_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'FB') & 
                             (trading_log['Order Size'] >= 200) & 
                             (trading_log['Order Size'] <= 1000) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderc_fb1 = s_pref_traderc_fb[~np.isnan(s_pref_traderc_fb)]
# print(np.average(s_pref_traderc_fb1))

# Trader C, FB, < 200 OR > 1000 (Sells)
s_npref_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') &
                             (trading_log['Symbol'] == 'FB') & 
                             ((trading_log['Order Size'] < 200) |
                             (trading_log['Order Size'] > 1000)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderc_fb1 = s_npref_traderc_fb[~np.isnan(s_npref_traderc_fb)]
# print(np.average(s_npref_traderc_fb1)) 

### 

# Trader D, BRK.A, >= 10 & <= 100 (Buys)
b_pref_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'BRK.A') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderd_brka1 = b_pref_traderd_brka[~np.isnan(b_pref_traderd_brka)]
# print(np.average(b_pref_traderd_brka1))

# Trader D, BRK.A, < 10 OR > 100 (Buys)
b_npref_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'BRK.A') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderd_brka1 = b_npref_traderd_brka[~np.isnan(b_npref_traderd_brka)]
# print(np.average(b_npref_traderd_brka1))

# Trader D, BRK.A, >= 10 & <= 100 (Sells)
s_pref_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'BRK.A') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderd_brka1 = s_pref_traderd_brka[~np.isnan(s_pref_traderd_brka)]
# print(np.average(s_pref_traderd_brka1))

# Trader D, BRK.A, < 10 OR > 100 (Sells)
s_npref_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'BRK.A') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderd_brka1 = s_npref_traderd_brka[~np.isnan(s_npref_traderd_brka)]
# print(np.average(s_npref_traderd_brka1)) 

### 

# Trader D, V, >= 10 & <= 100 (Buys)
b_pref_traderd_v = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'V') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderd_v1 = b_pref_traderd_v[~np.isnan(b_pref_traderd_v)]
# print(np.average(b_pref_traderd_v1))

# Trader D, V, < 10 OR > 100 (Buys)
b_npref_traderd_v = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'V') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderd_v1 = b_npref_traderd_v[~np.isnan(b_npref_traderd_v)]
# print(np.average(b_npref_traderd_v1))

# Trader D, V, >= 10 & <= 100 (Sells)
s_pref_traderd_v = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'V') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderd_v1 = s_pref_traderd_v[~np.isnan(s_pref_traderd_v)]
# print(np.average(s_pref_traderd_v1))

# Trader D, V, < 10 OR > 100 (Sells)
s_npref_traderd_v = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'V') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderd_v1 = s_npref_traderd_v[~np.isnan(s_npref_traderd_v)]
# print(np.average(s_npref_traderd_v1)) 

### 

# Trader D, JPM, >= 10 & <= 100 (Buys)
b_pref_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JPM') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderd_jpm1 = b_pref_traderd_jpm[~np.isnan(b_pref_traderd_jpm)]
# print(np.average(b_pref_traderd_jpm1))

# Trader D, JPM, < 10 OR > 100 (Buys)
b_npref_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JPM') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderd_jpm1 = b_npref_traderd_jpm[~np.isnan(b_npref_traderd_jpm)]
# print(np.average(b_npref_traderd_jpm1))

# Trader D, JPM, >= 10 & <= 100 (Sells)
s_pref_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JPM') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderd_jpm1 = s_pref_traderd_jpm[~np.isnan(s_pref_traderd_jpm)]
# print(np.average(s_pref_traderd_jpm1))

# Trader D, JPM, < 10 OR > 100 (Sells)
s_npref_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JPM') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderd_jpm1 = s_npref_traderd_jpm[~np.isnan(s_npref_traderd_jpm)]
# print(np.average(s_npref_traderd_jpm1)) 

### 

# Trader D, JNJ, >= 10 & <= 100 (Buys)
b_pref_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JNJ') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_pref_traderd_jnj1 = b_pref_traderd_jnj[~np.isnan(b_pref_traderd_jnj)]
# print(np.average(b_pref_traderd_jnj1))

# Trader D, JNJ, < 10 OR > 100 (Buys)
b_npref_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JNJ') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Buy'),
                             trading_log['Price'], np.nan)
b_npref_traderd_jnj1 = b_npref_traderd_jnj[~np.isnan(b_npref_traderd_jnj)]
# print(np.average(b_npref_traderd_jnj1))

# Trader D, JNJ, >= 10 & <= 100 (Sells)
s_pref_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JNJ') & 
                             (trading_log['Order Size'] >= 10) & 
                             (trading_log['Order Size'] <= 100) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_pref_traderd_jnj1 = s_pref_traderd_jnj[~np.isnan(s_pref_traderd_jnj)]
# print(np.average(s_pref_traderd_jnj1))

# Trader D, JNJ, < 10 OR > 100 (Sells)
s_npref_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') &
                             (trading_log['Symbol'] == 'JNJ') & 
                             ((trading_log['Order Size'] < 10) |
                             (trading_log['Order Size'] > 100)) & 
                             (trading_log['Order Type'] == 'Sell'),
                             trading_log['Price'], np.nan)
s_npref_traderd_jnj1 = s_npref_traderd_jnj[~np.isnan(s_npref_traderd_jnj)]
# print(np.average(s_npref_traderd_jnj1)) 

############################################################################################################# 

# Count number of trades in preferred order size range vs number of trades outside preferred order size range

# Trader A, AAPL, in preferred range

count_pref_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                                   (trading_log['Symbol'] == 'AAPL') & 
                                   (trading_log['Order Size'] >= 100) & 
                                   (trading_log['Order Size'] <= 500), 
                                   trading_log['Price'], np.nan)
count_pref_tradera_aapl1 = count_pref_tradera_aapl[~np.isnan(count_pref_tradera_aapl)]
# print(len(count_pref_tradera_aapl1))

# Trader A, AAPL, not in preferred range

count_npref_tradera_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                                   (trading_log['Symbol'] == 'AAPL') & 
                                   ((trading_log['Order Size'] < 100) | 
                                   (trading_log['Order Size'] > 500)), 
                                   trading_log['Price'], np.nan)
count_npref_tradera_aapl1 = count_npref_tradera_aapl[~np.isnan(count_npref_tradera_aapl)]
# print(len(count_npref_tradera_aapl1))

### 

# Trader A, MSFT, in preferred range

count_pref_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                                   (trading_log['Symbol'] == 'MSFT') & 
                                   (trading_log['Order Size'] >= 100) & 
                                   (trading_log['Order Size'] <= 500), 
                                   trading_log['Price'], np.nan)
count_pref_tradera_msft1 = count_pref_tradera_msft[~np.isnan(count_pref_tradera_msft)]
# print(len(count_pref_tradera_msft1))

# Trader A, MSFT, not in preferred range

count_npref_tradera_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                                   (trading_log['Symbol'] == 'MSFT') & 
                                   ((trading_log['Order Size'] < 100) | 
                                   (trading_log['Order Size'] > 500)), 
                                   trading_log['Price'], np.nan)
count_npref_tradera_msft1 = count_npref_tradera_msft[~np.isnan(count_npref_tradera_msft)]
# print(len(count_npref_tradera_msft1))

### 

# Trader B, GOOGL, in preferred range

count_pref_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                                   (trading_log['Symbol'] == 'GOOGL') & 
                                   (trading_log['Order Size'] >= 50) & 
                                   (trading_log['Order Size'] <= 300), 
                                   trading_log['Price'], np.nan)
count_pref_traderb_googl1 = count_pref_traderb_googl[~np.isnan(count_pref_traderb_googl)]
# print(len(count_pref_traderb_googl1))

# Trader B, GOOGL, not in preferred range

count_npref_traderb_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                                   (trading_log['Symbol'] == 'GOOGL') & 
                                   ((trading_log['Order Size'] < 50) | 
                                   (trading_log['Order Size'] > 300)), 
                                   trading_log['Price'], np.nan)
count_npref_traderb_googl1 = count_npref_traderb_googl[~np.isnan(count_npref_traderb_googl)]
# print(len(count_npref_traderb_googl1)) 

### 

# Trader B, AMZN, in preferred range

count_pref_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                                   (trading_log['Symbol'] == 'AMZN') & 
                                   (trading_log['Order Size'] >= 50) & 
                                   (trading_log['Order Size'] <= 300), 
                                   trading_log['Price'], np.nan)
count_pref_traderb_amzn1 = count_pref_traderb_amzn[~np.isnan(count_pref_traderb_amzn)]
# print(len(count_pref_traderb_amzn1))

# Trader B, AMZN, not in preferred range

count_npref_traderb_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                                   (trading_log['Symbol'] == 'AMZN') & 
                                   ((trading_log['Order Size'] < 50) | 
                                   (trading_log['Order Size'] > 300)), 
                                   trading_log['Price'], np.nan)
count_npref_traderb_amzn1 = count_npref_traderb_amzn[~np.isnan(count_npref_traderb_amzn)]
# print(len(count_npref_traderb_amzn1)) 

### 

# Trader C, TSLA, in preferred range

count_pref_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                                   (trading_log['Symbol'] == 'TSLA') & 
                                   (trading_log['Order Size'] >= 200) & 
                                   (trading_log['Order Size'] <= 1000), 
                                   trading_log['Price'], np.nan)
count_pref_traderc_tsla1 = count_pref_traderc_tsla[~np.isnan(count_pref_traderc_tsla)]
# print(len(count_pref_traderc_tsla1))

# Trader C, TSLA, not in preferred range

count_npref_traderc_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                                   (trading_log['Symbol'] == 'TSLA') & 
                                   ((trading_log['Order Size'] < 200) | 
                                   (trading_log['Order Size'] > 1000)), 
                                   trading_log['Price'], np.nan)
count_npref_traderc_tsla1 = count_npref_traderc_tsla[~np.isnan(count_npref_traderc_tsla)]
# print(len(count_npref_traderc_tsla1)) 

### 

# Trader C, FB, in preferred range

count_pref_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                                   (trading_log['Symbol'] == 'FB') & 
                                   (trading_log['Order Size'] >= 200) & 
                                   (trading_log['Order Size'] <= 1000), 
                                   trading_log['Price'], np.nan)
count_pref_traderc_fb1 = count_pref_traderc_fb[~np.isnan(count_pref_traderc_fb)]
# print(len(count_pref_traderc_fb1))

# Trader C, FB, not in preferred range

count_npref_traderc_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                                   (trading_log['Symbol'] == 'FB') & 
                                   ((trading_log['Order Size'] < 200) | 
                                   (trading_log['Order Size'] > 1000)), 
                                   trading_log['Price'], np.nan)
count_npref_traderc_fb1 = count_npref_traderc_fb[~np.isnan(count_npref_traderc_fb)]
# print(len(count_npref_traderc_fb1)) 

### 

# Trader D, BRK.A, in preferred range

count_pref_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'BRK.A') & 
                                   (trading_log['Order Size'] >= 10) & 
                                   (trading_log['Order Size'] <= 100), 
                                   trading_log['Price'], np.nan)
count_pref_traderd_brka1 = count_pref_traderd_brka[~np.isnan(count_pref_traderd_brka)]
# print(len(count_pref_traderd_brka1))

# Trader D, BRK.A, not in preferred range

count_npref_traderd_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'BRK.A') & 
                                   ((trading_log['Order Size'] < 10) | 
                                   (trading_log['Order Size'] > 100)), 
                                   trading_log['Price'], np.nan)
count_npref_traderd_brka1 = count_npref_traderd_brka[~np.isnan(count_npref_traderd_brka)]
# print(len(count_npref_traderd_brka1)) 

### 

# Trader D, V, in preferred range

count_pref_traderd_v = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'V') & 
                                   (trading_log['Order Size'] >= 10) & 
                                   (trading_log['Order Size'] <= 100), 
                                   trading_log['Price'], np.nan)
count_pref_traderd_v1 = count_pref_traderd_v[~np.isnan(count_pref_traderd_v)]
# print(len(count_pref_traderd_v1))

# Trader D, V, not in preferred range

count_npref_traderd_v = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'V') & 
                                   ((trading_log['Order Size'] < 10) | 
                                   (trading_log['Order Size'] > 100)), 
                                   trading_log['Price'], np.nan)
count_npref_traderd_v1 = count_npref_traderd_v[~np.isnan(count_npref_traderd_v)]
# print(len(count_npref_traderd_v1)) 

### 

# Trader D, JPM, in preferred range

count_pref_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'JPM') & 
                                   (trading_log['Order Size'] >= 10) & 
                                   (trading_log['Order Size'] <= 100), 
                                   trading_log['Price'], np.nan)
count_pref_traderd_jpm1 = count_pref_traderd_jpm[~np.isnan(count_pref_traderd_jpm)]
# print(len(count_pref_traderd_jpm1))

# Trader D, JPM, not in preferred range

count_npref_traderd_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'JPM') & 
                                   ((trading_log['Order Size'] < 10) | 
                                   (trading_log['Order Size'] > 100)), 
                                   trading_log['Price'], np.nan)
count_npref_traderd_jpm1 = count_npref_traderd_jpm[~np.isnan(count_npref_traderd_jpm)]
# print(len(count_npref_traderd_jpm1)) 

### 

 # Trader D, JNJ, in preferred range

count_pref_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'JNJ') & 
                                   (trading_log['Order Size'] >= 10) & 
                                   (trading_log['Order Size'] <= 100), 
                                   trading_log['Price'], np.nan)
count_pref_traderd_jnj1 = count_pref_traderd_jnj[~np.isnan(count_pref_traderd_jnj)]
# print(len(count_pref_traderd_jnj1))

# Trader D, JNJ, not in preferred range

count_npref_traderd_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                                   (trading_log['Symbol'] == 'JNJ') & 
                                   ((trading_log['Order Size'] < 10) | 
                                   (trading_log['Order Size'] > 100)), 
                                   trading_log['Price'], np.nan)
count_npref_traderd_jnj1 = count_npref_traderd_jnj[~np.isnan(count_npref_traderd_jnj)]
# print(len(count_npref_traderd_jnj1))

###########################################################################################################################

# Trader Position Analysis 

# Trader A 

# Trader A Buys 

tradera_buy = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy1 = tradera_buy[~np.isnan(tradera_buy)]
(np.sum(tradera_buy1))

# Trader A Sells 

tradera_sell = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell1 = tradera_sell[~np.isnan(tradera_sell)]
(np.sum(tradera_sell1))

# Trader A Closing Balance

# print((np.sum(tradera_buy1)) - (np.sum(tradera_sell1)))

### 

# Trader A Buys (AAPL)

tradera_buy_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_aapl1 = tradera_buy_aapl[~np.isnan(tradera_buy_aapl)]
(np.sum(tradera_buy_aapl1))

# Trader A Sells (AAPL)

tradera_sell_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_aapl1 = tradera_sell_aapl[~np.isnan(tradera_sell_aapl)]
(np.sum(tradera_sell_aapl1))

# Trader A Closing Balance (AAPL)

# print((np.sum(tradera_buy_aapl1)) - (np.sum(tradera_sell_aapl1))) 

### 

# Trader A Buys (MSFT)

tradera_buy_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_msft1 = tradera_buy_msft[~np.isnan(tradera_buy_msft)]
(np.sum(tradera_buy_msft1))

# Trader A Sells (MSFT)

tradera_sell_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_msft1 = tradera_sell_msft[~np.isnan(tradera_sell_msft)]
(np.sum(tradera_sell_msft1))

# Trader A Closing Balance (MSFT)

# print((np.sum(tradera_buy_msft1)) - (np.sum(tradera_sell_msft1)))  

### 

# Trader A Buys (GOOGL)

tradera_buy_googl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_googl1 = tradera_buy_googl[~np.isnan(tradera_buy_googl)]
(np.sum(tradera_buy_googl1))

# Trader A Sells (GOOGL)

tradera_sell_googl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_googl1 = tradera_sell_googl[~np.isnan(tradera_sell_googl)]
(np.sum(tradera_sell_googl1))

# Trader A Closing Balance (GOOGL)

# print((np.sum(tradera_buy_googl1)) - (np.sum(tradera_sell_googl1))) 

### 

# Trader A Buys (AMZN)

tradera_buy_amzn = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_amzn1 = tradera_buy_amzn[~np.isnan(tradera_buy_amzn)]
(np.sum(tradera_buy_amzn1))

# Trader A Sells (AMZN)

tradera_sell_amzn = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_amzn1 = tradera_sell_amzn[~np.isnan(tradera_sell_amzn)]
(np.sum(tradera_sell_amzn1))

# Trader A Closing Balance (AMZN)

# print((np.sum(tradera_buy_amzn1)) - (np.sum(tradera_sell_amzn1))) 

### 

# Trader A Buys (TSLA)

tradera_buy_tsla = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_tsla1 = tradera_buy_tsla[~np.isnan(tradera_buy_tsla)]
(np.sum(tradera_buy_tsla1))

# Trader A Sells (TSLA)

tradera_sell_tsla = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_tsla1 = tradera_sell_tsla[~np.isnan(tradera_sell_tsla)]
(np.sum(tradera_sell_tsla1))

# Trader A Closing Balance (TSLA)

# print((np.sum(tradera_buy_tsla1)) - (np.sum(tradera_sell_tsla1))) 

### 

# Trader A Buys (FB)

tradera_buy_fb = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_fb1 = tradera_buy_fb[~np.isnan(tradera_buy_fb)]
(np.sum(tradera_buy_fb1))

# Trader A Sells (FB)

tradera_sell_fb = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_fb1 = tradera_sell_fb[~np.isnan(tradera_sell_fb)]
(np.sum(tradera_sell_fb1))

# Trader A Closing Balance (FB)

# print((np.sum(tradera_buy_fb1)) - (np.sum(tradera_sell_fb1))) 

### 

# Trader A Buys (BRK.A)

tradera_buy_brka = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_brka1 = tradera_buy_brka[~np.isnan(tradera_buy_brka)]
(np.sum(tradera_buy_brka1))

# Trader A Sells (BRK.A)

tradera_sell_brka = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_brka1 = tradera_sell_brka[~np.isnan(tradera_sell_brka)]
(np.sum(tradera_sell_brka1))

# Trader A Closing Balance (BRK.A)

# print((np.sum(tradera_buy_brka1)) - (np.sum(tradera_sell_brka1))) 

### 

# Trader A Buys (V)

tradera_buy_v = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_v1 = tradera_buy_v[~np.isnan(tradera_buy_v)]
(np.sum(tradera_buy_v1))

# Trader A Sells (V)

tradera_sell_v = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_v1 = tradera_sell_v[~np.isnan(tradera_sell_v)]
(np.sum(tradera_sell_v1))

# Trader A Closing Balance (V)

# print((np.sum(tradera_buy_v1)) - (np.sum(tradera_sell_v1))) 

### 

# Trader A Buys (JPM)

tradera_buy_jpm = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_jpm1 = tradera_buy_jpm[~np.isnan(tradera_buy_jpm)]
(np.sum(tradera_buy_jpm1))

# Trader A Sells (JPM)

tradera_sell_jpm = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_jpm1 = tradera_sell_jpm[~np.isnan(tradera_sell_jpm)]
(np.sum(tradera_sell_jpm1))

# Trader A Closing Balance (JPM)

# print((np.sum(tradera_buy_jpm1)) - (np.sum(tradera_sell_jpm1))) 

### 

# Trader A Buys (JNJ)

tradera_buy_jnj = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_buy_jnj1 = tradera_buy_jnj[~np.isnan(tradera_buy_jnj)]
(np.sum(tradera_buy_jnj1))

# Trader A Sells (JNJ)

tradera_sell_jnj = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
tradera_sell_jnj1 = tradera_sell_jnj[~np.isnan(tradera_sell_jnj)]
(np.sum(tradera_sell_jnj1))

# Trader A Closing Balance (JNJ)

# print((np.sum(tradera_buy_jnj1)) - (np.sum(tradera_sell_jnj1))) 

### 

# Trader B

# Trader B Buys 

traderb_buy = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy1 = traderb_buy[~np.isnan(traderb_buy)]
(np.sum(traderb_buy1))

# Trader B Sells 

traderb_sell = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell1 = traderb_sell[~np.isnan(traderb_sell)]
(np.sum(traderb_sell1))

# Trader B Closing Balance

# print((np.sum(traderb_buy1)) - (np.sum(traderb_sell1)))

### 

# Trader B Buys (AAPL)

traderb_buy_aapl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_aapl1 = traderb_buy_aapl[~np.isnan(traderb_buy_aapl)]
(np.sum(traderb_buy_aapl1))

# Trader B Sells (AAPL)

traderb_sell_aapl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_aapl1 = traderb_sell_aapl[~np.isnan(traderb_sell_aapl)]
(np.sum(traderb_sell_aapl1))

# Trader B Closing Balance (AAPL)

# print((np.sum(traderb_buy_aapl1)) - (np.sum(traderb_sell_aapl1))) 

### 

# Trader B Buys (MSFT)

traderb_buy_msft = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_msft1 = traderb_buy_msft[~np.isnan(traderb_buy_msft)]
(np.sum(traderb_buy_msft1))

# Trader B Sells (MSFT)

traderb_sell_msft = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_msft1 = traderb_sell_msft[~np.isnan(traderb_sell_msft)]
(np.sum(traderb_sell_msft1))

# Trader B Closing Balance (MSFT)

# print((np.sum(traderb_buy_msft1)) - (np.sum(traderb_sell_msft1)))  

### 

# Trader B Buys (GOOGL)

traderb_buy_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_googl1 = traderb_buy_googl[~np.isnan(traderb_buy_googl)]
(np.sum(traderb_buy_googl1))

# Trader B Sells (GOOGL)

traderb_sell_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_googl1 = traderb_sell_googl[~np.isnan(traderb_sell_googl)]
(np.sum(traderb_sell_googl1))

# Trader B Closing Balance (GOOGL)

# print((np.sum(traderb_buy_googl1)) - (np.sum(traderb_sell_googl1))) 

### 

# Trader B Buys (AMZN)

traderb_buy_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_amzn1 = traderb_buy_amzn[~np.isnan(traderb_buy_amzn)]
(np.sum(traderb_buy_amzn1))

# Trader B Sells (AMZN)

traderb_sell_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_amzn1 = traderb_sell_amzn[~np.isnan(traderb_sell_amzn)]
(np.sum(traderb_sell_amzn1))

# Trader B Closing Balance (AMZN)

# print((np.sum(traderb_buy_amzn1)) - (np.sum(traderb_sell_amzn1))) 

### 

# Trader B Buys (TSLA)

traderb_buy_tsla = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_tsla1 = traderb_buy_tsla[~np.isnan(traderb_buy_tsla)]
(np.sum(traderb_buy_tsla1))

# Trader B Sells (TSLA)

traderb_sell_tsla = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_tsla1 = traderb_sell_tsla[~np.isnan(traderb_sell_tsla)]
(np.sum(traderb_sell_tsla1))

# Trader B Closing Balance (TSLA)

# print((np.sum(traderb_buy_tsla1)) - (np.sum(traderb_sell_tsla1))) 

### 

# Trader B Buys (FB)

traderb_buy_fb = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_fb1 = traderb_buy_fb[~np.isnan(traderb_buy_fb)]
(np.sum(traderb_buy_fb1))

# Trader B Sells (FB)

traderb_sell_fb = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_fb1 = traderb_sell_fb[~np.isnan(traderb_sell_fb)]
(np.sum(traderb_sell_fb1))

# Trader B Closing Balance (FB)

# print((np.sum(traderb_buy_fb1)) - (np.sum(traderb_sell_fb1))) 

### 

# Trader B Buys (BRK.A)

traderb_buy_brka = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_brka1 = traderb_buy_brka[~np.isnan(traderb_buy_brka)]
(np.sum(traderb_buy_brka1))

# Trader B Sells (BRK.A)

traderb_sell_brka = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_brka1 = traderb_sell_brka[~np.isnan(traderb_sell_brka)]
(np.sum(traderb_sell_brka1))

# Trader B Closing Balance (BRK.A)

# print((np.sum(traderb_buy_brka1)) - (np.sum(traderb_sell_brka1))) 

### 

# Trader B Buys (V)

traderb_buy_v = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_v1 = traderb_buy_v[~np.isnan(traderb_buy_v)]
(np.sum(traderb_buy_v1))

# Trader B Sells (V)

traderb_sell_v = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_v1 = traderb_sell_v[~np.isnan(traderb_sell_v)]
(np.sum(traderb_sell_v1))

# Trader B Closing Balance (V)

# print((np.sum(traderb_buy_v1)) - (np.sum(traderb_sell_v1))) 

### 

# Trader B Buys (JPM)

traderb_buy_jpm = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_jpm1 = traderb_buy_jpm[~np.isnan(traderb_buy_jpm)]
(np.sum(traderb_buy_jpm1))

# Trader B Sells (JPM)

traderb_sell_jpm = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_jpm1 = traderb_sell_jpm[~np.isnan(traderb_sell_jpm)]
(np.sum(traderb_sell_jpm1))

# Trader B Closing Balance (JPM)

# print((np.sum(traderb_buy_jpm1)) - (np.sum(traderb_sell_jpm1))) 

### 

# Trader B Buys (JNJ)

traderb_buy_jnj = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_buy_jnj1 = traderb_buy_jnj[~np.isnan(traderb_buy_jnj)]
(np.sum(traderb_buy_jnj1))

# Trader B Sells (JNJ)

traderb_sell_jnj = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderb_sell_jnj1 = traderb_sell_jnj[~np.isnan(traderb_sell_jnj)]
(np.sum(traderb_sell_jnj1))

# Trader B Closing Balance (JNJ)

# print((np.sum(traderb_buy_jnj1)) - (np.sum(traderb_sell_jnj1))) 

### 

# Trader C

# Trader C Buys 

traderc_buy = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy1 = traderc_buy[~np.isnan(traderc_buy)]
(np.sum(traderc_buy1))

# Trader C Sells 

traderc_sell = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell1 = traderc_sell[~np.isnan(traderc_sell)]
(np.sum(traderc_sell1))

# Trader C Closing Balance

# print((np.sum(traderc_buy1)) - (np.sum(traderc_sell1)))

### 

# Trader C Buys (AAPL)

traderc_buy_aapl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_aapl1 = traderc_buy_aapl[~np.isnan(traderc_buy_aapl)]
(np.sum(traderc_buy_aapl1))

# Trader C Sells (AAPL)

traderc_sell_aapl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_aapl1 = traderc_sell_aapl[~np.isnan(traderc_sell_aapl)]
(np.sum(traderc_sell_aapl1))

# Trader C Closing Balance (AAPL)

# print((np.sum(traderc_buy_aapl1)) - (np.sum(traderc_sell_aapl1))) 

### 

# Trader C Buys (MSFT)

traderc_buy_msft = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_msft1 = traderc_buy_msft[~np.isnan(traderc_buy_msft)]
(np.sum(traderc_buy_msft1))

# Trader C Sells (MSFT)

traderc_sell_msft = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_msft1 = traderc_sell_msft[~np.isnan(traderc_sell_msft)]
(np.sum(traderc_sell_msft1))

# Trader C Closing Balance (MSFT)

# print((np.sum(traderc_buy_msft1)) - (np.sum(traderc_sell_msft1)))  

### 

# Trader C Buys (GOOGL)

traderc_buy_googl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_googl1 = traderc_buy_googl[~np.isnan(traderc_buy_googl)]
(np.sum(traderc_buy_googl1))

# Trader C Sells (GOOGL)

traderc_sell_googl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_googl1 = traderc_sell_googl[~np.isnan(traderc_sell_googl)]
(np.sum(traderc_sell_googl1))

# Trader C Closing Balance (GOOGL)

# print((np.sum(traderc_buy_googl1)) - (np.sum(traderc_sell_googl1))) 

### 

# Trader C Buys (AMZN)

traderc_buy_amzn = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_amzn1 = traderc_buy_amzn[~np.isnan(traderc_buy_amzn)]
(np.sum(traderc_buy_amzn1))

# Trader C Sells (AMZN)

traderc_sell_amzn = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_amzn1 = traderc_sell_amzn[~np.isnan(traderc_sell_amzn)]
(np.sum(traderc_sell_amzn1))

# Trader C Closing Balance (AMZN)

# print((np.sum(traderc_buy_amzn1)) - (np.sum(traderc_sell_amzn1))) 

### 

# Trader C Buys (TSLA)

traderc_buy_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_tsla1 = traderc_buy_tsla[~np.isnan(traderc_buy_tsla)]
(np.sum(traderc_buy_tsla1))

# Trader C Sells (TSLA)

traderc_sell_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_tsla1 = traderc_sell_tsla[~np.isnan(traderc_sell_tsla)]
(np.sum(traderc_sell_tsla1))

# Trader C Closing Balance (TSLA)

# print((np.sum(traderc_buy_tsla1)) - (np.sum(traderc_sell_tsla1))) 

### 

# Trader C Buys (FB)

traderc_buy_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_fb1 = traderc_buy_fb[~np.isnan(traderc_buy_fb)]
(np.sum(traderc_buy_fb1))

# Trader C Sells (FB)

traderc_sell_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_fb1 = traderc_sell_fb[~np.isnan(traderc_sell_fb)]
(np.sum(traderc_sell_fb1))

# Trader C Closing Balance (FB)

# print((np.sum(traderc_buy_fb1)) - (np.sum(traderc_sell_fb1))) 

### 

# Trader C Buys (BRK.A)

traderc_buy_brka = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_brka1 = traderc_buy_brka[~np.isnan(traderc_buy_brka)]
(np.sum(traderc_buy_brka1))

# Trader C Sells (BRK.A)

traderc_sell_brka = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_brka1 = traderc_sell_brka[~np.isnan(traderc_sell_brka)]
(np.sum(traderc_sell_brka1))

# Trader C Closing Balance (BRK.A)

# print((np.sum(traderc_buy_brka1)) - (np.sum(traderc_sell_brka1))) 

### 

# Trader C Buys (V)

traderc_buy_v = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_v1 = traderc_buy_v[~np.isnan(traderc_buy_v)]
(np.sum(traderc_buy_v1))

# Trader C Sells (V)

traderc_sell_v = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_v1 = traderc_sell_v[~np.isnan(traderc_sell_v)]
(np.sum(traderc_sell_v1))

# Trader C Closing Balance (V)

# print((np.sum(traderc_buy_v1)) - (np.sum(traderc_sell_v1))) 

### 

# Trader C Buys (JPM)

traderc_buy_jpm = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_jpm1 = traderc_buy_jpm[~np.isnan(traderc_buy_jpm)]
(np.sum(traderc_buy_jpm1))

# Trader C Sells (JPM)

traderc_sell_jpm = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_jpm1 = traderc_sell_jpm[~np.isnan(traderc_sell_jpm)]
(np.sum(traderc_sell_jpm1))

# Trader C Closing Balance (JPM)

# print((np.sum(traderc_buy_jpm1)) - (np.sum(traderc_sell_jpm1))) 

### 

# Trader C Buys (JNJ)

traderc_buy_jnj = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_buy_jnj1 = traderc_buy_jnj[~np.isnan(traderc_buy_jnj)]
(np.sum(traderc_buy_jnj1))

# Trader C Sells (JNJ)

traderc_sell_jnj = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderc_sell_jnj1 = traderc_sell_jnj[~np.isnan(traderc_sell_jnj)]
(np.sum(traderc_sell_jnj1))

# Trader C Closing Balance (JNJ)

# print((np.sum(traderc_buy_jnj1)) - (np.sum(traderc_sell_jnj1))) 

### 

# Trader D

# Trader D Buys 

traderd_buy = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy1 = traderd_buy[~np.isnan(traderd_buy)]
(np.sum(traderd_buy1))

# Trader D Sells 

traderd_sell = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell1 = traderd_sell[~np.isnan(traderd_sell)]
(np.sum(traderd_sell1))

# Trader D Closing Balance

# print((np.sum(traderd_buy1)) - (np.sum(traderd_sell1)))

### 

# Trader D Buys (AAPL)

traderd_buy_aapl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_aapl1 = traderd_buy_aapl[~np.isnan(traderd_buy_aapl)]
(np.sum(traderd_buy_aapl1))

# Trader D Sells (AAPL)

traderd_sell_aapl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_aapl1 = traderd_sell_aapl[~np.isnan(traderd_sell_aapl)]
(np.sum(traderd_sell_aapl1))

# Trader D Closing Balance (AAPL)

# print((np.sum(traderd_buy_aapl1)) - (np.sum(traderd_sell_aapl1))) 

### 

# Trader D Buys (MSFT)

traderd_buy_msft = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_msft1 = traderd_buy_msft[~np.isnan(traderd_buy_msft)]
(np.sum(traderd_buy_msft1))

# Trader D Sells (MSFT)

traderd_sell_msft = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_msft1 = traderd_sell_msft[~np.isnan(traderd_sell_msft)]
(np.sum(traderd_sell_msft1))

# Trader D Closing Balance (MSFT)

# print((np.sum(traderd_buy_msft1)) - (np.sum(traderd_sell_msft1)))  

### 

# Trader D Buys (GOOGL)

traderd_buy_googl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_googl1 = traderd_buy_googl[~np.isnan(traderd_buy_googl)]
(np.sum(traderd_buy_googl1))

# Trader D Sells (GOOGL)

traderd_sell_googl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_googl1 = traderd_sell_googl[~np.isnan(traderd_sell_googl)]
(np.sum(traderd_sell_googl1))

# Trader D Closing Balance (GOOGL)

# print((np.sum(traderd_buy_googl1)) - (np.sum(traderd_sell_googl1))) 

### 

# Trader D Buys (AMZN)

traderd_buy_amzn = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_amzn1 = traderd_buy_amzn[~np.isnan(traderd_buy_amzn)]
(np.sum(traderd_buy_amzn1))

# Trader D Sells (AMZN)

traderd_sell_amzn = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_amzn1 = traderd_sell_amzn[~np.isnan(traderd_sell_amzn)]
(np.sum(traderd_sell_amzn1))

# Trader D Closing Balance (AMZN)

# print((np.sum(traderd_buy_amzn1)) - (np.sum(traderd_sell_amzn1))) 

### 

# Trader D Buys (TSLA)

traderd_buy_tsla = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_tsla1 = traderd_buy_tsla[~np.isnan(traderd_buy_tsla)]
(np.sum(traderd_buy_tsla1))

# Trader D Sells (TSLA)

traderd_sell_tsla = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_tsla1 = traderd_sell_tsla[~np.isnan(traderd_sell_tsla)]
(np.sum(traderd_sell_tsla1))

# Trader D Closing Balance (TSLA)

# print((np.sum(traderd_buy_tsla1)) - (np.sum(traderd_sell_tsla1))) 

### 

# Trader D Buys (FB)

traderd_buy_fb = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_fb1 = traderd_buy_fb[~np.isnan(traderd_buy_fb)]
(np.sum(traderd_buy_fb1))

# Trader D Sells (FB)

traderd_sell_fb = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_fb1 = traderd_sell_fb[~np.isnan(traderd_sell_fb)]
(np.sum(traderd_sell_fb1))

# Trader D Closing Balance (FB)

# print((np.sum(traderd_buy_fb1)) - (np.sum(traderd_sell_fb1))) 

### 

# Trader D Buys (BRK.A)

traderd_buy_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_brka1 = traderd_buy_brka[~np.isnan(traderd_buy_brka)]
(np.sum(traderd_buy_brka1))

# Trader D Sells (BRK.A)

traderd_sell_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_brka1 = traderd_sell_brka[~np.isnan(traderd_sell_brka)]
(np.sum(traderd_sell_brka1))

# Trader D Closing Balance (BRK.A)

# print((np.sum(traderd_buy_brka1)) - (np.sum(traderd_sell_brka1))) 

### 

# Trader D Buys (V)

traderd_buy_v = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_v1 = traderd_buy_v[~np.isnan(traderd_buy_v)]
(np.sum(traderd_buy_v1))

# Trader D Sells (V)

traderd_sell_v = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_v1 = traderd_sell_v[~np.isnan(traderd_sell_v)]
(np.sum(traderd_sell_v1))

# Trader D Closing Balance (V)

# print((np.sum(traderd_buy_v1)) - (np.sum(traderd_sell_v1))) 

### 

# Trader D Buys (JPM)

traderd_buy_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_jpm1 = traderd_buy_jpm[~np.isnan(traderd_buy_jpm)]
(np.sum(traderd_buy_jpm1))

# Trader D Sells (JPM)

traderd_sell_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_jpm1 = traderd_sell_jpm[~np.isnan(traderd_sell_jpm)]
(np.sum(traderd_sell_jpm1))

# Trader D Closing Balance (JPM)

# print((np.sum(traderd_buy_jpm1)) - (np.sum(traderd_sell_jpm1))) 

### 

# Trader D Buys (JNJ)

traderd_buy_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_buy_jnj1 = traderd_buy_jnj[~np.isnan(traderd_buy_jnj)]
(np.sum(traderd_buy_jnj1))

# Trader D Sells (JNJ)

traderd_sell_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size'] * trading_log['Price']), np.nan)
traderd_sell_jnj1 = traderd_sell_jnj[~np.isnan(traderd_sell_jnj)]
(np.sum(traderd_sell_jnj1))

# Trader D Closing Balance (JNJ)

# print((np.sum(traderd_buy_jnj1)) - (np.sum(traderd_sell_jnj1))) 

#############################################################################################################

# Trader Position Analysis (number of shares)

# Trader A 

# Trader A Buys (AAPL)

v_tradera_buy_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_aapl1 = v_tradera_buy_aapl[~np.isnan(v_tradera_buy_aapl)]
(np.sum(v_tradera_buy_aapl1))

# Trader A Sells (AAPL)

v_tradera_sell_aapl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_aapl1 = v_tradera_sell_aapl[~np.isnan(v_tradera_sell_aapl)]
(np.sum(v_tradera_sell_aapl1))

# Trader A Closing Balance (AAPL)

# print((np.sum(v_tradera_buy_aapl1)) - (np.sum(v_tradera_sell_aapl1))) 

### 

# Trader A Buys (MSFT)

v_tradera_buy_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_msft1 = v_tradera_buy_msft[~np.isnan(v_tradera_buy_msft)]
(np.sum(v_tradera_buy_msft1))

# Trader A Sells (MSFT)

v_tradera_sell_msft = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_msft1 = v_tradera_sell_msft[~np.isnan(v_tradera_sell_msft)]
(np.sum(v_tradera_sell_msft1))

# Trader A Closing Balance (MSFT)

# print((np.sum(v_tradera_buy_msft1)) - (np.sum(v_tradera_sell_msft1)))  

### 

# Trader A Buys (GOOGL)

v_tradera_buy_googl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_googl1 = v_tradera_buy_googl[~np.isnan(v_tradera_buy_googl)]
(np.sum(v_tradera_buy_googl1))

# Trader A Sells (GOOGL)

v_tradera_sell_googl = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_googl1 = v_tradera_sell_googl[~np.isnan(v_tradera_sell_googl)]
(np.sum(v_tradera_sell_googl1))

# Trader A Closing Balance (GOOGL)

# print((np.sum(v_tradera_buy_googl1)) - (np.sum(v_tradera_sell_googl1))) 

### 

# Trader A Buys (AMZN)

v_tradera_buy_amzn = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_amzn1 = v_tradera_buy_amzn[~np.isnan(v_tradera_buy_amzn)]
(np.sum(v_tradera_buy_amzn1))

# Trader A Sells (AMZN)

v_tradera_sell_amzn = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_amzn1 = v_tradera_sell_amzn[~np.isnan(v_tradera_sell_amzn)]
(np.sum(v_tradera_sell_amzn1))

# Trader A Closing Balance (AMZN)

# print((np.sum(v_tradera_buy_amzn1)) - (np.sum(v_tradera_sell_amzn1))) 

### 

# Trader A Buys (TSLA)

v_tradera_buy_tsla = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_tsla1 = v_tradera_buy_tsla[~np.isnan(v_tradera_buy_tsla)]
(np.sum(v_tradera_buy_tsla1))

# Trader A Sells (TSLA)

v_tradera_sell_tsla = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_tsla1 = v_tradera_sell_tsla[~np.isnan(v_tradera_sell_tsla)]
(np.sum(v_tradera_sell_tsla1))

# Trader A Closing Balance (TSLA)

# print((np.sum(v_tradera_buy_tsla1)) - (np.sum(v_tradera_sell_tsla1))) 

### 

# Trader A Buys (FB)

v_tradera_buy_fb = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_fb1 = v_tradera_buy_fb[~np.isnan(v_tradera_buy_fb)]
(np.sum(v_tradera_buy_fb1))

# Trader A Sells (FB)

v_tradera_sell_fb = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_fb1 = v_tradera_sell_fb[~np.isnan(v_tradera_sell_fb)]
(np.sum(v_tradera_sell_fb1))

# Trader A Closing Balance (FB)

# print((np.sum(v_tradera_buy_fb1)) - (np.sum(v_tradera_sell_fb1))) 

### 

# Trader A Buys (BRK.A)

v_tradera_buy_brka = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_brka1 = v_tradera_buy_brka[~np.isnan(v_tradera_buy_brka)]
(np.sum(v_tradera_buy_brka1))

# Trader A Sells (BRK.A)

v_tradera_sell_brka = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_brka1 = v_tradera_sell_brka[~np.isnan(v_tradera_sell_brka)]
(np.sum(v_tradera_sell_brka1))

# Trader A Closing Balance (BRK.A)

# print((np.sum(v_tradera_buy_brka1)) - (np.sum(v_tradera_sell_brka1))) 

### 

# Trader A Buys (V)

v_tradera_buy_v = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_v1 = v_tradera_buy_v[~np.isnan(v_tradera_buy_v)]
(np.sum(v_tradera_buy_v1))

# Trader A Sells (V)

v_tradera_sell_v = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_v1 = v_tradera_sell_v[~np.isnan(v_tradera_sell_v)]
(np.sum(v_tradera_sell_v1))

# Trader A Closing Balance (V)

# print((np.sum(v_tradera_buy_v1)) - (np.sum(v_tradera_sell_v1))) 

### 

# Trader A Buys (JPM)

v_tradera_buy_jpm = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_jpm1 = v_tradera_buy_jpm[~np.isnan(v_tradera_buy_jpm)]
(np.sum(v_tradera_buy_jpm1))

# Trader A Sells (JPM)

v_tradera_sell_jpm = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_jpm1 = v_tradera_sell_jpm[~np.isnan(v_tradera_sell_jpm)]
(np.sum(v_tradera_sell_jpm1))

# Trader A Closing Balance (JPM)

# print((np.sum(v_tradera_buy_jpm1)) - (np.sum(v_tradera_sell_jpm1))) 

### 

# Trader A Buys (JNJ)

v_tradera_buy_jnj = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_buy_jnj1 = v_tradera_buy_jnj[~np.isnan(v_tradera_buy_jnj)]
(np.sum(v_tradera_buy_jnj1))

# Trader A Sells (JNJ)

v_tradera_sell_jnj = np.where((trading_log['Trader'] == 'Trader A') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_tradera_sell_jnj1 = v_tradera_sell_jnj[~np.isnan(v_tradera_sell_jnj)]
(np.sum(v_tradera_sell_jnj1))

# Trader A Closing Balance (JNJ)

# print((np.sum(v_tradera_buy_jnj1)) - (np.sum(v_tradera_sell_jnj1))) 

### 

# Trader B

# Trader B Buys (AAPL)

v_traderb_buy_aapl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_aapl1 = v_traderb_buy_aapl[~np.isnan(v_traderb_buy_aapl)]
(np.sum(v_traderb_buy_aapl1))

# Trader B Sells (AAPL)

v_traderb_sell_aapl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_aapl1 = v_traderb_sell_aapl[~np.isnan(v_traderb_sell_aapl)]
(np.sum(v_traderb_sell_aapl1))

# Trader B Closing Balance (AAPL)

# print((np.sum(v_traderb_buy_aapl1)) - (np.sum(v_traderb_sell_aapl1))) 

### 

# Trader B Buys (MSFT)

v_traderb_buy_msft = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_msft1 = v_traderb_buy_msft[~np.isnan(v_traderb_buy_msft)]
(np.sum(v_traderb_buy_msft1))

# Trader B Sells (MSFT)

v_traderb_sell_msft = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_msft1 = v_traderb_sell_msft[~np.isnan(v_traderb_sell_msft)]
(np.sum(v_traderb_sell_msft1))

# Trader B Closing Balance (MSFT)

# print((np.sum(v_traderb_buy_msft1)) - (np.sum(v_traderb_sell_msft1)))  

### 

# Trader B Buys (GOOGL)

v_traderb_buy_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_googl1 = v_traderb_buy_googl[~np.isnan(v_traderb_buy_googl)]
(np.sum(v_traderb_buy_googl1))

# Trader B Sells (GOOGL)

v_traderb_sell_googl = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_googl1 = v_traderb_sell_googl[~np.isnan(v_traderb_sell_googl)]
(np.sum(v_traderb_sell_googl1))

# Trader B Closing Balance (GOOGL)

# print((np.sum(v_traderb_buy_googl1)) - (np.sum(v_traderb_sell_googl1))) 

### 

# Trader B Buys (AMZN)

v_traderb_buy_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_amzn1 = v_traderb_buy_amzn[~np.isnan(v_traderb_buy_amzn)]
(np.sum(v_traderb_buy_amzn1))

# Trader B Sells (AMZN)

v_traderb_sell_amzn = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_amzn1 = v_traderb_sell_amzn[~np.isnan(v_traderb_sell_amzn)]
(np.sum(v_traderb_sell_amzn1))

# Trader B Closing Balance (AMZN)

# print((np.sum(v_traderb_buy_amzn1)) - (np.sum(v_traderb_sell_amzn1))) 

### 

# Trader B Buys (TSLA)

v_traderb_buy_tsla = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_tsla1 = v_traderb_buy_tsla[~np.isnan(v_traderb_buy_tsla)]
(np.sum(v_traderb_buy_tsla1))

# Trader B Sells (TSLA)

v_traderb_sell_tsla = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_tsla1 = v_traderb_sell_tsla[~np.isnan(v_traderb_sell_tsla)]
(np.sum(v_traderb_sell_tsla1))

# Trader B Closing Balance (TSLA)

# print((np.sum(v_traderb_buy_tsla1)) - (np.sum(v_traderb_sell_tsla1))) 

### 

# Trader B Buys (FB)

v_traderb_buy_fb = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_fb1 = v_traderb_buy_fb[~np.isnan(v_traderb_buy_fb)]
(np.sum(v_traderb_buy_fb1))

# Trader B Sells (FB)

v_traderb_sell_fb = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_fb1 = v_traderb_sell_fb[~np.isnan(v_traderb_sell_fb)]
(np.sum(v_traderb_sell_fb1))

# Trader B Closing Balance (FB)

# print((np.sum(v_traderb_buy_fb1)) - (np.sum(v_traderb_sell_fb1))) 

### 

# Trader B Buys (BRK.A)

v_traderb_buy_brka = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_brka1 = v_traderb_buy_brka[~np.isnan(v_traderb_buy_brka)]
(np.sum(v_traderb_buy_brka1))

# Trader B Sells (BRK.A)

v_traderb_sell_brka = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_brka1 = v_traderb_sell_brka[~np.isnan(v_traderb_sell_brka)]
(np.sum(v_traderb_sell_brka1))

# Trader B Closing Balance (BRK.A)

# print((np.sum(v_traderb_buy_brka1)) - (np.sum(v_traderb_sell_brka1))) 

### 

# Trader B Buys (V)

v_traderb_buy_v = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_v1 = v_traderb_buy_v[~np.isnan(v_traderb_buy_v)]
(np.sum(v_traderb_buy_v1))

# Trader B Sells (V)

v_traderb_sell_v = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_v1 = v_traderb_sell_v[~np.isnan(v_traderb_sell_v)]
(np.sum(v_traderb_sell_v1))

# Trader B Closing Balance (V)

# print((np.sum(v_traderb_buy_v1)) - (np.sum(v_traderb_sell_v1))) 

### 

# Trader B Buys (JPM)

v_traderb_buy_jpm = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_jpm1 = v_traderb_buy_jpm[~np.isnan(v_traderb_buy_jpm)]
(np.sum(v_traderb_buy_jpm1))

# Trader B Sells (JPM)

v_traderb_sell_jpm = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_jpm1 = v_traderb_sell_jpm[~np.isnan(v_traderb_sell_jpm)]
(np.sum(v_traderb_sell_jpm1))

# Trader B Closing Balance (JPM)

# print((np.sum(v_traderb_buy_jpm1)) - (np.sum(v_traderb_sell_jpm1))) 

### 

# Trader B Buys (JNJ)

v_traderb_buy_jnj = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_buy_jnj1 = v_traderb_buy_jnj[~np.isnan(v_traderb_buy_jnj)]
(np.sum(v_traderb_buy_jnj1))

# Trader B Sells (JNJ)

v_traderb_sell_jnj = np.where((trading_log['Trader'] == 'Trader B') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_traderb_sell_jnj1 = v_traderb_sell_jnj[~np.isnan(v_traderb_sell_jnj)]
(np.sum(v_traderb_sell_jnj1))

# Trader B Closing Balance (JNJ)

# print((np.sum(v_traderb_buy_jnj1)) - (np.sum(v_traderb_sell_jnj1))) 

### 

# Trader C

# Trader C Buys (AAPL)

v_traderc_buy_aapl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_aapl1 = v_traderc_buy_aapl[~np.isnan(v_traderc_buy_aapl)]
(np.sum(v_traderc_buy_aapl1))

# Trader C Sells (AAPL)

v_traderc_sell_aapl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_aapl1 = v_traderc_sell_aapl[~np.isnan(v_traderc_sell_aapl)]
(np.sum(v_traderc_sell_aapl1))

# Trader C Closing Balance (AAPL)

# print((np.sum(v_traderc_buy_aapl1)) - (np.sum(v_traderc_sell_aapl1))) 

### 

# Trader C Buys (MSFT)

v_traderc_buy_msft = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_msft1 = v_traderc_buy_msft[~np.isnan(v_traderc_buy_msft)]
(np.sum(v_traderc_buy_msft1))

# Trader C Sells (MSFT)

v_traderc_sell_msft = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_msft1 = v_traderc_sell_msft[~np.isnan(v_traderc_sell_msft)]
(np.sum(v_traderc_sell_msft1))

# Trader C Closing Balance (MSFT)

# print((np.sum(v_traderc_buy_msft1)) - (np.sum(v_traderc_sell_msft1)))  

### 

# Trader C Buys (GOOGL)

v_traderc_buy_googl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_googl1 = v_traderc_buy_googl[~np.isnan(v_traderc_buy_googl)]
(np.sum(v_traderc_buy_googl1))

# Trader C Sells (GOOGL)

v_traderc_sell_googl = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_googl1 = v_traderc_sell_googl[~np.isnan(v_traderc_sell_googl)]
(np.sum(v_traderc_sell_googl1))

# Trader C Closing Balance (GOOGL)

# print((np.sum(v_traderc_buy_googl1)) - (np.sum(v_traderc_sell_googl1))) 

### 

# Trader C Buys (AMZN)

v_traderc_buy_amzn = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_amzn1 = v_traderc_buy_amzn[~np.isnan(v_traderc_buy_amzn)]
(np.sum(v_traderc_buy_amzn1))

# Trader C Sells (AMZN)

v_traderc_sell_amzn = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_amzn1 = v_traderc_sell_amzn[~np.isnan(v_traderc_sell_amzn)]
(np.sum(v_traderc_sell_amzn1))

# Trader C Closing Balance (AMZN)

# print((np.sum(v_traderc_buy_amzn1)) - (np.sum(v_traderc_sell_amzn1))) 

### 

# Trader C Buys (TSLA)

v_traderc_buy_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_tsla1 = v_traderc_buy_tsla[~np.isnan(v_traderc_buy_tsla)]
(np.sum(v_traderc_buy_tsla1))

# Trader C Sells (TSLA)

v_traderc_sell_tsla = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_tsla1 = v_traderc_sell_tsla[~np.isnan(v_traderc_sell_tsla)]
(np.sum(v_traderc_sell_tsla1))

# Trader C Closing Balance (TSLA)

# print((np.sum(v_traderc_buy_tsla1)) - (np.sum(v_traderc_sell_tsla1))) 

### 

# Trader C Buys (FB)

v_traderc_buy_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_fb1 = v_traderc_buy_fb[~np.isnan(v_traderc_buy_fb)]
(np.sum(v_traderc_buy_fb1))

# Trader C Sells (FB)

v_traderc_sell_fb = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_fb1 = v_traderc_sell_fb[~np.isnan(v_traderc_sell_fb)]
(np.sum(v_traderc_sell_fb1))

# Trader C Closing Balance (FB)

# print((np.sum(v_traderc_buy_fb1)) - (np.sum(v_traderc_sell_fb1))) 

### 

# Trader C Buys (BRK.A)

v_traderc_buy_brka = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_brka1 = v_traderc_buy_brka[~np.isnan(v_traderc_buy_brka)]
(np.sum(v_traderc_buy_brka1))

# Trader C Sells (BRK.A)

v_traderc_sell_brka = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_brka1 = v_traderc_sell_brka[~np.isnan(v_traderc_sell_brka)]
(np.sum(v_traderc_sell_brka1))

# Trader C Closing Balance (BRK.A)

# print((np.sum(v_traderc_buy_brka1)) - (np.sum(v_traderc_sell_brka1))) 

### 

# Trader C Buys (V)

v_traderc_buy_v = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_v1 = v_traderc_buy_v[~np.isnan(v_traderc_buy_v)]
(np.sum(v_traderc_buy_v1))

# Trader C Sells (V)

v_traderc_sell_v = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_v1 = v_traderc_sell_v[~np.isnan(v_traderc_sell_v)]
(np.sum(v_traderc_sell_v1))

# Trader C Closing Balance (V)

# print((np.sum(v_traderc_buy_v1)) - (np.sum(v_traderc_sell_v1))) 

### 

# Trader C Buys (JPM)

v_traderc_buy_jpm = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_jpm1 = v_traderc_buy_jpm[~np.isnan(v_traderc_buy_jpm)]
(np.sum(v_traderc_buy_jpm1))

# Trader C Sells (JPM)

v_traderc_sell_jpm = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_jpm1 = v_traderc_sell_jpm[~np.isnan(v_traderc_sell_jpm)]
(np.sum(v_traderc_sell_jpm1))

# Trader C Closing Balance (JPM)

# print((np.sum(v_traderc_buy_jpm1)) - (np.sum(v_traderc_sell_jpm1))) 

### 

# Trader C Buys (JNJ)

v_traderc_buy_jnj = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_buy_jnj1 = v_traderc_buy_jnj[~np.isnan(v_traderc_buy_jnj)]
(np.sum(v_traderc_buy_jnj1))

# Trader C Sells (JNJ)

v_traderc_sell_jnj = np.where((trading_log['Trader'] == 'Trader C') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_traderc_sell_jnj1 = v_traderc_sell_jnj[~np.isnan(v_traderc_sell_jnj)]
(np.sum(v_traderc_sell_jnj1))

# Trader C Closing Balance (JNJ)

# print((np.sum(v_traderc_buy_jnj1)) - (np.sum(v_traderc_sell_jnj1))) 

### 

# Trader D

# Trader D Buys (AAPL)

v_traderd_buy_aapl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_aapl1 = v_traderd_buy_aapl[~np.isnan(v_traderd_buy_aapl)]
(np.sum(v_traderd_buy_aapl1))

# Trader D Sells (AAPL)

v_traderd_sell_aapl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AAPL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_aapl1 = v_traderd_sell_aapl[~np.isnan(v_traderd_sell_aapl)]
(np.sum(v_traderd_sell_aapl1))

# Trader D Closing Balance (AAPL)

# print((np.sum(v_traderd_buy_aapl1)) - (np.sum(v_traderd_sell_aapl1))) 

### 

# Trader D Buys (MSFT)

v_traderd_buy_msft = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_msft1 = v_traderd_buy_msft[~np.isnan(v_traderd_buy_msft)]
(np.sum(v_traderd_buy_msft1))

# Trader D Sells (MSFT)

v_traderd_sell_msft = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'MSFT'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_msft1 = v_traderd_sell_msft[~np.isnan(v_traderd_sell_msft)]
(np.sum(v_traderd_sell_msft1))

# Trader D Closing Balance (MSFT)

# print((np.sum(v_traderd_buy_msft1)) - (np.sum(v_traderd_sell_msft1)))  

### 

# Trader D Buys (GOOGL)

v_traderd_buy_googl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_googl1 = v_traderd_buy_googl[~np.isnan(v_traderd_buy_googl)]
(np.sum(v_traderd_buy_googl1))

# Trader D Sells (GOOGL)

v_traderd_sell_googl = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'GOOGL'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_googl1 = v_traderd_sell_googl[~np.isnan(v_traderd_sell_googl)]
(np.sum(v_traderd_sell_googl1))

# Trader D Closing Balance (GOOGL)

# print((np.sum(v_traderd_buy_googl1)) - (np.sum(v_traderd_sell_googl1))) 

### 

# Trader D Buys (AMZN)

v_traderd_buy_amzn = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_amzn1 = v_traderd_buy_amzn[~np.isnan(v_traderd_buy_amzn)]
(np.sum(v_traderd_buy_amzn1))

# Trader D Sells (AMZN)

v_traderd_sell_amzn = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'AMZN'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_amzn1 = v_traderd_sell_amzn[~np.isnan(v_traderd_sell_amzn)]
(np.sum(v_traderd_sell_amzn1))

# Trader D Closing Balance (AMZN)

# print((np.sum(v_traderd_buy_amzn1)) - (np.sum(v_traderd_sell_amzn1))) 

### 

# Trader D Buys (TSLA)

v_traderd_buy_tsla = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_tsla1 = v_traderd_buy_tsla[~np.isnan(v_traderd_buy_tsla)]
(np.sum(v_traderd_buy_tsla1))

# Trader D Sells (TSLA)

v_traderd_sell_tsla = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'TSLA'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_tsla1 = v_traderd_sell_tsla[~np.isnan(v_traderd_sell_tsla)]
(np.sum(v_traderd_sell_tsla1))

# Trader D Closing Balance (TSLA)

# print((np.sum(v_traderd_buy_tsla1)) - (np.sum(v_traderd_sell_tsla1))) 

### 

# Trader D Buys (FB)

v_traderd_buy_fb = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_fb1 = v_traderd_buy_fb[~np.isnan(v_traderd_buy_fb)]
(np.sum(v_traderd_buy_fb1))

# Trader D Sells (FB)

v_traderd_sell_fb = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'FB'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_fb1 = v_traderd_sell_fb[~np.isnan(v_traderd_sell_fb)]
(np.sum(v_traderd_sell_fb1))

# Trader D Closing Balance (FB)

# print((np.sum(v_traderd_buy_fb1)) - (np.sum(v_traderd_sell_fb1))) 

### 

# Trader D Buys (BRK.A)

v_traderd_buy_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_brka1 = v_traderd_buy_brka[~np.isnan(v_traderd_buy_brka)]
(np.sum(v_traderd_buy_brka1))

# Trader D Sells (BRK.A)

v_traderd_sell_brka = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'BRK.A'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_brka1 = v_traderd_sell_brka[~np.isnan(v_traderd_sell_brka)]
(np.sum(v_traderd_sell_brka1))

# Trader D Closing Balance (BRK.A)

# print((np.sum(v_traderd_buy_brka1)) - (np.sum(v_traderd_sell_brka1))) 

### 

# Trader D Buys (V)

v_traderd_buy_v = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_v1 = v_traderd_buy_v[~np.isnan(v_traderd_buy_v)]
(np.sum(v_traderd_buy_v1))

# Trader D Sells (V)

v_traderd_sell_v = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'V'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_v1 = v_traderd_sell_v[~np.isnan(v_traderd_sell_v)]
(np.sum(v_traderd_sell_v1))

# Trader D Closing Balance (V)

# print((np.sum(v_traderd_buy_v1)) - (np.sum(v_traderd_sell_v1))) 

### 

# Trader D Buys (JPM)

v_traderd_buy_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_jpm1 = v_traderd_buy_jpm[~np.isnan(v_traderd_buy_jpm)]
(np.sum(v_traderd_buy_jpm1))

# Trader D Sells (JPM)

v_traderd_sell_jpm = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JPM'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_jpm1 = v_traderd_sell_jpm[~np.isnan(v_traderd_sell_jpm)]
(np.sum(v_traderd_sell_jpm1))

# Trader D Closing Balance (JPM)

# print((np.sum(v_traderd_buy_jpm1)) - (np.sum(v_traderd_sell_jpm1))) 

### 

# Trader D Buys (JNJ)

v_traderd_buy_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Buy') & 
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_buy_jnj1 = v_traderd_buy_jnj[~np.isnan(v_traderd_buy_jnj)]
(np.sum(v_traderd_buy_jnj1))

# Trader D Sells (JNJ)

v_traderd_sell_jnj = np.where((trading_log['Trader'] == 'Trader D') & 
                       (trading_log['Order Type'] == 'Sell') &
                       (trading_log['Symbol'] == 'JNJ'), 
                       (trading_log['Fill Size']), np.nan)
v_traderd_sell_jnj1 = v_traderd_sell_jnj[~np.isnan(v_traderd_sell_jnj)]
(np.sum(v_traderd_sell_jnj1))

# Trader D Closing Balance (JNJ)

# print((np.sum(v_traderd_buy_jnj1)) - (np.sum(v_traderd_sell_jnj1))) 

##################################################################################################################################

# Additional Analysis Task: Analyze frequency / distribution of trades across different exchanges and symbols

# Frequency / distribution discrepancy between exchanges & specific securities

# CME & AAPL
f_cme_aapl = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'AAPL'),
                        trading_log['Price'], np.nan)
f_cme_aapl1 = f_cme_aapl[~np.isnan(f_cme_aapl)]
(len(f_cme_aapl1))

# LSE & AAPL
f_lse_aapl = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'AAPL'),
                        trading_log['Price'], np.nan)
f_lse_aapl1 = f_lse_aapl[~np.isnan(f_lse_aapl)]
(len(f_lse_aapl1))

# NYSE & AAPL
f_nyse_aapl = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'AAPL'),
                        trading_log['Price'], np.nan)
f_nyse_aapl1 = f_nyse_aapl[~np.isnan(f_nyse_aapl)]
(len(f_nyse_aapl1))

# NASDAQ & AAPL
f_nasdaq_aapl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'AAPL'),
                        trading_log['Price'], np.nan)
f_nasdaq_aapl1 = f_nasdaq_aapl[~np.isnan(f_nasdaq_aapl)]
(len(f_nasdaq_aapl1))

###

# CME & MSFT
f_cme_msft = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'MSFT'),
                        trading_log['Price'], np.nan)
f_cme_msft1 = f_cme_msft[~np.isnan(f_cme_msft)]
(len(f_cme_msft1))

# LSE & MSFT
f_lse_msft = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'MSFT'),
                        trading_log['Price'], np.nan)
f_lse_msft1 = f_lse_msft[~np.isnan(f_lse_msft)]
(len(f_lse_msft1))

# NYSE & MSFT
f_nyse_msft = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'MSFT'),
                        trading_log['Price'], np.nan)
f_nyse_msft1 = f_nyse_msft[~np.isnan(f_nyse_msft)]
(len(f_nyse_msft1))

# NASDAQ & MSFT
f_nasdaq_msft = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'MSFT'),
                        trading_log['Price'], np.nan)
f_nasdaq_msft1 = f_nasdaq_msft[~np.isnan(f_nasdaq_msft)]
(len(f_nasdaq_msft1))

### 

# CME & GOOGL
f_cme_googl = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'GOOGL'),
                        trading_log['Price'], np.nan)
f_cme_googl1 = f_cme_googl[~np.isnan(f_cme_googl)]
(len(f_cme_googl1))

# LSE & GOOGL
f_lse_googl = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'GOOGL'),
                        trading_log['Price'], np.nan)
f_lse_googl1 = f_lse_googl[~np.isnan(f_lse_googl)]
(len(f_lse_googl1))

# NYSE & GOOGL
f_nyse_googl = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'GOOGL'),
                        trading_log['Price'], np.nan)
f_nyse_googl1 = f_nyse_googl[~np.isnan(f_nyse_googl)]
(len(f_nyse_googl1))

# NASDAQ & GOOGL
f_nasdaq_googl = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'GOOGL'),
                        trading_log['Price'], np.nan)
f_nasdaq_googl1 = f_nasdaq_googl[~np.isnan(f_nasdaq_googl)]
(len(f_nasdaq_googl1))

###

# CME & AMZN
f_cme_amzn = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'AMZN'),
                        trading_log['Price'], np.nan)
f_cme_amzn1 = f_cme_amzn[~np.isnan(f_cme_amzn)]
(len(f_cme_amzn1))

# LSE & AMZN
f_lse_amzn = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'AMZN'),
                        trading_log['Price'], np.nan)
f_lse_amzn1 = f_lse_amzn[~np.isnan(f_lse_amzn)]
(len(f_lse_amzn1))

# NYSE & AMZN
f_nyse_amzn = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'AMZN'),
                        trading_log['Price'], np.nan)
f_nyse_amzn1 = f_nyse_amzn[~np.isnan(f_nyse_amzn)]
(len(f_nyse_amzn1))

# NASDAQ & AMZN
f_nasdaq_amzn = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'AMZN'),
                        trading_log['Price'], np.nan)
f_nasdaq_amzn1 = f_nasdaq_amzn[~np.isnan(f_nasdaq_amzn)]
(len(f_nasdaq_amzn1))

### 

# CME & TSLA
f_cme_tsla = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'TSLA'),
                        trading_log['Price'], np.nan)
f_cme_tsla1 = f_cme_tsla[~np.isnan(f_cme_tsla)]
(len(f_cme_tsla1))

# LSE & TSLA
f_lse_tsla = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'TSLA'),
                        trading_log['Price'], np.nan)
f_lse_tsla1 = f_lse_tsla[~np.isnan(f_lse_tsla)]
(len(f_lse_tsla1))

# NYSE & TSLA
f_nyse_tsla = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'TSLA'),
                        trading_log['Price'], np.nan)
f_nyse_tsla1 = f_nyse_tsla[~np.isnan(f_nyse_tsla)]
(len(f_nyse_tsla1))

# NASDAQ & TSLA
f_nasdaq_tsla = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'TSLA'),
                        trading_log['Price'], np.nan)
f_nasdaq_tsla1 = f_nasdaq_tsla[~np.isnan(f_nasdaq_tsla)]
(len(f_nasdaq_tsla1))

###

# CME & FB
f_cme_fb = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'FB'),
                        trading_log['Price'], np.nan)
f_cme_fb1 = f_cme_fb[~np.isnan(f_cme_fb)]
(len(f_cme_fb1))

# LSE & FB
f_lse_fb = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'FB'),
                        trading_log['Price'], np.nan)
f_lse_fb1 = f_lse_fb[~np.isnan(f_lse_fb)]
(len(f_lse_fb1))

# NYSE & FB
f_nyse_fb = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'FB'),
                        trading_log['Price'], np.nan)
f_nyse_fb1 = f_nyse_fb[~np.isnan(f_nyse_fb)]
(len(f_nyse_fb1))

# NASDAQ & FB
f_nasdaq_fb = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'FB'),
                        trading_log['Price'], np.nan)
f_nasdaq_fb1 = f_nasdaq_fb[~np.isnan(f_nasdaq_fb)]
(len(f_nasdaq_fb1))

###

# CME & BRK.A
f_cme_brka = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'BRK.A'),
                        trading_log['Price'], np.nan)
f_cme_brka1 = f_cme_brka[~np.isnan(f_cme_brka)]
(len(f_cme_brka1))

# LSE & BRK.A
f_lse_brka = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'BRK.A'),
                        trading_log['Price'], np.nan)
f_lse_brka1 = f_lse_brka[~np.isnan(f_lse_brka)]
(len(f_lse_brka1))

# NYSE & BRK.A
f_nyse_brka = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'BRK.A'),
                        trading_log['Price'], np.nan)
f_nyse_brka1 = f_nyse_brka[~np.isnan(f_nyse_brka)]
(len(f_nyse_brka1))

# NASDAQ & BRK.A
f_nasdaq_brka = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'BRK.A'),
                        trading_log['Price'], np.nan)
f_nasdaq_brka1 = f_nasdaq_brka[~np.isnan(f_nasdaq_brka)]
(len(f_nasdaq_brka1)) 

###

# CME & V
f_cme_v = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'V'),
                        trading_log['Price'], np.nan)
f_cme_v1 = f_cme_v[~np.isnan(f_cme_v)]
(len(f_cme_v1))

# LSE & V
f_lse_v = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'V'),
                        trading_log['Price'], np.nan)
f_lse_v1 = f_lse_v[~np.isnan(f_lse_v)]
(len(f_lse_v1))

# NYSE & V
f_nyse_v = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'V'),
                        trading_log['Price'], np.nan)
f_nyse_v1 = f_nyse_v[~np.isnan(f_nyse_v)]
(len(f_nyse_v1))

# NASDAQ & V
f_nasdaq_v = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'V'),
                        trading_log['Price'], np.nan)
f_nasdaq_v1 = f_nasdaq_v[~np.isnan(f_nasdaq_v)]
(len(f_nasdaq_v1)) 

###

# CME & JPM
f_cme_jpm = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'JPM'),
                        trading_log['Price'], np.nan)
f_cme_jpm1 = f_cme_jpm[~np.isnan(f_cme_jpm)]
(len(f_cme_jpm1))

# LSE & JPM
f_lse_jpm = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'JPM'),
                        trading_log['Price'], np.nan)
f_lse_jpm1 = f_lse_jpm[~np.isnan(f_lse_jpm)]
(len(f_lse_jpm1))

# NYSE & JPM
f_nyse_jpm = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'JPM'),
                        trading_log['Price'], np.nan)
f_nyse_jpm1 = f_nyse_jpm[~np.isnan(f_nyse_jpm)]
(len(f_nyse_jpm1))

# NASDAQ & JPM
f_nasdaq_jpm = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'JPM'),
                        trading_log['Price'], np.nan)
f_nasdaq_jpm1 = f_nasdaq_jpm[~np.isnan(f_nasdaq_jpm)]
(len(f_nasdaq_jpm1)) 

### 

# CME & JNJ
f_cme_jnj = np.where((trading_log['Exchange'] == 'CME') & 
                        (trading_log['Symbol'] == 'JNJ'),
                        trading_log['Price'], np.nan)
f_cme_jnj1 = f_cme_jnj[~np.isnan(f_cme_jnj)]
(len(f_cme_jnj1))

# LSE & JNJ
f_lse_jnj = np.where((trading_log['Exchange'] == 'LSE') & 
                        (trading_log['Symbol'] == 'JNJ'),
                        trading_log['Price'], np.nan)
f_lse_jnj1 = f_lse_jnj[~np.isnan(f_lse_jnj)]
(len(f_lse_jnj1))

# NYSE & JNJ
f_nyse_jnj = np.where((trading_log['Exchange'] == 'NYSE') & 
                        (trading_log['Symbol'] == 'JNJ'),
                        trading_log['Price'], np.nan)
f_nyse_jnj1 = f_nyse_jnj[~np.isnan(f_nyse_jnj)]
(len(f_nyse_jnj1))

# NASDAQ & JNJ
f_nasdaq_jnj = np.where((trading_log['Exchange'] == 'NASDAQ') & 
                        (trading_log['Symbol'] == 'JNJ'),
                        trading_log['Price'], np.nan)
f_nasdaq_jnj1 = f_nasdaq_jnj[~np.isnan(f_nasdaq_jnj)]
(len(f_nasdaq_jnj1)) 

# create dataframe of the frequency / distribution of all trades grouped by securities and exchanges 
frequency_security_exchange = pd.DataFrame(np.array([[len(f_cme_aapl1), len(f_lse_aapl1), len(f_nyse_aapl1), len(f_nasdaq_aapl1)],
                                        [len(f_cme_msft1), len(f_lse_msft1), len(f_nyse_msft1), len(f_nasdaq_msft1)],
                                        [len(f_cme_googl1), len(f_lse_googl1), len(f_nyse_googl1), len(f_nasdaq_googl1)],
                                        [len(f_cme_amzn1), len(f_lse_amzn1), len(f_nyse_amzn1), len(f_nasdaq_amzn1)],
                                        [len(f_cme_tsla1), len(f_lse_tsla1), len(f_nyse_tsla1), len(f_nasdaq_tsla1)],
                                        [len(f_cme_fb1), len(f_lse_fb1), len(f_nyse_fb1), len(f_nasdaq_fb1)],
                                        [len(f_cme_brka1), len(f_lse_brka1), len(f_nyse_brka1), len(f_nasdaq_brka1)], 
                                        [len(f_cme_v1), len(f_lse_v1), len(f_nyse_v1), len(f_nasdaq_v1)], 
                                        [len(f_cme_jpm1), len(f_lse_jpm1), len(f_nyse_jpm1), len(f_nasdaq_jpm1)], 
                                        [len(f_cme_jnj1), len(f_lse_jnj1), len(f_nyse_jnj1), len(f_nasdaq_jnj1)]]),
                                        index=['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'BRK.A', 'V', 'JPM', 'JNJ'], 
                                        columns=['CME', 'LSE', 'NYSE', 'NASDAQ'])
# print(frequency_security_exchange)


trading_log.to_csv('new_trading_log.csv')
trader_security_buy.to_csv('trader_security_buy.csv') 
trader_security_sell.to_csv('trader_security_sell.csv')
trader_security_fill.to_csv('trader_security_fill.csv')
exchange_security_buy.to_csv('exchange_security_buy.csv')
exchange_security_sell.to_csv('exchange_security_sell.csv')
exchange_security_volume.to_csv('exchange_security_volume.csv')
frequency_security_exchange.to_csv('frequency_security_exchange.csv')

