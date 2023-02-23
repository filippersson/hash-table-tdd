from collections import Counter

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])


def plot(histogram):
    for key in histogram.keys():
        count = histogram[key] 
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'U+1F7E9'} {padding} ({count})")
