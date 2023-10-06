from pylocalstorage import LocalStorage, ObjectPersistence

print("# Tests with LocalStorage instance\n")

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

# Retrieving all existing keys
for i in range(ls.length):
    print(ls.key(i))

# Cleaning up LocalStorage
ls.clear()
print("Number of items:", ls.length)




print("\n# Tests with ObjectPersistence instance\n")

# Connecting to ObjectPersistence
op = ObjectPersistence()

op.setItem("test", "Hello")
op.clear()

op.setItem("test", {
    "country": "Brazil",
    "city": "Manaus"
})
print(op.getItem("test"))

op.removeItem("test")
print(op.getItem("test"))
