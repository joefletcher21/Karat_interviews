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

def stories(endings, choices, choice):
    book = dict()
    for i in range(len(choices)):
        current_page = choices[i][0]
        next_page = choices[i][choice]
        book[current_page] = next_page

    currPage = 1
    hasVisited = set()
    while(currPage not in endings):
        if currPage in hasVisited:
            return -1
        hasVisited.add(currPage)
        if currPage in book:
            currPage = book[currPage]
        else:
            currPage += 1
    return currPage    


print(stories(endings1,choices1_1,2))
