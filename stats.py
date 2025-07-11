def get_book_text(filepath):
        with open (filepath) as f:
                file_contents= f.read()
                return file_contents
def main():
        text=get_book_text("books/frankenstein.txt")
        words=text.split()
        print(f"{len(words)} words found in the document")

def character_count(text):
	char = text.lower()
	count_each = {}
	for i in char:
		if i not in count_each:
			count_each[i] = 1
		else:
			count_each[i] +=1
	return count_each

def sort_on(character):
	return character["num"]
def get_sorted_character_list(char_counts_dict):
	char_list_for_sorting = [] 
	for character, counts in char_counts_dict.items():
		if character.isalpha():
			char_list_for_sorting.append({"char": character, "num": counts})

	char_list_for_sorting.sort(reverse=True, key=sort_on)
	return char_list_for_sorting
