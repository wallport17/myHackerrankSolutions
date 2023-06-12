if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
     query_name = input()
     read = student_marks[query_name] #This line gets the scores of a particular student in the student_marks dictionary
     sum = sum(read) / len(read) #This line takes the sum of 'read' and divides it by the length of read 
                                 #to get the average
     print("{:.2f}".format(sum)) 
