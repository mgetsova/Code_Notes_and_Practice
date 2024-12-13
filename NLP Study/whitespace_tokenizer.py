# nltk.WhitespaceTokenizer
from nltk.tokenize import WhitespaceTokenizer 
     
# Create a reference variable for Class WhitespaceTokenizer 
tk = WhitespaceTokenizer() 
     
# Create a string input 
gfg = "GeeksforGeeks \nis\t for geeks"
     
# Use tokenize method 
geek = tk.tokenize(gfg) 
     
print(geek) 



tk = WhitespaceTokenizer() 
gfg = "The price\t of burger \nin BurgerKing is Rs.36.\n"
geek = tk.tokenize(gfg) 
print(geek) 