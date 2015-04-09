
from collections    import defaultdict
from random             import random, choice
from string             import ascii_lowercase
from subprocess     import Popen, PIPE
from time                 import time, sleep

# get a list of words with only ASCII characters
words = [w.strip().lower() for w in open("/usr/share/dict/words").readlines()]
words = [w for w in words if all([c in ascii_lowercase for c in w])]
words = ["^" + w + "$" for w in words if w != ""]

# construct a discrete-time markov chain of n-grams
n = 5 # this is the "n" in n-grams, try adjusting this for different results
transitions = defaultdict(lambda: defaultdict(float))
for word in words:
    if len(word) >= n:
        transitions[""][word[:n]] += 1.0
    for i in range(len(word) - n):
        gram = word[i : i + n]
        next = word[i + 1 : i + n + 1]
        transitions[gram][next] += 1.0

# normalize the probabilities
for gram in transitions:
    total = sum([transitions[gram][next] for next in transitions[gram]])
    for next in transitions[gram]:
        transitions[gram][next] /= total

# sample a probability mass function (dict from elements to probabilities)
def sample(pmf):
    sample = random()
    cdf = 0.0
    for e in pmf:
        cdf += pmf[e]
        if cdf >= sample:
            return e
    return choice(pmf.keys())

# generate a word according to the markov chain
def gen_word():
    # start with a prefix
    word = sample(transitions[""])

    # wait until the markov chain adds a terminator to the word
    while word[-1] != "$":
        # append a new letter chosen according to the markov chain
        gram = word[-n:]
        if gram in transitions:
            word += sample(transitions[gram])[-1:]
        else:
            word += choice(ascii_lowercase + "$")

        # optional: allow multi-word domains
        if word[-1] == "$" and random() > 0.7 and len(word) < 8:
            word += sample(transitions[""])

    # remove the boundary markers and return the word
    return word.replace("^", "").replace("$", "")

