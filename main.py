def binaryTodecimal(binary):
  sum=0
  index=0
  while (binary)>0:
   lastdigit=binary%10
   binary=binary//10
   sum=sum+(lastdigit*(2**index))
   index=index+1
  print(sum)
binaryTodecimal(101)