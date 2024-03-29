from pylocalstorage import LocalStorage

# Connecting to LocalStorage
ls = LocalStorage()

# Creating three items
ls.setItem("name", "David")
ls.setItem("age", 29)
ls.setItem("address", {
    "country": "Brazil",
    "city": "Manaus"
})
print("Number of items:", ls.length)

# Updating an item
ls.setItem("name", "David Ferreira")

# Getting an item
print(ls.getItem("name"))

# Removing an item
ls.removeItem("name")

# Saving numpy array
import numpy as np
ls.setItem("array", np.zeros((1080, 1920, 3), dtype=np.uint8))

# Retrieving all existing keys
for i in range(ls.length):
    print(ls.key(i))

# Cleaning up LocalStorage
ls.clear()
print("Number of items:", ls.length)
