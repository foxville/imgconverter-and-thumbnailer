from PIL import Image, ImageFilter
import sys, os
from pathlib import Path

try:
	path = sys.argv[1]
	directory = sys.argv[2]
except IndexError:
	print("Please add the input and output folders\' names: \"python Thumbnailer.py INPUT_FOLDER OUTPUT_FOLDER\"")
	exit()

if not os.path.exists(path):
	print('You need to create input folder first and put there the image files')
	exit()

if not os.path.exists(directory):
		os.makedirs(directory)

if not os.listdir(path):
	print(f'Put image files into the {sys.argv[1]} folder!')
else:
	print("What is the resolution of thumbnail?")

	while True:
		try:
			resolution = int(input("Input the number: "))
			break
		except ValueError:
			print("You need to enter a number!")

	for filename in os.listdir(path):
		img = Image.open(f'{path}/{filename}')
		img.thumbnail((resolution, resolution))
		img.save(f'{directory}/{filename}')
		print('The task is completed!')