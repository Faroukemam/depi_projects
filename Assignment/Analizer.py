# ======================= 📌 Conclusion ========================
# This Python file provides two key classes:
# 
# 1. TextAnalyzer:
#    - Handles raw textual input.
#    - Performs linguistic analysis including:
#        • Word count
#        • Sentence count
#        • Average word length
#        • Most frequent words (Top-N analysis)
#    - All processing is done using custom logic (no external libraries),
#      making it ideal for learning how basic text parsing works.
#
# 2. BasicStats:
#    - Accepts a numeric dataset and computes:
#        • Mean, Median, Mode
#        • Variance & Standard Deviation
#        • Min, Max, Range
#        • Interquartile Range (IQR)
#        • Skewness (asymmetry of distribution)
#        • Kurtosis (tail heaviness)
#    - Encapsulates all statistical logic using private methods and exposes
#      well-named public getters for clean API use.
# =============================================================

import math


class TextAnalyzer:
    def __init__(self, text):
        """
        Constructor: Takes the raw input text and initializes internal state.
        """
        self.original_text = text
        self.words = self._extract_words(text)
        self.sentences = self._split_sentences(text)


# Function: _is_letter
# Description: Checks if a character is a letter (A-Z, a-z)
    def _is_letter(self, ch):
        """
        Check if a character is a letter (A-Z or a-z).
        """
        return ch.isalpha()
    
# Function: LowerCaseEx
# Description: Converts all characters in a word to lowercase
    def _lower_case(self, word):
        """
        Convert all characters in a word to lowercase.
        """
        return ''.join(char.lower() for char in word)

# Function: WordCleaner
# Description: Cleans a word by removing any non-letter characters and making it lowercase
# Example: "Hello!" → "hello", "123abc!" → "abc"
    def _clean_word(self, word):
        """
        Remove non-letter characters from a word and make it lowercase.
        """
        return ''.join(c for c in self._lower_case(word) if self._is_letter(c))


# Function: TxtWordEX
# Description: Splits a full paragraph into cleaned words
# Steps:
# - Splits text by whitespace
# - Cleans each word using WordCleaner()
# - Adds only non-empty words to the final list
    def _extract_words(self, text):
        """
        Split text into words and clean them.
        """
        terms = text.split()
        words = []
        for word in terms:
            clean = self._clean_word(word)
            if clean:
                words.append(clean)
        return words


# Function: SplitInSentences
# Description: Splits a paragraph into sentences based on punctuation (., !, ?)
# Handles cases where text ends without punctuation
    def _split_sentences(self, text):
        """
        Split text into sentences based on punctuation.
        """
        sentences = []
        sentence = ""
        for char in text:
            sentence += char
            if char in ".!?":
                sentences.append(sentence.strip())
                sentence = ""
        if sentence.strip():
            sentences.append(sentence.strip())
        return sentences



# Function: TopWords
# Description: Returns a list of the most frequent words up to a specified limit
# Uses manual selection sort to sort word-frequency pairs in descending order
    def _get_top_words(self, limit):
        """
        Get the top `limit` most frequent words.
        Uses manual selection sort to keep it beginner-friendly.
        """
        word_freq = {}
        for word in self.words:
            word_freq[word] = word_freq.get(word, 0) + 1

        freq_list = [(word, count) for word, count in word_freq.items()]

        # Manual selection sort
        for i in range(len(freq_list)):
            max_idx = i
            for j in range(i + 1, len(freq_list)):
                if freq_list[j][1] > freq_list[max_idx][1]:
                    max_idx = j
            freq_list[i], freq_list[max_idx] = freq_list[max_idx], freq_list[i]

        return freq_list[:limit]


# Function: TextAnalizer
# Description: The main logic to analyze a paragraph of text.
# - Calculates word count, sentence count, average word length
# - Extracts the most common word and top 5 frequent words
# - Prints results in a report format
    def analyze(self):
        """
        Perform the full text analysis and print the results.
        """
        word_count = len(self.words)
        sentence_count = len(self.sentences)
        total_word_length = sum(len(word) for word in self.words)
        avg_word_length = total_word_length / word_count if word_count else 0

        most_common_word, freq = self._get_top_words(1)[0] if self.words else ("N/A", 0)
        top_five = self._get_top_words(5)

        # Display results
        print("\nText Analysis Result:")
        print("=" * 40)
        print(f"Total Words         : {word_count}")
        print(f"Total Sentences     : {sentence_count}")
        print(f"Average Word Length : {avg_word_length:.2f}")
        print(f"Most Frequent Word  : '{most_common_word}' ({freq} times)")
        print("Top 5 Most Common Words:")
        for word, count in top_five:
            print(f"   • {word:<10} - {count} times")
        print("=" * 40)
        print("Original content >>>")
        print(self.original_text)





class Stats:
    def __init__(self, data):
        """
        Initialize the statistics object with numerical data.
        Data is sorted to simplify median, IQR, and percentile-based calculations.
        """
        self.__Data = sorted(data)
        self.__DataLength = len(data)

    # ---------- Private Methods ---------- #

    def __mean(self):
        """
        Compute the arithmetic mean (average) of the dataset.
        """
        return sum(self.__Data) / self.__DataLength if self.__DataLength else None

    def __median(self):
        """
        Compute the median (middle value) of the sorted dataset.
        Handles even and odd lengths.
        """
        if not self.__DataLength:
            return None
        mid = self.__DataLength // 2
        return self.__Data[mid] if self.__DataLength % 2 else (self.__Data[mid - 1] + self.__Data[mid]) / 2

    def __mode(self):
        """
        Compute the mode(s) — the most frequent value(s) in the dataset.
        Returns a list to handle multimodal distributions.
        """
        if not self.__DataLength:
            return []
        freq = {}
        for val in self.__Data:
            freq[val] = freq.get(val, 0) + 1
        max_count = max(freq.values())
        return [val for val, count in freq.items() if count == max_count]

    def __variance(self):
        """
        Calculate the population variance (σ²) — average of squared deviations from the mean.
        """
        if not self.__DataLength:
            return None
        mean_val = self.__mean()
        return sum((x - mean_val) ** 2 for x in self.__Data) / self.__DataLength

    def __std_dev(self):
        """
        Calculate the standard deviation (σ) — square root of variance.
        """
        var = self.__variance()
        return math.sqrt(var) if var is not None else None

    def __minimum(self):
        """
        Return the smallest value in the dataset.
        """
        return min(self.__Data) if self.__DataLength else None

    def __maximum(self):
        """
        Return the largest value in the dataset.
        """
        return max(self.__Data) if self.__DataLength else None

    def __range_val(self):
        """
        Calculate the range: difference between max and min.
        """
        return self.__maximum() - self.__minimum() if self.__DataLength else None

    def __iqr(self):
        """
        Calculate the Interquartile Range (IQR = Q3 - Q1).
        Uses a linear interpolation method for percentile calculation.
        """
        if self.__DataLength < 4:
            return 0

        def percentile(p):
            rank = p * (self.__DataLength + 1) / 100
            k = int(rank)
            d = rank - k
            return (self.__Data[k - 1] if k == self.__DataLength else self.__Data[k - 1] + d * (self.__Data[k] - self.__Data[k - 1]))

        q1 = percentile(25)
        q3 = percentile(75)
        return q3 - q1

    def __skewness(self):
        """
        Calculate skewness: measure of asymmetry.
        Negative = left skewed, Positive = right skewed.
        """
        if self.__DataLength < 3:
            return 0
        m = self.__mean()
        sd = self.__std_dev()
        return (sum((x - m) ** 3 for x in self.__Data) / self.__DataLength) / (sd ** 3)

    def __kurtosis(self):
        """
        Calculate excess kurtosis: measure of tailedness.
        - Normal distribution = 0
        - Positive = heavy tails, Negative = light tails
        """
        if self.__DataLength < 4:
            return 0
        m = self.__mean()
        sd = self.__std_dev()
        return (sum((x - m) ** 4 for x in self.__Data) / self.__DataLength) / (sd ** 4) - 3

    # ---------- Public Getters ---------- #

    def get_DataSort(self): return self.__Data
    def get_DataLength(self): return self.__DataLength

    def get_mean(self): return self.__mean()
    def get_median(self): return self.__median()
    def get_mode(self): return self.__mode()

    def get_variance(self): return self.__variance()
    def get_std_dev(self): return self.__std_dev()
    
    def get_minimum(self): return self.__minimum()
    def get_maximum(self): return self.__maximum()
    def get_range(self): return self.__range_val()

    def get_iqr(self): return self.__iqr()
    def get_skewness(self): return self.__skewness()
    def get_kurtosis(self): return self.__kurtosis()

    def summary(self):
        """
        Print a clean and formatted summary of all calculated statistics.
        """
        print("\n📊 Full Statistics Summary:")
        print("-" * 40)
        print(f"Count      : {self.__DataLength}")
        print(f"Min        : {self.get_minimum()}")
        print(f"Max        : {self.get_maximum()}")
        print(f"Range      : {self.get_range()}")
        print(f"Mean       : {self.get_mean():.2f}")
        print(f"Median     : {self.get_median()}")
        print(f"Mode       : {self.get_mode()}")
        print(f"Variance   : {self.get_variance():.2f}")
        print(f"Std. Dev   : {self.get_std_dev():.2f}")
        print(f"IQR        : {self.get_iqr():.2f}")
        print(f"Skewness   : {self.get_skewness():.4f} {'Positive Skewness' if self.get_skewness()>0 else 'Nigative Skewness'}")
        print(f"Kurtosis   : {self.get_kurtosis():.4f}")
        print("-" * 40)
