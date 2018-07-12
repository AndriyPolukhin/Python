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

# 1. Ask for the tree height:
# 2. Convert the height string into an integer:
# 3. Variables
#string = space+space+space+space+hash+space+space+space+space

tree_height = input("How tall is the tree: ")
tree_height = int(tree_height)
numberOfSpaces = (tree_height - 1)


hash = "#"
space = " "
string = ""
spaces = ""
hashes = ""

numberOfHashes = (tree_height - numberOfSpaces)
print("Starting number of space _ is {}".format(numberOfSpaces))
print("Starting number of hash # is {}".format(numberOfHashes))

while(tree_height !=0 ):



        for s in range(numberOfSpaces):
            spaces += space
            print(spaces)
        for h in range(numberOfHashes):
            hashes += hash
            print(hashes)


    numberOfSpaces = numberOfSpaces - 1
    numberOfHashes += 2
    tree_height = tree_height - 1




