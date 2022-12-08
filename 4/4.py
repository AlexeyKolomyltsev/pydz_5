# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.
import os
def x_to_rle():
    path ='4' + os.sep + 'file.txt'
    with open(path, 'r') as my_file:
        x = my_file.readline()
        xc = x[0]
        x_rle = ""
        count = 1
        for i in range(1, len(x)):
            if x[i] == xc:
                count += 1
            else:
                x_rle += str(count) + xc
                xc = x[i]
                count = 1
        x_rle += str(count) + xc
    path ='4' + os.sep + 'file_rle.txt'
    with open(path, 'w') as my_file:   
            my_file.write(x_rle)

x_to_rle()