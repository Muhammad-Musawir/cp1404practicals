
user_input = input("Enter a string: ")

words = user_input.split()
word_counts = {}
for word in words:
    word = word.strip('.,?!').lower()
    word_counts[word] = word_counts.get(word, 0) + 1

max_word_length = max(len(word) for word in word_counts)
sorted_word_counts = sorted(word_counts.items())

for word, count in sorted_word_counts:
    print(f"{word:{max_word_length}} : {count}")
