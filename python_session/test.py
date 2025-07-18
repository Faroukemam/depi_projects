def is_letter(char):
    return char.isalpha()

def to_lower_case(text):
    return ''.join(char.lower() for char in text)

def remove_punctuation(word):
    punctuations = ".,!?;:'\"()-[]{}"
    return ''.join(char for char in word if char not in punctuations)

def split_into_words(text):
    text = to_lower_case(text)
    words = text.split()
    clean_words = []
    for word in words:
        word = remove_punctuation(word)
        if word != '':
            clean_words.append(word)
    return clean_words

def split_into_sentences(text):
    sentences = []
    sentence = ""
    for char in text:
        sentence += char
        if char in ".!?":
            sentences.append(sentence.strip())
            sentence = ""
    return sentences

def get_most_common_word(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    most_common = ""
    highest_count = 0
    for word in word_freq:
        if word_freq[word] > highest_count:
            highest_count = word_freq[word]
            most_common = word
    return most_common, highest_count

def get_top_five_words(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # convert dict to list of (word, count) and sort manually
    freq_list = []
    for word in word_freq:
        freq_list.append((word, word_freq[word]))

    # selection sort for top 5
    for i in range(min(5, len(freq_list))):
        max_idx = i
        for j in range(i+1, len(freq_list)):
            if freq_list[j][1] > freq_list[max_idx][1]:
                max_idx = j
        freq_list[i], freq_list[max_idx] = freq_list[max_idx], freq_list[i]

    return freq_list[:5]

def main():
    print("💬 Enter your paragraph below:\n")
    text = input()

    words = split_into_words(text)
    sentences = split_into_sentences(text)

    word_count = len(words)
    sentence_count = len(sentences)
    total_word_length = 0
    for word in words:
        total_word_length += len(word)
    avg_word_len = total_word_length / word_count if word_count > 0 else 0

    most_common_word, count = get_most_common_word(words)
    top_five = get_top_five_words(words)

    print("\n📊 Text Analysis Result:")
    print("-" * 40)
    print(f"Total Words         : {word_count}")
    print(f"Total Sentences     : {sentence_count}")
    print(f"Average Word Length : {avg_word_len:.2f}")
    print(f"Most Frequent Word  : '{most_common_word}' ({count} times)")
    print("Top 5 Most Common Words:")
    for word, freq in top_five:
        print(f"   • {word:<10} - {freq} times")
    print("-" * 40)

main()
