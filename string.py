str = input("str1:")
num=int(input("num:"))
if num>len(str) or len<0:
   print("num should be postive ,less than length of str")
else:
   print("result:",num*str[:num])
