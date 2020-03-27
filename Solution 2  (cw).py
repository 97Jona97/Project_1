#Alright what do you wanna do first:: what was your ideas bro to optimize the solution that we have built yesterday:
import random
import time
import timeit

season_info = {"Goals": [],"Fouls":[],"Assists":[]}#Dictionary--->k-->inside values
#games = int(input("Number of games"))
games = random.randint(1,1000)
start = time.time()
def scores(games):
    for i in range(games):
        scores_each_game = random.randint(0,10)
        season_info["Goals"].append(scores_each_game)
    return season_info["Goals"]
 
end = time.time()
print(end-start)

def assists(games):
    for i in range(games):
        assists_each_game = int(input("Enter the assists: "))
        season_info["Assists"].append(assists_each_game)
    return 

def sort_goal():
    start_time=time.time()
    for i in range(1,len(season_info["Goals"])):
        k = season_info["Goals"][i]
        j = i-1          #*
        while j>=0 and k < season_info["Goals"][j]:
            season_info["Goals"][j+1] = season_info["Goals"][j]
            j -= 1
        season_info["Goals"][j+1] = k
    end_time=time.time()
    print(end_time-start_time)
    return season_info["Goals"]

def search_goals(season_info,k):
    start_1=time.time()
    count = 0
    for i in range(len(season_info["Goals"])):
        if season_info["Goals"][i] == k:
            count +=1
    end_1=time.time()
    print(end_1-start_1)    
    
    return f"{k} was scored {count} times"

def sort_assists():
    for i in range(1, len(season_info["Assists"])): 
        k = season_info["Assists"][i]
        j = i-1
        while j>=0 and k < season_info["Assists"][j]:
            season_info["Assists"][j+1] = season_info["Assists"][j]
            j -= 1
            season_info["Assists"][j+1] = k
    return season_info["Assists"]
        
def clean_sheets(games):
    total = 0
    for i in range(games):
        given_clean_sheet = str(input("Did you get a clean sheet: ")).lower()
        if given_clean_sheet == "y" or given_clean_sheet=="yes":
            total +=1
        elif given_clean_sheet == "n" or given_clean_sheet=="no":
            total = total+0
    return total 

def fouls(games):
    yellow_cards = int(input("Total number of yellow cards given in the season:"))
    season_info["Fouls"].append(yellow_cards)
    red_cards = int(input("Total number of red cards in the season given out: "))
    season_info["Fouls"].append(red_cards)
    return season_info["Fouls"]

def percentages():
    highest, lowest = len(season_info["Goals"]),len(season_info["Goals"])
    high_perc, low_perc = max(season_info["Goals"])/highest, min(season_info["Goals"])/lowest
    return "Highest = " +str(high_perc), "Lowest = " + str(low_perc)

def main():
    print(scores(games))
    #assists(5)
    print(sort_goal())
    #print(sort_assists())
    #print(clean_sheets(5))
    #print(fouls(5))
    #print(percentages())
    #print(search_goals(season_info,5))
if __name__ == "__main__":
    main()

