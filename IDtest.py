#testing for identification input
while(1):
    identifier = input("Scan your identifier\n")
    print("what you scanned: " + identifier + "\n")
    interpretedID  = identifier.split('%n')
    print("What I interpreted: ")
    print ("Email: " + interpretedID[0])
    print ("Password: " + interpretedID[1])
    print("\n")
