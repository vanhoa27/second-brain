## intuitive Tipps fuer die Klausur
- Widerspruchbeweise und Kontraposition
- NTM darf man nicht einfach umdrehen 
- in der Klausur versuchen eine Reduktion anzugeben
	- sagen f ist total und berechenbar
## Polynomzeitreduktion
Ich schreib nochmal nen kleinen recap zu (polynomzeit)reduktionen, vielleicht hilft es jemanden. Zunächst nochmal als Erinnerung: "Probleme" sind erstmal einfach nur Sprachen, also Mengen an Wörtern über einem Alphabet. Für eine Reduktion A <= B wollen wir jetzt folgendes:

- eine Funktion die für alle Wörter über dem Alphabet von A definiert ist und auf Wörter über dem Alphabet von B abbildet (in der Praxis sind diese Alphabete oft einfach {0,1}, womit wir alles mögliche kodieren)
- wenn die Eingabe der Funktion ein Wort ist, das in A ist, soll die Ausgabe ein Wort in B sein
- wenn die Funktion einen Output gibt, der in B ist, soll die Eingabe auch in A gewesen sein

Wenn diese Funktion nun auch in polynomzeit berechenbar ist, gilt A <=p B. Wie zeigt man die Korrektheit? Dafür müssen wir die oben beschriebene Eigenschaft zeigen, dass w in A <=> f(w) in B. Dafür gibt es iA 2 Möglichkeiten:

1. Man zeigt die Implikationen w in A => f(w) in B, f(w) in B => w in A
2. Man zeigt die Implikationen w in A => f(w) in B, w not in A => f(w) not in B

Das ist logisch äquivalent, man kann also schauen, was sich eher anbietet. Man geht dann so vor, dass man bei den graphenproblemen erstmal definitionen anwendet, also "w ist per Annahme in A, also gilt/existiert Menge X sodass ...." und dann kommt irgendwann der Schritt wo man "die Idee" der Reduktion formalisieren muss um abzuleiten, dass f(w) in A. Bei der anderen Richtung dann das gleiche. Was bringt uns das? Wenn A <=p B und B in polynomzeit entscheidbar ist, können wir auch A in poly. Zeit entscheiden, indem wir unsere Eingabe (für welche wir schauen wollen, ob sie in A ist) in die Reduktionsfunktion packen (läuft in polyzeit) und dann schauen ob die Ausgabe in B ist (geht per Annahme in polyzeit). Wenn der Output in B ist, wissen wir, dank der oben beschriebenen Eigenschaft, dass die Eingabe auch in A war. Wenn nicht, dann wars nicht in A. Könnte man also für ein Problem A aus P zeigen, dass SAT <=p A, dann wäre plötzlich SAT in polyzeit entscheidbar. Da <=p transitiv ist würde das dann für alle Sprachen in NP gelten, also P=NP.

## Notes
- [[BekoKlausuer.excalidraw | Üben]] 