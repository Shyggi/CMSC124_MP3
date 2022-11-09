#Shygfred Christian D. Obado
#BS Computer Science III - A
#CMSC 124 - Design and Implementation of Programming Languages
#Machine Problem 3 - Lexical and Syntax Analysis

#Recursive-Descent Parser for Arithmetic Expressions

'''
GRAMMAR RULES
<expr> ::= <expr>+<term> | <expr>-<term> | <term>
<term> ::= <term>*<factor> | <term>/<factor> | <factor>
<factor> ::= (<expr>) | <digit>
<digit> ::= 0 | 1 | 2 | 3
'''

digit = 1
operator = 2
openParenthesis = 3 
closeParenthesis = 4 
end = 5 
error = 0

def getToken(token: str) -> str:
    match token:
        case '1' | '2' | '3':
            return digit
        case "+" | "-" | "*" | "/":
            return operator
        case "(":
            return openParenthesis
        case ")":
            return closeParenthesis
        case "$":
            return end
        case "":
            return error

def analyzer (string, n):
    next_token = getToken (string [n])
    if next_token != 5:
        next_next_token = getToken (string [n+1])
    if getToken (string[-1]) != 5:
        return False
    else:
        if next_token== getToken (string[-1]) and next_token == 5:
            return True
        else:
            if next_token == 5:
                return False             
            elif string.count ("(") != string.count (")"):
                return False
            else:
                if getToken (string[0]) == 2 or getToken (string[0]) == 4  :
                    return False
                if next_token == 0:
                    return False
                elif next_token== 3:
                    if next_next_token == 2  or next_next_token == 3 or next_next_token == 4 or  next_next_token == 5 or next_next_token == 4:
                        return False
                    else:
                        return analyzer (string, n+1)
                elif next_token== 4:
                    if next_next_token == 1 or next_next_token == 3:
                        return False
                    else:
                        return analyzer (string, n+1)
                elif next_token== 1:
                    if  next_next_token== 1 or next_next_token== 3:
                        return False
                    else:
                        return analyzer (string, n+1)
                elif next_token == 2:
                    if next_next_token == 2  or next_next_token == 4 or next_next_token == 5:
                        return False
                    else:
                        return analyzer (string, n+1)

keepGoing=True
expression = input ("Input String: ")
idx = 0
keepGoing= analyzer (expression, idx)

if keepGoing is True:
    print (f"{expression} is a valid expression.")
else:
    print (f"{expression} is an invalid expression.")
