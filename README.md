# stockpricedownloader
Downloads stock prices from google down to intraday (seconds if available) for last 20 days. Uses a list of ticker symbols to batch generate.

I use finviz to screen for stocks. Enter your paramenters and click for 'ticker' symbol. Highlight them all then paste into your favourite text editor without formatting. Then find and replace all the triple spaces '   ' with \n (ie newline) tested on gedit.

Save the resulting file as tickers.csv

start the downloader.py file and it will create a folder called data, then subfolders for each day run.

RECOMMENDED TO RUN AFTER EXCHANGE IS CLOSED. IT WILL OVERWRITE FILES IF RUN THE SAME DAY!

FOLLOW comments in download.py to edit what is downloaded:
  frequency 
  length of time to download
  prices, High, low, close, volume
  
 Be Kind, its my first project!
