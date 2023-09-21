# CS175
# Aidan Mazzola
# Stocks

amountPaidForStock = 0.0
purchaseCommission = 0.0
totalPaid = 0.0
stockSoldFor = 0.0
sellingCommission = 0.0
totalReceived = 0.0
profitOrLoss = 0.0

CommissionRatePurchase = float(input("Enter commission rate percentage purchase: "))
CommissionRateSale = float(input("Enter commission rate percentage on sale: "))
NumberSharesPurchased = int(input("Enter number of shares purchased: "))
NumberSharesSold = int(input("Enter number of shares sold: "))
PurchasePricePerShare = float(input("Enter purchase price per share: "))
SellPricePerShare = float(input("Enter sell price per share: "))

amountPaidForStock = NumberSharesPurchased * PurchasePricePerShare

purchaseCommission = CommissionRatePurchase * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission

stockSoldFor = NumberSharesPurchased * SellPricePerShare

sellingCommission = CommissionRateSale * stockSoldFor

totalReceived = stockSoldFor - sellingCommission

profitOrLoss = totalReceived - totalPaid


print("Amount paid for stock: $", amountPaidForStock)
print("Purchase Commission:$", purchaseCommission)
print("Total Paid:$", totalPaid)
print("Stock Sold for:$", stockSoldFor)
print("Selling Commission:$", sellingCommission)
print("Total Received:$", totalReceived)
print("Profit or Loss:$", profitOrLoss)
