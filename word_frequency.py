STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
PUNC = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
#create a string from read file and replace caps with lower
    read_file = open(file, 'r').read().lower()
#words separated by hyphens are replaced with white space
    read_file = read_file.replace('—', ' ')
#create a list words split at white space of read_file
    words = read_file.split()

#replace punctuation elements
#create dictionary counts and add each word in words to it and increment count
#skip over words that are in STOP_WORDS
    counts = dict()
    for word in words:
        for elem in word:
            if elem in PUNC:
                word = word.replace(elem, '')
        if word not in STOP_WORDS:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    #sorted_keys = sorted(counts.items())
    #counts_dict = dict(sorted_keys)
    import operator
    sorted_counts = sorted(counts.items(), key=operator.itemgetter(1))
    # Set star_display, word_length, and padded_key lists
    star_display = []
    word_length = []
    padded_key = []
    # Initial longest_word)length
    longest_word_length = len(sorted_counts[0][0])


# Initialize star and padded_key arrays and find longest_word_length
    for i in range(len(sorted_counts)):
        len(sorted_counts[i][0])
        star_display.append('')
        word_length.append(len(sorted_counts[i][0]))
        padded_key.append(sorted_counts[i][0])
        if i > 0:
            if len(sorted_counts[i][0])>longest_word_length:
                longest_word_length = word_length[i]

# Inner loops to assign padding to padded_key and set number of *'s for display
    for i in range(len(sorted_counts)):
        for j in range(longest_word_length - word_length[i]): 
            padded_key[i] = ' ' + padded_key[i]
        for k in range(int(sorted_counts[i][1])):
            star_display[i] += '*'

# Loop to print in descending order of word count        
    for i in reversed(range(len(sorted_counts))):
        if int(sorted_counts[i][1]) > 1:
            print(padded_key[i], '|', sorted_counts[i][1], star_display[i])
    
    return sorted_counts
    
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
