# Calculate the volume of a brick
## Formula pattern
## Comments added at request of unit instructrions, though the requested amount seems over the top.

# Compute the base area from width and length
# A positive int in any distance unit
width = int(input("Please provide the width: "))
# A positive int in any distance unit 
length = int(input("Please provide the length: "))

area = width * length

# Compute the volume from area and height
# A positive int in any distance unit
height = int(input("Please provide the height: "))

volume = area * height

# Output results
print(f"The volume of the brick is {volume}")