def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

def main():
    input_sentence = input("Enter a sentence: ")
    reversed_sentence = reverse_words(input_sentence)
    print("Reversed sentence with reversed words:", reversed_sentence)

if __name__ == "__main__":
    main()
