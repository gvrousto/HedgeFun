import pandas as pd
import matplotlib.pyplot as plt

def test_run():
	df = pd.read_csv("./AAPL.csv")
	df['High'].plot()
	plt.show()

if __name__ == '__main__':
	test_run()
