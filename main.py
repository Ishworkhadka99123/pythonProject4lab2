''' If the temperature is greater than 30 ,it is hot day otherwise if it's less than 10;
it's cold day;otherwise,
it's neither hot nor cold.
'''

Temperature=int(input("Enter the Tempurature:"))
if Temperature >= 30:
    print("It's a hot day")
elif Temperature <= 10:
    print("It's a cold day")
else:
    print("Its neither hot nor cold")