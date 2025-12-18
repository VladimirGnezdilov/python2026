def delivery_price(city,weight_kg, urgent):
   if urgent==True:
    return 500 + 30 * weight_kg
   else:
     return   300 + 20 * weight_kg
print(delivery_price(city="something" ,weight_kg=200,urgent=True))
print(delivery_price(city="somewhere" ,weight_kg=300,urgent=False))
print(delivery_price("something" ,200,True))
print(delivery_price("somewhere" ,300,False))
#print(delivery_price(weight_kg=300,"somewhere",urgent=False))
