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

	#get rows and columns of matrix
	np.random.seed(693)
	a = np.random.randint(0, 10, size =(5,4))
	print a.shape
	# a.shape[0] rows
	# a.shape[1] columns

	#number of elements in the array
	print a.size

	#sum of all elements
	print a.sum()

	#(axis: 0 = rows 1 = columns) sum specific direction of array
	print a.sum(axis=0)
	print a.sum(axis=1)

	#max and min in each row
	print a.min(axis=0)
	print a.max(axis=1)
	print a.mean()


	#find index of max element in array
	print np.argmax(a)


	#access elements
	print a[3,2]
	print a[0,1:3]

	#modifying element
	a[0,0] = 93
	a[1,:] = 6
	a[:,3] = [1,2,3,4,5]
	print a
	
	#indexing array
	indices = np.array([1,1,2,3])
	print a[indices]

	#boolean mask arrays
	mean = a.mean()
	print a[a<mean]

	#multiply all by 2
	print 2*a

	#matrix mulitplication and addition is the same as linear algebra

if __name__ == "__main__":
	test_run()
