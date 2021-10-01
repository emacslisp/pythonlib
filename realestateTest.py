from realestate_com_au import RealestateComAu

api = RealestateComAu()

# Get property listings
listings = api.search(locations=["westmead, nsw 2145"], channel="buy", min_bedrooms=3,min_bathrooms=2)
print(listings)
