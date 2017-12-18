import pandas as pd

def test_run():

	df = pd.read_csv("./AAPL.csv")

	print "High column max = " 
	print df['High'].max()
	print "High column mean = " 
	print df['High'].mean()
	print "High column min = "
	print df['High'].min()

	print df

if __name__ == '__main__':
	test_run()
