class complex_no:
    def __init__(self,real1,real2,complex1,complex2):
        self.real1=real1
        self.real2=real2
        self.complex2=complex2
        self.complex1=complex1
        #addition
        addr=self.real1+self.real2   
        addc=self.complex1+self.complex2
        
        print("addition :" ,str(addr), "+", str(addc),"i")

        #substraction
        subr=self.real1-self.real2   
        subc=self.complex1-self.complex2
        
        print("substraction :",str(subr), "+", str(subc),"i")
        #multiplication
        mulr=self.real1*self.real2
        mulc=(self.complex1*self.complex2)*(-1)
        x=self.real1*self.complex2
        y=self.complex1*self.real2
        mul2=x+y
        mul1=mulr+mulc
        

        print("multiplication : ",str(mul1),"+",str(mul2),"i")
        #division
        mulr=self.real1*self.real2
        mulc=(self.complex1*self.complex2*(-1))*(-1)
        x=(self.real1*self.complex2)*(-1)
        y=self.complex1*self.real2
        mul2=x+y
        mul1=mulr+mulc
        print("division : ",mul1/((self.real2)**2+((self.complex2)**2)),"+",mul2/((self.real2)**2+((self.complex2)**2)),"i")
        
        


    
        

#cox1=complex_no(1,2,4,-2)
cox2=complex_no(2,4,6,-5)

