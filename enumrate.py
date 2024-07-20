
#enumitare function / mannual way 
index = 0
marks =[12, 34, 56, 78, 98, 44]
for mark in marks:
    print(mark)
    if(index==3):
        print("hello soya !")
    index +=1

    #using enumrate function 

    for index, mark in enumerate(marks, start=1):
        print(mark)
        if(index == 3):
            print("i am the king !")

#enumrate is use to get value or index number at a same time ! also can set indexing from where we want 
  