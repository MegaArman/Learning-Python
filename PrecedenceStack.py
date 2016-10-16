#Arman Bahraini

PF1 = "0!!!1/10&1!!&=1=0|"
PF2 = "10=!10/&11!0/=1|11!&|&0/"
tos = -1 

def push(stack, element):
    global tos
    tos += 1
    stack[tos] = element
    
def pop(stack): 
    global tos
    temp = stack[tos]
    stack[tos] = None
    if tos > -1:
        tos -= 1
        
    return temp

def LogicalEval(expression):
    global tos
    tos = -1 # Must reset
    length = len(PF1)
    myStack = [None] * length

    def Not(expr):
        negateExpr = None

        if expr == 1:
            negateExpr = 0
        elif expr == 0:
            negateExpr = 1

        push(myStack, negateExpr)
        return negateExpr
        
    def And(expr1, expr2):
        andExpr = expr1 & expr2
        push(myStack, andExpr)
        return andExpr
        
    def Not_equal(expr1, expr2):

        notEqualExpr = 0

        if expr1 != expr2:
            notEqualExpr = 1

        push(myStack, notEqualExpr)
        return notEqualExpr
        
    def Equal(expr1, expr2):
        equalExpr = 0
        
        if (expr1 == expr2):
            equalExpr = 1
            
        push(myStack, equalExpr)
        return equalExpr

    def Or(expr1, expr2):
        orExpr = expr1 | expr2
        push(myStack, orExpr)
        return orExpr 

# process expression
 
    for c in expression:
        if c == '0':
            push(myStack, 0)
        elif c == '1':
            push(myStack, 1)
        elif c == '!':
            Not(pop(myStack))
        elif c == '&':
            And(pop(myStack), pop(myStack))
        elif c == '/':
            Not_equal(pop(myStack), pop(myStack))
        elif c == '=':
            Equal(pop(myStack), pop(myStack))
        elif c == '|':
            Or(pop(myStack), pop(myStack))

    print('stack[0] is ', myStack[0])
    

LogicalEval(PF1)
LogicalEval(PF2)
LogicalEval('11=0/0!&1|')
