
rule all:
    input:
        "words_chart.txt"

rule count_words:
    input:
        "data/doc.txt"
    output:
        "output/wc.txt"
    shell:
        """
        python count_words.py -in {input} -out {output}
        """

rule words_chart:
    input:
        "output/wc.txt"
    output:
        "words_chart.txt"
    shell:
        """
        python words_chart.py
        """
