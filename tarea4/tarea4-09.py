for i in range(0,3):
    f = open("dato.txt")
    f.seek(17+(i*77),0) 
    x1= int(f.read(2))
    f.seek(20+(i*77),0) 
    y1= int(f.read(2))
    f.seek(35+(i*77),0) 
    a= int(f.read(2))
    f.seek(38+(i*77),0) 
    b= int(f.read(2))
    f.seek(60+(i*77),0) 
    x2= int(f.read(2))
    f.seek(63+(i*77),0) 
    y2= int(f.read(2))
    f.seek(73+(i*77),0) 
    r= int(f.read(2))
    print (x1,y1,a,b,x2,y2,r ,"    ")
    f.close()

    y=(y1+((b/a)*(x2-x1))) #ecuacion es de la recta
    d=(r*(1+y))



    print ("ecuacion", y)

    f = open("dato.txt","a")
    f.write("En la opcion "+str(i)+" ecuacuion que falta "+"\n") 
    f.close()
  