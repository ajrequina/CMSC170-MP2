import random
import math
import copy
import os

from PIL import Image

def extract_values_file(filename=None):
    if filename:
        values = []
        f = open(filename)
        for line in f:
            l = line.split(" ")
            row = []
            for c in l:
                c = c.strip('\n')
                c = c.strip('\r')
                if c != '':
                    row.append(float(c))
            values.append(row)

        return values

def get_sample(values=[], num=1):
    sample = random.sample(values, num)
    return sample

def extract_values_image(filename=None):
    if filename:
        values = []
        im = Image.open(filename)
        pix = im.load()
        dim = im.size
        for row in xrange(0, dim[0]):
            value_row = []
            for col in xrange(0, dim[1]):
                value_row.append(list(pix[row, col]))
            values += value_row
        return values

def modify_rgba(source=None, target=None, values=[]):
    cwd = os.getcwd()
    if source:
        value = iter(values)
        im = Image.new("RGB", (128, 128))
        pix = im.load()
        for x in range(128):
            for y in range(128):
                pix[x,y] = tuple(next(value))

        im.save(target, "PNG")

def get_assignments(values, centroids):
    assignments = []

    for pair in values:
        distances = []

        for centroid in centroids:
            distance = get_distance(pair, centroid)
            distances.append(distance)

        min_distance = min(distances)
        assignments.append([min_distance, distances.index(min_distance)])
    return assignments

def get_distance(pair, centroid):
    distance = 0;
    for index, feature in enumerate(centroid):
        distance += (pair[index] - centroid[index])**(2)
    return math.sqrt(distance)

def get_new_centroids(values, assignments, length):
    new_centroids = []
    mu_sizes = []
    feature_length = len(values[0])
    temp_centroid = []
    for i in xrange(0, feature_length):
        temp_centroid.append(0)

    while length > 0:
        new_centroids.append(copy.deepcopy(temp_centroid))
        mu_sizes.append(0)
        length -= 1;

    for index, pair in enumerate(values):
        i = assignments[index][1]
        temp_centroid = []
        for j in xrange(0, feature_length):
            temp_centroid.append(new_centroids[i][j] + values[index][j])

        new_centroids[i] = copy.deepcopy(temp_centroid)
        mu_sizes[i] += 1

    for index, pair in enumerate(new_centroids):
        for j in xrange(0, feature_length):
            new_centroids[index][j] /= mu_sizes[index]

    return new_centroids

def get_cost_j(assignments, m):
    cost_j = (sum(x[0] for x in assignments))/m
    return cost_j

def get_compressed_values(assignments, centroids):
    assignments = [x[1] for x in assignments]
    compressed_values = []
    for index in assignments:
        compressed_values.append(centroids[index])
    return compressed_values
