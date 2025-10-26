# # story creation 

def make_story():
    name = input('enter your name:')
    place = input('enter your place:')
    object = input('enter your object:')
    feeling = input('enter your feelings')
    ans = name +  ' '  + place +  ' '  + object + ' ' + feeling + ''
    print(ans)
# make_story()    

# word formatter 
def format_word(word):
    return word
word = input('Enter Your Word:')
reversed_word =  word[::-1]
print(word.title() , word.replace("a", "*") , word.replace("e", "*") ,word.replace("i","*") , word.replace("o","*") ,word.replace("u","*") , reversed_word )


# # string analyzer 

def analyze_text(text):
    return text
text = input('enter your sentence:')
first =text[0]
last =text[-1]
print( text.upper(),  text.__len__(), first ,last)

