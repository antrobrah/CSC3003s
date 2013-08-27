--- README ---------------------------------------------------------------

Course:     CSC3003S Assignment 1
Author:     Lauren Antrobus, ANTLAU001
27 August 2013



--- Program Description -------------------------------------------------

This program uses the PLY lexical analyser generator 
(see http://www.dabeaz.com/ply/ply.html) to create a lexical analyser (lexer), 
implemented in Python 3.2, for a made-up programming language called s-lang. 

The created lexer should 
convert a specified s-lang input source code file into tokens which can be 
used for the remaining modules of a compiler.

Token types include comments (both single and multiline), identifiers,
operators, integers, floats, whitespace and reserved words.



--- Run Instructions ----------------------------------------------------

1. Change the current directory to the directory containing the source file

2. Ensure that the lexicalAnalysis_ANTLAU001.py file, input file and ply folder 
    are present in this directory
    
3. Run the command:
        $ python lexicalAnalysis_ANTLAU001.py [input file name]
    where the input file name is specified as the second cmd line argument.
    For example:
        $ python lexicalAnalysis_ANTLAU001.py test.sl
        
4. The code will execute and output will display to the terminal

Should you choose to use it, a sample input file named "test.sl" containing all
recognised token types has been provided for your convenience. 

Enjoy your day! :)



--- Included files ----------------------------------------------------

1. lexicalAnalysis_ANTLAU001.py 
2. PLY-3.4 package (available from http://www.dabeaz.com/ply/)
3. test.sl
4. README.txt