def add_note():
    note = input("Write your note: ")

    # Open the file in append mode ("a") so new notes are added each time
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("Your note has been saved.")


# -------------------------
# Run the function
# -------------------------

add_note()