import random
logo ="""       

         _________ _______             _______  _______    _        _______             _______           _______  _______  _______ 
|\     /|\__   __/(  ____ \|\     /|  (  ___  )(  ____ )  ( \      (  ___  )|\     /|  (  ____ \|\     /|(  ____ \(  ____ \(  ____ \
| )   ( |   ) (   | (    \/| )   ( |  | (   ) || (    )|  | (      | (   ) || )   ( |  | (    \/| )   ( || (    \/| (    \/| (    \/
| (___) |   | |   | |      | (___) |  | |   | || (____)|  | |      | |   | || | _ | |  | |      | |   | || (__    | (_____ | (_____ 
|  ___  |   | |   | | ____ |  ___  |  | |   | ||     __)  | |      | |   | || |( )| |  | | ____ | |   | ||  __)   (_____  )(_____  )
| (   ) |   | |   | | \_  )| (   ) |  | |   | || (\ (     | |      | |   | || || || |  | | \_  )| |   | || (            ) |      ) |
| )   ( |___) (___| (___) || )   ( |  | (___) || ) \ \__  | (____/\| (___) || () () |  | (___) || (___) || (____/\/\____) |/\____) |
|/     \|\_______/(_______)|/     \|  (_______)|/   \__/  (_______/(_______)(_______)  (_______)(_______)(_______/\_______)\_______)
                                                                                                                                    

"""
ar = ['Sayan', 'Piyasha', 'Shiladittya', 'Jyotika', 'Basanti', 'Das', 'Subha']
ab = []
ac = []
dict_ = {}
for i in range (0,100) :
  i += 1
  ac.append(i)
for i in range (0,len(ar)) :
  xd = random.choice(ac)
  ab.append(xd)
  ac.pop(xd)
for i in range (0,len(ar)) :
  dict_[ar[i]] = ab[i]
ap = ar
count = len(ap)
f = random.randint(0,count-1)
x = ap[f]
x_ = dict_[x]
ap.pop(f)
print(logo)
for i in range (0,count-1) :
  count -= 1
  f_1 = random.randint(0,count-1)
  y = ap[f_1]
  y_ = dict_[y]
  ap.pop(f_1)
  print(f"choose whether you think {y} is higher or lower than {x} ")
  check = input("guess high or low ").lower()
  if count > 0 :
    if y>x and check == 'high' :
      print("congrats you win.")
    elif y>x and check == 'low' :
      print("Sorry! Wrong Guess")
      break
    elif y<x and check == 'low' :
      print("congrats you win.")
    elif y<x and check == 'high' :
      print("Sorry You Lose.")
      break
  else :
    break 
  x = y
  x_ = y_
