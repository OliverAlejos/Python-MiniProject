import matplotlib.pyplot as plt
import csv
from datetime import datetime
import matplotlib.dates as mdates
import numpy as np
import matplotlib.ticker


with open ('PRICESBRUH.csv') as file:
    csv_file = csv.reader(file)
    header_row = next(csv_file)
    date_list = []
    price = []

    for row in csv_file:
   
        datetime_object = datetime.strptime('1/5/2015', "%m/%d/%Y")
        date_list.append(datetime_object)
        priceec = float(row[1])
        price.append(priceec)
    

plt.plot(date_list, price, color = 'turquoise', linestyle = 'solid',
		marker = 'o',label = "Gas Prices")


plt.xlabel('DATE')
plt.ylabel('PRICE (US DOLLAR)')
plt.title('Gas Price Over Time (2015)', fontsize = 20)
plt.grid()

left = (1,5,2015)
right = (12,18,2015)

plt.show()
