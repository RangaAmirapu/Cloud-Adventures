import zipfile, os, argparse, shutil

def collectPaths():
   parser = argparse.ArgumentParser()
   parser.add_argument('-sd','-sourceDir', help='List of directories to zip', nargs='+' , required=True)

   #nargs options
   # '+' == 1 or more.
   # '*' == 0 or more.
   # '?' == 0 or 1.
   parser.add_argument('-td','-targetDir', help='Target directory to place the compressed folders' , required=True)
   args = parser.parse_args()
   return args

def get_all_file_paths(directory): 
	# initializing empty file paths list 
	file_paths = [] 

	# crawling through directory and subdirectories 
	for root,directories, files in os.walk(directory): 
		for filename in files: 

			# join the two strings to form the full filepath. 
			filepath = os.path.join(root, filename) 
			file_paths.append(filepath) 

	# returning all file paths 
	return file_paths

def zip(sourceDir): 
	# path to folder which needs to be zipped 
	directory = sourceDir
	file_paths = get_all_file_paths(directory) 

	# printing the list of all files to be zipped 
	print('Following files will be zipped:') 
	for file_name in file_paths: 
		print(file_name) 

	# writing files to a zipfile 
	with zipfile.ZipFile(sourceDir + '.zip','w', zipfile.ZIP_DEFLATED) as zip: 

		# writing each file one by one 
		for file in file_paths: 
			zip.write(file) 
	print('All files zipped successfully!')

def main():
   for s in collectPaths().sd :
      print(s)
      zip(s)
      shutil.move(s +'.zip',collectPaths().td)

if __name__ == '__main__':
   main()