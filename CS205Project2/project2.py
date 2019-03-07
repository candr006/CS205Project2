import math
import numpy

data= []
def getDist(a):
	return a[0]

def euclidean_distance(a,b):
	num_feat=len(a)-1
	i=1
	total=0
	while i<num_feat:
		#print("Float a: "+str(float(a[i]))+"  Float b: "+str(float(b[i])))
		total+=(math.pow(abs((float(b[i])-float(a[i]))),2))
		i=i+1
	return math.sqrt(total)

def nearest_neighbor(a,a_ind):
	#keeps track of the distance and uses the key of the node to identify it
	distance_list=[]
	key_list=[]

	#find the distance between a and all other nodes
	for key,d in enumerate(data):
		#do not compare nodes against themselves
		if(key!=a_ind):
			dist=euclidean_distance(a,d)
			print('key: '+str(key)+' - Dist: '+str(dist))
			node=(dist,key)
			distance_list.append(node)
			key_list.append(key)

	#sort distance list
	distance_list= sorted(distance_list, key=getDist)
	nn_key=-1
	for val in distance_list:
		nn_key=val[1]
		print("neighbor : "+str(val[0]))
		break
	#print('Original node: '+str(data[0]))
	print('nnkey: '+str(nn_key))
	print('Nearest neighbor: '+str(data[nn_key]))
	return data[key]


#open the file for reading and add to the list of lists - 23-34
f = open("test.txt", "r")
for line in f:
   data.append(line.split())
   #print(line)
nearest_neighbor(data[0],0)