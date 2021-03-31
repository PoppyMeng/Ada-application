from decimal import Decimal
def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """

    print("Welcome to the Ada+ Account Dashboard")
    print()
    
    def round_number(number):
        return str(Decimal(number).quantize(Decimal("0.00")))
    total = 0
    premium_content = 0
    cost_per_account = [] #每个客户花的钱
    userdic = {}
    for i in range(len(months_subscribed)):
        userdic[i] = {'month': months_subscribed[i], 'ad_free': ad_free_months[i], 'video_on_demand': video_on_demand_purchases[i]}
        month = userdic[i]['month'] // 3 * 18 + userdic[i]['month']%3*7
        ad_free = userdic[i]['ad_free']*2
        on_demand = userdic[i]['video_on_demand'] * 27.99
        account_total = month + ad_free + on_demand
        total += account_total
        premium_content += ad_free + on_demand
        cost_per_account.append(account_total)
    
        print("Account "+ str(i+1) + " made $" + round_number(account_total) + ' total')
        print(">>> $" + round_number(month) + " from monthly subscription fees")
        print(">>> $" + round_number(ad_free) + " from Ad-free upgrades")
        print(">>> $" + round_number(on_demand) + " from Video on Demand purchases")
        print()
    
    print("Combined all accounts made $" + round_number(total) + " total")
    print("Premium content (Ad-free watching and Video on Demand) made $" + round_number(premium_content) + " total")
    print()
    max_account=[]
    max_cost = max(cost_per_account) #最高的钱数 
    for j in range(len(months_subscribed)):
        if cost_per_account[j] == max_cost:
            max_account.append(j+1)   
    max_account=['#'+ str(i) for i in max_account]
    
    print(f"${round_number(max_cost)} was the most earned by any single account")
    print("The accounts that earned the most were: "+ ", ".join(max_account))
