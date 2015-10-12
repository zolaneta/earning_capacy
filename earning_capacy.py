# Earning Cappacy 
# Created on March 10, 2015 
# by Aneta K Zolkiewicz

def years_to_mil(savings):
    """Calculates how many years it  takes to reach million dollars, it prints how much somoeone should make each year,
       and how much should save by the end of the period"""
    print "Here is the plan how to achieve it!"
    count = 0     
    while (savings <= 1000000):
        count = count + 1
        compounding = savings 
        savings = savings + compounding
        print "year", count, "you should make:", compounding, "you should have saved ", savings, "by the end of year"

    return count
        
   

    
# MAIN PROGRAM


count = years_to_mil(input('What are your savings? '))
print " It should take you ", count, "years to become a millionaire!"

        
