def caseVowel(chr):
    match chr:
        case 'a': print ("Vowel: {}".format(chr))
        case 'e': print ("Vowel: {}".format(chr))
        case 'i': print ("Vowel: {}".format(chr))
        case 'o': print ("Vowel: {}".format(chr))
        case 'u': print ("Vowel: {}".format(chr))
        case _: print ("Not a vowel: {}".format(chr))

caseVowel('a')
caseVowel('z')

def caseVowel1(chr):
    match chr:
        case 'a' | 'e' | 'i' | 'o' | 'u': print ("Vowel: {}".format(chr))
        case _: print ("Not a vowel: {}".format(chr))

caseVowel1('e')
caseVowel1('y')
