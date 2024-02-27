
### Prerequisites
- Python 3: Ensure you have Python 3.x installed on your system. You can verify this by running the followinf command in your terminal:
`python3 --version`


### Installation
- Project root directory located at /home/cosc4315/team39/HW navigate there to run setops.js and setops.py and run.sh
`cd /home/cosc4315/team39/HW`
- or clone the repository:
`git clone https://github.com/rominasbh/setops.git`

### Usage
-Test Cases: Test cases are located in `/home/cosc4315/team39/HW/Data`. To run the program with these files, specify the file name using the `Data/` prefix followed by the file name. Here are examples for both Python and JavaScript:
    Python Example:
    `python3 setops.py "set1=Data/a.txt;set2=Data/b.txt;operation=difference"`
    Javascript Example:
    `node setops.js Data/a.txt Data/b.txt operation`
    Where operation can be `union` or `intersection` or `difference`

-If you're using new data located in the root directory, specify the file names without the Data/ prefix.

- Batch Execution: To execute multiple test cases as defined in /home/cosc4315/team39/HW/run.sh, run each command line by line. Note that executing run.sh directly will sequentially execute all test cases and overwrite previous results, leaving result.txt with the output relevant to the last executed case.

-File Execution Syntax:
    Python:
    `python3 setops.py "set1=[filename];set2=[filename];operation=[difference   union|intersection]"`

    Javascript:
   `node setops.js [filename] [filename] operation`
    Where operation can be `union` or `intersection` or `difference`



