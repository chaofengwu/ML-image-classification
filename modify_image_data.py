import numpy as np
import image_processing
from sklearn.decomposition import PCA
import json
import image_metadata


def pca_value(input_data, n_components):
	pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True)
	# pca = PCA()
	a = pca.fit_transform(np.array(input_data))
	# print(a.explained_variance_ratio_)
	# print(a.singular_values_)
	return a#.singular_values_

def add(x,y): 
	return x+y

###### for dimension, nothing to do ###### 2

###### for color, divided into group, 255-251, 250-169, 168-87, 86-5, 4-0 ###### 5

###### for histo, PCA to 6 ###### 6

###### for mean, may get avarage pixel ###### 4*3

###### for PCA_image, PCA image to 10 ###### 10

def modify_color(co):
	res = [0,0,0,0,0]
	temp = 0
	# print(co)
	for idx in range(len(co)):
		a = 1
		temp += co[idx][0]
		if (co[idx][1]) < 5:
			res[0] += co[idx][0]
		elif co[idx][1] < 87:
			res[1] += co[idx][0]
		elif co[idx][1] < 169:
			res[2] += co[idx][0]
		elif co[idx][1] < 251:
			res[3] += co[idx][0]
		elif co[idx][1] < 256:
			res[4] += co[idx][0]
		else:
			print('modify color: color index out of range')
	return [i / temp for i in res]


def modify_histogram(hi):
	res = []
	temp = [hi[0:255],hi[255:510],hi[510:765]]
	# print(temp)
	# for i in range(3):
		# res += [pca_value([temp[i],[1]*255],2).tolist()]
	res += [pca_value(temp,2).tolist()]
	return res


def modify_square(sq):
	n = len(sq)
	h = len(sq[0])
	# try:
	w = len(sq[0][0])
	#rint(sq)
	# print('\n\n\n\n\n')
	total = h*w
	ttt = []
	res = []
	for k in range(n):
		temp = [0,0,0]
		for i in range(h):
			for j in range(w):
				temp = map(add, (sq[k][i][j]), temp)
		t = list(temp)
		res += [[i/total for i in t]]
		# res += [sum([i/total for i in t])/3]
	# print(res)
	return res
	# except:
	# 	print('==============')
	# 	return sq
	

def modify_pca_image(pca_ima):
	return

def modify_image_metadata():
	###### First get raw image data and then modify them
	raw_image_matadata = []
	# dimension = []
	# mode = []
	# color = []
	# histo = []
	# square = []
	# pca_ima = []
	count = 1
	try:
		# with open("modified_data.json") as json_file:
		# 		[dimension, mode, color, histo, square, extrema] = json.load(json_file)
		with open("data.json") as json_file:
			[dimension, histo, square] = json.load(json_file)
	except:
		with open("data.json") as json_file:
			[dimension, histo, square] = json.load(json_file)


	# # print(color[0])
	# print(histo[0])
	# print(square[0])
		for i in range(len(dimension)):
			# print(i)
			if dimension[i] != [-1,-1]:
				# print(dimension[i])
				color[i] = modify_color(color[i])
				histo[i] = modify_histogram(histo[i])
				square[i] = modify_square(square[i])
			else:
				color[i] = [0,0,0,0,0]
				histo[i] = [[0,0],[0,0],[0,0]]
				square[i] = [0,0,0]
		with open('modified_data.json', 'w') as outfile:
			json.dump([dimension, color, histo, square], outfile)
			# print(histo)
	
	return [dimension, histo, square]

# [dimension, mode, color, histo, pca_ima, square] = modify_image_metadata(['/home/chaofeng/Documents/practicum/copy_images/images/s04ialk.jpg', '/home/chaofeng/Documents/practicum/copy_images/images/septalkmap.jpg','/home/chaofeng/Documents/practicum/copy_images/images/SAVE_All.jpg', '/home/chaofeng/Documents/practicum/copy_images/images/sr3dic.jpg', '/home/chaofeng/Documents/practicum/copy_images/images/TH2012.jpg'])

# print(square)
