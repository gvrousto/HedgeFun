import numpy as np

def test_run():
	#1D array
	print np.array([2,3,4])

	print
	
	#2D array
	print np.array([(2,3,4),(5,6,7)])

	print

	#random array
	print np.empty(5)
	print np.empty((5,4))

	print

	#array filled with ones
	print np.ones((5,4))	

	print

	#specify datatype
	print np.ones((5,4), dtype=np.int_)	

	print

	#create random array
	print np.random.random((5,4))

	print

	#create random array with tuple
	print np.random.rand(5,4)


	
if __name__ == "__main__":
	test_run()
