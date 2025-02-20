l1=[("pizza",60),("Burger",50),("pasta",65)]

def get_price(item):
    return item[1]
sorted_food_prices=sorted(l1,key=get_price,reverse=True)
print(sorted_food_prices)