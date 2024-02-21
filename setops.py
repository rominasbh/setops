import string 
import sys
import re

# Reading input and preprocessing

def read_file(file_name):
    """
    Reads and processes a file line by line to collect words.
    :param file_name: The name of the file to be processed.
    :return: A list of preprocessed words from the file.
    """

    try:
        with open(file_name, 'r') as file:
            return process_file_lines(file,[])

    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return []
    except PermissionError:
        print(f"Error: No permission to read the file {file_name}.")
        return []




#Recursively read lines from the file, process them, and accumulate the results.
def process_file_lines(file, accumulator):
    """
    Recursively processes lines from a file to extract and preprocess words.
    :param file: File object to read from.
    :param accumulator: Accumulator for collecting processed words.
    :return: List of processed words.
    """
    line = file.readline()
    if line == '':
        return accumulator  #End of file reached
    else:
        processed_words = process_line(line.strip(), [])
        return process_file_lines(file, accumulator + processed_words)



#Recursively process each word in the line, preprocess, and accumulate the results.
def process_line(line, accumulator):
    """
    Processes a single line to extract words, preprocess them, and accumulate the results.
    :param line: A string representing a single line from the file.
    :param accumulator: Accumulator for collecting processed words from the line.
    :return: List of processed words from the line.
    """  
    # Base case: line is empty
    if not line:
        return accumulator
    else:

        first, sep, remainder = (line.partition(' ') if ' ' in line else (line, '', ''))
        # Preprocess the first word and recurse on the remainder of the line
        processed_word = preprocess_word(first)
        return process_line(remainder, accumulator + [processed_word] if processed_word else accumulator)


# Recursive function to remove punctuation and convert to lowercase
def preprocess_word(word):
    """
    Preprocesses a word by removing punctuation and converting it to lowercase.
    :param word: The word to preprocess.
    :return: The preprocessed word.
    """
    return to_lowercase(remove_punctuation(word))

def remove_punctuation(word):
    """
    Removes punctuation from a word recursively.
    :param word: The word to remove punctuation from.
    :return: The word without punctuation.
    """
    # Define the punctuation marks
    punctuation_marks = string.punctuation  # if this is not allowed in the assignment define own string of punctuation marks
    
    def remove_punctuation_recursive(word, index=0):
        # Base case: if the index is beyond the last character, return an empty string
        if index == len(word):
            return ''
        else:
            # If the current character is not a punctuation, keep it and proceed to the next
            if word[index] not in punctuation_marks:
                return word[index] + remove_punctuation_recursive(word, index + 1)
            else:
                return remove_punctuation_recursive(word, index + 1)
    
    return remove_punctuation_recursive(word)

def to_lowercase(word):
    """
    Converts a word to lowercase recursively.
    :param word: The word to convert.
    :return: The word in lowercase.
    """
     def to_lowercase_recursive(word, index=0):
        # Base case
        if index == len(word):
            return ''
        else:
            char = word[index]
            # Convert uppercase to lowercase
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + 32)
            return char + to_lowercase_recursive(word, index + 1)
    
    return to_lowercase_recursive(word)



# Set operations
def set_difference(set1, set2):
    # Recursive function to find the difference between two sets
    def difference_recursive(set1, set2, index=0):
        # Base case: If set1 is empty, return an empty list
        if index == len(set1):
            return []
        else:
            if set1[index] not in set2:
                return [set1[index]] + difference_recursive(set1, set2, index + 1)
            else:
                return difference_recursive(set1, set2, index + 1)
    
    return difference_recursive(set1, set2)

def set_union(set1, set2):
    # Recursive function to find the union of two sets
    # Base case: If set1 is empty, add all unique elements from set2
    if not set1:
        return unique_elements(set2, [])
    else:
        return [set1[0]] + set_union(set1[1:], [x for x in set2 if x != set1[0]])

def unique_elements(set2, accumulator):
    if not set2:
        return accumulator
    elif set2[0] not in accumulator:
        return unique_elements(set2[1:], accumulator + [set2[0]])
    else:
        return unique_elements(set2[1:], accumulator)

def set_intersection(set1, set2):
    # Recursive function to find the intersection of two sets
    def intersection_recursive(s1, s2, result=[]):
        if not s1 or not s2:
            return result
        if s1[0] in s2:
            return intersection_recursive(s1[1:], s2, result + [s1[0]])
        else:
            return intersection_recursive(s1[1:], s2, result)
    
    return intersection_recursive(set1, set2)

# Sorting and searching
def recursive_sort(list_to_sort):
    #recursive sorting algorithm mergesort (can do quicksort too later)
     if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        mid = len(list_to_sort) // 2
        left_half = recursive_sort(list_to_sort[:mid])
        right_half = recursive_sort(list_to_sort[mid:])
        return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def recursive_search(sorted_list, item_to_find):
    # recursive binary search, assume list is already sorted 
    def search_helper(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if sorted_list[mid] == item_to_find:
            return mid
        elif sorted_list[mid] < item_to_find:
            return search_helper(mid + 1, high)
        else:
            return search_helper(low, mid - 1)
    
    return search_helper(0, len(sorted_list) - 1)


# Main program function
def setops():
    """
    Main program function to parse input parameters, read and preprocess files,
    perform the specified set operation, sort the result, and write to an output file.
    """
    # Parse input parameters
    #argument validation
    if len(sys.argv) < 2:
        print("Usage: python setops.py \"set1=[filename];set2=[filename];operation=[difference|union|intersection]\"")
        return

    input_str = sys.argv[1]
    params = dict(re.findall(r'(\w+)=([^\;]+)', input_str))

    set1_filename = params.get('set1')
    set2_filename = params.get('set2')
    operation = params.get('operation')

    if not (set1_filename and set2_filename and operation):
        print("Invalid parameters. Please specify set1, set2, and operation.")
        return

    # Read input files and preprocess
    set1 = read_file(set1_filename)
    set2 = read_file(set2_filename)

    # Ensure non-empty results before proceeding
    if not set1 or not set2:
        print("Error: One or both files are empty or could not be processed.")
        return


    # Perform the specified set operation
    if operation == 'difference':
        result = set_difference(set1, set2)
    elif operation == 'union':
        result = set_union(set1, set2)
    elif operation == 'intersection':
        result = set_intersection(set1, set2)
    else:
        print(f"Invalid operation: {operation}")
        return

    # Sort the result
    sorted_result = recursive_sort(result)

    try:
    # Write the result to "result.txt"
        with open("result.txt", "w") as f:
            for word in sorted_result:
                f.write(f"{word}\n")
    
    except IOError as e:
        print(f"Error writing to result.txt: {e}")
        return

    if not sorted_result:
        print("empty set")
    else:
        print(f"Operation {operation} completed. Results saved to result.txt.")

if __name__ == "__main__":
    setops()

'''
input param passed as command-line arguemnts in this format : 
python3 setops.py "set1=a.txt;set2=b.txt;operation=difference"
'''