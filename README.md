# Set Operations Programs

This repository contains two programs for performing set operations (union, intersection, and difference) on text data. The first program is written in JavaScript (Node.js) and the second in Python. Both programs read from text files, process the contents to extract words, perform the specified set operation, and save the results.

## JavaScript Program

### Prerequisites
- Node.js installed on your system.

### Installation
- Clone the repository or download the JavaScript file.

### Usage
Run the script from the command line, passing in the names of two text files and the operation to perform:

`node setOps.js file1.txt file2.txt operation`

Available operations: `union`, `intersection`, `difference`.

### File Format
- The input files should be text files with words separated by new lines or spaces.

## Python Program

### Prerequisites
- Python 3 installed on your system.

### Installation
- Clone the repository or download the Python file.

### Usage
Run the script from the command line with a single argument in the format:

`set1=[filename];set2=[filename];operation=[operation]"`

Available operations: `difference`, `union`, `intersection`.

### File Format
- The input files should be text files with words separated by new lines or spaces.

## Features
- Both programs support three set operations: union, intersection, and difference.
- Recursive functions are used for reading files, processing lines, and performing set operations.
- The Python version includes additional functionality for recursive sorting and searching.

