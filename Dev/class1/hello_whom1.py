import sys

cmd_list = sys.argv

counter = 0

for element in cmd_list:
    print("["+ str(counter)+"]["+element +"]")
    counter = counter + 1

print("\n")
print("Hello "+ cmd_list[1]+"!\n")