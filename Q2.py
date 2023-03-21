def revword(str1:str):
            str1 = str1.lower()[::-1]
            return str1


def countword():
    str1 = open("text.txt","r")
    count = 1
    for i in str1:
        list_words = i.split(" ")
        if len(list_words)==1:
            first_word = list_words[0].lower().strip()
        else:
            for j in list_words :
                word = revword(j).strip()
                if word == first_word:
                    count += 1
    print(count)

countword()

