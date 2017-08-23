def main():
    score = float(input("Enter score: "))
    x = calculate_score(score)
    print(x)


def calculate_score(score):
    if score > 100 or score < 0:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()