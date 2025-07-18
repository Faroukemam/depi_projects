
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





class BasicStats:
    def __init__(self, data):
        """
        Initialize with a list of numerical data.
        Automatically sorts and stores essential info.
        """
        self.data = sorted(data)
        self.n = len(data)

    def _mean(self):
        """Return the mean (average) value."""
        return sum(self.data) / self.n if self.n else None

    def GetMean(self):
        return self._mean()

    def _median(self):
        """Return the median (middle) value."""
        if self.n == 0:
            return None
        mid = self.n // 2
        return self.data[mid] if self.n % 2 else (self.data[mid - 1] + self.data[mid]) / 2

    def GetMedian(self):
        return self._median()

    def _mode(self):
        """Return a list of mode(s) — most frequent value(s)."""
        if self.n == 0:
            return []
        freq = {}
        for val in self.data:
            freq[val] = freq.get(val, 0) + 1
        max_count = max(freq.values())
        return [val for val, count in freq.items() if count == max_count]

    def variance(self):
        """Return the variance of the dataset."""
        if self.n == 0:
            return None
        mean_val = self.mean()
        return sum((x - mean_val) ** 2 for x in self.data) / self.n

    def std_dev(self):
        """Return the standard deviation."""
        var = self.variance()
        return math.sqrt(var) if var is not None else None

    def minimum(self):
        """Return the minimum value."""
        return min(self.data) if self.n else None

    def maximum(self):
        """Return the maximum value."""
        return max(self.data) if self.n else None

    def range_val(self):
        """Return the range (max - min)."""
        return self.maximum() - self.minimum() if self.n else None

    def summary(self):
        """Print a formatted summary of all statistics."""
        print("\n📊 Basic Statistics Summary:")
        print("-" * 40)
        print(f"Count      : {self.n}")
        print(f"Min        : {self.minimum()}")
        print(f"Max        : {self.maximum()}")
        print(f"Range      : {self.range_val()}")
        print(f"Mean       : {self.mean():.2f}")
        print(f"Median     : {self.median()}")
        print(f"Mode       : {self.mode()}")
        print(f"Variance   : {self.variance():.2f}")
        print(f"Std. Dev   : {self.std_dev():.2f}")
        print("-" * 40)
