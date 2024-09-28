# ymdhms_to_jd.py
#
# Usage: python3 year month day hour minute second
# Converts ymdhms to jd
# 
# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
# Output:
#  Prints the jd_frac
#
# Written by Vineet Keshavamurthy
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# ymdhms_to_jd.py
import sys
import math


def ymdhms_to_jd(year, month, day, hour, minute, second):
    #calculates the julian date 
    if month <= 2:
        year -= 1
        month += 12
    #the century is calculated
    Century = math.floor((1/100)*year)
    #account for leap year adjustment
    leapyearadjustment = -Century + math.floor(Century/4) + 2
   
    #calculation of jd whole number
    julian_date_whole = math.floor((4716 + year)*365.25) + math.floor((month + 1)*30.6001) - 1524.5 + leapyearadjustment + day 
    
    #calculation of jd fraction
    Dayconversion = 1/24
    Secondsconversion = 1/3600
    Minuteconversion = 1/60
    julian_date_fraction = (Dayconversion) * (minute*Minuteconversion + second*Secondsconversion + hour)
   
    #calculation of jd by adding jd whole number and jd fraction
    jd = julian_date_whole + julian_date_fraction

    return jd #return jd value

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Incorrect number of input arguments passed")
        sys.exit(1)
   
   #Take in input variables
    year = int(sys.argv[1])

    month = int(sys.argv[2])

    day = int(sys.argv[3])

    hour = int(sys.argv[4])

    minute = int(sys.argv[5])

    second = float(sys.argv[6])

   #final output of jd_frac
    jd_frac = ymdhms_to_jd(year,month,day,hour,minute,second)
   #print jd_frac
    print(jd_frac)

