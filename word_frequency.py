STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
PUNC = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

fileObject = open('praise_song_for_the_day.txt', 'r')
data = fileObject.read()
# print(data)
# print(type(fileObject))
# print(type(data))

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        l_word = word.lower()
        for elem in l_word:
            if elem in PUNC:
                l_word = l_word.replace(elem, '')
        if l_word not in STOP_WORDS:

            if l_word in counts:
                counts[l_word] += 1
            else:
                counts[l_word] = 1
    print(type(counts))
    print(counts.values())
    return counts
    

print(word_count(data))


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
