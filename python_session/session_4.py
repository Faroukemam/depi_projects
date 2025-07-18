''' list 

first_list = ["a",44,66,87,"c"]
print("first list is ",first_list)
first_list.append("NiceToMeetU")
print("first list after adding is ",first_list)
first_list.pop(2)
print("first list after using pop in 2 is ",first_list)
first_list.remove(44)
print("first list after using remove with 44 is ",first_list)
print("first cell is ",first_list[0])
print("first cell is ",first_list[::2])'''

"""
my_dict = {'name': 'Farouk', 'age': 25, 'field': 'Mechatronics'}

for key, value in my_dict.items():
    print(f"{key}: {value}")

my_dict['name']="karim"
my_dict['age']=19
my_dict['field']="Mechanical"

for key, value in my_dict.items():
    print(f"{key}: {value}")

students = {
    "student_1": {"name": "Farouk", "age": 24, "major": "Mechatronics"},
    "student_2": {"name": "Mona", "age": 23, "major": "AI"},
    "student_3": {"name": "Ahmed", "age": 25, "major": "Robotics"}
}

for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"{key}: {value}")




"""
def to_lower_case(text):
    return ''.join(char.lower() for char in text)

def remove_punctuation(word):
    punctuations = ".,!?;:'\"()-[]{}<>~`@#$%^&*_+=|\\/"
    return ''.join(char for char in word if char not in punctuations)

def split_into_words(text):
    text = to_lower_case(text)
    words = text.split()
    clean_words = []
    for word in words:
        cleaned = remove_punctuation(word)
        if cleaned != '':
            clean_words.append(cleaned)
    return clean_words

def split_into_sentences(text):
    sentences = []
    sentence = ""
    for char in text:
        sentence += char
        if char in ".!?":
            sentences.append(sentence.strip())
            sentence = ""
    if sentence.strip():
        sentences.append(sentence.strip())  # in case it ends without punctuation
    return sentences

def get_top_five_words(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    freq_list = []
    for word in word_freq:
        freq_list.append((word, word_freq[word]))

    # Manual selection sort for top 5
    for i in range(min(5, len(freq_list))):
        max_idx = i
        for j in range(i + 1, len(freq_list)):
            if freq_list[j][1] > freq_list[max_idx][1]:
                max_idx = j
        freq_list[i], freq_list[max_idx] = freq_list[max_idx], freq_list[i]

    return freq_list[:5]

def display_results(word_count, sentence_count, avg_word_len, top_five):
    print("\n" + "="*44)
    print("🧾 TEXT ANALYSIS REPORT".center(44))
    print("="*44)
    print(f"📄 Total Words         : {word_count}")
    print(f"🧠 Total Sentences     : {sentence_count}")
    print(f"✏️  Average Word Length : {avg_word_len:.2f}")

    if top_five:
        most_common_word, count = top_five[0]
        print(f"🔥 Most Frequent Word  : '{most_common_word.upper()}' ({count} times)")
    else:
        print("🔥 Most Frequent Word  : N/A")

    print("🏆 Top 5 Words:")
    for i, (word, freq) in enumerate(top_five, start=1):
        print(f"   {i}. {word:<10} - {freq} times")
    print("="*44)

def main():
    print("💬 Enter your paragraph below:\n")
    text = input(">>> ")

    if text.strip() == "":
        print("\n No input detected. Please enter a valid paragraph.")
        return

    words = split_into_words(text)
    sentences = split_into_sentences(text)

    word_count = len(words)
    sentence_count = len(sentences)
    total_word_length = sum(len(word) for word in words)
    avg_word_len = total_word_length / word_count if word_count > 0 else 0

    top_five = get_top_five_words(words)
    display_results(word_count, sentence_count, avg_word_len, top_five)

main()
