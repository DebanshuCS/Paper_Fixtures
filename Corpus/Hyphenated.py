import re


def correct_hyphenated_words(text):
    # Merge hyphenated words split across lines
    corrected_text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    return corrected_text


def process_text_file(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Correct hyphenated words split across lines
    corrected_text = correct_hyphenated_words(text)

    # Overwrite the original file with the corrected text
    with open(input_file, "w", encoding="utf-8") as file:
        file.write(corrected_text)


if __name__ == "__main__":
    input_text_file = "healthcare_preserving_privacy.txt"  # Replace with your input text file
    process_text_file(input_text_file)
