product = {
    'name' : 'Ray-Ban Wayfarer Sungalsses',
    'unit_price' :  112.99,
    'taxable' : True,
    'in_stock' : 10,
    'Models': ['Black','Tortoise']
    }

print('Name:    ',product['name'])
print('Price:   ',f"${product['unit_price']:.2f}")
print('Taxable: ',product['taxable'])
print('In Stock:',product['in_stock'])
print('Models:')
for model in product['Models']:
    print(" "*10 + model)