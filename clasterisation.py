import random
import math
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import os
file_paths = list()
"""
for i in range(1, 7931):
    file_paths.append(str(i)+".jpg")
print(file_paths)

for i in file_paths:
    try:
        image = Image.open('E:/OneDrive/SPBU/Clasterisation_group/skins/'+i)
        cropped = image.convert('L').crop((8,8, 16, 16))
        cropped.save('E:/OneDrive/SPBU/Clasterisation_group/cropped_images/'+i)
    except:
        image = Image.open('E:/OneDrive/SPBU/Clasterisation_group/skins/1.jpg')
        cropped = image.convert('L').crop((8, 8, 16, 16))
        cropped.save('E:/OneDrive/SPBU/Clasterisation_group/cropped_images/' + i)
coded_faces = list()
from sklearn.cluster import AgglomerativeClustering
for i in file_paths:
    image = Image.open('E:/OneDrive/SPBU/Clasterisation_group/cropped_images/'+i)

    pixels = image.load()
    width, height = 8, 8

    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    coded_faces.append(all_pixels)

single_clustering = AgglomerativeClustering(n_clusters=5, linkage='single').fit(coded_faces)
average_clustering = AgglomerativeClustering(n_clusters=5, linkage='average').fit(coded_faces)
ward_clustering = AgglomerativeClustering(n_clusters=5, linkage='ward').fit(coded_faces)
for i in range(7930):
    image = Image.open('E:/OneDrive/SPBU/Clasterisation_group/cropped_images/' + str(i+1)+'.jpg')
    path = 'E:/OneDrive/SPBU/Clasterisation_group/single/'+str(single_clustering.labels_[i]+1) +'/' +str(i+1)+'.jpg'
    image.save(path)
for i in range(7930):
    image = Image.open('E:/OneDrive/SPBU/Clasterisation_group/cropped_images/' + str(i+1)+'.jpg')
    path = 'E:/OneDrive/SPBU/Clasterisation_group/average/'+str(average_clustering.labels_[i]+1) +'/' +str(i+1)+'.jpg'
    image.save(path)
for i in range(7930):
    image = Image.open('E:/OneDrive/SPBU/Clasterisation_group/cropped_images/' + str(i+1)+'.jpg')
    path = 'E:/OneDrive/SPBU/Clasterisation_group/ward/'+str(ward_clustering.labels_[i]+1) +'/' +str(i+1)+'.jpg'
    image.save(path)"""

total_width = 45
max_height = 45
for k in range(1, 6):
    new_image = Image.new('L', (total_width, max_height))

    for i in range(5):
        for j in range(5):
            DIR = 'E:/OneDrive/SPBU/Clasterisation_group/ward/' +str(k)
            file = os.path.join(DIR, random.choice(os.listdir(DIR)))
            image = Image.open(file)
            new_image.paste(image, (j*9, i*9))
    new_image.save(str(k)+".jpg")
