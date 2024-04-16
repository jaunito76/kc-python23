# This will implement the book cipher that is described in your
# book on page ___ 
BOOK = 'don-quixote.txt'

def main():
    gen_code_keys = (lambda book, plain_text:
        ({c: str(book.find(c)) for c in plain_text}))
    with open(BOOK) as file:
        book = file.read()
    message = "Hello this is a test message"
    encoder = (lambda code_keys, plain_text:
        ''.join([':' + code_keys[c] for c in plain_text])[1:])
    encrypt = (lambda book, plain_text: encoder(gen_code_keys(book, plain_text), plain_text))
    
    
    
if __name__=="__main__":
    main()