if __name__ == '__main__':
    #grade = 50
    grade = input("Enter a grade:")
    grade = int(grade)
    module_1 = "python"

    if grade >= 70 and module_1 == "python":
        print('You have earned a Distinction!')
    elif grade >= 60:
        print("You have earned a M.1.")
    elif grade >= 50:
        print("You have earned a M.2.")
    elif grade >= 40:
        print("You have passed")
    else:
        print("Please try again")
