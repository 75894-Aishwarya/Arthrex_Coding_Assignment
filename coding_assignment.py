data = {
    'A': ['B', 'C', 'J'],
    'D': ['E', 'F', 'G'],
    'H': ['I', 'K', 'V'],
    'J': ['V'],
    'K': ['L', 'M', 'N', 'A'],
    'O': ['P', 'V', 'U'],
    'Q': ['S', 'T', 'D'],
    'U': ['H', 'J'],
    'V': ['W', 'X', 'Y', 'Z']
}

def get_contacts(person, contact=[]):
    if person not in contact:     # Check if the person is already in the contact list to avoid duplicates
        contact.append(person)
        if person in data:
            for friend in data[person]:
                get_contacts(friend, contact)
        else:
            for key, value in data.items():
                if person in value:
                    get_contacts(key, contact)

    return contact

input_person = input("Enter person's name to select for the job (letters from A-Z): ").upper()

contacted_candidates = get_contacts(input_person)

print(', '.join(contacted_candidates))