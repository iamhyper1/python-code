def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse each word
    reversed_words = [word[::-1] for word in words]

    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence
