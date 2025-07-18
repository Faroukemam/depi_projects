# Function: IsLetter
# Description: Checks if a character is a letter (A-Z, a-z)
def IsLetter(CH):
    return CH.isalpha()


# Function: LowerCaseEx
# Description: Converts all characters in a word to lowercase
def LowerCaseEx(word):
    return ''.join(char.lower() for char in word)


# Function: WordCleaner
# Description: Cleans a word by removing any non-letter characters and making it lowercase
# Example: "Hello!" → "hello", "123abc!" → "abc"
def WordCleaner(word):
    return ''.join(c for c in LowerCaseEx(word) if IsLetter(c))


# Function: TxtWordEX
# Description: Splits a full paragraph into cleaned words
# Steps:
# - Splits text by whitespace
# - Cleans each word using WordCleaner()
# - Adds only non-empty words to the final list
def TxtWordEX(Txt):
    terms = Txt.split()
    words = []
    for word in terms:
        word = WordCleaner(word)
        if word:  # Add only if the cleaned word is not empty
            words.append(word)
    return words


# Function: SplitInSentences
# Description: Splits a paragraph into sentences based on punctuation (., !, ?)
# Handles cases where text ends without punctuation
def SplitInSentences(Txt):
    sentences = []
    sentence = ""
    for char in Txt:
        sentence += char  # Build sentence character by character
        if char in ".!?":  # End of sentence
            sentences.append(sentence.strip())
            sentence = ""  # Reset for next sentence
    if sentence.strip():  # Add last sentence if there's leftover
        sentences.append(sentence.strip())
    return sentences


# Function: TopWords
# Description: Returns a list of the most frequent words up to a specified limit
# Uses manual selection sort to sort word-frequency pairs in descending order
def TopWords(words, limit):
    # Step 1: Count frequency of each word
    WordFreq = {}
    for word in words:
        WordFreq[word] = WordFreq.get(word, 0) + 1

    # Step 2: Convert dictionary to list of tuples
    freq_list = []
    for word in WordFreq:
        freq_list.append((word, WordFreq[word]))

    # Step 3: Sort the list manually using selection sort
    for idx in range(len(freq_list)):
        MaxIdx = idx
        for WordIdx in range(idx + 1, len(freq_list)):
            if freq_list[WordIdx][1] > freq_list[MaxIdx][1]:
                MaxIdx = WordIdx
        freq_list[idx], freq_list[MaxIdx] = freq_list[MaxIdx], freq_list[idx]

    return freq_list[:limit]  # Return top 'limit' words


# Function: TextAnalizer
# Description: The main logic to analyze a paragraph of text.
# - Calculates word count, sentence count, average word length
# - Extracts the most common word and top 5 frequent words
# - Prints results in a report format
def TextAnalizer(text):
    words = TxtWordEX(text)                # Get cleaned list of words
    sentences = SplitInSentences(text)     # Get list of sentences

    WordCounter = len(words)               # Total number of words
    SentenceCount = len(sentences)         # Total number of sentences
    TotalWordLength = sum(len(word) for word in words)  # Sum of all word lengths
    AvgWordLength = TotalWordLength / WordCounter if WordCounter else 0  # Prevent division by 0

    MostCommonWord, count = TopWords(words, 1)[0] if words else ("N/A", 0)
    TopFivewords = TopWords(words, 5)

    # Print analysis results
    print("\n📊 Text Analysis Result:")
    print("-" * 40)
    print(f"Total Words         : {WordCounter}")
    print(f"Total Sentences     : {SentenceCount}")
    print(f"Average Word Length : {AvgWordLength:.2f}")
    print(f"Most Frequent Word  : '{MostCommonWord}' ({count} times)")
    print("Top 5 Most Common Words:")
    for word, freq in TopFivewords:
        print(f"   • {word:<10} - {freq} times")


# Function: main
# Description: Entry point of the program. Asks the user for input and runs the analyzer.
def main():
    print("Enter your paragraph below:\n")
    text = input()
    TextAnalizer(text)


# Best practice to only run main if this file is the entry script
if __name__ == "__main__":
    main()
