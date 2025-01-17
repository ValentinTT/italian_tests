import participio_passato.forme_irregolari as pp_fi

if __name__ == "__main__":
    print("Benvenuto! Digita '0' per uscire.")

    choice = None
    while choice != "0":
        print("*"*100)
        print("""
1. Participio passato - forme irregolari.
2. Participio passato - forme irregolari (only wrongs).
0. Uscire.""")
        choice = input("Scegli: ")

        if choice == "1":
            print()
            pp_fi.version_complete()
        elif choice == "2":
            print()
            pp_fi.version_reinforcement()