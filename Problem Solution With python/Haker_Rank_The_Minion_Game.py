def minion_game(string):

    Stuart_Score,Kevin_Score=0,0
    for i in range(len(s)):
        if s[i] in ["A","E","I","O","U"]:
            
            Kevin_Score+=len(s)-i

        else:
            Stuart_Score+=len(s)-i

    if Kevin_Score> Stuart_Score:
        print("Kevin",Kevin_Score)
    elif Kevin_Score<Stuart_Score:
        print("Stuart",Stuart_Score)
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)