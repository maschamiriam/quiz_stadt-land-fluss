### Quiz: Stadt-Land-Fluss

''' Aufgabe: Entwickle eine Python-Anwendung mit Tkinter für ein einfaches Quiz mit Fragen und mehreren Antwortmöglichkeiten über Radiobuttons. 
    Die Anwendung soll Ergebnisse in einer Datei speichern und frühere Ergebnisse laden sowie Threads für Timer nutzen, um die GUI reaktionsfähig zu halten.
    
    Dateiname: 'quizz_app_stadt-land-fluss.py'
              - Bitte lade die Datei 'quizfragen_stadt-land-fluss.json' für die Quizfragen oder erstelle eine eigene JSON-Datei nach vorgegebenem Muster:
              [{"frage": "An welchem Fluss liegt die Stadt Prag?", "antworten": ["A: Rhein", "B: Moldau", "C: Donau"],"richtig": "B"}, {...})
                
    Autorin: Mascha Friedrich
    letzte Änderung: 24.05.2025
    '''

from tkinter import Tk, Label, Button, Radiobutton, filedialog, StringVar, Frame, Text, Scrollbar, W, NE, N, END, VERTICAL
from threading import Thread
import json
from random import choice
from time import sleep

# Globale Variablen
ergebnisse = []
antwort_gegeben = False
quizfragen = []
aktuelle_frage = None

# Funktions-Buttons
def lade_frage_antwort():
    global quizfragen
    path = filedialog.askopenfilename(filetypes=[("JSON Dateien", "*.json")])   # Dialogbox zur Auswahl einer JSON-Datei 
    if path:
        with open(path, "r", encoding='utf-8') as stream:                       # Quizfragen laden, z.B. quizfragen_MFriedrich.json
            quizfragen = json.load(stream)
            zeig_naechste_frage()                                               # Funktionsaufruf für erste Quizfrage

def zeig_naechste_frage():
    global aktuelle_frage, antwort_gegeben
    antwort_gegeben = False
    
    if quizfragen == []:                                                        # Falls zuerst auf "Nächste Frage" und nicht auf "Los geht's" geklickt wird
        lade_frage_antwort()

    elif start_button.winfo_exists():                                           # start_button wird bei der ersten Frage entfernt
        start_button.grid_forget()

    aktuelle_frage = choice(quizfragen)                                         # zufällige Auswahl einer Quizfrage

    fragenfeld.config(text=aktuelle_frage["frage"])                             # Ausspielen des Fragentexts im Fragen-Label
    auswahl.set(None)

    a.config(text=aktuelle_frage["antworten"][0], value="A", state="normal")    # Ausspielen der Antwortmöglichkeiten in die Radiobuttons
    b.config(text=aktuelle_frage["antworten"][1], value="B", state="normal")
    c.config(text=aktuelle_frage["antworten"][2], value="C", state="normal")
    antwortfeld.config(text="")

    countdown()                                                                 # startet den Countdown von 30sec 

def zeige_antwort(neue_frage):
    global antwort_gegeben
    if antwort_gegeben:
        return
    antwort_gegeben = True

    index_map = {"A": 0, "B": 1, "C": 2}                                        # Mapping von Buchstabe mit Text der richtigen und der gewählten Antwort 
    richtige_antwort = neue_frage["antworten"][index_map[neue_frage["richtig"]]]
    gewaehlte_antwort = neue_frage["antworten"][index_map[auswahl.get()]]

    if gewaehlte_antwort == richtige_antwort:                                   # Abgleich, ob richtige Auswahl getroffen wurde mit Antworten
        antwortfeld.config(text=f"✅ Super, '{richtige_antwort}' ist richtig.", bg="#76EE46")
    elif not gewaehlte_antwort:
        antwortfeld.config(text="⚠️ Bitte eine Antwort auswählen.", bg="#F3F5E9")
        return
    else:
        antwortfeld.config(text=f"❌ Falsch, richtig wäre: {richtige_antwort}",bg="#FD7A63")

    a.config(state="disabled")
    b.config(state="disabled")
    c.config(state="disabled")

    ergebnis = (neue_frage["frage"], richtige_antwort, gewaehlte_antwort)
    ergebnisse.append(ergebnis)

def ergebnis_speichern():
    save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if save_path:
        try:
            try:                                                  
                with open(save_path, 'r', encoding='utf-8') as f:               # Alte Datei laden (falls vorhanden)
                    alte_ergebnisse = json.load(f)
                    if not isinstance(alte_ergebnisse, list):
                        alte_ergebnisse = []
            except (FileNotFoundError, json.JSONDecodeError):
                alte_ergebnisse = []
            ergebnisse_gesamt = alte_ergebnisse + ergebnisse                    # Neue Ergebnisse anhängen
            
            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(ergebnisse_gesamt, f, ensure_ascii=False, indent=4)   # Datei speichern
            print("Ergebnisse erfolgreich gespeichert.")

        except Exception as e:
            print("Fehler beim Speichern:", e)
            
def zeige_ergebnisse():                                                         # zusätzlicher Funktionsbutton, um alte Ergebnisse anzuzeigen
    dateipfad = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not dateipfad:
        return
    try:
        with open(dateipfad, 'r', encoding='utf-8') as f:
            daten = json.load(f)
            if not isinstance(daten, list):
                daten = []
        for widget in fenster.grid_slaves():
            if int(widget.grid_info()["row"]) > 6:
                widget.destroy()

        frame = Frame(fenster)                                                  # Frame mit Scrollbar und Textfeld
        frame.grid(row=7, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

        scrollbar = Scrollbar(frame, orient=VERTICAL)
        textfeld = Text(frame, height=10, width=70, wrap="word", yscrollcommand=scrollbar.set, font=("Calibri", 11))
        scrollbar.config(command=textfeld.yview)

        scrollbar.pack(side="right", fill="y")
        textfeld.pack(side="left", fill="both", expand=True)

        for eintrag in daten:
            frage = eintrag[0]
            richtig = eintrag[1]
            ausgewaehlt = eintrag[2]
            korrekt = "✅" if richtig == ausgewaehlt else "❌"
            textfeld.insert(END, f"{korrekt} Frage: {frage}\n   Richtige Antwort: {richtig}\n   Deine Antwort: {ausgewaehlt}\n\n")        
                
                
    except Exception as e:
        print("Fehler beim Laden der Datei:", e)          

def countdown(sekunden=30):
    def aktualisiere_timer():
        nonlocal sekunden
        if antwort_gegeben:
            return
        if sekunden > 0:                                                        # zwischen 30 und 1 sec zeigt das Timer-Label die verbleibenden Sekunden an
            timer.config(text=f"{sekunden} sec")
            sekunden -= 1
            sleep(1)                                                            # 1 sec Abstand zwischen Countdown-Schritten
            aktualisiere_timer()
        else:
            timer.config(text="⏰ Zeit abgelaufen", bg="#FCA453")            # bei 0 sec zeigt es "Zeit abgelaufen an" und gibt die richtige Antwort aus
            zeige_antwort(aktuelle_frage)
    thread = Thread(target=aktualisiere_timer)
    thread.start()
    
def close_program():
    if ergebnisse != []:                                                        # Falls es Ergebnisse gibt, anbieten diese zu speichern
        ergebnis_speichern()
    fenster.destroy()                                                           # Hauptfenster schließen
    
# Hauptfenster
fenster = Tk()
fenster.title("Stadt-Land-Fluss-Quiz")
fenster.geometry("550x600")

# GUI-Elemente für Frage, Antwortmöglichkeiten, Antwort und Timer
auswahl = StringVar()
start_button = Button(master=fenster, font=('Calibri', 12), bg="#76EE46", text="Los geht's", command=lambda: lade_frage_antwort())
fragenfeld = Label(master=fenster, font=('Calibri', 14), text="Frage...")
a = Radiobutton(master=fenster, font=('Calibri', 14), text="", value="A", variable=auswahl, command=lambda: zeige_antwort(aktuelle_frage))
b = Radiobutton(master=fenster, font=('Calibri', 14), text="", value="B", variable=auswahl, command=lambda: zeige_antwort(aktuelle_frage))
c = Radiobutton(master=fenster, font=('Calibri', 14), text="", value="C", variable=auswahl, command=lambda: zeige_antwort(aktuelle_frage))
antwortfeld = Label(master=fenster, font=('Calibri', 14), text="")
timer = Label(master=fenster, font=('Calibri', 12), text="30sec", width=17, bg="#58DDF5")

# Buttons: Neue Frage & Speichern
button_functions = [("Nächste Frage", zeig_naechste_frage),("Ergebnisse speichern", ergebnis_speichern), ("Ergebnisse anzeigen", zeige_ergebnisse), ("Beenden", close_program)]
for col, (text, function) in enumerate(button_functions):
    button = Button(master=fenster, font=('Calibri', 12), text=text, command=function)
    button.grid(row=6, column=col, padx=10, pady=10, sticky=W)                              # Layout der 4 Funktions-Buttons
    
# Layout der anderen GUI-Elemente
start_button.grid(row=0, column=1, padx=10, pady=10, sticky=N)
fragenfeld.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky=W)
a.grid(row=2, column=1, padx=10, pady=10, sticky=W)
b.grid(row=3, column=1, padx=10, pady=10, sticky=W)
c.grid(row=4, column=1, padx=10, pady=10, sticky=W)
antwortfeld.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=W)
timer.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky=NE)

fenster.mainloop()