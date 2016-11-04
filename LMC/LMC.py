#LMC
#Daniel Jolly
#24/10/2016
#missing branch ifs
print("Please note for commands (halt add subtract store load and branch/branch if 0/branch if +) please enter only the first digit (0,1,2,3,5 or 6/7/8 respectively")
mailbox = []
loop1 = 0
loop2 = 0
acc = 0
for loop in range (100):
    mailbox.append(" ")

print (mailbox)

while loop2 == 0:
    mbox = int(input("What box do you wish to edit:"))
    changes = int(input("What number do you wish to enter into box "+str(mbox)+"?  :"))
    mailbox[mbox] = changes
    print (mailbox)
    cont = input("Would you like to edit another box? YES/NO:").lower()
    if cont == "no":
        loop2 = 1
        print (mailbox)
      

mbox = 0

while loop1 == 0:
      if mailbox[mbox] == 1:
          add = int(input("What mailbox would you like to add the digit from:"))
          added = acc + mailbox[add]
          acc = added
          mbox = mbox + 1
      elif mailbox[mbox] == 2:
          sub = int(input("What mailbox would you like to use the digit from:"))
          minused = acc - mailbox[sub]
          acc = minused
          mbox = mbox + 1
      elif mailbox[mbox] == 3:
          store = int(input("What mailbox would you like to store the digit in:"))
          mailbox[store] = (acc)
          mbox = mbox + 1
      elif mailbox[mbox] == 5:
          load = int(input("What mailbox would you like to load the digit from:"))
          (acc) = mailbox[load]
          mbox = mbox + 1
      elif mailbox[mbox] == 6:
          jump = int(input("Where would you like to branch too:"))
          mbox = jump
      elif mailbox[mbox] == 7:
          if acc == 0:
              jump = int(input("Where would you like to branch too:"))
              mbox = jump
      elif mailbox[mbox] == 8:
          if acc >= 0:
              jump = int(input("Where would you like to branch too:"))
              mbox = jump
      elif mailbox[mbox] == 901:
          inp = int(input("Enter a digit:"))
          (acc) = (inp)
          mbox = mbox + 1
      elif mailbox[mbox] == 902:
          print (acc)
          mbox = mbox + 1
      elif mailbox[mbox] == 0:
          loop1 = 1
      
    

