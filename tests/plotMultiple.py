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

def plot_data(df):
	#normalizes data
	df = df/df.ix[0,:]

	#creates plot
	title = "Stock Prices"
	ax = df.plot(title=title,fontsize=2)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()
	
if __name__ == '__main__':
	df = test_run()
	print df.mean()
	print df.std()
	plot_data(df)	
