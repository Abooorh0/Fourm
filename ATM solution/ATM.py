def withdraw(money, request):
    print "Current balance = " + str (money)
    
    if   request > money:
        print "Can't gvies all this money!"

    elif request <= 0:
        print "Please inter the number?"

    else:
        money -= request
        while request > 0:

            if request >= 100:
                request -= 100
                print "Give 100"
        
            elif request >= 50:
                request -= 50
                print "Give 50"

            elif request >= 10:
                request -= 10
                print "Give 10" 

            elif request >= 5:
                request -= 5
                print "Give 5"

            elif request >= 1:
                request -= 1
                print "Give 1"

    return money - request

money = 500

money = withdraw(money, 376) 
money = withdraw(money, 30)
money = withdraw(money, 5)
money = withdraw(money, 500)                


	