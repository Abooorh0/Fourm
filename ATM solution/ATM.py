class ATM:

    def __init__(self, balance, bank_name):
        self.withdrawals_list = []
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print "Welcome to " + self.bank_name
        print "Current balance = " + str(self.balance)

        if   request > self.balance:
            print "Can't gvies all this money!"

        elif request <= 0:
            print "Please inter the number?"

        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            ATM.process_request(self, request)

    def process_request(self, request):
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

            return self.balance

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

print "============="

atm2.withdraw(100)
atm2.withdraw(2000)