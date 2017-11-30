import itertools
import time


from utils import extract_values_file, extract_values_image, get_sample, modify_rgba, get_assignments, get_new_centroids, get_cost_j, get_compressed_values

class Main(object):
	def __init__(self):
		super(Main, self).__init__()
		self.values = []
		self.assignments = []
		self.centroids = []
		self.is_file = False

	def compress_image(self, values):
		self.is_file = False
		centroids = get_sample(values=values_from_image, num=16)
		self.solve_k_means(values, centroids)
		self.write_new_image(self.assignments, self.centroids)

	def evaluate_file(self, values):
		self.is_file = True
		centroids = [
		    [3, 3],
		    [6, 2],
		    [8, 5]
		]
		self.solve_k_means(values, centroids)

	def solve_k_means(self, values, centroids):
		J = 0
		for iter in xrange(1,11):
			assignments = get_assignments(values, centroids)

			centroids = get_new_centroids(values, assignments, len(centroids))

			new_j = get_cost_j(assignments, len(values))

			dJ = J - new_j
			if self.is_file:
				self.write_new_assignments(assignments, iter)
				self.write_new_centroids(centroids, new_j, dJ, iter)
			J = new_j
			self.assignments = assignments
			self.centroids = centroids

	def write_new_assignments(self, assignments, iter):
	    file_name = "iter" + str(iter) + "_ca.txt"
	    file = open(file_name, "w")
	    for value in assignments:
	        file.write("" + str(value[1] + 1) + "\n")
	    file.close()

	def write_new_centroids(self, centroids, J, dJ, iter):
		file_name = "iter" + str(iter) + "_cm.txt"
		file = open(file_name, "w")
		for value in centroids:
			file.write("" + str(value[0]) + " " + str(value[1]) + "\n")
		file.write("J= " + str(J) + "\n")
		file.write("dJ= " + str(dJ) + "\n")
		file.close()

	def write_new_image(self, assignments, centroids):
		compressed_values = get_compressed_values(assignments, centroids)
		modify_rgba(source="kmimg1.png", target="kmimg2.png", values=compressed_values)

values_from_file = extract_values_file(filename="kmdata1.txt")
values_from_image = extract_values_image(filename="kmimg1.png")

main = Main()
start = int(round(time.time() * 1000))
print("---- Part 1 Processing ----")
main.evaluate_file(values_from_file)
end = int(round(time.time() * 1000))
print("---- Part 1 Finished (" + str(end - start) + " ms) ----\n")
start = int(round(time.time() * 1000))
print("---- Part 2 Processing ----")
main.compress_image(values_from_image)
end = int(round(time.time() * 1000))
print("---- Part 2 Finished (" + str(end - start) + " ms) ----\n")
