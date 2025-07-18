def IsLetter(CH):
    return CH.isalpha()

def LowerCaseEx(word):
    return ''.join(char.lower() for char in word)

def WordCleaner(word):
    word = LowerCaseEx(word)
    CleanWord = ""
    for Character in word :
        if IsLetter(Character) :
            CleanWord= ''.join(Character)
    return CleanWord


def TxtWordEX(Txt):
    terms = Txt.split()
    words = []
    for word in terms:
        word = WordCleaner(word)
        words.append(word) if word else None
    return words

def SplitInSentences(Txt):
    sentences = []
    sentence = ""
    for char in Txt:
        sentence = "".join(char)
        if char in ".!?":
            sentences.append(sentence.strip())
            sentence = ""
    return sentences

def TopWords(words,limit):
    WordFreq = {}
    for word in words:
        WordFreq[word] = WordFreq.get(word, 0) + 1

    freq_list = []
    for word in WordFreq:
        freq_list.append((word, WordFreq[word]))

    for idx in range(len(freq_list)):
        MaxIdx = idx
        for WordIdx in range(idx+1, len(freq_list)):
            if freq_list[WordIdx][1] > freq_list[MaxIdx][1]:
                MaxIdx = WordIdx
        freq_list[idx], freq_list[MaxIdx] = freq_list[MaxIdx], freq_list[idx]

    return freq_list[:limit]

def TextAnalizer (text):
    words = TxtWordEX(text)
    sentences = SplitInSentences(text)

    WordCounter = len(words)
    SentenceCount = len(sentences)

    TotalWordLength = sum(len(word) for word in words)
    AvgWordLength = TotalWordLength/WordCounter

    MostCommonWord, count = TopWords(words,1)[0]
    TopFivewords = TopWords(words,5)

    print("\nText Analysis Result:")
    print("-" * 40)
    
    print(f"Total Words         : {WordCounter}")
    print(f"Total Sentences     : {SentenceCount}")
    print(f"Average Word Length : {AvgWordLength:.2f}")
    print(f"Most Frequent Word  : '{MostCommonWord}' ({count} times)")
    print("Top 5 Most Common Words:")
    for word, freq in TopFivewords:
        print(f"   • {word:<10} - {freq} times")

def main():
    print("💬 Enter your paragraph below:\n")
    text = input()
    TextAnalizer(text)

main()


    