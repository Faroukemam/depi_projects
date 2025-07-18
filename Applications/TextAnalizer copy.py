class TextAnalyzer:
    def __init__(self, text):
        """
        Constructor: Initialize the TextAnalyzer with the original text.
        It automatically extracts cleaned words and sentences from the input.
        
        Args:
            text (str): The raw paragraph to be analyzed.
        """
        self.original_text = text
        self.words = self._extract_words(text)      # Extract and clean words
        self.sentences = self._split_sentences(text)  # Split into sentences

    def _is_letter(self, ch):
        """
        Check whether a character is a letter (A-Z or a-z).
        
        Args:
            ch (str): Single character.
        Returns:
            bool: True if it's an alphabetic letter.
        """
        return ch.isalpha()

    def _lower_case(self, word):
        """
        Convert all characters in a word to lowercase.
        
        Args:
            word (str): A single word or string.
        Returns:
            str: Lowercased version of the word.
        """
        return ''.join(char.lower() for char in word)

    def _clean_word(self, word):
        """
        Remove non-letter characters from a word and convert it to lowercase.
        Example: "Hello!" → "hello", "123abc!" → "abc"
        
        Args:
            word (str): The original word (may include punctuation or numbers).
        Returns:
            str: A cleaned word containing only lowercase letters.
        """
        return ''.join(c for c in self._lower_case(word) if self._is_letter(c))

    def _extract_words(self, text):
        """
        Extract and clean all words from the input text.
        
        Steps:
        - Split the paragraph by whitespace.
        - Clean each term using _clean_word().
        - Keep only non-empty valid words.
        
        Args:
            text (str): The original paragraph.
        Returns:
            list[str]: List of cleaned words.
        """
        terms = text.split()
        words = []
        for word in terms:
            clean = self._clean_word(word)
            if clean:
                words.append(clean)
        return words

    def _split_sentences(self, text):
        """
        Split the paragraph into individual sentences.
        Sentences end with '.', '!' or '?'.
        
        Args:
            text (str): The original paragraph.
        Returns:
            list[str]: List of trimmed sentences.
        """
        sentences = []
        sentence = ""
        for char in text:
            sentence += char
            if char in ".!?":
                sentences.append(sentence.strip())
                sentence = ""
        if sentence.strip():  # Handle leftover text with no punctuation
            sentences.append(sentence.strip())
        return sentences

    def _get_top_words(self, limit):
        """
        Get the top N most frequent words.
        Uses manual selection sort (for educational clarity).
        
        Args:
            limit (int): The number of top frequent words to return.
        Returns:
            list[tuple[str, int]]: List of (word, frequency) tuples sorted by count.
        """
        word_freq = {}

        # Count word frequencies
        for word in self.words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Convert to list of tuples
        freq_list = [(word, count) for word, count in word_freq.items()]

        # Manual sorting using selection sort
        for i in range(len(freq_list)):
            max_idx = i
            for j in range(i + 1, len(freq_list)):
                if freq_list[j][1] > freq_list[max_idx][1]:
                    max_idx = j
            freq_list[i], freq_list[max_idx] = freq_list[max_idx], freq_list[i]

        return freq_list[:limit]

    def analyze(self):
        """
        Perform the full analysis:
        - Count words and sentences
        - Calculate average word length
        - Find the most common word
        - Display top 5 most frequent words
        
        The result is printed to the console in a formatted report.
        """
        word_count = len(self.words)
        sentence_count = len(self.sentences)

        # Total length of all words combined
        total_word_length = sum(len(word) for word in self.words)

        # Avoid division by zero
        avg_word_length = total_word_length / word_count if word_count else 0

        # Get most frequent word and top 5 list
        most_common_word, freq = self._get_top_words(1)[0] if self.words else ("N/A", 0)
        top_five = self._get_top_words(5)

        # Print formatted report
        print("\n📊 Text Analysis Result:")
        print("-" * 40)
        print(f"Total Words         : {word_count}")
        print(f"Total Sentences     : {sentence_count}")
        print(f"Average Word Length : {avg_word_length:.2f}")
        print(f"Most Frequent Word  : '{most_common_word}' ({freq} times)")
        print("Top 5 Most Common Words:")
        for word, count in top_five:
            print(f"   • {word:<10} - {count} times")


# Main entry point
def main():
    """
    Entry point of the program.
    Accepts user input from the console and runs the analysis.
    """
    print("Enter your paragraph below:\n")
    text = input()
    analyzer = TextAnalyzer(text)
    analyzer.analyze()


# Prevent auto-execution if imported elsewhere
if __name__ == "__main__":
    main()
