car_info={'brand': 'Ford', 'model': 'F-150', 'year': 2012, 'plate': 'AGP-567', 'vin': '23483242340'}
type(car_info)
#<class 'dict'>
the_values = car_info.values()
for v in the_values:
    print('Value', v)
    
the_keys = car_info.keys()

for k in the_keys:
    print('Key: ', k)

for e in car_info:
    print('Key: ', e, ', value: ', car_info[e])
