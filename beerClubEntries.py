#!/usr/bin/python
import math
import random
import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.
    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y/%m/%d', prop)

def randomBeers(num):   
        OldValue = num       
        OldRange = (10 - 0)  
        NewRange = (15 - 1)  
        numBeer = (((OldValue - 0) * NewRange) / OldRange) + 1       
        return int(numBeer)

def randomMember(num):   
        OldValue = num       
        OldRange = (10 - 0)  
        NewRange = (7  - 0)  
        memberIndex = (((OldValue - 0) * NewRange) / OldRange) + 1       
        return int(memberIndex)
        

# Generating random dates for Beer club session
count =0
beerClubDates =[]
while (count < 100):
    beerClubDates.append(randomDate("2017/1/1", "2017/7/19", random.random()))
    count = count + 1

beerClubDates[0:10]


# List of Beer club members
memberCode = ['UG', 'VIR', 'ALX', 'OK', 'AFF', 'HNS', 'ART', 'DIM', 'SIM']
memberCode[0:]



beerClubDates.sort()
for i in range(100):
    for j in range(10):
        member = memberCode[randomMember(random.random() * 10)] 
        beer = randomBeers(random.random() * 10)
        st = 'INSERT INTO beerclub (UserID, date, beers) VALUES ('
        print st ,  '"',  member ,  '","' , beerClubDates[i] , '",' ,  beers, ');'   
