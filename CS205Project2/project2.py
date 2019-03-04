import math

data= []

def euclidean_distance(a,b):
	num_feat=len(a)-1
	i=1
	total=0
	while i<num_feat:
		total+=(math.pow((float(b[i])-float(a[i])),2))
		i=i+1
	return math.sqrt(total)

def nearest_neighbor(a):
	#keeps track of the distance and uses the key of the node to identify it
	distance_list=[]
	#find closest neighbor to a in data
	for d in data:
		print(euclidean_distance(a,d))



#open the file for reading and add to the list of lists - 23-34
f = open("small_input.txt", "r")
for line in f:
   data.append(line.split())
   #print(line)
nearest_neighbor(data[0])