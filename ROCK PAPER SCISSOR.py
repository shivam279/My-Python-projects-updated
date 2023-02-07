import random
options=['rock','paper','scissors']
def check (comp, user):
  if comp=='paper' and user=='rock':
    return -1
  if comp=='rock' and user=='scissors':
    return -1
  if comp=='scissors' and user=='paper':
    return -1
  if comp=='rock' and user=='rock':
    return 0
  if comp=='scissors' and user=='scissors':
    return 0
  if comp=='paper' and user=='paper':
    return 0
comp=random.choice(options)

user=input(f"Enter your choice, available options are {options}")
score=check(comp, user)
print(f"your choice is {user}")
print(f"computer chose{comp}")

if score == -1:
  print("You Lose BETTER LUCK NEXT TIME")
elif score== 0:
    print("THE GAME IS DRAW")
else:
    print("CONGRATULATIONS YOU WON")
    
  