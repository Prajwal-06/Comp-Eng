'''

Assignemt No: 01 (A-01)
Assignemt Title: Write a Python program to store marks scored in subject “Fundamental
⦁ The average score of class
⦁ Highest score and lowest score of class
⦁ Count of students who were absent for the test
⦁ Display mark with highest frequency
'''
def marksentry(A):
    n=int(input("Enter the number of Student: "))
    for i in range (n):
        marks=input("Enter marks of roll no. %d student:"%(i+1))
        if marks=="AB":
            marks=-1
        A.append(int(marks))

    print(*A,sep=",")
    
    
def showmark(A):
    for i in range (len(A)):
        if A[i]==-1:
            print("Marks of roll no. %d: Absent "%(i+1))
        if A[i]!=-1:
            print("Marks of roll no. %d:"%(i+1),A[i])
            
            
def minmax(A):
    mini=31
    maxi=-1
    for i in range (len(A)):
        if A[i]>maxi:
            maxi=A[i]
            
        if A[i]<mini and A[i]!=-1:
            mini=A[i]
    print("Maximum marks:",maxi)
    print("Minimum marks:",mini)
    
def average(A):
    summ=0
    count=0
    for i in range (len(A)):
        if A[i]!=-1:
            count=count+1
            summ=summ+A[i]
    average=summ/count
    print("Averange marks of student:",average)
    
def main():
    lst=[]
    while True:
        print("1. Enter 1 for marks entry")
        print("2. Enter 2 for average marks")
        print("3. Enter 3 for show marks")
        print("4. Enter 4 for minimum and maximum marks")
        print("5. Stop")
        ch=int(input("Enter your choice : "))
        if ch==1:
            marksentry(lst)
        elif ch==2:
            average(lst)
        elif ch==3:
            showmark(lst)
        elif ch==4:
            minmax(lst)
        elif ch==5:
            print("Thank you")
            break
        else :
            print("Please enter valid choice")
main()
    
    
    
    