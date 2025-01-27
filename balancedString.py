#write a python program for balanced paranthesis(check whether the string is balanced or not)
def is_balanced_parentheses(input_string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False
    return len(stack) == 0
input_string = "(({}))((()))"
if is_balanced_parentheses(input_string):
    print("The string is balanced.")
else:
    print("The string is not balanced.")
