import sys

if __name__ == "__main__":
	file_path = sys.argv[1]
	with open(file_path, 'r') as file:
		lines = file.readlines()
		print(len(lines))
