import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def test_run():
	start_date = '2017-7-18'
	end_date = '2017-12-18'
	dates = pd.date_range(start_date, end_date)
	emptydf = pd.DataFrame(index=dates)

	#SPY always has to be first for reference
	symbols = ['SPY','GOOG', 'AAPL']
	
	for symbol in symbols:
		#create dataframe from csv
		temp_df = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
		
		#rename to prevent clash
		temp_df = temp_df.rename(columns = {'Adj Close' : symbol})
		#left join to empty dataframe
		emptydf = emptydf.join(temp_df, how='inner')

	return emptydf

if __name__ == '__main__':
	df = test_run()
	print df
	
	print df.ix['2017-10-10':'2017-11-11']
	
	print df['GOOG']
	print df[['GOOG', 'AAPL']]
	
	print df.ix['2017-10-10':'2017-11-11',['GOOG','AAPL']]
	
	
