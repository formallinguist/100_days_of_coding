products = {
    'RB00111':{'name':'Rayban Sunglasses', 'price':112.98,'models':['black','tortoise']},
    'DWC0317':{'name':'Drone with camera', 'price':72.95, 'models':['white','black']},
    'MTS054':{'name':'T-shirt','price':2.95,'models':['small','medium','large']},
    'ECD2989': {'name':'Echodot','price':29.99,'models':[]}
}

print(f"{'ID':<6} {'Name':<17} {'Price':>8} {'Modles'}")
print('-'*60)

for oneproduct in products.keys():

    id = oneproduct

    name = products[oneproduct]['name']

    unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"

    models = ''

    for m in products[oneproduct]['models']:
        models += m +', '
    
    if len(models)>2:
        models = models[:-2]
    else:
        models = '<none>'
    print(f"{id:<6} {name:<17} {unit_price:>8} {models}")    