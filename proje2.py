from operator import itemgetter
def main():
    print("Enter contestant number: ",end="")
    contestant_number=get_contestant_number()
    coach_number=contestant_number
    print("Enter week number: ",end="")
    while True:
        try:
            week_number=int(input())
            if week_number>=3:
                break
            else:
                print(f"Enter a integer value greater than {week_number}: ",end="")
        except ValueError:
            print("Please enter a valid integer: ",end="")
    print()
    weekly_champions=[0]*contestant_number

    total_weeks_scoreboard=[0]*contestant_number
    for column in range(contestant_number):
        total_weeks_scoreboard[column]=[0]*4

    total_score_each_week=[0]*contestant_number
    for column in range(contestant_number):
        total_score_each_week[column]=[0]*week_number

    total_score_each_coach=[0]*contestant_number
    for column in range(contestant_number):
        total_score_each_coach[column]=[0]*coach_number

    overall_rank_to_coach = [0] * contestant_number
    for column in range(contestant_number):
        overall_rank_to_coach[column] = [0] * 2
        overall_rank_to_coach[column][0]=column+1

    overall_rank_to_audience = [0] * contestant_number
    for column in range(contestant_number):
        overall_rank_to_audience[column] = [0] * 2
        overall_rank_to_audience[column][0]=column+1

    for week in range(week_number):
        selected_three_players_by_coach=selected_three_players_by_coach_list(coach_number)
        selected_three_players_by_audience = selected_three_players_by_audience_list(contestant_number)

        weekly_total_scores_from_coaches,weekly_total_audience_scores,weekly_scoreboard,score_each_coach=weekly_scoreboard_list(selected_three_players_by_coach,selected_three_players_by_audience,contestant_number)
        weekly_champions_list(weekly_champions, weekly_scoreboard)

        print(f"Scoring results for week-{week + 1}:")
        weekly_score_result_display(weekly_scoreboard,contestant_number)
        print()

        total_weeks_scoreboard_list(total_weeks_scoreboard, weekly_scoreboard, contestant_number)
        overall_rank_to_coach_list(overall_rank_to_coach, weekly_total_scores_from_coaches, contestant_number)
        overall_rank_to_audience_list(overall_rank_to_audience, weekly_total_audience_scores, contestant_number)
        total_score_each_week_list(total_score_each_week, weekly_scoreboard, week, contestant_number)
        total_score_each_coach_list(total_score_each_coach, score_each_coach, contestant_number)

        print(f"Overall standings at the end of week-{week+1}:")
        weekly_score_result_display(total_weeks_scoreboard,contestant_number)
        print()
    print("Overall standings based on the coaches' scores only:")
    overall_standings_display(overall_rank_to_coach, contestant_number)
    print()
    print("Overall standings based on the audience scores only:")
    overall_standings_display(overall_rank_to_audience, contestant_number)
    print()

    print("Total scores for each week and the number of week championships of the\ncontestants:")
    print("Contestant No", end="")
    for week in range(week_number):
        print(f"  Week-{week+1}", end="")
    print("  Week Championships")
    print("-------------", end="")
    for week in range(week_number):
        print(f"  ------", end="")
    print("  ------------------")
    for i in range(contestant_number):
        print(format(i + 1, "7"), end="    ")
        for week in range(week_number):
            print(format(total_score_each_week[i][week], "8"), end="")
        print(format(weekly_champions[i], "13"))
    print()

    print("Total scores received by the contestants from the coaches:")
    print("Contestant No", end="")
    for coach in range(coach_number):
        print(f"  Coach-{coach+1}", end="")
    print()
    print("-------------", end="")
    for coach in range(coach_number):
        print(f"  -------", end="")
    print()
    for i in range(contestant_number):
        print(format(i + 1, "7"), end="   ")
        for coach in range(coach_number):
            if coach!=i:
                print(format(total_score_each_coach[i][coach], "9"), end="")
            else:
                print("        -", end="")
        print()

def selected_three_players_by_coach_list(coach_number):
    selected_three_players_by_coach=[0]*coach_number
    for column in range(coach_number):
        selected_three_players_by_coach[column]=[0]*3

    for coach in range(coach_number):
        avoid_same_selection=[]
        for point in range(3):
            print(f"Coach{coach+1} selected contestant for {point+1}point: ",end="")
            selected_three_players_by_coach[coach][point]=get_selected_contestant_coach(coach_number,coach,avoid_same_selection)-1
        print()
    return selected_three_players_by_coach

def selected_three_players_by_audience_list(contestant_number):
    selected_three_players_by_audience = [0] * 3
    avoid_same_selection=[]
    for points in range(3):
        print(f"Audience's selected contestant for {points + 1}point: ",end="")
        selected_three_players_by_audience[points]=get_selected_contestant_audience(contestant_number,avoid_same_selection)-1
    print()
    return selected_three_players_by_audience

def weekly_scoreboard_list(selected_three_players_by_coach,selected_three_players_by_audience,contestant_number):
    weekly_scoreboard=[0]*contestant_number
    for column in range(contestant_number):
        weekly_scoreboard[column]=[0]*4

    score_each_coach=[0]*contestant_number
    for column in range(contestant_number):
        score_each_coach[column]=[0]*contestant_number

    for i in range(contestant_number):
        for point in range(3):
            selected=selected_three_players_by_coach[i][point]
            score_each_coach[selected][i]=point+1

    weekly_total_scores_from_coaches=[0]*contestant_number
    for i in range(contestant_number):
        total=0
        for j in range(contestant_number):
            total+=score_each_coach[i][j]
        weekly_total_scores_from_coaches[i]=total

    weekly_total_audience_scores=[0]*contestant_number
    for i in range(3):
        selected=selected_three_players_by_audience[i]
        weekly_total_audience_scores[selected]=(i+1)*(contestant_number-1)

    for i in range(contestant_number):
        weekly_scoreboard[i][0]=i+1
        weekly_scoreboard[i][1]=weekly_total_scores_from_coaches[i]
        weekly_scoreboard[i][2]=weekly_total_audience_scores[i]
        weekly_scoreboard[i][3]=weekly_total_audience_scores[i]+weekly_total_scores_from_coaches[i]
    return weekly_total_scores_from_coaches,weekly_total_audience_scores,weekly_scoreboard,score_each_coach

def weekly_champions_list(weekly_champions,weekly_scoreboard):
    copy=[]+weekly_scoreboard
    list.sort(copy, key=itemgetter(3,1), reverse=True)
    selected=copy[0][0]-1
    weekly_champions[selected]+=1
    return weekly_champions

def total_weeks_scoreboard_list(total_weeks_scoreboard,weekly_scoreboard,contestant_number):
    for i in range(contestant_number):
        total_weeks_scoreboard[i][0] = weekly_scoreboard[i][0]
        total_weeks_scoreboard[i][1]+=weekly_scoreboard[i][1]
        total_weeks_scoreboard[i][2]+=weekly_scoreboard[i][2]
        total_weeks_scoreboard[i][3]+=weekly_scoreboard[i][3]
    return total_weeks_scoreboard

def overall_rank_to_coach_list(overall_rank_to_coach,weekly_total_scores_from_coaches,contestant_number):
    for i in range(contestant_number):
        overall_rank_to_coach[i][1]+=weekly_total_scores_from_coaches[i]
    return overall_rank_to_coach

def overall_rank_to_audience_list(overall_rank_to_audience,weekly_total_audience_scores,contestant_number):
    for i in range(contestant_number):
        overall_rank_to_audience[i][1]+=weekly_total_audience_scores[i]
    return overall_rank_to_audience

def total_score_each_week_list(total_score_each_week,weekly_scoreboard,week,contestant_number):
    copy=[]+weekly_scoreboard
    list.sort(copy, key=lambda a: a[0])
    for i in range(contestant_number):
        total_score_each_week[i][week]=copy[i][3]
    return total_score_each_week

def total_score_each_coach_list(total_score_each_coach,score_each_coach,contestant_number):
    for i in range(contestant_number):
        for j in range(contestant_number):
            total_score_each_coach[i][j]+=score_each_coach[i][j]
    return total_score_each_coach

def weekly_score_result_display(et_was_list,contestant_number):
    copy=[]+et_was_list
    list.sort(copy, key=itemgetter(3,1), reverse=True)
    print("Rank  Contestant No  Coach Score  Audience Score  Total Score")
    print("----  -------------  -----------  --------------  -----------")
    for row in range(contestant_number):
        print(format(row+1,"3"),end="")
        print(format(copy[row][0],"10"),end="")
        print(format(copy[row][1],"14"),end="")
        print(format(copy[row][2],"15"),end="")
        print(format(copy[row][3],"15"))

def overall_standings_display(et_was_list,contestant_number):
    copy=[]+et_was_list
    list.sort(copy, key=lambda a: a[1], reverse=True)
    print("Rank  Contestant No  Score")
    print("----  -------------  -----")
    for row in range(contestant_number):
        print(format(row + 1, "3"), end="")
        print(format(copy[row][0], "10"),end="")
        print(format(copy[row][1],"12"))

def get_contestant_number():
    while True:
        try:
            value = int(input())
            if value >= 5:
                return value
            else:
                print("Please enter a number of at least 5: ",end="")
        except ValueError:
            print("Please enter a valid integer: ",end="")

def get_selected_contestant_audience(contestant_number,avoid_same_selection):
    while True:
        try:
            value=int(input())
            if value not in avoid_same_selection:
                if 0<value<contestant_number+1:
                    avoid_same_selection.append(value)
                    return value
                else:
                    print(f"Please enter a number in 1-{contestant_number}: ",end="")
            else:
                print("Can't select same contestant: ",end="")
        except ValueError:
            print("Please enter a valid integer: ",end="")

def get_selected_contestant_coach(coach_number,coach,avoid_same_selection):
    while True:
        try:
            value=int(input())
            if value not in avoid_same_selection:
                if 0<value<coach_number+1 and value!=coach+1:
                    avoid_same_selection.append(value)
                    return value
                elif value==coach+1:
                    print("Coach cannot select own contestant: ",end="")
                elif value<=0:
                    print("Enter positive integer: ",end="")
                elif value>coach_number:
                    print(f"Value out of range 1-{coach_number}: ",end="")
            else:
                print("Can't select same contestant: ", end="")
        except ValueError:
            print("Please enter a valid integer: ",end="")
main()

