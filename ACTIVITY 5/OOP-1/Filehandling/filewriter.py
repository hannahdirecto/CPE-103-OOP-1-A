#filewriter
name = "Royce Chua"
file = open ("newfile1.txt", 'w')
file.write (f"Hello, {name}!\n")
file.write ("Isn't this amazing!\n")
file.write ("that we can create and write on text files\n")
file.write ("using python.")
file.close

name = "Royce Chua"
file = open("newfile2.txt", 'w')
file.write("This message was created using Python!\n")
file.close()
