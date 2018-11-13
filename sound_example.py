import convertdate

date1 = convertdate.hebrew.from_gregorian(1, 1, 1)
date2 = convertdate.hebrew.from_gregorian(2014, 10, 31)

print(f"Zgodnie z kalendarzem hebrajskim, na dzień 1 stycznia pierwszego roku naszej ery przypadał: {date1}  ")
print(date2)
