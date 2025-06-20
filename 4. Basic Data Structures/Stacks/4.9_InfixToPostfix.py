from pythonds.basic import Stack


def infixToPostfix(infixExpr):
    #prec is basically to hold the precenedance values for the operators
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    #stack used to temp hold operators and parentheses
    opStack = Stack()
    #list to store the resulting posfix expression
    postfixList = []
    #infix expression split into individual tokens (as tokens, operators, opperands...)
    tokenList = infixExpr.split()

    for token in tokenList:
    
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        
        elif token == "(":
            #the open parthensis is pushed - marking the start of a subexpression
            opStack.push(token)

        elif token == ")":
            #when encountering a closing parenthesis, pop from the stack until an open parenthesis is found
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        #operators are only poped when their precedence dictates it or when the parthenese are closed.        
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

        