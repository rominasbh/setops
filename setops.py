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
def process_line(line, accumulator, current_word='', index=0):
    """
    Recursively processes a single line to extract words and numbers, including decimals,
    ensuring that decimal numbers are treated as single entities and not split.
    :param line: A string representing a single line from the file.
    :param accumulator: Accumulator for collecting processed words and numbers from the line.
    :param current_word: The current word or number being accumulated.
    :param index: The current index in the line being processed.
    :return: List of processed words and numbers from the line.
    """
    # Base case: Reached the end of the line
    if index == len(line):
        if current_word:  # Add any final accumulated word or number
            accumulator.append(preprocess_word(current_word))
        return accumulator
    
    char = line[index]
    next_char = line[index + 1] if index + 1 < len(line) else None
    
    # Check if character is part of a word/number, including decimal numbers
    if char.isalnum() or (char == '.' and current_word.isdigit() and next_char and next_char.isdigit()):
        return process_line(line, accumulator, current_word + char, index + 1)
    else:
        # If current_word is not empty, it means we've reached the end of a word/number
        if current_word:
            accumulator.append(preprocess_word(current_word))
            return process_line(line, accumulator, '', index + 1)
        # If current_word is empty and char is not part of a word/number, skip it
        return process_line(line, accumulator, current_word, index + 1)

def preprocess_word(word):
    """
    Converts a word to lowercase. This function can be expanded to include
    additional preprocessing steps as needed.
    """
    return word.lower()



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

def set_union(set1, set2,result=[]):
    """
    Recursively finds the union of two sets, ensuring each element appears exactly once.
    Assumes both sets are already preprocessed to be case-insensitive.
    :param set1: List representing the first set.
    :param set2: List representing the second set.
    :param result: Accumulator for the union result.
    :return: A sorted list representing the union of the two sets with unique elements.
    """
    if not set1 and not set2:
        # Base case: both sets are empty, return the deduplicated, sorted result
        return sorted(list(set(result)))
    elif set1:
        # Process the first element of set1 if it's not empty
        if set1[0] not in result:
            result.append(set1[0])
        return set_union(set1[1:], set2, result)
    else:
        # Process the first element of set2 if set1 is empty and set2 is not
        if set2[0] not in result:
            result.append(set2[0])
        return set_union(set1, set2[1:], result)



def set_intersection(set1, set2):
    # Recursive function to find the intersection of two sets
    def intersection_recursive(s1, s2, index=0, result=None):
        if result is None:
            result = []
        # Recursive exit condition
        if index == len(s1):
            return result

        item = s1[index]
        if item in s2 and item not in result:
            # Condition ensures only first-time noticed intersections are added
            result.append(item)
        # Call the next level of the stack, accounting for all cases
        return intersection_recursive(s1, s2, index + 1, result)
    
    # Call to a helper method to effectively recurse, providing the unicity factor
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

    if not sorted_result:  #check this 
        print("empty set")
    else:
        print(f"Operation {operation} completed. Results saved to result.txt.")

if __name__ == "__main__":
    setops()

'''
input param passed as command-line arguemnts in this format : 
python3 setops.py "set1=a.txt;set2=b.txt;operation=difference"
'''