import csv
import requests
from datetime import datetime
import os, errno



day = datetime.now().strftime(" %Y %m %d")
#   ^^change this if you want a different date structure^^

directory = (str('./data/')+str(day))

url = 'https://www.google.com/finance/getprices?i=60&p=20d&f=d,o,h,l,c,v&df=cpct&q='

#url breakdown:i= is the interval in seconds. Not all stocks give this much detail and the amount of days its available changes
#		  minute data is only availble for 20 days, but if you grab daily it will do the full history
#	       p= is the number of days
#	       f= o=open, h=high, l=low c=close, v=volume


with open('tickers.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        ticker = (str(row))

        ticker = ticker.replace(']','')
        ticker = ticker.replace("'",'')
        ticker = ticker.replace('[','')
        



        test = (str(url)+str(ticker))
        response = requests.get(test)
        filename = (str('./data/')+str(day)+str('/')+str(ticker)+str(day)+str(".csv"))
        print(test)

        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise





        file = open(filename, 'w')
        file.write(response.text)
        file.close()
