# Digital Identity - Python Script

# String: Name and Email
name = "Siyabonga Magagula"
email = "siyabongam26@gmail.com"

# Integer: Age
age = 28

# Float: Height (in meters)
height = 1.75  # meters

# Whether you are a programmer or not
is_programmer = True

# List: A list of skills
skills = ["Python", "JavaScript", "Data Analysis", "Machine Learning"]

# Dictionary: A dictionary to store contact information
contact_info = {
    "phone": "+27813456507",
    "address": "South Africa"
}

# Hobbies 
hobbies = ("Reading", "Gaming", "Traveling")

# Displaying the "digital identity" using formatted strings
print(f"Digital Identity:\n")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Age: {age} years old")
print(f"Height: {height} meters")
print(f"Is a Programmer: {is_programmer}")
print(f"Skills: {', '.join(skills)}")
print(f"Contact Information: {contact_info}")
print(f"Hobbies: {', '.join(hobbies)}")