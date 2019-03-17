import math
import numpy

data= []

#for use when sorting by dist
def getDist(a):
	return a[0]

def getClass(a):
	return a[0]

def returnAccuracy(a):
	return a[1]

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

def nearest_neighbor_class(a,a_ind,feature_list,data_list=data):
	#keeps track of the distance and uses the key of the node to identify it
	distance_list=[]

	#find the distance between a and all other nodes
	for key,d in enumerate(data_list):

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

	return data_list[nn_key][0]

def getAccuracy(data,feature_list):
	num_correct=0

	for key,d in enumerate(data):
		nn_class=nearest_neighbor_class(d,key,feature_list)

		#if the classification of nn is correct then add to correct count
		if d[0]==nn_class:
			num_correct=num_correct+1

	return (float(num_correct)/float(len(data)))


def leave_one_out_cv(num_features):
	k=1
	features=[]
	while k<=num_features:
		features.append(k)
		k=k+1

	num_rows=len(data)
	num_correct=0

	#loop through all the instances, leave one instance out at each run
	#run nearest neighbor and check if the instance is classified correctly
	for i in range(0,num_rows-1):
		temp_data=data[:]
		a=temp_data.pop(i)

		nn_class=nearest_neighbor_class(a,i,features)

		#if the classification of nn is correct then add to correct count
		if(a[0]==nn_class):
			num_correct=num_correct+1

	print("Running nearest neighbor with all features, using 'leaving-one-out' evaluation, I get an accuracy of : "+str(float(num_correct)/float(num_rows)))


def forward_selection(num_features):
	current_set_of_features = []
	best_overall_features=[]
	best_overall_accuracy=float(0)

	print("\nBeginning Search\n")

	#start with 1 feature and add a feature at every level
	for i in range(1,num_features+1):
		feature_to_add_at_this_level = 0
		best_so_far_accuracy=float(0)

		for j in range(1,num_features+1):

			if j not in current_set_of_features:

				#temporarily add j to the set of features and test its accuracy
				temp_features=current_set_of_features[:]
				temp_features.append(j)
				accuracy=getAccuracy(data,temp_features)
				print('     Using features '+str(temp_features)+' accuracy is: '+str(accuracy))

				#if the new feature set is better than the bsf at this level, then add j to current feature set
				if accuracy>best_so_far_accuracy:
					best_so_far_accuracy=accuracy
					feature_to_add_at_this_level=j
					

		current_set_of_features.append(feature_to_add_at_this_level)

		#keep track of the best overall features and accuracy
		if(best_so_far_accuracy>best_overall_accuracy):
			best_overall_accuracy=best_so_far_accuracy
			best_overall_features=current_set_of_features[:]

		print("\nFeature set "+str(current_set_of_features)+" was best, accuracy is: "+str(best_so_far_accuracy)+"\n")

	print("\nFinished Search!!! The best feature subset is "+str(best_overall_features)+" with an accuracy of "+str(best_overall_accuracy)+"\n")


def backward_elimination(num_features):
	k=1
	current_set_of_features=[]
	while k<=num_features:
		current_set_of_features.append(k)
		k=k+1
	best_overall_features=[]
	best_overall_accuracy=float(0)

	i=num_features
	j=num_features

	print("\nBeginning Search\n")

	#start with all features and remove a feature at every level
	for j in range(1,num_features):
		feature_to_remove_at_this_level = 0
		best_so_far_accuracy=float(0)
		j=num_features

		for j in range(1,num_features+1):

			if j in current_set_of_features:

				#temporarily remove j from the set of features and test its accuracy
				temp_features=current_set_of_features[:]
				ri=temp_features.index(j)
				temp_features.pop(ri)
				accuracy=getAccuracy(data,temp_features)
				print('     Using features '+str(temp_features)+' accuracy is: '+str(accuracy))

				#if the new feature set is better than the bsf at this level, then add j to current feature set
				if accuracy>best_so_far_accuracy:
					best_so_far_accuracy=accuracy
					feature_to_remove_at_this_level=j

		ri=current_set_of_features.index(feature_to_remove_at_this_level)
		current_set_of_features.pop(ri)

		#keep track of the best overall features and accuracy
		if(best_so_far_accuracy>=best_overall_accuracy):
			best_overall_accuracy=best_so_far_accuracy
			best_overall_features=current_set_of_features[:]
		print("\nFeature set "+str(current_set_of_features)+" was best, accuracy is: "+str(best_so_far_accuracy)+"\n")

	print("\nFinished Search!!! The best feature subset is "+str(best_overall_features)+" with an accuracy of "+str(best_overall_accuracy)+"\n")
 
 
def original_algorithm(num_features):
	k=1
	current_set_of_features=[]

	#start with all features in the set
	while k<=num_features:
		current_set_of_features.append(k)
		k=k+1
	best_overall_features=[]
	best_overall_accuracy=float(0)

	print("\nBeginning Search\n")
	i=1
	while len(current_set_of_features)>0:
		if (len(current_set_of_features)>1) and (i>1):

			#halve the current set of features
			first_half=current_set_of_features[:len(current_set_of_features)//2]
			second_half=current_set_of_features[len(current_set_of_features)//2:]

			if(len(first_half)<len(second_half)):
				first_half.append(second_half[0])

			#get the accuracy of each half of the features
			first_accuracy=getAccuracy(data,first_half)
			print('     Using features '+str(first_half)+' accuracy is: '+str(first_accuracy))

			second_accuracy=getAccuracy(data,second_half)
			print('     Using features '+str(second_half)+' accuracy is: '+str(second_accuracy))
			
			#choose the better of the two halves' accuracies
			if first_accuracy>second_accuracy:
				current_set_of_features=first_half[:]
				best_so_far_accuracy=first_accuracy
			else:
				current_set_of_features=second_half[:]
				best_so_far_accuracy=second_accuracy
      
		else:
			best_so_far_accuracy=getAccuracy(data,current_set_of_features)
			print('     Using features '+str(current_set_of_features)+' accuracy is: '+str(best_so_far_accuracy))

		#keep track of the best overall accuracy
		if(best_so_far_accuracy>=best_overall_accuracy):
			best_overall_accuracy=best_so_far_accuracy
			best_overall_features=current_set_of_features[:]
		print("\nFeature set "+str(current_set_of_features)+" was best, accuracy is: "+str(best_so_far_accuracy)+"\n")

		#stop when there is only 1 feature in the set
		if len(current_set_of_features)<2:
			break
		i=i+1

	print("\nFinished Search!!! The best feature subset is "+str(best_overall_features)+" with an accuracy of "+str(best_overall_accuracy)+"\n")



#open the file for reading and add to the list of lists
fn= raw_input('Welcome to Bertie Woosters Feature Selection Algorithm.\nType in the name of the file to test :\n ')
f = open(fn, "r")
num_features=0
for line in f:
   arr_line=line.split()
   data.append(arr_line)
   num_features=len(arr_line)-1

#take user choice
ui=raw_input("\n\nType the number of the Algorithm you want to run:\n1.Forward Selection\n2.Backward Elimination\n3.Original Algorithm\n\n")
message="\n\nThis dataset has "+str(num_features)+" features (not including the class attribute), with "
message=message+str(len(data))+" instances\n"
print(message)

#run leave one out cross validation
leave_one_out_cv(num_features)

#let user pick the algorithm to run
if ui=='1':
	forward_selection(num_features)
if ui=='2':
	backward_elimination(num_features)
if ui=='3':
	original_algorithm(num_features)