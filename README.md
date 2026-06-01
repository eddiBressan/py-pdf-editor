# py-pdf-editor

Un tool Python minimale, leggero e nativo per Linux pensato per fare due cose sacrosante sui PDF (unire e dividere) senza portarsi dietro dipendenze mastodontiche o interfacce web gonfie di JavaScript.

La particolarità? È strutturato in modo totalmente modulare: separa nettamente il motore logico dalle interfacce. Questo significa che puoi usarlo al volo da terminale (stile utility nativa Linux) o lanciare la GUI classica se preferisci il punta-e-clicca.

## 🛠️ Com'è strutturato il codice

Invece del classico "file unico" caotico, il progetto è diviso in tre componenti con responsabilità separate, ottimo se vuoi giocarci, estenderlo o fare refactoring:

* `pdf_engine.py`: Il cuore pulsante. Gestisce la manipolazione reale dei file (sfruttando `pypdf`) e integra una serie di validazioni preventive sui path per evitare brutte sorprese.
* `gui.py`: L'interfaccia grafica nativa in Tkinter, ridotta all'osso e senza fronzoli.
* `main.py`: Il regista del tool. Se gli passi degli argomenti agisce da CLI, altrimenti si accorge che non c'è input e tira su la GUI caricando Tkinter in modo dinamico.

## ✨ Le chicche tecniche (Safety First)

Anche se è un progetto leggero, non è stato trascurato l'aspetto della robustezza:
* **Anti-Data-Loss:** Se provi a fare un'estrazione impostando come output lo stesso nome del file di input, il motore intercetta il conflitto e si blocca *prima* di aprire lo stream di scrittura, salvando il file originale dall'azzeramento (0 byte).
* **Parsing dell'intervallo resiliente:** La stringa dell'intervallo viene ripulita preventivamente dagli spazi bianchi (es. `" 3 - 10 "` diventa `"3-10"`), digerendo sia notazioni classiche che pagine singole.
* **Validazione preventiva:** Controlla l'esistenza dei file, i permessi di scrittura sulla cartella di destinazione e la reale lunghezza del PDF prima di iniziare i cicli di copia delle pagine.

## 🚀 Quick Start

### 1. Clona e prepara l'ambiente
Niente installazioni globali "sporche" nel sistema. Creiamo un ambiente virtuale isolato:

```bash
git clone [https://github.com/tuo-username/py-pdf-editor.git](https://github.com/tuo-username/py-pdf-editor.git)
cd py-pdf-editor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt