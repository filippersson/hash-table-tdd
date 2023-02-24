from collections import Counter

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])


def plot(histogram):
    for key in histogram:
        count = histogram[key] 
        padding = (max(histogram.values()) - count) * " "
        unichar = "\u25A1"
        print(f"{key:3} {unichar * count} {padding} ({count})")
        
def hash_function(key):
    
    return sum(
        index * ord(character) 
        for index,character in enumerate(repr(key).lstrip("'"), start=1)
    )
