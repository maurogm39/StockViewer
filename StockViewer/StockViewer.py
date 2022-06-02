import yfinance as yf

def add_linebreaks (s, col_width = 120):

  s_out = ""
  break_at_next_space = False
  for i in range(len(s)):
    if (i+1) % col_width == 0:
      break_at_next_space = True
    if break_at_next_space and s[i] == ' ':
      s_out += "\n"
      break_at_next_space = False
    else:
      s_out += s[i]
  return s_out


print("Enter the period 'Y' (1 year), 'M' (1 month), 'D' (1 day): ")
valid_options = {
    'Y': ('y', 'year'), 
    'M': ('mo', 'month'), 
    'D': ('d', 'day')
}
option = input()
while option.upper() not in valid_options.keys():
  print("Input not valid..")
  option = input("Enter the period 'Y' (1 year), 'M' (1 month), 'D' (1 day): ")

tickers = yf.Tickers(input("Enter the company ticker: "))

for ticker in tickers.tickers.values():

  print(f"{ticker.info['longName']} ({ticker.info['exchange']})")

  summary = ticker.info['longBusinessSummary']
  summary = add_linebreaks(summary)
  print(summary)
  print()

  period_code, period_name = valid_options[option.upper()]
  if period_code == 'd':
    interval = '1m'
  else:
    interval = '1d'
  values = ticker.history(period=f"1{period_code}", interval=interval).Close

  pct = 100 * (values[-1] - values[0]) / values[0]

  if pct > 0:
    print(f"Price has gone up a {pct:.2f}% in the last {period_name}.")

  elif pct < 0:
    print(f"Price has gone down a {pct:.2f}% in the last {period_name}.")
  
  else:
    print(f"No price changes in the last {period_name}")

  print("\n\n")