import matplotlib.pyplot as plt
import csv
from datetime import datetime
import matplotlib.dates as mdates

with open ('PRICESBRUH.csv') as file:
    csv_file = csv.reader(file)
    header_row = next(csv_file)
 #   for line in csv_file:
#        print(line)
#    for row in csv_file:
#        x.append(int(row[2]))
#        y.append(string_(row[2]))
    date_list = []
    price = []

    for row in csv_file:
      #  date_string = ("2010 {0}/")
        datetime_object = datetime.strptime('1/5/2015', "%m/%d/%Y")
        date_list.append(datetime_object)
        priceec = float(row[1])
        price.append(priceec)


plt.plot(date_list, price, color = 'g', linestyle = 'solid',
		marker = 'o',label = "Gas Prices")

plt.xticks( )
plt.xlabel('TIME')
plt.ylabel('PRICE (US DOLLAR)')
plt.title('Gas Price Over Time (1995 - 2021', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
