print("Welcome to the 5 A Side Team List")
team = []

#user input for 5 postions
gk = input("\nWho is playing in goal: ").title()
team.append(gk)
dfs = input("Who is playing in defense: ").title()
team.append(dfs)
mid1 = input("Who is the first midfielder: ").title()
team.append(mid1)
mid2 = input("Who is the second midfielder: ").title()
team.append(mid2)
fwd = input("Who is playing in attack: ").title()
team.append(fwd)

#print current team in tabular format
print("\n\tThis is your current team:")
print("\n\t\t\tGoalkeeper:\t\t\t" + team[0])
print("\t\t\tDefender:\t\t\t" + team[1])
print("\t\t\tMidfielder:\t\t\t" + team[2])
print("\t\t\tMidfielder:\t\t\t" + team[3])
print("\t\t\tStriker:\t\t\t" + team[4])

#advise defender is injured, advise how many players in team and ask for replacement

print("\nYour defender, " + team[1] + ", is injured.")
injured = team.pop(1)
print("\nYour team currently has " + str(len(team)) + " players.")
new_dfs = input("\nWho will replace " + injured + " in the team: ").title()
team.insert(1,new_dfs)

#confirm new team and final number of players
print("\n\tThis is your revised team:")
print("\n\t\t\tGoalkeeper:\t\t\t" + team[0])
print("\t\t\tDefender:\t\t\t" + team[1])
print("\t\t\tMidfielder:\t\t\t" + team[2])
print("\t\t\tMidfielder:\t\t\t" + team[3])
print("\t\t\tStriker:\t\t\t" + team[4])

print("\nGood luck " + team[1] + ", you'll do great.")
print("\nYour team now has " + str(len(team)) + " players.")







