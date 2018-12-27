vowels = ("a","e","i","o","u")

message = input("Enter mesage: ")

new_message = ""

for letters in message:
    if letters not in vowels:
        new_message = new_message+letters

print("message without vowels: {}".format(new_message))