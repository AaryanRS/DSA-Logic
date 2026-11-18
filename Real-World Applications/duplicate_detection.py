"""
Real-world use:
Set → Duplicate detection.

Used in signup systems, data processing, and validation
when we only care whether an item already exists.
"""

emails = set()

emails.add("a@gmail.com")
emails.add("b@gmail.com")
emails.add("c@gmail.com")

email = "e@gmail.com"

if email in emails:              # uses O(1) TC, Set → fast membership check → O(1) average
    print("Duplicate email")
else:
    print("New email")
    emails.add(email)

print(emails)