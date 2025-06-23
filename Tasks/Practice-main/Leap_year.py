# given year is leap year or not
# ==
year=int(input("Enter a year::"))
if ((year%4==0) & (year%400==0)) | year%100!=0:
    print("Leap year")
else:
    print("Not a leap year")