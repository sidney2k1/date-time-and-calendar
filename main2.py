import random
import time
def getrandomdate(startdate,enddate):
    print("Printing random numbers between",startdate,"and",enddate)
    randomgenerator=random.random()
    dateformat="%m/%d/%Y"
    startime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=startime+randomgenerator*(endtime-startime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("The randomdate chosen is:",getrandomdate("1/1/2016","12/31/2016"))
