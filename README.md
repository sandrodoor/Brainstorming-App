Brainstorming AI Interattivo
Questa applicazione ti permette di fare brainstorming su un problema o un'idea con un gruppo di agenti AI che possiedono diverse personalità: il Visionario, il Critico e il Pragmatico. Un Supervisore coordina il loro lavoro, guidando la discussione attraverso un ciclo di 3 turni per ciascuna idea.

Come Funziona
L'applicazione segue un flusso conversazionale:

Tu inserisci un'idea o un problema.

Il Visionario propone idee creative e fuori dagli schemi.

Il Critico analizza le implicazioni e le criticità dell'idea.

Il Pragmatico sintetizza e offre soluzioni concrete e attuabili.

Il ciclo si ripete per ogni tua nuova idea.

Quando digiti "stop", il Supervisore fornisce una valutazione finale complessiva di tutti i brainstorming della sessione.

Requisiti
Assicurati di avere Python 3.9+ installato sul tuo sistema.

Setup del Progetto
Segui questi passaggi per configurare ed eseguire l'applicazione.

1. Clona il Repository (se applicabile) e Naviga nella Directory
Se hai ricevuto questi file in un repository Git, clonalo. Altrimenti, assicurati che tutti i file (.env, requirements.txt, brainstorming.py, utils.py) si trovino nella stessa directory.

Bash

# Esempio per clonare un repository (se applicabile)
git clone <url_del_tuo_repository>
cd <nome_della_directory>
2. Creare un Ambiente Virtuale
È buona pratica creare un ambiente virtuale per gestire le dipendenze del progetto in modo isolato.

Per Windows (CMD o PowerShell):

Bash

python -m venv venv
Per macOS / Linux / PowerShell:

Bash

python3 -m venv venv
(Nota: python3 potrebbe essere necessario su alcuni sistemi Linux/macOS se python punta a Python 2).

3. Accedere all'Ambiente Virtuale
Dopo aver creato l'ambiente virtuale, devi attivarlo.

Per Windows (CMD):

Bash

.\venv\Scripts\activate
Per Windows (PowerShell):

PowerShell

.\venv\Scripts\Activate.ps1
Per macOS / Linux:

Bash

source venv/bin/activate
Una volta attivato, vedrai (venv) apparire all'inizio della riga di comando, indicando che sei nell'ambiente virtuale.

4. Installare le Dipendenze
Con l'ambiente virtuale attivo, installa tutte le librerie necessarie elencate nel file requirements.txt.

Per tutti i sistemi (con ambiente virtuale attivo):

Bash

pip install -r requirements.txt
5. Configurare la GOOGLE_API_KEY
L'applicazione richiede una chiave API di Google Gemini per funzionare.

Generare la Chiave API:

Vai alla Google AI Studio.

Accedi con il tuo account Google.

Crea una nuova chiave API.

Salvare la Chiave API:

Nella directory del progetto, apri o crea un file chiamato .env.

Aggiungi la tua chiave API in questo formato (sostituisci la_tua_chiave_api_qui con la chiave effettiva):

GOOGLE_API_KEY="la_tua_chiave_api_qui"
Salva il file .env.

6. Eseguire l'Applicazione
Ora sei pronto per avviare il brainstorming!

Per tutti i sistemi (con ambiente virtuale attivo):

Bash

python brainstorming.py
L'applicazione si avvierà e ti chiederà di inserire la tua idea o problema.
