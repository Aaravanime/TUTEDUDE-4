text = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data written to output.txt successfully.")
extra_text = input("Enter more text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(extra_text + "\n")
print("Additional data appended to output.txt successfully.")
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
