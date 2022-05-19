# Apartment.py

class Apartment:
    def __init__(self, rent= 0, metersFromUCSB= 0, condition= "N/A"):
        self.rent = int(rent)
        self.metersFromUCSB = int(metersFromUCSB)
        self.condition = condition
        if self.condition != "N/A":
            self.condition = str(condition)

    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    def getCondition(self):
        return self.condition
    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}"\
               .format(self.rent, self.metersFromUCSB, self.condition)
    def __gt__(self, rhs):
        if (self.rent == rhs.rent) and (self.metersFromUCSB == rhs.metersFromUCSB):
            if len(self.condition) > len(rhs.condition):
                return False
            else:
                return True
        elif (self.rent == rhs.rent):
            return self.metersFromUCSB > rhs.metersFromUCSB
        else:
            return self.rent > rhs.rent
    def __lt__(self, rhs):
        if (self.rent == rhs.rent) and (self.metersFromUCSB == rhs.metersFromUCSB):
            if len(self.condition) > len(rhs.condition):
                return True
            else:
                return False
        elif (self.rent == rhs.rent):
            return self.metersFromUCSB < rhs.metersFromUCSB
        else:
            return self.rent < rhs.rent
    def __eq__(self, rhs):
        if (self.rent == rhs.rent) and (self.metersFromUCSB == rhs.metersFromUCSB) and (self.condition==rhs.condition):
            return True
        else:
            return False
