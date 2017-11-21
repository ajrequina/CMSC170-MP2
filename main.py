from . import extract_values_file, extract_values_image, get_sample, modify_rgba


values_from_file = extract_values_file(filename="kmdata1.txt")
file_centroids = [
    [3, 3],
    [6, 2],
    [8, 5]
]
print(values_from_file)

values_from_image = extract_values_image(filename="kmimg1.png")
image_centroids = get_sample(values=values_from_image, num=16)


new_values = values_from_image
modify_rgba(source="kmimg1.png", target="kmimg2.png", values=new_values)

