import sys
import os
from PIL import Image

try:
	path = sys.argv[1]
	directory = sys.argv[2]
except IndexError:
	print("Please add the input and output folders\' names: \"python IMGconverter.py INPUT_FOLDER OUTPUT_FOLDER\"")
	exit()

if not os.path.exists(path):
	print('You need to create input folder first and put there the image files')
	exit()

if not os.path.exists(directory):
		os.makedirs(directory)

if not os.listdir(path):
	print(f'Put image files into the {sys.argv[1]} folder!')
else:
	file_format = input('Input the file format you want to convert to (png, ico, bmp, jpeg, pdf): ')

	for filename in os.listdir(path):
	  clean_name = os.path.splitext(filename)[0]
	  img = Image.open(f'{path}/{filename}')
	  img.save(f'{directory}/{clean_name}.{file_format}', f'{file_format}')
	  print('The task is completed!')
