
#practice problem
def pal_checker(string):
   clean_str = ""
   for char in string:
        if char.isalpha():
            clean_str += char.lower()
    return clean_str == clean_str[::-1]



strings = ["sit on a potato pan, Otais.",
           "Cigar? Toss it in a can. It is so tragic",
           "Go hand a salami, I'm a lasagna hog.",
           "A man, a plan, a canal, Panama!"]

for string in strings:
    print(pal_checker(string))

