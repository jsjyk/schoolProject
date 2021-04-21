import os

search_dir = "articles/"




def read_articles(sortedList):
    number = input("type number of articles (1,2,3,4,5):")
    try:
        number = int(number)
        if number <= 5:
            with open(f"articles/{sortedList[-number]}", 'r', encoding='utf-8') as f:
                myString = f.read()
                print("-----------" * 6)
                print(f"Title : {sortedList[-number]}")
                print(myString)
                print("-----------" * 6)

        else:
            print(f"Type from 1 to 5 or use find command")

    except:
        print("type number of articles from 1 to 5")




def write_articles():
    name = input("type title:")
    subjects = input("type subjects:")
    with open(f"articles/{name}", "w", encoding='utf-8') as f:
        f.write(subjects)

def find_keywords(sortedList):
    keyword = input("type keyword:")
    expected = [s for s in sortedList if keyword in s]
    if len(expected) >0:
        print(f"""Searching results
      : {expected}""")
        res = input("type title of article:")
        end_code = 0
        while end_code == 0:
            if res != 'q':
                try:
                    with open(f"articles/{res}", 'r', encoding='utf-8') as f:
                        myString = f.read()
                        print("-----------" * 6)
                        print(f"Title : {res}")
                        print(myString)
                        print("-----------"*6)
                    end_code = 1
                except:
                    res = input("type the name of article! or 'q' to quit")
            else :
                break
    else :
        print(f"There are no match title with keyword '{keyword}'")


ending = 0
while ending == 0:
    sortedList = sorted(os.scandir('articles'), key=lambda d: d.stat().st_mtime)
    sortedList = [str(s).split("'")[1] for s in sortedList]

    print(f"""
    <recent Articles>
     1. {sortedList[-1]}
     2. {sortedList[-2]}
     3. {sortedList[-3]}
     4. {sortedList[-4]}
     5. {sortedList[-5]}""")
    command = input("""
    Enter commands:
        r. Read articles
        w. Write articles
        f. Find keyword
        q. Terminate
        >>>""")
    if command.lower() == 'r':
        print('got command :',command)
        read_articles(sortedList)
    elif command.lower() == 'w':
        print('got command :', command)
        write_articles()
    elif command.lower() == 'f':
        print('got command :', command)
        find_keywords(sortedList)
    elif command.lower() == 'q':
        print('got command :', command)
        print("---Terminate board program---")
        ending = 1
    else:
        print("**제대로 써라**")

print("Done")