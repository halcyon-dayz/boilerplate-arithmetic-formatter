import re

#set the "optional" argument (a quick google search gives you a stackoverflow link)
def arithmetic_arranger(problems, answers=False):
    #Start the function off with some error cases. iterate through the items(i) in [problems], and use regex to
    #match and print an error message if any return True.

    #update: Let"s give some variables scope in this block
    first = ""
    second = ""
    dashes = "" #cause it seems like we"re gonna need it
    answer_row = "" #this one too
    arranged_problems = "" #making this a string cause that"s what we"re ultimately printing, right?

    #First, check the length of "problems" and return an error if there"s more than five
    if (len(problems) > 5):
        return "Error: Too many problems."


        

    for i in problems:
        #based on test cases, these should suffice
        numbers = re.search(r"[^\s0-9.+-]", i) 
        mult = re.search("[*]", i)
        div = re.search("[/]", i)
        if (div or mult):
            return "Error: Operator must be '+' or '-'."
        if (numbers):
            return "Error: Numbers must only contain digits."
        # Obviously here I am simply splitting the three parts of each string and assigning them.
        top = i.split()[0]
        op = i.split()[1]
        bottom = i.split()[2]

        #Check the operands, and make sure they are 4 or less in length
        if (len(top) >= 5 or len(bottom) >= 5):
            return "Error: Numbers cannot be more than four digits."

        #Test cases finished! Let"s go back and make "top" "op" and "bottom" have scope!

        #Find the total width(len) of each set of problems, so we can make dashes and also place the operator!
        width = max(len(top), len(bottom)) + 2 #Add two cause there"s a space and an operator there
        dash = ""
        for i in range(width):
            dash += "-" #Let"s add some dashes now that we have the total width of each set

        #Let"s find the answers! First I tried to just convert to int() and then add or subtract
        #but you can do that while retaining the string type, if you wrap the expression in str() like this
        if (op == "+" or "-"):
            if (op == "+"):
                answer = str(int(top) + int(bottom)) # if +, then add
            else:
                answer = str(int(top) - int(bottom)) # else subtract
        
        #Okay now we have basically all we need, let"s add some spaces and combine it all into the
        #arranged_problems string!
        top_row = top.rjust(width)
        bottom_row = op + bottom.rjust(width - 1)
        answer_row = answer.rjust(width)

        #first we add four spaces "    " to the end of each (i) in problems (our main loop) by appending 
        #each row. We add the op string to the bottom row as well.
        count = 2
        if count < len(problems):
            top_row += top + "    "
            bottom_row += bottom + "    "
            dashes += dash + "    "
            answer_row += answer + "    "
            count += 1
        else:
            top_row += top
            bottom_row += bottom
            dashes += dash
            answer_row += answer
        
        #Let"s concat each part of the finished set to the arranged_problems string, with two cases,
        #one for the answers=True argument, and one for the default (answers=False)
    if answers == True:
        arranged_problems = first + "\n" + second + "\n" + dashes + "\n" + answer_row
    else:
        arranged_problems = first + "\n" + second + "\n" + dashes
    return arranged_problems 

#I pulled some of the test problems from test_module.py to assist, as I don"t like the replit.com IDE
#print(arithmetic_arranger(["32 + 8", "1 - 333801", "659999 + 9999", "523 - 49"]))
#print(arithmetic_arranger(["32 + 8", "1 - 333", "6599 + 9999", "523 - 49", "32 + 8", "32 + 8"]))
#print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["98 + 35", "3801 - 2", "45 * 43", "123 + 49"]))
#print(arithmetic_arranger(["98 + 35", "3801 - 2", "45 + 43", "123 / 49"]))
