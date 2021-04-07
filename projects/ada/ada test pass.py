#
# Complete the 'subscription_summary' function below.
#

from decimal import Decimal #this is used later for round all teh number to 2 decimals
def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
   
    price_dic = {"single_month": 7, "ad_free": 2, "bundle_price": 18, "video_on_demand_price":27.99} #create a price dictionary so that all the values can be found in one place--easier to find and change in future or for someone who will work on this code
    cost_per_account = []  ##put each customer's expense in order inside the cost_per_account list, eg [100,200,300] means the 1st customer spend 100, and 2nd spend 200, third spend 300
    
    userinfo = {} # I am going to build a nested dictionary that will include each customer's info. Each item inside the  userinfo dictionary will be a dictionary that containes 3 key-value pairs of a single customer. Example as following: 
    # {{months_subscribed1: 1, ad_free_months1: 1, video_on_demand_purchases1: 1},
    #{months_subscribed2: 2, ad_free_months2: 2, video_on_demand_purchases2: 2},        {months_subscribed3: 3, ad_free_months3: 3, video_on_demand_purchases3: 3}
    
    premium_content = 0 #total earned from ad_free and video on demand, give the variable an initial value so that we can use it for calculation in the future
    total = 0  #the total earning for all customers, refer to question 6.2. Give an initial value 0
    account_total=0 # how much a customer spend in total, give an initial value 0
    
    def check_input(): #check if all the inputs are corret format, if not we will give a reminding message--"All input should be integers!"
        input_list=months_subscribed+ad_free_months+video_on_demand_purchases  # here we combine all the lists 
        for index in input_list: #check each element in the list using for loop
            if type(index)!=int: #if element type is not integer
                print("All input should be integers!")
             
    
    def round_number(number): #This function is to make all the doller output into 2 decimals
        return str(Decimal(number).quantize(Decimal("0.00")))
    
    def each_customer_info(): #This is a function calculating how much each account spend, refer to question 6.1
        nonlocal total #pull the variables from main function, we need to make them nolocal inorder to avoid "use before assign" error
        nonlocal premium_content #same as avove
        
        month_fee = userinfo[i]['month'] // 3 * price_dic['bundle_price'] + userinfo[i]['month']%3*7 # userinfo[i]['month'] // 3: calculating how many bundles the (i+1)st customer have
        ad_free = userinfo[i]['ad_free']*price_dic['ad_free']  # the money spend on ad_free for a customer
        on_demand = userinfo[i]['video_on_demand'] * price_dic['video_on_demand_price']  #the money spent on video_on_demand
        
        account_total = month_fee + ad_free + on_demand # how much a customer spend in total
        total += account_total #the total earning for all customers, refer to question 6.2
        premium_content += ad_free + on_demand #The total ewarning for ad_free and video on demand, refer to question 6.3
        cost_per_account.append(account_total) #put each customer's expense in order inside the cost_per_account list
          
        print("Account "+ str(i+1) + " made $" + round_number(account_total) + ' total') #str(i+1) is because python counts from 0 while human count from 1
        print(">>> $" + round_number(month_fee) + " from monthly subscription fees")
        print(">>> $" + round_number(ad_free) + " from Ad-free upgrades")
        print(">>> $" + round_number(on_demand) + " from Video on Demand purchases")
        print()
            
    def find_max_account(): #This is a function used to find which account spent the most and print out the account number
        max_account=[]
        max_cost = max(cost_per_account) #find the max amount by using max() function
        for j in range(len(cost_per_account)):  #check which account spend the most by looking at each account using for loop
            if cost_per_account[j] == max_cost: #if the amount spent by an account is equal to max amount, we need to record the account position
                max_account.append(j+1)   #add the account number to a list, if multiple accounts spend equal to max value, add everyone of them
        max_account=['#'+ str(i) for i in max_account] #change element name into a string with a "#" ahead  
        print(f"${round_number(max_cost)} was the most earned by any single account") #print the most cost
        print("The accounts that earned the most were: "+ ", ".join(max_account)) #print all the items inside the max_account list, seperated by comma
    
        
############  Here starts the main function
    check_input() #check if all the inputs are corret format, give a reminding message otherwise
    print("Welcome to the Ada+ Account Dashboard")
    print()   # a blank line
    
    for i in range(len(months_subscribed)): #check each customer by using for loop, len(months_subscribed) means how many customer we have
        
        userinfo[i] = {'month': months_subscribed[i], 'ad_free': ad_free_months[i], 'video_on_demand': video_on_demand_purchases[i]} #create a dictionary with 3 key-value pairs for each customer
        each_customer_info()
        
    print("Combined all accounts made $" + round_number(total) + " total")
    print("Premium content (Ad-free watching and Video on Demand) made $" + round_number(premium_content) + " total")
    print()
    find_max_account()
