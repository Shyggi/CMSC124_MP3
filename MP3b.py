#Shygfred Christian D. Obado
#BS Computer Science III - A
#CMSC 124 - Design and Implementation of Programming Languages
#Machine Problem 3 - Lexical and Syntax Analysis

#Recursive-Descent Parser for Multi-Digit Decimal Numbers

'''
GRAMMAR RULES
<expr> ::= +<num> | -<num> | <num>
<num> ::= <num><digits> | <digits>
<digits> ::= <digit> | <digit>.<digit>
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
'''

import string

def getType(token: str) -> str:
    match token:
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0':
            return "Digit"
        case "+" | "-":
            return "Sign"
        case ".":
            return "Dot"
        case "$":
            return "End"
        case "":
            return "None"


class Token:
    def __init__(self, value: str):
        self.value = value
        self.token_type = getType(value)
    
    def getType(self) -> str:
        return self.token_type


class Parser:
    def __init__(self, string: str):
        self.string = string
        self.pos = 0
        self.currToken = Token("")
           

    def parse(self):
        self.currToken = Token(self.string[self.pos])

        self.next()
        self.expr()

        if self.currToken.getType() == "End" and self.pos - 1 == len(self.string) - 1:
            print(f"{self.string} is a valid expression.")
            return 
        else:
            print(f"{self.string} is an invalid expression.")
            return 

    def next(self):
        if self.pos < len(self.string):
            self.currToken = Token(self.string[self.pos])
            self.pos += 1
        else:
            self.currToken = Token("") 

    def expr(self):
        if self.currToken.getType() in ["Digit", "Dot"]:
            self.num()
        elif self.currToken.getType() == "Sign":
            self.next()
            self.num()
        else:
            return
    
    def num(self):
        if self.currToken.getType() == "Digit":
            self.next()
            self.num()
        elif self.currToken.getType() == "Dot":
            self.next()
            if self.currToken.getType() == "End":
                return
            self.int()
        elif self.currToken.getType() == "End":
            pass
        else:
            return

    def int(self):
        if self.currToken.getType() == "Digit":
            self.next()
            self.int()
        elif self.currToken.getType() == "End":
            pass
        else:
            return

string = input("Enter string to parse: ")
p = Parser(string)
p.parse()
