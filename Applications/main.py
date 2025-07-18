from Analizer import TextAnalyzer as an
def main():
    print("Enter your paragraph below:\n")
    text = input()
    analyzer = an(text)
    analyzer.analyze()

if __name__ == "__main__":
    main()