print("APNI DUKAN MAI APKA SWAGAT HAI")
sum=0
while(True):
  a=input('enter amount of item')
  if (a!="q"):
    sum=sum+int(a)
    print("Your order total till now is",sum)
  else:
    print("Your final amount to be paid", sum)
    print("apka din shubh ho !!")
    break