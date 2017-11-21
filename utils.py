import random
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
