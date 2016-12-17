import sys
import numpy as np
import json

# https://www.quantiacs.com/For-Quants/GetStarted/Markets.aspx
futuresList = ['F_AD', 'F_BO', 'F_BP', 'F_C', 'F_CC', 'F_CD', 'F_CL', 'F_CT', 'F_DX', 'F_EC', 'F_ED', 'F_ES', 'F_FC', 'F_FV', 'F_GC', 'F_HG', 'F_HO', 'F_JY', 'F_KC', 'F_LB', 'F_LC', 'F_LN', 'F_MD', 'F_MP', 'F_NG', 'F_NQ', 'F_NR', 'F_O', 'F_OJ', 'F_PA', 'F_PL', 'F_RB', 'F_RU', 'F_S', 'F_SB', 'F_SF', 'F_SI', 'F_SM', 'F_TU', 'F_TY', 'F_US', 'F_W', 'F_XX', 'F_YM', 'F_AX', 'F_CA', 'F_DT', 'F_UB', 'F_UZ']
stocksList = ['AAPL', 'MMM', 'ABT', 'ABBV', 'ACN', 'ALL', 'MO', 'AMZN', 'AEP', 'AXP', 'AIG', 'AMGN', 'APC', 'APA', 'AAPL', 'T', 'BAC', 'BK', 'BAX', 'BRK.B', 'BA', 'BMY', 'COF', 'CAT', 'CVX', 'CSCO', 'C', 'KO', 'CL', 'CMCSA', 'COP', 'COST', 'CVS', 'DVN', 'DOW', 'DD', 'EBAY', 'EMC', 'EMR', 'EXC', 'XOM', 'FB', 'FDX', 'F', 'FCX', 'GD', 'GE', 'GM', 'GILD', 'GS', 'GOOG', 'GOOGL', 'HAL', 'HPQ', 'HD', 'HON', 'INTC', 'IBM', 'JNJ', 'JPM', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDT', 'MRK', 'MET', 'MSFT', 'MDLZ', 'MON', 'MS', 'NOV', 'NKE', 'NSC', 'OXY', 'ORCL', 'PEP', 'PFE', 'PM', 'PG', 'QCOM', 'RTN', 'SLB', 'SPG', 'SO', 'SBUX', 'TGT', 'TXN', 'TWX', 'FOXA', 'USB', 'UNP', 'UPS', 'UTX', 'UNH', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'WFC', 'A', 'AA', 'ABC', 'ACE', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADS', 'ADSK', 'ADT', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AIV', 'AIZ', 'AKAM', 'ALLE', 'ALTR', 'ALXN', 'AMAT', 'AME', 'AMG', 'AMP', 'AMT', 'AN', 'AON', 'APD', 'APH', 'ARG', 'ATI', 'AVB', 'AVGO', 'AVP', 'AVY', 'AZO', 'BBBY', 'BBT', 'BBY', 'BCR', 'BDX', 'BEN', 'BF.B', 'BHI', 'BLK', 'BLL', 'BMS', 'BRCM', 'BSX', 'BWA', 'BXP', 'CA', 'CAG', 'CAH', 'CAM', 'CB', 'CBG', 'CBS', 'CCE', 'CCI', 'CCL', 'CELG', 'CERN', 'CF', 'CHK', 'CHRW', 'CI', 'CINF', 'CLX', 'CMA', 'CME', 'CMG', 'CMI', 'CMS', 'CNP', 'CNX', 'COG', 'COH', 'COL', 'CPB', 'CRM', 'CSC', 'CSX', 'CTAS', 'CTL', 'CTSH', 'CTXS', 'CVC', 'D', 'DAL', 'DE', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DISCA', 'DISCK', 'DLPH', 'DLTR', 'DNB', 'DNR', 'DO', 'DOV', 'DPS', 'DRI', 'DTE', 'DUK', 'DVA', 'EA', 'ECL', 'ED', 'EFX', 'EIX', 'EL', 'EMN', 'EOG', 'EQR', 'EQT', 'ESRX', 'ESS', 'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXPD', 'EXPE', 'FAST', 'FE', 'FFIV', 'FIS', 'FISV', 'FITB', 'FLIR', 'FLR', 'FLS', 'FMC', 'FOSL', 'FSLR', 'FTI', 'FTR', 'GAS', 'GCI', 'GGP', 'GIS', 'GLW', 'GMCR', 'GME', 'GNW', 'GPC', 'GPS', 'GRMN', 'GT', 'GWW', 'HAR', 'HAS', 'HBAN', 'HCBK', 'HCN', 'HCP', 'HES', 'HIG', 'HOG', 'HOT', 'HP', 'HRB', 'HRL', 'HRS', 'HST', 'HSY', 'HUM', 'ICE', 'IFF', 'INTU', 'IP', 'IPG', 'IR', 'IRM', 'ISRG', 'ITW', 'IVZ', 'JCI', 'JEC', 'JNPR', 'JOY', 'JWN', 'K', 'KEY', 'KIM', 'KLAC', 'KMB', 'KMI', 'KMX', 'KORS', 'KR', 'KSS', 'KSU', 'L', 'LB', 'LEG', 'LEN', 'LH', 'LLL', 'LLTC', 'LM', 'LNC', 'LRCX', 'LUK', 'LUV', 'LVLT', 'LYB', 'M', 'MAC', 'MAR', 'MAS', 'MAT', 'MCHP', 'MCK', 'MCO', 'MHFI', 'MHK', 'MJN', 'MKC', 'MLM', 'MMC', 'MNK', 'MNST', 'MOS', 'MPC', 'MRO', 'MSI', 'MTB', 'MU', 'MUR', 'MYL', 'NAVI', 'NBL', 'NBR', 'NDAQ', 'NE', 'NEE', 'NEM', 'NFLX', 'NFX', 'NI', 'NLSN', 'NOC', 'NRG', 'NTAP', 'NTRS', 'NUE', 'NVDA', 'NWL', 'NWSA', 'OI', 'OKE', 'OMC', 'ORLY', 'PAYX', 'PBCT', 'PBI', 'PCAR', 'PCG', 'PCL', 'PCLN', 'PCP', 'PDCO', 'PEG', 'PFG', 'PGR', 'PH', 'PHM', 'PKI', 'PLD', 'PNC', 'PNR', 'PNW', 'POM', 'PPG', 'PPL', 'PRGO', 'PRU', 'PSA', 'PSX', 'PVH', 'PWR', 'PX', 'PXD', 'QEP', 'R', 'RAI', 'REGN', 'RF', 'RHI', 'RHT', 'RIG', 'RL', 'ROK', 'ROP', 'ROST', 'RRC', 'RSG', 'SCG', 'SCHW', 'SE', 'SEE', 'SHW', 'SJM', 'SNA', 'SNDK', 'SNI', 'SPLS', 'SRCL', 'SRE', 'STI', 'STJ', 'STT', 'STX', 'STZ', 'SWK', 'SWN', 'SYK', 'SYMC', 'SYY', 'TAP', 'TDC', 'TE', 'TEL', 'THC', 'TIF', 'TJX', 'TMK', 'TMO', 'TRIP', 'TROW', 'TRV', 'TSCO', 'TSN', 'TSO', 'TSS', 'TWC', 'TXT', 'TYC', 'UA', 'UHS', 'UNM', 'URBN', 'URI', 'VAR', 'VFC', 'VIAB', 'VLO', 'VMC', 'VNO', 'VRSN', 'VRTX', 'VTR', 'WAT', 'WDC', 'WEC', 'WFM', 'WHR', 'WIN', 'WM', 'WMB', 'WU', 'WY', 'WYN', 'WYNN', 'XEC', 'XEL', 'XL', 'XLNX', 'XRAY', 'XRX', 'XYL', 'YHOO', 'YUM', 'ZION', 'ZTS' ]
settings = {}

dates = {'20010102', '20020102', '20030102', '20040102', '20050103', '20060103', '20070103', '20080102', '20090102', '20100104', '20110103', '20120103', '20130102', '20140102', '20150102', '20160104'}
settings['markets'] = stocksList[:int(sys.agv[1])]
settings['beginInSample'] = '20020506'
settings['endInSample'] = '20150506'
settings['budget'] = 10**6
settings['slippage'] = 0.05
settings['window_size'] = 40
settings['lookback'] = settings['window_size']
settings['topk'] = 50
settings['band'] = 10

def topk(newData, oldSet, band):
    '''Selects the top k elements from newData where k is the length of the oldSet
    An item will be added if its rank falls below the k - band.
    An item will be removed if its rank rises above the k + band
    If there are too many items, the worst will be removed.
    If there are too few items, the best will be added.

    newData: numpy array
    oldSet: python set
    band: integer
    returns a set'''
    ranking = newData.argsort()
    newSet = set()

    # retain old ones that haven't fallen below the threshold
    for x in oldSet:
        if ranking[x] < len(oldSet) + band:
            newSet.add(x)

    # add new ones that have risen above the threshold
    for x in ranking[:len(oldSet) - band]:
        newSet.add(x)

    while len(newSet) > len(oldSet):
        # we have added too many, take out the largest in the set
        maxx = max([(ranking[x], x) for x in newSet])[1]
        newSet.remove(maxx)

    while len(newSet) < len(oldSet):
        # we have added too few, add the smallest not in the set
        minx = min([(ranking[x], x) for x in range(0, len(newData)) if x not in newSet])[1]
        newSet.add(minx)

    return newSet

def last(data):
    return data[-1, :]

def window(data, window_size):
    s = np.mean(data[-window_size:, :], axis=0)
    assert(s.shape == last(data).shape)
    return s

def diff_window(data, window_size):
    return last(data) - window(data, window_size)

def stddev(data, window_size):
    return np.sqrt(np.sum(
        (data - window(data, window_size)[np.newaxis, :])**2) / len(data))

def sharpe_window(data, window_size):
    return (last(data) - window(data, window_size)) / stddev(data, window_size)

with open('marketcap_data.json') as file:
    marketcap_data = json.load(file)

def get_market_cap(stocks, date):
    output = np.zeros(len(stocks))
    if date in marketcap_data:
        for i, stock in enumerate(stocks):
            if stock in marketcap_data[date]:
                price = float(marketcap_data[data][stock][7])
                shares = int(marketcap_data[data][stock][8])
                output[i] = price * shares
    return output

def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings):
    if str(DATE[-1]) in dates:
        print(DATE[-1])
        return myTradingSystem2(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings)
    else:
        return exposure[-1], settings

def myTradingSystem2(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings):
    historical_points, n_markets = CLOSE.shape

    data = get_market_cap(settings['markets'], DATE[-1])

    if not hasattr(myTradingSystem, 'portfolio'):
        myTradingSystem.portfolio = set()
        newPortfolio = set(data.argsort()[:settings['topk']])
    else:
        newPortfolio = topk(data, myTradingSystem.portfolio, settings['band'])

    #assert(all([x < n_markets for x in newPortfolio]) and len(newPortfolio) == settings['topk'])
    pos = np.zeros(n_markets)
    pos[list(newPortfolio)] = 1

    if newPortfolio ^ myTradingSystem.portfolio:
        print(newPortfolio ^ myTradingSystem.portfolio)
    myTradingSystem.portfolio = newPortfolio

    return pos, settings

def mySettings():
    # np.genfromtxt('569c0745d53595a1.csv', delimiter=',', skip_header=1)
    return settings

# Evaluate trading system defined in current file.
if __name__ == '__main__':
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)

# 20130506 to 20140506
# raw: 2.9187, 5.7206
# window: 2.8240, 5.5459
# diff_window: 1.5858, 2.6302
# sharpe_window: 1.9894, 3.2374
