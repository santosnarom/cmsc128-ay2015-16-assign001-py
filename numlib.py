# Number Library 
# by: Narom P. Santos 
# Functions: 
# Number to Words 
# Words to Numbers 
# Words to Currency 
# Numbers Delimited 

## Numbers to Words ##
def numToWords(num):    #convert a whole number to words

    #dictionaries of digit-to-word mapping
    ones = {'0' : '', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five',
            '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}
    tenths = {'0' : '','1' : 'ten', '2' : 'twenty', '3' : 'thirty', '4' : 'forty', '5' : 'fifty',
              '6' : 'sixty', '7' : 'seventy', '8' : 'eighty', '9' : 'ninety'}
    special = {'0' : 'ten', '1' : 'eleven', '2' : 'twelve', '3' : 'thirteen', '4' : 'fourteen',
               '5' : 'fifteen', '6' : 'sixteen', '8' : 'eighteen', '9' : 'nineteen'}

    #variable initializations 
    string = str(num)
    position = len(string)
    ignore = True   #if true, ignores printing of "thousand"
    specialCase = False #for numbers 11-19

    if position > 7:
        print("Error: Number too large")
    else:

        #zero special case
        if position == 1 and string == '0':
            print('zero')
        
        #iterates for each place in the number string
        for place in string:

            #special case, prints using the special dict
            if specialCase == True:
                print(special[place] + " ")

            #millionths place
            if (position == 7) and (place != '0'):
                print(ones[place] + " " + "million")

            #hundred thousandths place
            elif (position == 6) and (place != '0'):
                print(ones[place] + " " + "hundred")
                ignore = False

            #ten thousandths place    
            elif (position == 5) and (place != '0'):
                if place == '1':
                    specialCase = True
                else:
                    print(tenths[place])
                ignore = False

            #thousandths place    
            elif (position == 4):
                if specialCase == True:
                    print("thousand")
                    specialCase = False
                else:
                    if ignore == False:
                        print(ones[place] + " " + "thousand")
                    elif (ignore == True) & (place != '0'):
                        print(ones[place] + " " + "thousand")
                        
            #hundredths place
            elif (position == 3) and (place != '0'):
                print(ones[place] + " " + "hundred")

            #tenths place  
            elif (position == 2) and (place != '0'):
                if place == '1':
                    specialCase = True
                else:
                    print(tenths[place])

            #ones place        
            elif (position == 1) & (place != '0') and (specialCase == False):
                print(ones[place])

            position = position - 1
            
        #end of for loop

#########################################################################

import re

## Words to Numbers ##
def wordsToNum(word):

    #dictionary of word-to-value mapping
    words = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6,
             'seven' : 7, 'eigth' : 8, 'nine' : 9, 'ten' : 10, 'eleven' : 11, 'twelve' : 12,
             'thirteen' : 13, 'fourteen' : 14, 'fifteen' : 15, 'sixteen' : 16, 'seventeen' : 17,
             'eighteen' : 18, 'nineteen' : 19, 'twenty' : 20, 'thirty' : 30, 'forty' : 40,
             'fifty' : 50, 'sixty' : 60, 'eighty' : 80, 'ninety' : 90, 'hundred' : 100,
             'thousand' : 1000, 'million' : 1000000}

    #initializations
    chars = word.split()
    accumulator = 0
    previous = 0
    failed = False

    for char in chars:   
        if re.search('(thousand|million)', char):
            previous = previous * words[char]
            accumulator = accumulator + previous
            previous = 0
        elif re.search('(hundred)', char):
            previous = previous * words[char]
        else:
            if char in words:
                previous = previous + words[char]
            else:
                print('Unknown character: ' + char)
                failed = True
    accumulator = accumulator + previous
    
    if failed == False:
        return accumulator
    
#############################################################

import re                

## Words to Currency ##
def wordsToCurrency(word, currency):

    num = wordsToNum(word)

    if re.search('(USD|JPY|PHP)', currency):
        return currency + str(num)
    else:
        print("Error: Invalid currency")





        
