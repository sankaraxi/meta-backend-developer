favorite_stars = ["Vijay", "Anirudh", "Siva Karthikeyan", "Vijay Sethupathi", "Hip Hop Tamizha"]

for star in favorite_stars:
    print("My favorite Star is" ,star)

print("End of the For loop")

print()
count = 0
while count < len(favorite_stars):
    print("My favorite Star is" ,favorite_stars[count])
    count += 1

print("End of the While loop")

print()
#enumerate
#enumerate() function is used to add a counter to an iterable and return it in a form of enumerate object.

for index, star in enumerate(favorite_stars):
    print("My favorite Star is" ,star, "at index", index)

print("End of the For loop with enumerate")