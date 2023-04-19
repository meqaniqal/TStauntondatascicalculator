#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python calculator
# Exercise for TStaunton Python for data science part 3
# 4/19/2023


# In[2]:


def strip_point_zero(num):
    """
    Reformat numbers as strings that contain no unnecessary decimal points or leading or trailing zeroes
       param: num: the number to process
       returns num as string that has integer format if possible.
    """
    # initialize negative flag
    neg=False
    # make the number a float if it isn't already.
    fltnum=float(num)
    # Get the zero case out of the way
    if fltnum==0:
        return '0'
    # turn negative numbers positive for processing. neg flag will ensure the result is 
    # turned back into a negative number later.
    if fltnum<0:
        neg=True
        fltnum=-fltnum
    
        
    # make string from fltnum.
    processednum=str(fltnum)
    
    # strip off leading or trailing zeros,
    # and if the result has a period at the end, remove the period
    if '.' in processednum:
        processednum=processednum.strip('0').rstrip('.')
        # tack the neg symbol back on after processing if the number was negative
        if neg:
            processednum='-'+processednum
        return processednum
    
    
    return processednum
    ''' previous method:
    numsplit=str(num).split('.')
    if len(numsplit)>1 and numsplit[1].isnumeric():
        # if zero value after decimal point, return the int before the decimal point
        if int(numsplit[1])==0:
            return int(numsplit[0])
    # return the processed or unprocessed number
    return num
    '''


# In[4]:


def calculate(operation,*args):
    """
    Given an option 0-3 representing addition, subtraction, multiplication, and division,
    return a string that shows the order of the operation,
    with result formatted to 2 decimal places.
    
    param: operation: option representing arithmetic operation desired:
                      0: add
                      1: subtract
                      2: multiply
                      3: divide
    param: *args: a tuple containing a list() of numbers
    to perform the arithmetic operation upon.
    """
    # initialize outputstring
    # this will be built based on the operator
    outputstr=''
    # this gives the inner list of numbers
    arglist=args[0]
    # make a version of arglist that is all floats.
    arglistflt=[float(arg) for arg in arglist]
    #print(arglistflt)
    
    # get first number
    result=arglistflt[0]
    # this gets the string value of the chosen operation
    operator=options_list[operation]
    
    if operator=='Add':
        # opstr used in building the output string, assigned different operators depending
        # on the desired operation
        opstr=' + '
        result=sum(arglistflt)
    if operator=='Subtract':
        opstr=' - '
        # since result already contains the first number,
        # use the rest of the numbers after it in the calculation:
        for num in arglistflt[1:]:
           result=result-num
    if operator=='Multiply':
        opstr=' x '
        for num in arglistflt[1:]:
            result=result*num
    if operator=='Divide':
        opstr=' / '
        for num in arglistflt[1:]:
            try:
                #print(type(result),type(num))
                result=result/num
            except ZeroDivisionError:
                print('Cannot divide by zero!')
                return ''
    # build up the string that shows the operation:    
    for num in arglist:
        outputstr+=str(strip_point_zero(num))+opstr
    #strip off last operator (and the space after it) and add equals sign
    outputstr=outputstr[:-2]+' = '
    
    if float(result) != 0:
        # convert result to float with 2 decimal places but turn it into int if equal to int
        resultstr=str(strip_point_zero(f'{float(result):.2f}'))
    else:
        resultstr='0'  
    return outputstr+resultstr


# In[15]:


options_list=['Add','Subtract','Multiply','Divide']
print(('-'*10)+' Python Calculator '+('-'*10)+'\n')
print('Select calculation.\n')
for idx, menuitem in enumerate(options_list,start=1):
    print(f'{idx}. {menuitem}')
while True:
    try:
        option=int(input('Enter 1,2,3,4: '))-1
    except ValueError:
        print('Just numbers, please')
    else:
        break


# In[9]:


while True:
        numbers=input(f'Enter at least 2 numbers to {options_list[option].lower()} separated by commas: ')
        try:
            numberslist=[strip_point_zero(float(num)) for num in numbers.split(',')]
            

        except Exception as e:
            print(e)
            print('Just numbers, please (integer or float). Try again')
            continue
        else:
            # str(numberslist).strip('[]') converts list to string and strips off sq brackets
            # and also do not display integers as floats (followed by '.0'):
            # also, get rid of quotation marks.
            print('you entered: '+ str(numberslist).strip('[]').replace("'",'').replace("'",'').replace('-0','-'))
            if len(numberslist)<2:
                print('You need to enter at least 2 numbers. Please try again.')
            else:
                break


# In[16]:


print(calculate(option,numberslist))


# In[ ]:




