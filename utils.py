import random
import math
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
            values.append(value_row)
        return values

def modify_rgba(source=None, output=None, values=[]):
    if source:
        im = Image.open(source)
        pix = im.load()

        for ridx, row_val in enumerate(values):
            for cidx, col_val in enumerate(values[ridx]):
                pix[ridx, cidx] = tuple(values[ridx][cidx])

        im.save(output)

def get_assignments(values, centroids):
    assignments = []

    for pair in values:
        distances = []

        for centroid in centroids:
            distance = get_distance(pair, centroid)
            distances.append(distance)

        min_distance = min(distances)
        assignments.append([math.ceil(min_distance*1000000)/1000000, distances.index(min_distance)])
        #assignments.append(centroids[get_min_centroid(a, b, c)]);
    return assignments

def get_distance(pair, centroid):
    return math.sqrt((pair[0] - centroid[0])**(2) + (pair[1] - centroid[1])**(2))

def get_min_centroid(a, b ,c):
    min = a
    index = 0
    if min > b:
        min = b
        index = 1
    if min > c:
        min = c
        index = 2
    return index

def get_new_centroids(values, assignments, length):
    new_centroids = []
    mu_sizes = []
    while length > 0:
        new_centroids.append([0, 0])
        mu_sizes.append(0)
        length -= 1;

    for index, pair in enumerate(values):
        i = assignments[index][1]
        new_centroids[i] = [(new_centroids[i][0] + values[index][0]), (new_centroids[i][1] + values[index][1])]
        mu_sizes[i] += 1

    for index, pair in enumerate(new_centroids):
        new_centroids[index][0] /= mu_sizes[index]
        new_centroids[index][1] /= mu_sizes[index]

        new_centroids[index][0] = math.ceil(new_centroids[index][0]*1000000)/1000000
        new_centroids[index][1] = math.ceil(new_centroids[index][1]*1000000)/1000000
    return new_centroids  

def get_cost_j(assignments, m):
    cost_j = (sum(x[0] for x in assignments))/m
    return cost_j