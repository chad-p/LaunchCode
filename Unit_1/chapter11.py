def sort_contacts(contacts):
    sorted_contacts = []

    for k, [p, e] in sorted(contacts.items()):
        sorted_contacts.extend([(k, p, e)])

    return sorted_contacts

def main():

    contacts = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
                "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
                "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}

    print(sort_contacts(contacts))


main()
