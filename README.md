# quiz_stadt-land-fluss
Simple quiz in German to ask for e.g. European cities, their rivers and their countries (single choice from 3 options). It was programmed in python 3.13 as part of a course to practice GUI implementation with tkinter, threading and filedialog handling.

To start the app, it asks for a question file to be uploaded and directly starts with the randomly picked first question. As soon as the user chooses one of the 3 possible answers (radiobuttons), the answer is evaluated and either it says "Super, the answer '(chosen answer)' is correct" or it says "Wrong, the correct answer is: ...". The timer to answer each question is set to 30 secs, afterwards the correct answer is presented. Clicking the button "Nächste Frage" presents the next queston. The results (question, correct answer, chosen answer) can be saved as a json file ("Ergebnisse speichern") and reloaded to show in a frame below ("Ergebnisse anzeigen"). "Beenden" closes the app with optionally saving results first. 

To test the quiz, the JSON-file *'quizfragen_stadt-land-fluss.json'* was provided, which contains 15 questions about cities in Europe, given their river or vice versa, or their countries (generated with chatGPT). 
Nevertheless, the app can be used with any question template, if the questions are single choice from 3 options and the JSON-file follows this "dictionary" format: 

[{"frage": "...", "antworten": ["A: ...", "B: ...", "C: ..."],"richtig": "A"}, {...}] 

"frage" = question as string, "antworten" = 3 possible answers for A, B, C as string, "richtig" = correkt answer (only capital letter "A" or "B" or "C"). 

If you have any questions or recommendations to improvethe quiz app - please share. Otherwise enjoy testing your geography or whatever knowledge :)

![screenshot_quiz_app](https://github.com/user-attachments/assets/d857ea18-2f7a-4062-b268-673b289e53d2)

____________
*German version:*

Einfaches Quiz mit jeweils 3 vorgegebenen Antwortmöglichkeiten, von denen nur 1 korrekt ist. Es wurde im Rahmen eines Kurses in Python 3.13 programmiert, um grafische Benutzeroberflächen (GUI), parallele Abläufe (Threads) und Datei-Benutzung (filedialog) zu üben.

Beim starten der App mit "Los geht's" wird nach einer JSON-Datei gefragt, aus der Quizfragen geladen werden können. Wird eine valide Datei bereitgestellt, beginnt das Quiz direkt mit der ersten, zufällig gewählten Frage. Sobald eine der 3 Antwortmöglichkeiten ausgewählt wird, wertet das Programm die Antwort aus und gibt eine Rückmeldung, ob dies richtig oder falsch ist sowie die richtige Antwortoption. Der Countdown oben rechts ist für jede Frage auf 30 Sekunden eingestellt und wenn die Zeit abgelaufen ist, wird die korrekte Antwort präsentiert. Die Ergebnisse (Frage, richtige Antwort, gewählte Antwort) können über Funktionsfelder als JSON-Datei gespeichert und in einem Fenster angezeigt werden. "Beenden" bietet ebenfalls an, die Ergebnisse (falls vorhanden) vom dem Schließen zu speichern.

Zum Testen des Quizzes wurde die JSON-Datei *'quizfragen_stadt-land-fluss.json'* mitgegeben, die 15 Fragen über Städte, ihre Flüsse und Länder enthält (erstellt mit chatGPT), z.B. An welchem Fluss liegt die Stadt Prag? - A: Rhein, B: Moldau, C: Donau - richtige Antwort: B.
Theoretisch kann das Quiz jedoch mit jeder anderen Fragen-Datei bespielt werden, wenn es sich um "1-aus-3-Fragen" handelt und die JSON-Datei das folgende Format einhält: 

[{"frage": "...", "antworten": ["A: ...", "B: ...", "C: ..."],"richtig": "A"}, {...}]

Bei Fragen oder Verbesserungsvorschlägen gerne melden - ansonsten viel Spaß beim Testen deiner Geografie oder sonstiger Kenntnisse :)

