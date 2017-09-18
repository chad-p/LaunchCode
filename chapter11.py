def sort_contacts(contacts):
    new_list = []

    for k, [p, e] in sorted(contacts.items()):
        new_list.extend([(k, p, e)])

    return new_list

def main():
    sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
                   "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
                   "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")})


main()
