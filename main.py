from hash_distribution import distribute, plot
from string import printable

plot(distribute(printable, num_containers=2))

print(f"\n")

plot(distribute(printable, num_containers=5))
