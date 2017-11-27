from utils import extract_values_file, extract_values_image, get_sample, modify_rgba, get_assignments, get_new_centroids, get_cost_j

class Main(object):
	def __init__(self):
		super(Main, self).__init__()
		
	def solve_k_means(self, values, centroids):
		J = 0
		for iter in xrange(1,11):
			assignments = get_assignments(values, centroids)

			centroids = get_new_centroids(values, assignments, len(centroids))
			# print("\n")
			# print(new_centroids)

			new_j = get_cost_j(assignments, len(values))
			# print("\n")
			# print new_j

			dJ = J - new_j
			self.write_new_assignments(assignments, iter)
			self.write_new_centroids(centroids, new_j, dJ, iter)
			J = new_j
		print("First part accomplished!")

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

values_from_file = extract_values_file(filename="kmdata1.txt")
file_centroids = [
    [3, 3],
    [6, 2],
    [8, 5]
]

values_from_image = extract_values_image(filename="kmimg1.png")
image_centroids = get_sample(values=values_from_image, num=16)

for values in image_centroids:
	print len(values)
	print "\n"
print(len(image_centroids))
# print(values_from_image)
# print("\n\n\n\n\n\n")
# print(image_centroids)

main = Main()
main.solve_k_means(values_from_file, file_centroids)

# new_values = 
# modify_rgba(source="kmimg1.png", target="kmimg2.png", values=new_values)


