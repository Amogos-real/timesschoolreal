letter=[]
while True:
    try:
        b=str(input("whats ur favorite book? "))
        c=int(input("when was it made? "))
        d=str(input("who made it? "))
    except ValueError or NameError:
        print("u made mistake. in first question and third use letters. in second question use numbers (not numbers like 1.0,2.0)")
    a={'book':b,'creator':d,'year production':c}
    letter.append(a)
    try:
        e=str(input("do u wanna delete books?"))
        if e == "no":
            m=str(input("do u wanna find books? "))
            if m == "yes":
                s=str(input("what book u wanna find? "))
                if s in letter:
                    print(letter)


            h=str(input("do u wanna add more books? "))
            if h != "yes":
                break
        elif e == "yes":
            try:
                k=int(input("which book u want to delete? use numbers (like first book is 0, second is 1) "))
                letter.pop(k)
            except:
                print("use numbers!!. or u just gave wrong index")


    except ValueError:
        print("type yes or no")

print(letter)


