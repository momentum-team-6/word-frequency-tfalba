STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
PUNC = r'''!()-[]{};:'"\, <>./?@#$%^&*_~'''

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    read_file = open(file, 'r').read().lower()
    read_file = read_file.replace('—', '  ')
    read_file = read_file.replace('-', ' ') 
    words = read_file.split()

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
    
    print(counts)
    # Next up write a sorter to sort by count value over keys and then print **** based on number
    # for value in counts.values():
    #     print(value)
    return counts
    
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
