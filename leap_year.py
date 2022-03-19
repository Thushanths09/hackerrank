def leap_year(year):
    if year%100==0:
        if year%400==0:
            return "Leap"
        else:
            return "Not Leap"
    elif year%4==0:
        return "Leap"
    else:
        return "Not Leap"
year=int(input("Enter the year:"))
print(leap_year(year))