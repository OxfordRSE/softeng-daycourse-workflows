from pathlib import Path
import argparse


def count_words(input_path, output_path):
    word_counts = {}

    out_folder = Path(output_path).parent
    if not out_folder.exists():
        out_folder.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r") as infile:
        for line in infile:
            for word in line.strip().split():
                word = word.lower().strip(".,!?\"'()[]{}:;")
                if word:
                    word_counts[word] = word_counts.get(word, 0) + 1

    with open(output_path, "w") as outfile:
        for word in sorted(word_counts):
            outfile.write(f"{word} {word_counts[word]}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Count word occurrences in a text file."
    )
    parser.add_argument("-in", "--input_file", help="Path to the input text file")
    parser.add_argument(
        "-out", "--output_file", help="Path to the output word count file"
    )

    args = parser.parse_args()

    count_words(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
