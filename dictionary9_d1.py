product = {
    'name' : '',
    'unit_price' :0,
    'taxable' :True,
    'in_stock' :0,
    'Models': ['Black','Tortoise']
    }

DWC001 = dict.fromkeys(product.keys())
DWC001.setdefault('taxable',True)
DWC001.setdefault('Models',[])
DWC001.setdefault('reorder_point',100)

print("Dictionary after from keys() and setdefault()")
print(DWC001)

print("\nDictionary after from keys() and setdefault()")
DWC001['taxable'] = True

print(DWC001)