from random import uniform


def star(options, allow_co_presidents, co_president_threshold):
    election_data = calculate_star(options, allow_co_presidents, co_president_threshold)
    print_star(election_data)

def calculate_star(options, allow_co_presidents, co_president_threshold):
    scores = []
    star_rankings = ""
    for option in options:
        score = round(option[1] + uniform(0, option[2]), 2)

        star_rankings += f"{option[0]} - {score}/5 rating\n"
        scores.append((option[0].split(" - ")[0], score))


    top_two = sorted(scores, key=lambda x: x[1], reverse=True)[:2]
    
    # top_two = []

    # for score in scores:
    #     if len(top_two) > 0: first_place_score = top_two[0][1]
    #     if len(top_two) > 1: second_place_score = top_two[1][1]
    #     judging_score = score[1]

    #     if len(top_two) == 2 and judging_score > second_place_score:
    #         top_two.pop(1)
    #         top_two.insert(0 if judging_score > first_place_score else 1, score)
    #     elif len(top_two) == 1:
    #         top_two.insert(0 if judging_score > first_place_score else 1, score)
    #     elif len(top_two) == 0:
    #         top_two.append(score)

    print(top_two)

    first_place_score = top_two[0][1]
    first_place_name = top_two[0][0].split(" (")[0]
    second_place_score = top_two[1][1]
    second_place_name = top_two[1][0].split(" (")[0]
    co_president_threshold = round(first_place_score - (first_place_score * co_president_threshold), 2)
    percentage_ranked_over = round(first_place_score + uniform(42, 56), 2)
    total_ranked_over = round(uniform(94, 100), 2)

    # if allow_co_presidents:
    #     if second_place_score > co_president_threshold:
    #         winner = second_place_name if second_place_score > co_president_threshold else first_place_name
    #     else: winner = first_place_name
    # else: winner = first_place_name

    return [star_rankings, first_place_score, first_place_name, second_place_score, second_place_name, co_president_threshold, percentage_ranked_over, total_ranked_over]

def print_star(election_data):
    star_rankings, first_place_score, first_place_name, second_place_score, second_place_name, co_president_threshold, percentage_ranked_over, total_ranked_over = election_data

    print(star_rankings)

    print(f"Top two - {first_place_name}: {first_place_score}/5, {second_place_name}: {second_place_score}/5. For a co-presidency, the rule is that the second placing candidate must be within 3% of the winning candidate.")

    if second_place_score > co_president_threshold:
        print(f"{second_place_name}'s score is greater than the threshold of {co_president_threshold}, so we will have co-presidents!")
    else:
        print(f"{second_place_name}'s score did not meet the threshold of {co_president_threshold}. \
                Under STAR voting, the winner is determined by seeing what percentage of people rank {first_place_name} over {second_place_name} \
                and what percentage rank {second_place_name} over {first_place_name}. {percentage_ranked_over}% of people ranked {first_place_name} over {second_place_name}, \
                while {total_ranked_over - percentage_ranked_over}% ranked {second_place_name} over {first_place_name}.")
        print(f"This means {first_place_name if percentage_ranked_over > total_ranked_over - percentage_ranked_over else second_place_name} is the President of the United Cold Nation!")


if __name__ == "__main__":
    options = [("Morgan (Capybara) - Extremely popular Capybara leader, running for 3rd term during the 'golden age' of the UCN", 4.3, 0.7),
("Barton (Capybara) - Will create a rigid government (government, not laws), inspired by early Purple", 2.7, 1.7),
("Briggs (CP) - Trying again as a classical center in case people want change", 3.2, 1.5),
("Jones (CP) - Strong leader, voice of reason for CP, mayor experience", 2.2, 1.2),
("Adams (CP) - Caring immensly about the environment and ethics, a humanitarian hoping to serve as co-president", 3.8, 0.8),
("Wilson (Normalist) - Classical early Howardian Normalist", 2.1, 0.9),
("Fran Yvan (Normalist) - Wants to begin more innovation instead of having just peace", 3.7, 1.1),
("Shaylyn Eve (Vulture) - Promises to replacating Arjun's success at prosperity and financial gains", 2.2, 2.8),
("Parks (Vulture) - Strict laws like Pearce, but innovation like Arjun", 4.2, 0.7)]
    star(options, True, 0.03)
    