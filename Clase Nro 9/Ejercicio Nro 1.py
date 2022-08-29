def getAList():
  countryList = []
  more = True
  while more:
    country = input("Enter a country: ")
    if country == "":
      return list(set(countryList))
    commas = country.count(",")
    if commas > 0:
      countries = country.split(",")
      for country in countries:
        countryList.append(country.title())
    else:
      countryList.append(country.title())
    wantMore = input("Do you want to add more countries? (y/n): ")
    if wantMore == "n" or wantMore == "N":
      more = False
  return list(set(countryList))

countryList = getAList()
print(countryList)