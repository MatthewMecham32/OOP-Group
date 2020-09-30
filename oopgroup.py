class Customer:
    Company_Name = "Critter Watch"
    def __init__(self, sCustFirst, sCustLast,sAddress1 , sAddress2,sCity,sState,sZip) :
        self.sCustFirstName = sCustFirst
        self.sCustLastName = sCustLast
        self.sAddress1 = sAddress1
        self.sAddress2 = sAddress2
        self.sCity = sCity
        self.sState = sState
        self.sZip = sZip
        self.fBalance = 0.0
        self.Cust_Pet = None
        self.sCustID = Customer.gen_id(self, sCustFirst, sCustLast, sAddress1)
        
    def gen_id(self,sCustFirstName, sCustLastName, sAddress1) :
        #d takes the first 3 letters from
        # the first name, first 3 letters from the last name, and first 5 letters from the address to
        # create the cust_id and returns that string value which when called will be assigned back to
        # the cust_id attribute in the Customer class
        # Replace any spaces in the string with no space ('')
        sCustID = sCustFirstName[0:3]
        sCustID = sCustID + sCustLastName[0:3]
        sCustID= sCustID + sAddress1[0:5]
        return sCustID


    def return_bill(self, sCustFirstName, sCustLastName, fBalance, Cust_Pet, sBeginDate, sEndDate) :
        #return this statement 
        # Customer greand2677e with name greg anderson  
        # owes $123.50 for charlie's stay
        # from 10/01/2020 to 10/20/2020
        pass

    def make_payment(self):
        pass
oCustomer = Customer('matt', 'mecham', '565west 520 north', '356s 900w', 'provo', 'UTAH', '84601' )
print(oCustomer.sCustID)