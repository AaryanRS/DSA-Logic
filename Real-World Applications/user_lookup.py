"""
Real-world use:
Hash Map → User lookup.

A website can use a user ID as the key and user data
as the value, making it easy to quickly find a user among 1 million.
"""

users = {
    48291: "Aaryan",
    73921: "Rahul",
    19382: "Aman",
}

user = users[48291]

print(user)  # Aaryan