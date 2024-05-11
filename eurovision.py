def read_ranking(file_name):
    with open(file_name, 'r') as f:
        ranking = f.read().split(",")
        ranking = [country.strip() for country in ranking]
        return ranking

def read_user_bets(file_name):
    with open(file_name, 'r') as f:
        user_bets = f.read().split(",")
        user_bets = [country.strip() for country in user_bets]
        return user_bets

def calculate_points(ranking, user_bets):
    points = 0
    for i, country in enumerate(user_bets):
        if country == ranking[i]:
            points += 5
            print(country, "5")
        elif (i < len(ranking) - 1 and country == ranking[i+1]) or (i > 0 and country == ranking[i-1]):
            points += 4
            print(country, "4")
        elif (i < len(ranking) - 2 and country == ranking[i+2]) or (i > 1 and country == ranking[i-2]):
            points += 3
            print(country, "3")
        elif (i < len(ranking) - 3 and country == ranking[i+3]) or (i > 2 and country == ranking[i-3]):
            points += 2
            print(country, "2")
        elif i < len(ranking) - 4 and country == ranking[i+4]:
            points += 1
            print(country, "1")
        elif i > 3 and country == ranking[i-4]:
            points += 1
            print(country, "1")
    return points

def calculate_total_points(user_bets_file, ranking_file):
    ranking = read_ranking(ranking_file)
    user_bets = read_user_bets(user_bets_file)
    points = calculate_points(ranking, user_bets)
    return points

def main():
    user1_file = "user1_bets.txt"
    user2_file = "user2_bets.txt"
    ranking_file = "real_ranking.txt"
    print("Ola")
    user1_points = calculate_total_points(user1_file, ranking_file)
    print("Witek")
    user2_points = calculate_total_points(user2_file, ranking_file)
    print("User 1 score: ", user1_points)
    print("User 2 score: ", user2_points)
    if user1_points > user2_points:
        print("User 1 wins!")
    elif user1_points < user2_points:
        print("User 2 wins!")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    main()
