BOOK = "words.txt"


def word_frequency(file_name: str) -> dict:
    """
    file_name (str): this is the name
        of the file that is located in your project directory
    word_frequency returns a DICTIONARY in the form
        {<WORD: str>: <count_of_word: int>} that contains the
        number of times a word is used in the file above
    """

    #   Open the file
    #   read the file
    #   close the file
    #   Make the list of words from the file
    #   Loop through all the words
    #       # Count each word
    #       If I've seen the word ->
    #           add to the dictionary value
    #       Else
    #           Add word (key) to the dictionary
    #   Return dict
    def get_word_list(file_name: str) -> list:
        """ """
        with open(file_name, "r", encoding="utf8") as daniels_book:
            return [word for line in daniels_book for word in line.split()]

    def remove_punctuation(word: str) -> str:
        new_word = ""
        for chr in word:
            if chr.lower() in "abcdefghijklmnopqrstuvwxyz\'":
                new_word += chr
        return new_word

    word_list = [remove_punctuation(word).lower() for word in get_word_list(file_name)]
    # print(word_list)
    mydict = {}
    for word in word_list:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1
    return mydict


def sort_by_frequency(frequency):
    """
    frequency: dict in the form of
        {<WORD: str>: <count_of_word: int>}
    sort_by_frequency returns a sorted dictionary with the largest
        first (hint the sorted() function will be a big help here)

        For Extra Credit:
        Use a lambda function to sort the dictionary
    """
    sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_frequency


def get_arguments():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--input", help="input filename")
    argParser.add_argument("-o", "--output", help="output filename")
    return argParser.parse_args()


def main():
    args = get_arguments()
    fn = BOOK
    if not args.input is None:
        print("*********** args.input: ", args.input)
        fn = args.input
    if not args.output is None:
        try:
            old_std, sys.stdout = sys.stdout, open(args.output, "w")
        except:
            print(" ** Unable to open the file **")
    print(f"File name is: {fn}")
    frequency = word_frequency(fn)
    sorted_frequency = sort_by_frequency(frequency)
    for word, freq in sorted_frequency:
        freq_txt = f"Frequency: {freq}"
        print(f"Word: {word:25s} {freq_txt:15s}")


if __name__ == "__main__":
    main()
