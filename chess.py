import pandas
def edit():
   print("If any previous value you want to edit :")
   t=0
   while (t!=1):
      print("Enter teamname :")#no need for now too much i sleep
def emerging(y:dict):
   print("Enter team name of the emerging player : ")
   teamname =str(input())
   teamname=teamname.lower()
   teamname = teamname.capitalize()
   y[teamname]+=50
def Player_of_the_day(y : dict):
   print("Enter team name of the player of the day : ")
   teamname =str(input())
   teamname=teamname.lower()
   teamname = teamname.capitalize()
   y[teamname]+=100
def descending(c:dict) -> dict:
   serve = ((value, key) for (key,value) in c.items())
   slay = dict(sorted(serve,reverse=True))
   return slay
def inp(SS):
   for i in SS.keys():
       print("Team  ",i)
       print("Enter points scored : ")#( Careful of which you are entering check if it is blitz or bullet )
       SS[i] = int(input())   
Match_1_blitz = {"a":0,"b":0,"c":0,"d":0}#{"a":238,"b":227,"c":184,"d":181}
Match_1_bullet = {"a":0,"b":0,"c":0,"d":0}#{"a":199,"b":287,"c":286,"d":236}
Match_2_blitz = {"a":0,"b":0,"c":0,"d":0}#{"a":250,"b":216,"c":187,"d":176}
Match_2_bullet = {"a":0,"b":0,"c":0,"d":0}#{"a":288,"b":282,"c":222,"d":204}
rank = [250,150,75,50]
match1=["Karpov","Tal","Tate","Gukesh"]
match2=["Nepo","Fischer","Magnus","Vidit"]
Match_1_blitz= dict(zip(match1,list(Match_1_blitz.values())))
Match_1_bullet = dict(zip(match1,list(Match_1_bullet.values())))
Match_2_blitz= dict(zip(match2,list(Match_2_blitz.values())))
Match_2_bullet = dict(zip(match2,list(Match_2_bullet.values())))
print("Blitz first match")
inp(Match_1_blitz)
print("Bullet first match")
inp(Match_1_bullet)
print("Blitz second match")
inp(Match_2_blitz)
print("Bullet second match")
inp(Match_2_bullet)
edit()#not complete 
a1 = descending(Match_1_blitz)
a2 = descending(Match_1_bullet)
b1 = descending(Match_2_blitz)
b2 = descending(Match_2_bullet)
Match_1_blitz.update(Match_2_blitz)
Match_1_bullet.update( Match_2_bullet)
final_blitz = Match_1_blitz
final_bullet = Match_1_bullet
yeet = {"Nepo" : [0,0,0],
        "Tal": [0,0,0],
        "Fischer": [0,0,0],
        "Tate": [0,0,0],
        "Karpov": [0,0,0],
        "Gukesh": [0,0,0],
        "Magnus": [0,0,0],
        "Vidit": [0,0,0]
    }
m=0
for i in a1.values():
   yeet[i][2] += rank[m]
   m+=1
n=0
for i in a2.values():
   yeet[i][2] += rank[n]
   n+=1
pp=0
for i in b1.values():
   yeet[i][2] += rank[pp]
   pp+=1
tt=0
for i in b2.values():
   yeet[i][2] += rank[tt]
   tt+=1
for j in  yeet.keys():
   yeet[j][0]= final_blitz[j]
   yeet[j][1]= final_bullet[j]
for i in yeet.keys():
   yeet[i][2] += ((yeet[i][0]*9) + (yeet[i][1]*6))
condense = {}
for i in yeet.keys():
   condense[i]=yeet[i][2]
print(condense)
Player_of_the_day(condense)
emerging(condense)
out = descending(condense)
print(out)