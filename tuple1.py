list=[('yash','ramesh','nikul'),'hetvi','rahi','yami',('harsh',),'archi']
boy=0
girls=0
for name in list:
    print(name)
    if type(name)==tuple:
        
        for i in name:
            boy+=1
        
    else :
        
       
            girls+=1
print(boy,girls)
   
