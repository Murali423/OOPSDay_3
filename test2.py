#Multiple inheritance
class Bank:

    def transaction(self):
        print('total balance')
    def account_opening(self):
        print('This will show you account opening status')
    def deposite(self):
        print("this will show your deposite amount")
    def test(self):
        print('this method from bank class')

class HDFC_bank():
    def hdfc_to_icici(self):
        print("this will show you all tranction happened icici through hdfc")

    def test(self):
        print('this is from hdfc class')

class ineuron_bank:
    def account_status_icici(self):
        print('print account status in icici')

class icici(HDFC_bank, Bank, ineuron_bank ):
    pass

i = icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
i.transaction()
i.test()
i.account_status_icici()