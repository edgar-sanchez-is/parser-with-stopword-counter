# Write a Python script that takes in command line arguments.
# The first argument will be a URL. The second will be a file containing stopwords.
# Each line in the stopword file will be a new stopword.

# Your Python script should return the top 10 words with the number of occurrences
# regardless of casing sorted by most frequent. Your script should ignore tags,
# ignore stopwords, and remove punctuation.

import sys
import re
import collections
import urllib2
from bs4 import BeautifulSoup


def main():
    with open(sys.argv[2]) as f:
        stopwords = f.read().split()
    stopwords.append('s')

    # data from url
    data = urllib2.urlopen(sys.argv[1]).read()
    soup = BeautifulSoup(data, 'html.parser')

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()

    # Use regular expressions to do a find-and-replace
    text = re.sub("[^a-zA-Z]",  # The pattern to search for
                          " ",  # The pattern to replace it with
                          soup.get_text())  # The text to search
    lower_case = text.lower()
    words = lower_case.split()

    words = [w for w in words if not w in stopwords]

    counter = collections.Counter(words)

    iter = 1
    for value, count in counter.most_common()[:10]:
        print iter, " - ", str(value), " : ", count
        iter += 1

if __name__ == "__main__":
    main()