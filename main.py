'''
For in Loop
'''
# students = ['bob', 'jane', 'jase']
# for a in students:
  # print('Hi', a)
#====================

#print(range(10))
#print(list(range(10)))
#print(list(range(3, 6)))
#print(list(range(3, 12, 7)))
#====================

# for x in range(1, 6, 3):
 # print(x * 8)
#====================
#for i in range(1, 6):
   # for j in range(i):
      # print("*", end=" ")
   # print()

'''
While Loop
'''
#i = 1
#while i < 10:
  #print(i)
  #i += 1
  #====================

# Break Statements
#i = 1
#while i < 10:
  #print(i)
  #if i == 4:
   # break
  #i += 1
#====================  stops at (4)

# Continue statemnts
#i = 1
#while i < 10:
   # i += 1
    #if i == 8:
       # continue
   # print(i)
# misses out the number (8)

for i in range(1, 10):
    if i == 3:
      break
    print(i)
