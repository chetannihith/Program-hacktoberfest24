import random

tops = ["T-shirt", "Hoodie", "Button-up shirt"]
bottoms = ["Jeans", "Shorts", "Joggers"]
shoes = ["Sneakers", "Sandals", "Loafers"]

outfit = {
    "Top": random.choice(tops),
    "Bottom": random.choice(bottoms),
    "Shoes": random.choice(shoes)
}

print("Your casual outfit:", outfit)
