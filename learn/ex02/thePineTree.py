'''
how tall is the tree : 5
            #
           ###
          #####
         #######
        #########
            #
'''
# TIPS to breakdown the problem:
    # I. Use 1 while loop and 3 for loops
    # II. Analyse the tree rules:

#  4 spaces _ : # 1 hash
#  3 spaces _ : # 3 hashes
#  2 spaces _ : # 5 hashes
#  1 space  _ : # 7 hashes
#  0 spaces _ : # 9 hashes

    # III. Save the first and the last as 1 hash

# Need to do:

# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and hashses for each row
# 6. Print stump spaces and then 1 hash


# THE CODE FOR THE PINE TREE PROBLEM:
# How to solve a pine tree:

# 1. Get the number of rows for the tree
tree_height = input("How tall is the tree ")

# 2. Convert into an integer
tree_height = int(tree_height)

# 3. Get the starting spaces for the top of the tree
spaces = tree_height - 1

# 4. Track number of hashes that will be incremented
hashes = 1

# 5. Save some spaces for later
stump_spaces = tree_height - 1

# 6. Make Sure the right number of rows are printed
while tree_height != 0:

# 7. Print the spaces end=""
    for i in range(spaces):
		    print(' ', end="")

# 8. Print the hashes
    for i in range(hashes):
		    print('#', end="")

# 9. Newline after each row is printed
    print()

# 10. Decrement spaces by 1 each time through the loop
    spaces -= 1

# 11. Increment hashes by 2 each time through the loop
    hashes += 2

# 12. Decrement tree_height each time to jump out of the loop
    tree_height -= 1

# 13. Print the spaces befor the stamp and then the hash
for i in range(stump_spaces):
    print(' ', end="")

print("#")

















































