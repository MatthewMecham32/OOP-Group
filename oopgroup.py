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


    def return_bill(self) :
        sBill = "Customer " + self.sCustID + " with name " + self.sCustFirstName + " " + self.sCustLastName + " owes $" + str(self.fBalance) + " for " + str(self.Cust_Pet) + "'s stay from " #+ str(self.sBeginDate) + " to " + str(self.sEndDate)

        return sBill

    def make_payment(self):
        pass
oCustomer = Customer('matt', 'mecham', '565west 520 north', '356s 900w', 'provo', 'UTAH', '84601' )
print(oCustomer.sCustID)
print(oCustomer.return_bill())
