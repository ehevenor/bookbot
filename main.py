import stats
import sys

def check():
	sys_argv_list = len(sys.argv)
	if sys_argv_list < 2:
		print("Usage: python3 main.py <path_to_book>"); sys.exit(1)
	else:
		return
check()

book_text_content = stats.get_book_text(sys.argv[1])

my_character_counts = stats.character_count(book_text_content)

sorted_characters_list  = stats.get_sorted_character_list(my_character_counts)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {len(book_text_content.split())} total words")
print("--------- Character Count -------")
for item in sorted_characters_list:
	print(f"{item['char']}: {item['num']}")
print("============= END ===============")
