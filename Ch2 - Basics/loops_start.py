#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#

def main():
    x = 0

    # TODO: define a while loop
    while(x<5):
        print(x)
        x = x + 1


    # TODO: define a for loop
    for x in range(5,10):
        print(x)
    ####print 5 6 7 8 9

    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)
    ## prints all days    


    # TODO: use the break and continue statements
    for x in range(5,10):
        if x == 7:
            break
        print(x)
    ## only prints 5 and 6

    for x in range(5,10):
        if x % 2 == 0:
            continue
        print(x)
    ##only prints odd numbers    



    # TODO: using the enumerate() function to get index 
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(days):
        print(i, d)




        
if __name__ == "__main__":
    main()


