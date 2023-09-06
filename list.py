#This is a simple code demonstrating how to work with lists and using the for loop
besties = []
print("step 1: This is a simple code demonstrating how to work with lists and using the for loop")
besties.append("Rejoice")
besties.append("Jane")
besties.append("Rose")
print("step 2", besties)
for i in range(2):
    besties.append(input("new bestie club member: ").lower())
print("step 3", besties)
del besties[-1]
del besties[-1]
print("step 4", besties)
besties.insert(0, "Ringostar")
print("step 5", besties)
print("the fabulous:", len(besties))
