
with open("books/frankenstein.txt") as f:
	file_contents = f.read()

letters_dictionary = {}
letters_list = []

def count_words(file_contents) :
	
	words = file_contents.split()
	letters = list(file_contents)
	
	for l in letters:
		lowered_string = l.lower()
		if lowered_string.isalpha() :
			if lowered_string not in letters_dictionary :
				letters_dictionary[lowered_string] = 1
			else :
				letters_dictionary[lowered_string] += 1
	

	for k , value in letters_dictionary.items() :
		letters_list.append({"char": k, "count": value})
	letters_list.sort(reverse=True , key= lambda item: item["count"])
print("--- Begin report of books/frankenstein.txt ---")
count_words(file_contents)
print(f"{len(file_contents.split())} words found in the document")
for letter in letters_list:
	print(f"The '{letter['char']}' character was found {letter['count']} times") 
	
print("--- End report ---")





