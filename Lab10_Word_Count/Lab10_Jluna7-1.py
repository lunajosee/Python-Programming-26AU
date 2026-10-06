"""
Program Name: Lab10_Jluna7-1.py
Author: Jose Luna
Purpose: Analyze a selected book and print alphabetical word counts.
Starter code: None
Date: 10/6/2026
"""

import pathlib
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = pathlib.Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        translation_table = str.maketrans("", "", string.punctuation)

        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            with self.__filepath.open("r", encoding="utf-8-sig") as file:
                for line in file:
                    line = line.translate(translation_table).lower()

                    for word in line.split():
                        count = self.__frequencies.get(word, 0)
                        self.__frequencies[word] = count + 1

            return True

        except FileNotFoundError:
            print("File not found:", self.__filepath.name)
            return False

    def print_report(self):
        words = sorted(self.__frequencies.keys())

        for word in words:
            print(f"{word:<20} :: {self.__frequencies[word]}")

def main():
    folder = pathlib.Path(__file__).resolve().parent

    files = {
        "1": folder / "monte_cristo.txt",
        "2": folder / "treasure_island.txt",
        "3": folder / "tarzan.txt",
        "4": folder / "princess_mars.txt",
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")

        for number, filepath in files.items():
            name = filepath.stem.replace("_", " ").title()
            print(f"  {number}. {name}")

        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("Exiting the program.")
            break

        if choice not in files:
            print("Invalid choice. Please try select from 1-5.")
        else:
            filepath =files[choice]
            print("Processing:", filepath.name)
            analyzer = WordAnalyzer(filepath)
            if analyzer.process_file():
                analyzer.print_report()

            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
