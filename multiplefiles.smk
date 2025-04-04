
rule all:
    input:
        "words_chart.txt"

rule count_words:
    input:
        "data/doc{n}.txt"
    output:
        "output/wc{n}.txt"
    shell:
        """
        python count_words.py -in {input} -out {output}
        """

rule words_chart:
    input:
        [f"output/wc{n}.txt" for n in range(1, 101)]
    output:
        "words_chart.txt"
    shell:
        """
        python words_chart.py
        """
