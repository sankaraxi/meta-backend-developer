with open("newly_created_file.txt", 'w') as file:
    file.write("This is a new file created by Python.")

    file.writelines(["\n", "This is the second line of the file.", "\n", "This is the third line of the file.", "\n", "This is the fourth line of the file."])

with open("newly_created_file.txt", 'a') as file:
    file.write("\nThis is the fifth line appended by python.")