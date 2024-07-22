endings1 = [6, 15, 21, 30]
choices1_1 = [
    [3, 7, 8],
    [9, 4, 2],
]
choices1_2 = [
    [3, 14, 2],
]
choices1_3 = [
    [5, 11, 28],
    [9, 19, 29],
    [14, 16, 20],
    [18, 7, 22],
    [25, 6, 30],
]
choices1_4 = [
    [2, 10, 15],
    [3, 4, 10],
    [4, 3, 15],
    [10, 3, 15],
]

endings2 = [11]
choices2_1 = [
    [2, 3, 4],
    [5, 10, 2],
]
choices2_2 = []

endings3 = [4, 11]
choices3_1 = [
    [10, 6, 8],
]

endings4 = [20]
choices4_1 = [
    [2, 6, 3],
    [3, 1, 4],
    [4, 10, 5],
    [6, 3, 7]
]

"""
currPage = choices1_1[0][0]
hasVisited = false
if currPage in endings
    return currPage
elif hasVisted == True
    return -1
elif currPage not in choices1_1[i][0]:
    currPage+=1
else:
    hasVistited = True
    
"""

def stories(endings, choices, choice):
    currPage = choices1_1[0][0]
    hasVisited = False
    for i in range(len(choices)):
        print(currPage)
        print(choices1_1[i])

        if currPage in endings:
            return currPage
        elif hasVisited == True:
            return -1
        elif currPage != choices1_1[i][0]:
            currPage+=1
        elif currPage == choices1_1[i][0]:
            currPage = choices1_1[i][choice]
        else:
            hasVistited = True
    print("Oops")
    return -3
    
print(stories(endings1, choices1_1, 1))
