a=['New Delhi','Banglore','pune','Kolkata']
print('Which of the below the capital of india')
print(a)
ans1=str(input())
def amt(a):
  return a+1000
if ans1 == a[0]:
  print("SAHI JAWAB")
else:
  print("Galat Jawab") 
  print("apne jeete hai amt 0")
  exit()
b=['37','98','100','97']
print('Which of the below is the normal body temperature')
print(b) 
ans2=(input())
if ans2 == b[0]:
  print("SAHI JAWAB")
else:
  print("Galat Jawab")
  print(f"apne jeete hai {amt(0)}")
  exit()
c=['Bill Gates', 'Elon Musk', 'Steve Jobs', 'you']
print("Who founded Microsoft")
ans3=(input())
if ans3 == c[0]:
  print("SAHI JAWAB")
  print(f"apne jeete hai {amt(2000)}")
else:
  print("Galat Jawab")
  print("apne jeete hai amt 1000")
  exit()
