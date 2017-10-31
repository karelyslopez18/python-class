def oddfloats(float_num):
    odds=0
    for x in float_num:
        if x %2==1:
            odds= x+odds
    print(odds, len(odds))

        
