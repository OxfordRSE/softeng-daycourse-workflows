import glob
import argparse


def count_words(files):
    counts = {}
    for filepath in files:
        with open(filepath, "r") as f:
            for line in f:
                word, count = line.strip().split()
                if word:
                    counts[word] = int(count)
    return counts


def print_bar_chart(counts, top_n=10, max_width=25):
    lines = []
    top_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    if not top_words:
        print("No words to display.")
        return

    max_count = top_words[0][1]
    max_word_len = max(len(word) for word, _ in top_words)
    max_count_len = len(str(max_count))

    for word, count in top_words:
        bar_len = int((count / max_count) * max_width)
        bar = "█" * bar_len
        word_field = word.ljust(max_word_len)
        count_field = f"({count})".rjust(max_count_len + 2)  # +2 for parentheses
        line = f"{word_field} {count_field} {bar}"
        lines.append(line)

    with open("words_chart.txt", "w") as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(
        description="Display top word frequencies from file* inputs as a bar chart."
    )
    parser.add_argument(
        "--pattern", default="output/*", help="File pattern to read (default: output/*)"
    )
    parser.add_argument(
        "--top", type=int, default=10, help="Number of top words to show (default: 10)"
    )
    parser.add_argument(
        "--width",
        type=int,
        default=25,
        help="Maximum bar width in characters (default: 25)",
    )

    args = parser.parse_args()

    files = sorted(glob.glob(args.pattern))
    if not files:
        print(f"No files match pattern: {args.pattern}")
        return

    counts = count_words(files)
    print_bar_chart(counts, top_n=args.top, max_width=args.width)


if __name__ == "__main__":
    main()
