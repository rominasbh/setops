const fs = require('fs');
const path = require('path');

// Helper function to read file and process lines
function readFile(fileName) {
    try {
        const content = fs.readFileSync(fileName, 'utf-8');
        const lines = content.split('\n');
        return processLines(lines, 0, []);
    } catch (error) {
        console.error(`Error reading file ${fileName}: ${error}`);
        return [];
    }
}

// Recursively process lines from the file
function processLines(lines, index, accumulator) {
    if (index >= lines.length) return accumulator;
    const processedWords = processLine(lines[index], []);
    return processLines(lines, index + 1, accumulator.concat(processedWords));
}

// Recursively process a single line to extract words, handling decimals correctly
function processLine(line, accumulator, currentWord = '', index = 0) {
    if (index >= line.length) {
        if (currentWord) accumulator.push(currentWord.toLowerCase());
        return accumulator;
    }

    const char = line[index];
    const nextChar = line[index + 1];

    // Check for word characters, digits, and decimal points
    if (/\w/.test(char) || (char === '.' && /\d/.test(nextChar))) {
        return processLine(line, accumulator, currentWord + char, index + 1);
    } else {
        if (currentWord) accumulator.push(currentWord.toLowerCase());
        return processLine(line, accumulator, '', index + 1);
    }
}

// Set operations implemented recursively
function setUnion(set1, set2) {
    const combined = [...set1, ...set2];
    const unique = [...new Set(combined)];
    return recursiveSort(unique);
}

function setIntersection(set1, set2) {
    const intersection = set1.filter(item => set2.includes(item));
    return recursiveSort([...new Set(intersection)]);
}

function setDifference(set1, set2) {
    const difference = set1.filter(item => !set2.includes(item));
    return recursiveSort([...new Set(difference)]);
}

// Recursive merge sort for sorting the results
function recursiveSort(array) {
    if (array.length <= 1) return array;
    const mid = Math.floor(array.length / 2);
    const left = recursiveSort(array.slice(0, mid));
    const right = recursiveSort(array.slice(mid));
    return merge(left, right);
}

function merge(left, right) {
    let result = [], indexLeft = 0, indexRight = 0;
    while (indexLeft < left.length && indexRight < right.length) {
        if (left[indexLeft] < right[indexRight]) {
            result.push(left[indexLeft++]);
        } else {
            result.push(right[indexRight++]);
        }
    }
    return result.concat(left.slice(indexLeft)).concat(right.slice(indexRight));
}

// Main function to orchestrate the set operation
function setOps(file1, file2, operation) {
    const set1 = readFile(file1);
    const set2 = readFile(file2);
    let result = [];

    switch(operation) {
        case 'union':
            result = setUnion(set1, set2);
            break;
        case 'intersection':
            result = setIntersection(set1, set2);
            break;
        case 'difference':
            result = setDifference(set1, set2);
            break;
        default:
            console.log("Invalid operation");
            return;
    }

    fs.writeFileSync('result.txt', result.join('\n'));
    console.log(`Operation ${operation} completed. Results saved to result.txt.`);
}

// Parsing command line arguments and executing the program
const [node, script, file1, file2, operation] = process.argv;
setOps(file1, file2, operation);



/*  This is the command line argument syntax to run the code
node script.js a.txt b.txt union
*/