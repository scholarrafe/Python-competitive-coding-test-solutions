team_alpha = [1, 2, 3, 4, 5] 
team_beta = [4, 3, 2, 1, 1]

# merge_list = [alpha+beta for alpha, beta in zip(team_alpha, team_beta) if (alpha+beta)%2!=0]

merge_list = [alpha+beta for alpha, beta in zip(team_alpha, team_beta)] # Merge two list
merge_list = list(filter(lambda x:x%2!=0, merge_list)) # filter the odd elements


manipulated_merge_list = list(map(lambda x : x**2 + 3*x + 2, merge_list)) # applying given formula

print(manipulated_merge_list)