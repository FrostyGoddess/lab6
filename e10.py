print("Testing on Terminal")
name = input("What's your name?\n")
print("Hello,",name)
#== lab5 ex10==
class computer:
   def __init__(self,cpu,color,portability):
      self.c = cpu
      self.co = color
      self.p = portability
   def playgame(self,nameofGame):
      if self.p:
         print("you are playing", nameofGame,"on your laptop")
      else:
         print("you are playing",nameofGame,"on your desktop.")
class laptop(computer):
   def __init__(self,cpu,color):
      computer.__init__(self,cpu,color,True)
class desktop(computer):
   def __init__(self,cpu,color):
      computer.__init__(self,cpu,color,False)
myMac = laptop('A6', 'White')
print("My pc runs on",myMac.c)
myMac.playgame('Growtopia')
myHP = desktop('i7')