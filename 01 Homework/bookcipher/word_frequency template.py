BOOK = 'don-quixote.txt'



def word_frequency(file_name: str) -> dict:
    """
    file_name (str): this is the name 
        of the file that is located in your project directory
    word_frequency returns a DICTIONARY in the form 
        {<WORD: str>: <count_of_word: int>} that contains the 
        number of times a word is used in the file above
    """

    def get_list_from_file(file_name: str) -> list:
        file = open(file_name)
        with file:
            

    #   Open the file
    #   read the file
    #   close the file
    #   Make the list of words from the file
    #   Loop through all the words
    #       Count each word 
    #       If I've seen the word ->
    #           add to the dictionary value
    #       Else
    #           Add word (key) to the dictionary
    #   Return dict

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

def main():
    frequency = word_frequency(BOOK)
    print(frequency)
    sorted_frequency = sort_by_frequency(frequency)
    for word, freq in sorted_frequency:
        freq_txt = f'Frequency: {freq}'
        print(f'Word: {word:25s} {freq_txt:15s}')

if __name__ == "__main__":
    main()