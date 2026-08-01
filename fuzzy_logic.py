"""
FLC: Speed control of a vehicle
Let two fuzzy inputs (speed difference (SD) and acceleration (A)) and one fuzzy
output throttle control (TC) be there.

X: Universe of discourse [0,240]

Partitions: 
    NL: Open left MF (a = 30, b = 60) 
    NM: Traingular(a = 30, b = 60, c = 90)
    NS: Traingular(a = 60, b = 90, c = 120)
    ZE: Traingular(a = 90, b = 120, c = 150)
    PS: Traingular(a = 120, b = 150, c = 180)
    PM: Traingular(a = 150, b = 180, c = 210)
    PL: Open right (a = 180, b = 210) 
    
Rules
R1: if SD is NL and A is ZE then TC is PL
R2: if SD is ZE and A is NL then TC is PL
R3: if SD is NM and A is ZE then TC is PM
R4: if SD is NS and A is PS then TC is PS
R5: if SD is PS and A is NS then TC is NS
R6: if SD is PL and A is ZE then TC is NL
R7: if SD is ZE and A is NS then TC is PS
R8: if SD is ZE and A is NM then TC is PM

# PLTC means Positive Large Throttle Control
# PMTC means Positive Medium Throttle Control
# PSTC means Positive Small Throttle Control
# NSTC means Negative Small Throttle Control
# NLTC means Negative Large Throttle Control

# ----Full form of the variables are given in the comments---
# NLSD MEANS Negative Large Speed
# NMSD MEANS Negative Medium Speed
# NSSD MEANS Negative Small Speed
# ZESD MEANS Zero Speed
# PSSD MEANS Positive Small Speed
# PMSD MEANS Positive Medium Speed
# PLSD MEANS Positive Large Speed
# NLAC MEANS Negative Large Acceleration
# NMAC MEANS Negative Medium Acceleration
# NSAC MEANS Negative Small Acceleration 

"""
import numpy as np
Speed=120
Acceleration=125

print("The speed input is:", Speed)
print("The acceleration input is:", Acceleration)

print("\n")


# Functions for open left and open right membership functions
def openLeft(x, a, b):
    if x < a:
        return 1
    if a < x and x<=b:
        return (b-x)/(b-a)
    else:
        return 0

def openRight(x, a, b):
    if x < a:
        return 0
    if a < x and x <= b:
        return (x-a)/(b-a)
    else:
        return 0

# Functions for triangular membership function for fuzzification
def triangular(x, a, b, c):
    return max(min((x-a)/(b-a), (c-x)/(c-b)), 0)

# Fuzzy Partitions
def partition(x):
    NL = 0;  NM = 0; NS = 0; ZE = 0; PS = 0; PM = 0; PL = 0
    
    if x> 0 and x<60:
        NL = openLeft(x,30,60)
    if x> 30 and x<90:
        NM = triangular(x,30,60,90)
    if x> 60 and x<120:
        NS = triangular(x,60,90,120)
    if x> 90 and x<150:
        ZE = triangular(x,90,120,150)
    if x> 120 and x<180:
        PS = triangular(x,120,150,180)
    if x> 150 and x<210:
        PM = triangular(x,120,150,180)
    if x> 180 and x<240:
        PL = openRight(x,180,210)
 
    return NL,NM,NS,ZE,PS,PM,PL


# Getting the fuzzy values for speed and acceleration

NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD = partition(Speed)
NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC = partition(Acceleration)


# Displaying the fuzzy values for speed and acceleration
output=[[NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD],
        [NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC]]

print("The fuzzy values of the crisp inputs are:")

print(["NL","NM","NS","ZE","PS","PM","PLSD"])
# Here the first row is for speed and second row is for acceleration
# np.round is used to round the values to 2 decimal places
print(np.round(output,2))

# Rules implementation

# Rules implementation
# This function is used to compare the two fuzzy values and return the
# minimum of the two
def compare(TC1, TC2):
    TC = 0
    # if both the fuzzy values are not zero then return the minimum of
    #  the two
    if TC1>TC2 and TC1 !=0 and TC2 !=0:
        TC = TC2
    else:
        TC = TC1

    # if one of the fuzzy values is zero then return the other fuzzy value
    
    if TC1 == 0 and TC2 !=0:
        TC = TC2
    
    # if one of the fuzzy values is zero then return the other fuzzy value 
    if TC2 == 0 and TC1 !=0:
        TC = TC1
        
    return TC





def rule(NLSD,NMSD,NSSD,ZESD,PSSD,PMSD,PLSD,NLAC,NMAC,NSAC,ZEAC,PSAC,PMAC,PLAC):
    # Calculating the fuzzy values for throttle control based on the rules

    # pltc1 = min(NLSD,ZEAC) means that if the speed is negative large and the 
    # acceleration is zero then the throttle control is positive large

    # here why min is used is because we want to take the minimum of the two values
    # as the final fuzzy value for positive large throttle control
    PLTC1 = min(NLSD,ZEAC) 

    # pltc2 = min(ZESD,NLAC) means that if the speed is zero and the acceleration is 
    # negative large then the throttle control is positive large
    PLTC2 = min(ZESD,NLAC)

    # PLTC = compare(PLTC1, PLTC2) means that the final fuzzy value for positive large 
    # throttle control is the and of the two fuzzy values calculated above. The compare 
    # function is used to take the minimum of the two values as the final fuzzy value 
    # positive large throttle control
    PLTC = compare(PLTC1, PLTC2)

    # pmtc means positive medium throttle control
    # PMTC1 = min(NMSD,ZEAC) means that if the speed is negative medium and the
    # acceleration is zero then the throttle control is positive medium
    PMTC1 = min(NMSD,ZEAC)
    # PMTC2 = min(ZESD,NMAC) means that if the speed is zero and the acceleration is
    # negative medium then the throttle control is positive medium
    PMTC2 = min(ZESD,NMAC)
    # PMTC = compare(PMTC1, PMTC2) means that the final fuzzy value for positive medium
    # throttle control is the and of the two fuzzy values calculated above. 
    PMTC = compare(PMTC1, PMTC2)

    # pstc means positive small throttle control
    # PSTC1 = min(NSSD,PSAC) means that if the speed is negative small and the acceleration
    # is positive small then the throttle control is positive small
    PSTC1 = min(NSSD,PSAC)
    # PSTC2 = min(ZESD,NSAC) means that if the speed is zero and the acceleration is
    # negative small then the throttle control is positive small
    PSTC2 = min(ZESD,NSAC)

    # PSTC = compare(PSTC1, PSTC2) means that the final fuzzy value for positive small
    # throttle control is the and of the two fuzzy values calculated above.
    PSTC = compare(PSTC1, PSTC2)

    # nstc means negative small throttle control
    # NSTC = min(PSSD,NSAC) means that if the speed is positive small and the acceleration is
    # negative small then the throttle control is negative small
    NSTC = min(PSSD,NSAC)


    # nltc means negative large throttle control
    # NLTC = min(PLSD,ZEAC) means that if the speed is positive large and the acceleration is 
    # zero then the throttle control is negative large
    NLTC = min(PLSD,ZEAC)

    # these are the final fuzzy values for throttle control based on the rules implemented above
    return PLTC, PMTC, PSTC, NSTC, NLTC



# Defuzzification
















