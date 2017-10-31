
dict1={'home':'NY', 'work':'NJ'}
dict2= {'salary':3000, 'tax':200, 'soc_sec': 56, 'med_care':3}

car_info = {'brand':'Ford','model':'F-150',
'year':2012,'plate':'AGP-567','vin':'23483242340'}
type(car_info)

the_values= car_info.values()
for v in the_values:
    print('Value',v)
the_keys= car_info.keys()
for k in the_keys:
    print('Key: ',k)
for e in car_info:
    print('Key: ',e, 'value:' ,car_info[e])


