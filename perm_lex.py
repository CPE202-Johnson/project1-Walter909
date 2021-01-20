#a string -> string
#return a list of strings
def perm_gen_lex(a):
    #Base cases
    if a == '':
        return []
    if len(a) == 1:
        return [a]

    list = []                               #create list
    for letter in a:
        simple = a.replace(letter,'')       #Reduced: remove a letter to create a simpler string

        for perm in perm_gen_lex(simple):   #generate all permutations & recursive call

            list.append(letter + perm)      #Combined: add the character back to the permutations and append them to a list

    return list                             #return our list with permutations