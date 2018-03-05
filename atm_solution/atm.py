class ATM :
  def __init__(self,balance,bank_name) :
    self.balance = balance
    self.bank_name = bank_name

  def withdraw (self, request):
    print("Welcome to "+ self.bank_name)
    print("current balance = "+str(self.balance))
    print("================================")

    if request > self.balance :
      print("Can't give you all this money !!")
      

    elif request < 0 :
      print("Plz More than zero")
      

    else :
      self.balance -= request
     
      while request > 0 :

        if request >= 100 :
          print ("give 100")
          request-=100

        elif request >= 50 :
          print("give 50")
          request-=50

        elif request >= 10 :
          print("give 10")
          request-=10

        elif request >= 5 :
          print("give5")
          request-=5

        elif request < 5 :
          print("give "+ str(request))
          request=0

atm1=ATM(500,"Smart Bank")
atm1.withdraw(277)
atm1.withdraw(300)
