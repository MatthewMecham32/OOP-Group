from datetime import datetime
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
        self.sCustID = self.gen_id(sCustFirst, sCustLast, sAddress1)
        
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

    def make_payment(self, fPayment):
        self.fBalance = self.fBalance - float(fPayment)
        return self.fBalance
class Pet :
    def __init__ (self, spetName, spetBreed, ipetAge, oCustomerOwner) :
        self.pet_name = spetName
        self.breed = spetBreed
        self.age = ipetAge
        self.appointment = Appointment(oCustomerOwner)


class Appointment :  
    def __init__(self, customer_owner) :
        self.dBegin_Date = None  
        self.dEndDate = None
        self.fDayRate = None
        self.iTotalDays = 0
        self.fTotalCost = 0.0
        self.customer_owner = customer_owner
    def set_appointment(self, dBeginDate, dEndDate, fDayRate) :
        self.iTotalDays = self.calc_days(dBeginDate, dEndDate)
        self.fTotalCost = self.iTotalDays * fDayRate
        self.total_cost = (self.iTotalDays  * self.fDayRate)
    
        # receives begin_date, end_date, and day_rate and calls the
        # calc_days() method and store the total_days and calculate the total_cost (total_days *
        # day_rate)
        # updates the balance by calling the self.owner.balance which is the
        # customer object that was created and assigning it the total_cost
        
        
    def calc_days(self, dBeginDate, dEndDate) :
        # calculates the total_days by substracting the end_date from the begin_date.
        # However, you must return the days value for the formula:
        # self.total_days = (self.end_date - self.begin_date).days
        # calc_days() should check if the total_days is less than or equal 0 and if so, assign a 1 to the total_days
        # calc_days() should calculate the total_cost by multiplying total_days by day_rate
        self.iTotalDays = dEndDate - dBeginDate
        return self.iTotalDays

oCustomer = Customer('matt', 'mecham', '565west 520 north', '356s 900w', 'provo', 'UTAH', '84601' )
print(oCustomer.sCustID)
print(oCustomer.return_bill())