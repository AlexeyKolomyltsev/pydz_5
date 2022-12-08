# Реализуйте RLE алгоритм: реализуйте модуль восстановления данных.
import os

def rle_to_x():
    path ='4' + os.sep + 'file_rle.txt'
    with open(path, 'r') as my_file:
        x_rle = my_file.readline()
        x =''
        for i in range(0, len(x_rle), 2):
            count = x_rle[i]
            x += int(count) * x_rle[i+1]


    path ='4' + os.sep + 'new_file.txt'
    with open(path, 'w') as my_file:   
        my_file.write(x)

rle_to_x()