from random import randint

def borda(options):
    for option in options:
        score = [option[1] + randint(0, option[2]) for _ in range(3)]
        
        print(f"{option[0]} - {score[0]}% 1st, {score[1]}% 2nd, {score[2]}% 3rd, {(score[0] * 3) + (score[1] * 2) + (score[2])} points\n")

if __name__ == "__main__":
    options = [("Kira Fowler (Vulture)", 0, 12),
                ("Ulysses Pearce (CP)", 7, 6),
                ("Frazier Barton (Capybara)", 5, 8),
                ("Hector Fuller (Independent)", 3, 5),
                ("Russel Crowley (Normalist)", 5, 6),
                ("Tasha Parks (Vulture)", 4, 9),
                ("Zachary Jones (CP)", 5, 6),
                ("Fran Yvan (Normalist)", 8, 6),
                ("Aldéric Belinda (Independent)", 3, 9),
                ("Steven Justice (Capybara)", 7, 4),
                ("Sango Wray (Normalist)", 4, 3),
                ("Jenna 'Izevel Ellisson (Capybara)", 3, 5)]
    borda(options)
