# lab06.py
from Apartment import Apartment

def mergesort(apartmentList):
        if len(apartmentList) > 1:
            mid = len(apartmentList) // 2
            
            lefthalf = apartmentList[:mid]
            righthalf = apartmentList[mid:]
            
            mergesort(lefthalf)
            mergesort(righthalf)
            
            i = 0 
            j = 0
            k = 0 

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    apartmentList[k] = lefthalf[i]
                    i = i + 1
                else:
                    apartmentList[k] = righthalf[j]
                    j = j + 1
                k = k + 1
                
            while i < len(lefthalf):
                apartmentList[k] = lefthalf[i]
                i = i + 1
                k = k + 1
            while j < len(righthalf):
                apartmentList[k] = righthalf[j]
                j = j + 1
                k = k + 1

def ensureSortedAscending(apartmentList):
    check_sorted = True
    for i in range(len(apartmentList)-1):
        if apartmentList[i] > apartmentList[i+1]:
            check_sorted = False
    return check_sorted

def getNthApartment(apartmentList, n):
    try:
        return apartmentList[n].getApartmentDetails()
    except Exception:
        return "(Apartment) DNE"
def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    if len(apartmentList) >= 3:
        return "1st: " + apartmentList[0].getApartmentDetails() +\
    "\n" + "2nd: " + apartmentList[1].getApartmentDetails() +\
    "\n" + "3rd: " + apartmentList[2].getApartmentDetails()
    elif len(apartmentList) == 2:
        return "1st: " + apartmentList[0].getApartmentDetails() + "\n" + "2nd: " + apartmentList[1].getApartmentDetails()
    elif len(apartmentList) == 1:
        return "1st: " + apartmentList[0].getApartmentDetails()
        
