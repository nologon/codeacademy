#!/usr/bin/python

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!
print duck_index
animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation
