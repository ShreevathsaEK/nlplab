import nltk
from nltk import CFG, RecursiveDescentParser, tree, ChartParser
grammer=CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "Janice"  | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"|"his"
    N -> "dog" | "cat" | "telescope" | "park"| "Moon"| "terrace"
    P -> "in" | "on" | "by" | "with"| "from"                     
""")

s=input("Enter a sentence: ").split()

def parse(parser, s, parse_type):
    print(f"Parse type is", parse_type)
    trees=list(parser.parse(s))
    if not trees:
        print("NO parse tree is formed")
    else:
        for tree in trees:
            tree.pretty_print()
            tree.draw()

parse(ChartParser(grammer), s, "Bottom-up")
parse(RecursiveDescentParser(grammer), s, "TOP DOwn")