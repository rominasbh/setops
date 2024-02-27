#Commands to run setops.py for the test cases
python3 setops.py "set1=Data/a1.txt;set2=Data/b1.txt;operation=intersection"
python3 setops.py "set1=Data/a2.txt;set2=Data/b2.txt;operation=difference"
python3 setops.py "set1=Data/a3.txt;set2=Data/b3.txt;operation=union"
python3 setops.py "set1=Data/a4.txt;set2=Data/b4.txt;operation=intersection"


#Commands to run setops.js for the test cases
`node setops.js Data/a1.txt Data/b1.txt intersection`
`node setops.js Data/a2.txt Data/b2.txt difference`
`node setops.js Data/a3.txt Data/b3.txt union`
`node setops.js Data/a4.txt Data/b4.txt intersection`
