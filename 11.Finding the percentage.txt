if __name__ == '__main__':
    #Step 1: First, n will take input for a total number of students.
    n = int(input())
    #Step 2: then, I created a dictionary to store the name and marks of students.
    student_marks = {}
    #Step 3: After this, I created a for loop.
    for _ in range(n):

        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores
    #Step 4: inside for loop, I have taken an input of the name.
    query_name = input()
    #Step 5: I have also taken the input of scores and stored them in a list.
    l1 = list(student_marks[query_name]) 

    addition = sum(l1)

    result = addition/len(l1)

    print('%.2f'% result)