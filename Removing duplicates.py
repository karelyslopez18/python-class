Exercise a

def remove_duplicates(listing):
    n = []
    print listing
    for part in range(len(listing)):
        exists = 0
        for part2 in range(len(n)):
            if listing[part] == n[part2]:
                exists = 1
        if exists == 0:
            n.append(listing[part])
    return n
