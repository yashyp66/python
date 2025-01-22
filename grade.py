def marks():
    sub1=float(input("what's your marks in computer ? "))
    sub2=float(input("what's your marks in maths ? "))
    sub3=float(input("what's your marks in physics ? "))
    total=sub1+sub2+sub3
    average=total/3
    #sub1
    if sub1>=80 and sub1<=100:
        print("Grade O in computer ")
    elif sub1>=70 and sub1<80:
        print("Grade A+in computer")
    elif sub1>=60 and sub1<70:
        print("Grade A in computer")
    elif sub1>=50 and sub1<60:
        print("Grade B in computer")
    elif sub1>=40 and sub1<50:
        print("Grade P in computer")
    else:
        print("Fail in computer")
    #sub2 
    if sub2>=80 and sub2<=100:
        print("Grade O in maths ")
    elif sub2>=70 and sub2<80:
        print("Grade A+in maths")
    elif sub2>=60 and sub2<70:
        print("Grade A in maths")
    elif sub2>=50 and sub2<60:
        print("Grade B in maths")
    elif sub2>=40 and sub2<50:
        print("Grade P in maths")
    else:
        print("Fail in maths")
    #sub 3
    if sub3>=80 and sub3<=100:
        print("Grade O in physics ")
    elif sub3>=70 and sub3<80:
        print("Grade A+in physics")
    elif sub3>=60 and sub3<70:
        print("Grade A in physics")
    elif sub3>=50 and sub3<60:
        print("Grade B in physics")
    elif sub3>=40 and sub3<50:
        print("Grade P in physics")
    else:
        print("Fail in maths")
    print("Total marks are:  ",total ,"out of 300")
    print("Average of marks are : ",average)
marks()
