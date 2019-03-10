import math
import numpy

data= []

#for use when sorting by dist
def getDist(a):
	return a[0]

def getClass(a):
	return a[0]

#calculate the euclidean distance between two rows
#exclude the class feature
def euclidean_distance(a,b,feature_list):
	num_feat=len(a)-1
	i=1
	total=0
	while i<num_feat:
		if i in feature_list:
			total+=(math.pow(abs((float(b[i])-float(a[i]))),2))
		i=i+1
	return math.sqrt(total)

def nearest_neighbor(a,a_ind,feature_list):
	#keeps track of the distance and uses the key of the node to identify it
	distance_list=[]

	#find the distance between a and all other nodes
	for key,d in enumerate(data):

		#do not compare nodes against themselves
		if(key!=a_ind):
			dist=euclidean_distance(a,d,feature_list)
			node=(dist,key)

			#store distance and the key to the original list of records
			distance_list.append(node)

	#sort distance list
	distance_list= sorted(distance_list, key=getDist)
	nn_key=-1

	#get the first value in distance_list, this is the nearest neighbor
	for val in distance_list:
		nn_key=val[1]
		break

	print('Nearest neighbor class: '+str(data[nn_key][0]))
	return data[nn_key][0]

def feature_selection(num_features):
	current_set_of_features = []

	for i in range(1,num_features-1):
		feature_to_add_at_this_level = []
		best_so_far_accuracy    = 0

		for j in range(1,num_features-1):
			if not j in current_set_of_features:
				temp_features=current_set_of_features
				temp_features.append(j)





#open the file for reading and add to the list of lists
fn= raw_input('Welcome to Bertie Woosters Feature Selection Algorithm.\nType in the name of the file to test :\n ')
f = open(fn, "r")
num_features=0
for line in f:
   arr_line=line.split()
   data.append(arr_line)
   num_features=len(arr_line)-1
   #print(line)
message="\n\nThis dataset has "+str(num_features)+" features (not including the class attribute), with "
message=message+str(len(data))+" instances"
print(message)
nearest_neighbor(data[0],0)
feature_selection(num_features)