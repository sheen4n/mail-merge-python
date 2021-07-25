# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as template_file:
    template_file_content = template_file.read()

with open("./Input/Names/invited_names.txt") as invited_names_file:
    invited_names_list = invited_names_file.readlines()

for name in invited_names_list:
    updated_content = template_file_content.replace("[name]", name.replace('\n', ''))
    with open(f"./Output/ReadyToSend/Invitation-{name.replace(' ','_').strip()}.txt", mode="w") as invite:
        invite.write(updated_content)
