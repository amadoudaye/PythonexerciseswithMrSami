def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(s1) == sorted(s2)

print(are_anagrams("Listen", "Silent"))