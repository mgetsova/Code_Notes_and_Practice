import re

s = 'geeks.forgeeks'
'''
Escape Symbol (\) - if want to match for the characters "+", ".", etc., add a 
backslash before it
'''
# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\.', s)
print(match)

'''
Square Brackets [] - represent a character class consisting of a set of characters that we wish to match. For example, the character class [abc] will match any single a, b, or c. 
We can also specify a range of characters using – inside the square brackets. For example, 

[0, 3] is sample as [0123]
[a-c] is same as [abc]
We can also invert the character class using the caret(^) symbol. For example, 

[^0-3] means any character except 0, 1, 2, or 3
[^a-c] means any character except a, b, or c
'''
string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)
print(result)

'''
Caret Symbol (^) - match must start at the begining of the string or line
'''
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')

'''
Dollar Symbol ($) - match must occur at end of the string or before \n
'''
string = "Hello World!"
pattern = r"World!$"
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

'''
Dot (.) - can take place of any other symbol

a.b will check for the string that contains any character at the place of the dot such as acb, acbd, abbb, etc
.. will check if the string contains at least 2 characters
'''
string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")

'''
Or (|) - any one element separated by the | char

a|b will match any string that contains a or b such as acd, bcd, abcd, etc.
'''

'''
Question Mark (?) - preceeding char may or may not be present in the string to be matched

ab?c will be matched for the string ac, acb, dabc but will not be 
matched for abbc because there are two b. Similarly, it will not be matched 
for abdc because b is not followed by c.
'''

'''
Asterix (*) - match preceeding char or set of chars for 0 or more times

ab*c will be matched for the string ac, abc, abbbc, dabc, etc. but will not 
be matched for abdc because b is not followed by c.
'''

'''
Plus (+) - repeat preceeding character or set of characters at least 1 or more times
(up to inifnity)

ab+c will be matched for the string abc, abbc, dabc, but will not be matched for ac, abdc, 
because there is no b in ac and b, is not followed by c in abdc.
'''

'''
Curly Brackets {} - repeat preceeeding char or set of chars as many times as 
the value inside the bracket 

{2} - repeat 2x
{min,} - preceeding char matches/repeated min or more times
{min, max} - preceeding char repeated at least min or at most max times

a{2, 4} will be matched for the string aaab, baaaac, gaad, but will not be 
matched for strings like abc, bc because there is only one a or no a in both
the cases.
'''

'''
Parenthesis / Group () - used to group subpatterns 

(a|b)cd will match for strings like acd, abcd, gacd, etc.
'''


# Speacial Sequences
'''
\A --- matches if string begins with given char --- \Afor matches "for geeks" "for the world"
\b --- matches if the word begins or ends with the given char, \bstring checks for begining of the word and string\b checks for the ending --- \bge matches "geeks" "get" 
\B --- opposite of \b, string should not start or end with the given regex --- \Bge matches "together" "forge"
\d --- matches any decimal digit, equivalent to the set class [0-9] --- \d matches "123" "gee1"
\D --- matches any non-digit char, this is equivalent to the set calss [^0-9] --- \D matches "geeks" "geek1"
\s --- matches any whitespace char --- \s matches "gee ks" "a bc a"
\S --- matches any non-whitespace char --- \S matches "a bd" "abcd"
\w --- matches any alphanumeric char, this is equivalent to the class [a-zA-Z0-9_] --- \w matches "123" "geeKs4"
\W --- matches any non-alphanumeric char --- \W matches ">$" "gee<>"
\Z --- matches if the string ends with the given regex --- ab\Z matches "abcdab" "abababab"
'''


# Python Regex functions from re module:
'''
re.findall() --- finda and returns all matching occurrences in a list
'''
string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
regex = '\d+'
match = re.findall(regex, string)
print(match)

'''
re.compile() --- regexs are compiled into pattern objects
'''
p = re.compile('[a-e]')
print(p.findall("Aye, said Mr. Gibenson Stark"))

p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p = re.compile('\w')
print(p.findall("He said * in some_lang."))

p = re.compile('\w+')
print(p.findall("I went to him at 11 A.M., he said *** in some_language."))

p = re.compile('\W')
print(p.findall("he said *** in some_language."))

p = re.compile('ab*')
print(p.findall("ababbaabbb"))

'''
re.split() --- split string by the occurrences of a char or a pattern
'''
print(re.split('\W+', 'Words, words , Words'))
print(re.split('\W+', "Word's words Words"))
print(re.split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))


'''
re.sub() --- repalces all occurrences of a char or pattern with a replacement string

syntax:
re.sub(pattern, repl, string, count=0, flags=0)
'''
print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
print(re.sub('ub', '~*', 'Subject has Uber booked already'))
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))

'''
re.subn() --- similar to sub() in all ways, except in its way of providing output. 
It returns a tuple with a count of the total of replacement and the new string rather 
than just the string. 
'''
print(re.subn('ub', '~*', 'Subject has Uber booked already'))
t = re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE)
print(t)
print(len(t))
print(t[0])

'''
re.escape() --- escapes special character
'''
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

'''
re.search() --- searches for first occurrences of character or pattern
'''
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "I was born on June 24")
if match != None:
    print ("Match at index %s, %s" % (match.start(), match.end()))
    print ("Full match: %s" % (match.group(0)))
    print ("Month: %s" % (match.group(1)))
    print ("Day: %s" % (match.group(2)))

else:
    print ("The regex pattern does not match.")


# match object:
s = "Welcome to GeeksForGeeks"
res = re.search(r"\bG", s)
print(res.re)
print(res.string)

# getting index of matched object
res = re.search(r"\bGee", s)
print(res.start())
print(res.end())
print(res.span())

# getting matched string
res = re.search(r"\D{2} t", s)
print(res.group())

