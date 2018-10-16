import csv
import os
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python3 quote.py SYMBOL")
symbol = sys.argv[1]

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    sys.exit("Missing API_KEY")

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&datatype=csv&outputsize=full"
response = requests.get(url)

reader = csv.DictReader(response.text.splitlines())

for row in reader:
    print(f"{row['timestamp']} ${row['close']}")
