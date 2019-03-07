import math
import numpy

data= []

#for use when sorting by dist
def getDist(a):
	return a[0]

#calculate the euclidean distance between two rows
#exclude the class feature
def euclidean_distance(a,b):
	num_feat=len(a)-1
	i=1
	total=0
	while i<num_feat:
		total+=(math.pow(abs((float(b[i])-float(a[i]))),2))
		i=i+1
	return math.sqrt(total)

def nearest_neighbor(a,a_ind):
	#keeps track of the distance and uses the key of the node to identify it
	distance_list=[]

	#find the distance between a and all other nodes
	for key,d in enumerate(data):

		#do not compare nodes against themselves
		if(key!=a_ind):
			dist=euclidean_distance(a,d)
			node=(dist,key)
			distance_list.append(node)

	#sort distance list
	distance_list= sorted(distance_list, key=getDist)
	nn_key=-1

	#get the first value in distance_list, this is the nearest neighbor
	for val in distance_list:
		nn_key=val[1]
		break

	print('Nearest neighbor: '+str(data[nn_key]))
	return data[nn_key]


#open the file for reading and add to the list of lists - 23-34
f = open("test.txt", "r")
for line in f:
   data.append(line.split())
   #print(line)
nearest_neighbor(data[0],0)