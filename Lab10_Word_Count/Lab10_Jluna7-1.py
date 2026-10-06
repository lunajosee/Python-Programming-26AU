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