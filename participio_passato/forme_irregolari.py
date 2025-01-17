import random
import os

FILE_NAME = "saved/participio_passato_forme_irregolari_wrong_answers.txt"

def load_wrong_answers():
    """Load previously saved wrong answers from a file into a set."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return set(line.strip() for line in file)
    return set()

def save_wrong_answers(wrong_answers):
    """Save the set of wrong answers to a file."""
    with open(FILE_NAME, "w") as file:
        for verb in wrong_answers:
            file.write(f"{verb}\n")

# Dictionary of verbs and their participles
all_verbs = {
    "fare": "fatto",
    "dire": "detto",
    "leggere": "letto",
    "correggere": "corretto",
    "scrivere": "scritto",
    "friggere": "fritto",
    "rompere": "rotto",
    "cuocere": "cotto",
    "tradurre": "tradotto",
    "aprire": "aperto",
    "offrire": "offerto",
    "soffrire": "sofferto",
    "coprire": "coperto",
    "scoprire": "scoperto",
    "morire": "morto",
    "accorgersi": "accorto",
    "piangere": "pianto",
    "spegnere": "spento",
    "spingere": "spinto",
    "vincere": "vinto",
    "aggiungere": "aggiunto",
    "dipingere": "dipinto",
    "assumere": "assunto",
    "accendere": "acceso",
    "spendere": "speso",
    "scendere": "sceso",
    "offendere": "offeso",
    "prendere": "preso",
    "rendere": "reso",
    "decidere": "deciso",
    "uccidere": "ucciso",
    "ridere": "riso",
    "dividere": "diviso",
    "chiudere": "chiuso",
    "concludere": "concluso",
    "diffondere": "diffuso",
    "rimanere": "rimasto",
    "chiedere": "chiesto",
    "rispondere": "risposto",
    "comporre": "composto",
    "proporre": "proposto",
    "disporre": "disposto",
    "vedere": "visto",
    "perdere": "perso",
    "correre": "corso",
    "scegliere": "scelto",
    "togliere": "tolto",
    "raccogliere": "raccolto",
    "sciogliere": "sciolto",
    "risolvere": "risolto",
    "rivolgersi": "rivolto",
    "mettere": "messo",
    "succedere": "successo",
    "permettere": "permesso",
    "esprimere": "espresso",
    "muovere": "mosso",
    "discutere": "discusso",
}

def version_complete():
    wrong_answers = load_wrong_answers()  # Load mistakes from the file
    main(all_verbs, wrong_answers)

def version_reinforcement():
    wrong_answers = load_wrong_answers()  # Load mistakes from the file

    if len(wrong_answers) == 0:
        print("Non ci sono errori precedenti. Avvio della modalità normale.")
        version_complete()
        return
    
    filtered_verbs = {key: all_verbs[key] for key in wrong_answers if key in all_verbs}
    main(filtered_verbs, wrong_answers)

def main(verbs, wrong_answers):
    print("="*100)
    print("\nBenvenuto! Inserisci il participio corretto per ogni verbo. Digita '0' per uscire.")
    
    while True:
        # Select a random verb
        verb = random.choice(list(verbs.keys()))
        participio_corretto = verbs[verb]

        # Prompt user for input
        risposta = input(f"\nParticipio del verbo '{verb}': ")

        # Check if the user wants to exit
        if risposta == "0":
            print("Arrivederci! Salvando le risposte sbagliate...")
            save_wrong_answers(wrong_answers)  # Save wrong answers to the file
            break

        # Check the answer
        if risposta == participio_corretto:
            print("\tCorretto! 🎉")
            wrong_answers.discard(verb)
        else:
            print(f"\tSbagliato. La risposta corretta è: {participio_corretto}")
            wrong_answers.add(verb)  # Add the incorrect verb to the set


if __name__ == "__main__":
    version_complete()
