#Multi level inheritance
class Bank:

    def transaction(self):
        print('total balance')
    def account_opening(self):
        print('This will show you account opening status')
    def deposite(self):
        print("this will show your deposite amount")

class HDFC_bank(Bank):
    def hdfc_to_icici(self):
        print("this will show you all tranction happened icici through hdfc")

class icici(HDFC_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
i.transaction()