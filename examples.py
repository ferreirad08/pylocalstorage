from pylocalstorage import LocalStorage

# Connecting to LocalStorage
my_storage = LocalStorage()

# Creating three items
my_storage.setItem("name", "David")
my_storage.setItem("age", 29)
my_storage.setItem("address", {
    "country": "Brazil",
    "city": "Manaus"
})
print("Number of keys:", my_storage.length)

# Updating an item
my_storage.setItem("name", "David Ferreira")

# Getting an item
print(my_storage.getItem("name"))

# Removing an item
my_storage.removeItem("name")
print(my_storage.getItem("name"))

# Retrieving all existing keys
for i in range(my_storage.length):
    print(my_storage.key(i))

# Cleaning up LocalStorage
my_storage.clear()
print("Number of keys:", my_storage.length)
