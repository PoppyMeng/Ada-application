class Category:
  
  #######
  def __init__(self,name):
    self.name=name
    self.ledger=[]
  #When objects are created, they are passed in the name of the category. so for the initiate we have a name inside the function
  #The class should have an instance variable called ledger that is a list.
  ###Instance: under function
  ###objects: inside func variable


  ########
  def deposit(self,amount,description=""):
    #initialising a dictionary
    self.dic={}
    #adding the amount and description to dictionary
    self.dic["amount"]=amount
    self.dic["description"]=description
    #adding the deposit to ledger list
    self.ledger.append(self.dic)

  def check_funds(self,amount):
    self.balance=0
    for i in range(len(self.ledger)):
      self.balance+=self.ledger[i]["amount"]
    if amount>self.balance:
      return False
    else:
      return True
    


  def withdraw(self,amount,description=""):
    if check_funds(self,amount):
      #checking if total amount less than or greaten than amount to be withdrawn
      self.dic={}
      self.dic["amount"]=-amount
      self.dic["description"]=description
      self.ledger.append(self.dic)
      return True
    else:
      return False
  

  def get_balance(self):
    self.initial=0
    for i in range(len(self.ledger)):
     self.initial+=self.ledger[i]["amount"]
    return self.initial


  def transfer(self, amount, another_category):
    if amount>self.check_funds(amount):
      return False
    else:
      self.withdraw(amount,description="Transfer to "+ another_category.name)
      another_category.deposit(amount,description="Transfer from "+self.name)
      return True


  def __str__(self):
  #When the budget object is printed
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for i in range(len(self.ledger)):
      items += f"{self.ledger[i]['description'][0:23]:23}{self.ledger[i]['amount']:>7.2f}\n"
      #items += {self.ledger[i]['description'][0:23]:23} +{self.ledger[i]['amount']:>7.2f}+'\n'

      total += self.ledger[i]['amount']

    output = title + items + "Total: " + str(total)
    return output

#def create_spend_chart(categories):
