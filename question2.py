count = 0
max_books = 5
running_cost = 0
while count < max_books:
    print('Enter the name of the book:')
    book_title = input()
    print("Enter the cost")
    cost = input()

    running_cost += float(cost)

    print(book_title, cost, running_cost)

    count += 1
print("Finished. Total Cost was: ", running_cost)






