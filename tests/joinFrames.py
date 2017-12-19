import pandas as pd
import matplotlib.pyplot as plt

def test_run():
	start_date = '2016-12-18'
	end_date = '2017-12-18'
	dates = pd.date_range(start_date, end_date)
	emptydf = pd.DataFrame(index=dates)

	spydf = pd.read_csv('SPY.csv',index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
	

	#rename title of column to prevent future clash
	spydf = spydf.rename(columns = {'Adj Close' : 'SPY'})
	


	#only includes values for index that appear in left table
	emptydf = emptydf.join(spydf, how='inner')
	
	symbols = ['GOOG', 'AAPL']
	for symbol in symbols:
		temp_df = pd.read_csv('{}.csv'.format(symbol),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
		temp_df = temp_df.rename(columns = {'Adj Close' : symbol})
		emptydf = emptydf.join(temp_df, how='inner')

	print emptydf

if __name__ == '__main__':
	test_run()
