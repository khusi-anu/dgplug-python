#!/usr/bin/env python3

import requests

def image_processing(url, extensions):

	"""Downloads the file if it is a image
		:arg url: URL of the file to be downloaded.
	"""

	#checks the file extension
	if (url.endswith(extension) for extension in extensions):	
		request = requests.get(url)
		filename = url.split('/')[-1]
		with open(filename, 'wb') as file_:
			file_.write(request.content)
		print("Download over")
	else:
		print("No pictures")

if __name__ == '__main__':
	input_url = input("Enter URL:")
	image_extensions = ['.jpg', '.jpeg', '.png', '.svg']
	image_processing(input_url, image_extensions)
