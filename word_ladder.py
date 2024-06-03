from stack import Stack
from my_queue import Queue
from time_this import *

def read_words(filename):
    """
    Reads the words in the specified file and returns a dictionary containing those words
    :param filename: name of file containing all legal words
    :return: dictionary containing all the legal words
    """
    word_dict = {}
    infile = open(filename, "r")
    key = 1
    for line in infile:
        word_dict[key] = line.strip()
        key += 1

    infile.close()

    return word_dict



def get_next_words(word, dict):
    """
    Returns a list of "unused" words in dict from the read_words function that are one letter different from word

    :param word: a word
    :param dict: dictionary containing all the legal words
    :return: a list of "unused" words in dictionary that are exactly one letter different from word
    """

    next_words = []
    for candidate in dict.values():
        diff_count = 0
        if len(candidate) != len(word):
            continue  # Skip words of different lengths

        for i in range(len(word)):
            if word[i] != candidate[i]:
                diff_count += 1
                if diff_count > 1:
                    break  # Exit inner loop if difference is more than 1

        if diff_count == 1:
            # If the word hasn't been used already
            next_words.append(candidate)

    return next_words






def find_ladder(start_word, end_word, dict):
    """
    Finds and returns a stack representing the word ladder between start_word and end_word
    :param start_word: the starting word for the ladder
    :pram end_word: the ending word for the ladder
    :param dict: dictionary containing all the legal words
    :return: a stack representing the word ladder between start_word and end_word, if one
            exists, None otherwise
    """
    word_stack = Stack()  # Create a new stack
    word_stack.push(start_word)  # Push the word onto the new stack
    words_queue = Queue()        # Create a new queue
    words_queue.enqueue(word_stack)     # Enqueue the stack into the queue

    duplicate_words = []         # Initialize an empty list that will be used to track words that have been used in the stack so that they won't be used again (causing an infinite loop)

    max_queue_length = words_queue.size()      # Initializes the max queue length
    while not words_queue.is_empty():          # Check to see if the queue is empty, if not:

        current_stack = words_queue.dequeue()    # Dequeue the stack from the queue and assign it a variable
        current_word = current_stack.peek()      # Peek the current stack and assign it a variable for tracking

        if current_word == end_word:     # If the word from the peeked stack is the end word:
            return current_stack, max_queue_length    # Return the word ladder stack and the maximum length the queue reached

        next_words_list = get_next_words(current_word, dict)       # Call the get_next_words function and assign it a variable

        for word in next_words_list:       # Loop through the list of words from the get_next_words function
            if word not in duplicate_words:     # If the word from the words list is not also in the duplicate words list:
                duplicate_words.append(word)    # Append the word to duplicate words
                cloned_stack = current_stack.clone()    # Clone the current stack being used
                cloned_stack.push(word)                 # Push the word onto the cloned stack
                words_queue.enqueue(cloned_stack)       # Queue the cloned stack onto the words queue

        if max_queue_length < words_queue.size():
            max_queue_length = words_queue.size()     # Replace the variable max_queue_length with the size of the current words queue if it is larger

    return None, max_queue_length    # Return no word ladder and the max queue length if there is no word ladder to return



def main():
    word_dict = read_words("resources/dictionary.txt")

    input_file = open("resources/input.txt", "r")
    test_number = 0
    for line in input_file:
        words = line.strip().split()       # Split the two words from the line into two items
        start_word, end_word = words[0], words[1]     # Assign start_word to the first item/string on the line and end_word to the second
        test_number += 1

        # time_this function has been edited to simply return the time taken for the function to run
        # so that the following method in main can be accomplished
        timed = time_this(find_ladder, start_word, end_word, word_dict)
        result, max_queue_length = find_ladder(start_word, end_word, word_dict)

        if result is None:
            print(str(test_number) + ". " + str(timed) + " seconds: " + "There is no word ladder between " + str(start_word) + " and " + str(end_word) + "! Maximum queue length = " + str(max_queue_length))
        else:
            result_for_print = str(result).replace("'", "")
            print(str(test_number) + ". " + str(timed) + " seconds: ladder length = " + str(result.size()) + ": " + result_for_print + ". Maximum queue length = " + str(max_queue_length))


main()


