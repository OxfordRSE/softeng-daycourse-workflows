import os
import random
import argparse


def load_word_list():
    return [
        "apple",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "kiwi",
        "lemon",
        "mango",
        "nectarine",
        "orange",
        "papaya",
        "quince",
        "raspberry",
        "strawberry",
        "tangerine",
        "ugli",
        "vanilla",
        "watermelon",
        "xigua",
        "yam",
        "zucchini",
        "apricot",
        "blueberry",
        "coconut",
    ]


def generate_file(filename, words, count):
    total_words = len(words)
    weights = [1 / (i + 1) ** 1.2 for i in range(total_words)]
    weights = random.sample(weights, len(weights))
    selected = random.choices(words, weights=weights, k=count)
    with open(filename, "w") as f:
        f.write(" ".join(selected) + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate one or more text files with random words."
    )
    parser.add_argument(
        "-w",
        "--word_count",
        nargs="?",
        type=int,
        default=100,
        help="Number of words per file (default: 100)",
    )
    parser.add_argument(
        "-n",
        "--num_files",
        nargs="?",
        type=int,
        default=1,
        help="Number of files to generate (default: 1)",
    )

    args = parser.parse_args()
    word_count = args.word_count
    num_files = args.num_files

    words = load_word_list()

    os.makedirs("data", exist_ok=True)

    if num_files == 1:
        filename = "data/doc.txt"
        generate_file(filename, words, word_count)
    else:
        for i in range(1, num_files + 1):
            filename = f"data/doc{i}.txt"
            generate_file(filename, words, word_count)


if __name__ == "__main__":
    main()
