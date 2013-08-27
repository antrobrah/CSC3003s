# CSC3003S
# Lauren Antrobus, ANTLAU001
# COMPILERS Assignment 1: 
# Lexical analysis, using PLY (http://www.dabeaz.com/ply/ply.html)
# 25 August 2013

# --- Reserved words -------------------------------------------
reserved = {
   'else' : 'ELSE',
   'float' : 'FLOAT',
   'for' : 'FOR',
   'if' : 'IF',   
   'int' : 'INT',
   'return' : 'RETURN',
   'void' : 'VOID',
   }


# --- Recognised token names ------------------------------------
tokens = [
   'COMMENT',   
   'ID',
   'OPERATOR',
   'INT_LITERAL',
   'FLOAT_LITERAL',
   'WHITESPACE',
   ] + list(reserved.values())

''' 
--- Function definitions -----------------------------------------
'''

# --- Comments ---------------------------------------------------
# Both /*...*/ and // (\n handled by whitespace) comments
# listed before OPERATOR for preference ordering 
def t_COMMENT(t):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
    return t


# --- Float literals ---------------------------------------------
# defined before integer literal, for preference ordering
# exponential notation checked before normal decimal, for preference ordering
def t_FLOAT_LITERAL(t):
    r'(\d+)(\.)(\d)*(((e|E)((\+|-)?))?)(\d)*(F|f)*'
    return t


# --- Integer literal --------------------------------------------
def t_INT_LITERAL(t):
    r'\d+'
    t.value = int(t.value)    
    return t


# --- ID's -------------------------------------------------------
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value,'ID')  
    return t


# --- Whitespace -------------------------------------------------
def t_WHITESPACE(t):
    r'[\n\r\s\t]+'
    return t


# --- Operators --------------------------------------------------
# single operators implemented as literals (checked last)
literals = ['+',  '-',  '*',  '/',  '%', '<',  '>', '=', '!',  ';',  ',',  '.', '(', ')', '{', '}', '[', ']']
# two-character operators implemented as function
# checked before single operators
# implemented after comments for preference ordering
def t_OPERATOR(t):
    r'<=|>=|={2}|!=|&{2}|\|{2}|\(\)|\{\}|\[\]'
    return t


# --- Error function ---------------------------------------------
def t_error(t):
    print("ERROR("+t.value+")")
    t.lexer.skip(1)


''' 
--- Run code -----------------------------------------------------
'''

#imports
import ply.lex as lex 
import sys #to extract command line values

# set up lexer
lexer = lex.lex()

# file management
filename = str(sys.argv[1]) # get filename from cmd line args
infile = open(filename, "r")
data = infile.read()

# give input file data to lexer
lexer.input(data) 

# Tokenize data, until end of file
while True:
    tok = lexer.token() # get next token
    if not tok: break      # No more input
    
    # process output
    if tok.type == 'OPERATOR':
        print(tok.value)
    elif tok.type == 'FLOAT_LITERAL':
        print("FLOAT_LITERAL("+str(tok.value)+")")    
    elif tok.type == 'INT_LITERAL':
        print("INT_LITERAL("+str(tok.value)+")")
    elif tok.type == "ID":
        print("ID("+tok.value+")")        
    else:
        print(tok.type)