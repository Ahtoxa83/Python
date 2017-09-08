import re

without_duplicates = []
raw_list_of_links = []

try:
	with open (r"python_wiki.txt", "r", encoding = "utf-8") as f:

		for line in f:	
			links_from_file = re.compile(r'(\[\[)(.*?)(\]\]|\|)')
			result = links_from_file.findall(line)
			if result:
				for i in result:
					r = i[1]
					raw_list_of_links.append(r)
		
		raw_list_of_links.sort()

		for i in raw_list_of_links:
			if i not in without_duplicates:
				without_duplicates.append(i)

	with open("links.txt", "w") as file:
		for d in without_duplicates:
   			file.write(d + '\n')

except FileNotFoundError:
	print (FileNotFoundError.args())