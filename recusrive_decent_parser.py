#grammar
# E--> iE'
# E'--> +iE'/epsilon

input = "i+i+i$" #$ is end of input,,
i=0
charc = input[i] # we will start with first charcter
rval = True # This is global flag to check whether parsing was succeed
# we are declaring input as global, so that it is accessable to all functions

# This function will match input charatcer with Grammar Charatcer
def match(var): # here charc point to the charcter, that need to be matched
    global i
    global input
    global charc
    global rval
    if(var == input[i] and var != "$"): 
        # if the charcter is matched with string charcter, but it should not be the end charcter
         i=i+1  # You need to go to next charcter
         charc =  input[i]
         rval = True
         return rval #Its Fine Go Ahead,,as no error is their
    else:
        #print("\n There is an Error in the input string")
        rval = False
        return rval  # It means their is an Error, You need to quite

def E(): #This function implemnts E non-terminal
    global i
    global input
    global charc
    global rval
    if( charc == "i"): 
        rval = match("i")
        if rval and charc !="$": #It means its True and we are not at end of input
            rval = E_bar()  # Then proceed further in parsing
        else:
            return rval
    else:
        return False
    return rval

def E_bar():
    global i
    global input
    global charc
    global rval
    if( charc == "+"): #if input is +, we also need to check next charcter
    # whether it is i or not ,,as production is E'--->+iE'
        rval = match("+")
        #rval = match("i")
        if rval: # then match next i
            rval = match("i")
            if rval and charc != "$": # we are not at end of input
                rval = E_bar()
            else:
                return rval
        else:
            return rval # return rvale 
        
    else:
        rval = False
        return rval # simply return to previous function in recusrrion
    return rval

if __name__ == "__main__": # This is the main Function 
    #global rval
    rval = E()
    if( rval): # we reached end of parsing, and still rval is True
        print("\n Parsing Succeed")
    else:
        print("\n There is an Error While Parsing")
