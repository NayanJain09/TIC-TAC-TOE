w=3
h=3
a=[['' for x in range(w)] for y in range(h)]

def display():
  for i in range(3):
        print("| ", end = '')
        for j in range(3):
           print(a[i][j]," |", end = '')
        print("")
        print("-------------")
    
def check():
    if a[0][0]==a[0][1] and a[0][0]==a[0][2] and a[0][0]!='':
        if ((a[0][0])==t1):
            print("Player1 won")
        else:
            print("Player2 won\n")
        exit(0)
 
    elif(a[0][0]==a[1][1] and a[0][0]==a[2][2] and a[0][0]!=''):
       
          if ((a[0][0])==t1):
            print("Player1 won")
          else:
            print("Player2 won")
          exit(0)
        
    elif(a[0][0]==a[1][0] and a[0][0]==a[2][0] and a[0][0]!=''):
          if ((a[0][0])==t1):
            print("Player1 won")
          else:
            print("Player2 won")
          exit(0)
        
    elif(a[1][0]==a[1][1] and a[1][0]==a[1][2] and a[1][0]!=''):
          if ((a[1][0])==t1):
            print("Player1 won")
          else:
            print("Player2 won")
          exit(0)
        
    elif(a[2][0]==a[2][1] and a[2][0]==a[2][2] and a[2][0]!=''):
          if ((a[2][0])==t1):
            print("Player1 won")
          else:
            print("Player2 won")
          exit(0)
        
    elif(a[0][1]==a[1][1] and a[0][1]==a[2][1] and a[0][1]!=''):
          if ((a[0][1])==t1):
            print("Player1 won")
          else:
            print("Player2 won")
          exit(0)
    
    elif(a[0][2]==a[1][2] and a[0][2]==a[2][2] and a[0][2]!=''):
          if ((a[0][2])==t1):
            print("Player1 won")
          else:
            print("Player2 won")
          exit(0)

    elif(a[0][2]==a[1][1] and a[0][2]==a[2][0] and a[0][2]!=''):
          if ((a[0][2])==t1):
            print("Player1 won")
          else:
            print("Player2 won")
          exit(0)

print("enter the first player's choice(O or X):")
t1= input()
if t1=='X':
      t2='O'
else:
      t2='X'
c=0
print("Rules: enter the choice as index no. starting with 0,0.....")
for l in range(5):
      print("Player1 enter the choice:")
      j=int(input())
      k=int(input())
      a[j][k]=t1
      display()
      c=c+1
      if(c==9):
          check()
          break
      elif(c>=5):
          check()
      print("Player2 enter the choice:")
      j=int(input())
      k=int(input())
      a[j][k]=t2
      c=c+1
      if(c>=5):
        check()
      display()
