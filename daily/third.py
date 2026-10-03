# s = input("enter a word ")
# rs = ""
# for i in range(len(s)-1 , -1,-1):
#     rs+=s[i]
# if(rs == s):
#     print("pal")
# else:
#     print("not pal")

################################

# a = [1,2,3,4,5]
# sum = 0
# for i in a:
#     sum+=i

# print(sum/len(a))

############################

# list1 = [1,2,7]
# list2 = [2,4,5]
# list3 = []
# for i in list1:
#     list3.append(i)
# for i in list2:
#     list3.append(i)
# list3.sort()
# print(list3)

############################

# t = (1,2,7)
# e = ()
# o = ()
# for i in t:
#     if(i%2 ==0):
#         e+=(i,)
#     else:
#         o+=(i,)
# print(e)
# print(o)

############################

# t = (1,2,7)
# e = ()
# o = ()
# for i in t:
#     if(i%2 ==0):
#         e+=(i,)
#     else:
#         o+=(i,)
# print(e)
# print(o)

############################

# dic = {

# }
# while(True):
#     o = input("enter a o ")
#     if(o == 'A'):
#         k = input("enter a key ")
#         v = input("enter a value ")
#         dic[k] = v
#     elif(o == 'B'):
#         k = input("enter a the student name ")
#         v = input("enter a value ")
#     elif(o == 'C'):
#         k = input("enter a the student name ")
#         print(dic[k])
#     elif(o == 'D'):
#         for i in dic:
#             print(i , dic[i])

###############################

# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# dic = {}
# for i in words:
#     dic[i] = len(i)

# for i in dic:
#     print(i , dic[i])

#############################

# s = input("enter a word ")
# space = 0
# for i in s:
#     if(i == ' '):
#         space+=1


# print(space)

##############################

# # list1 = [1, 2, 3] 
# # list2 = [3, 4]

# list1 = [1, 2, 3, 4] 
# list2 = [5, 6, 7, 8]
# found = False
# for i in list1:
#     for j in list2:
#         if(i == j):
#             print("c")
#             found = True
#     if(found): break

# if(not found):
#    print("nc")


##############################

# list = [5, 6, 7, 8,5,8,6,5]
# found = False
# for i in range(0,len(list)):
#     for j in range(0,len(list)):
#         if(i == j): continue
#         if(list[i] == list[j]):
#             print(list[i])

##############################

s = input("enter a word ")
sett = set()

for i in s:
    sett.add(i)
print(sett,len(sett))
