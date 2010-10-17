import dao
from decimal import Decimal

account_value = Decimal('48000')
risk_factor = 100
chart ='http://finance.yahoo.com/q/bc?s=SCA-A.ST&t=2y&l=on&z=l&q=l&c='
print "Symbol\tDate\tClose\tStop\tShares\tPosition\tChart"
print "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
for quote in dao.Quote.get_latest_quotes():
  if quote.is_above_20_day_high():
    #print "||||||||||||||||||||||| Should enter %s " % quote.symbol
    if(quote.is_above_sma20() and quote.is_above_sma50()):
      #print "Above sma20 and sma50"
      chart = "http://finance.yahoo.com/echarts?s=%s" % quote.symbol
      #print "https://www.avanza.se/aza/sok/standard.jsp?word=%s" % (
      #    quote.symbol.replace('.ST', '').replace('-A', '').replace('-B', ''))

      stop = quote.get_indicator().calculate_stop(quote.close)
      shares = dao.Position.get_shares(quote, account_value/risk_factor)
      position = long(shares * quote.close)
      print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (quote.symbol, quote.date, quote.close, stop, shares, position, chart)
      #chart = chart + "+" + quote.symbol
  else:
    #print "Leave %s " % quote.symbol
    pass