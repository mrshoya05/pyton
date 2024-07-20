
questions = [
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none", 4],
    
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php",  "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    ["which language is use to create facebook", "python", "java",  "franch", "php", "none",4 ],
    
    ]

levels = [10000, 100000, 1000000, 10000000]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  
  print(f"Quesion for rupes Rs. {levels[i]}")
  print(question[i])
  print(f"a.{question[1]}      b.  {question[2]}")
  print(f"c.{question[3]}      d.  {question[4]}")
  reply = int(input("enter your answer : \n"))
  if (reply == question[-1]):
   print("you won Rs. ", levels[i])
   if(i== 4):
    money == 4000
   elif(i == 9):
    money == 32000
   elif(i == 10):
    money == 3200000
  else:
    print("wrong ansewer !")
    break;

# convrt mst to codee language..
# print("hello world")

str = 'shoya'
str += "minku"
str = str[::-1]
print(str)


decode = str
decode = decode[::-1]
decode = decode[:5]
print(decode)