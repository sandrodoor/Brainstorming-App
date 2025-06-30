# 🧠 Brainstorming AI Interattivo

Questa applicazione ti permette di fare brainstorming su un problema o un'idea con un gruppo di agenti AI che possiedono diverse personalità: il **Visionario**, il **Critico** e il **Pragmatico**. Un **Supervisore** coordina il loro lavoro, guidando la discussione attraverso un ciclo di turni per ciascuna idea.

## 💡 Come Funziona

L'applicazione segue un flusso conversazionale intuitivo:

1.  Tu inserisci un'idea o un problema.

2.  Il **Visionario** propone idee creative e fuori dagli schemi.

3.  Il **Critico** analizza le implicazioni e le criticità dell'idea.

4.  Il **Pragmatico** sintetizza e offre soluzioni concrete e attuabili.

Il ciclo si ripete per ogni tua nuova idea.

Quando digiti `"esci"`, la sessione di brainstorming termina.

## 📋 Requisiti

Assicurati di avere **Python 3.9+** installato sul tuo sistema.

## 🚀 Setup del Progetto

Segui questi passaggi per configurare ed eseguire l'applicazione.

### 1. Clona il Repository (se applicabile) e Naviga nella Directory

Se hai ricevuto questi file in un repository Git, clonalo. Altrimenti, assicurati che tutti i file (`.env`, `requirements.txt`, `brainstorming.py`, `utils.py`)

```bash
git clone <url_del_tuo_repository>
cd <nome_della_directory>
```

###2. Creare un Ambiente Virtuale
È buona pratica creare un ambiente virtuale per gestire le dipendenze del progetto in modo isolato.

#Per Windows (CMD o PowerShell):
```bash
python -m venv venv
```

#Per macOS / Linux / PowerShell:
```bash
python3 -m venv venv
```
(Nota: python3 potrebbe essere necessario su alcuni sistemi Linux/macOS se python punta a Python 2).


###3. Accedere all'Ambiente Virtuale
Dopo aver creato l'ambiente virtuale, devi attivarlo.

#Per Windows (CMD):
```DOS
.\venv\Scripts\activate
```

#Per Windows (PowerShell):
```PowerShell
.\venv\Scripts\Activate.ps1
```

#Per macOS / Linux:
```Bash
source venv/bin/activate
```
Una volta attivato, vedrai (venv) apparire all'inizio della riga di comando, indicando che sei nell'ambiente virtuale.


###4. Installare le Dipendenze
Con l'ambiente virtuale attivo, installa tutte le librerie necessarie elencate nel file requirements.txt.

#Per tutti i sistemi (con ambiente virtuale attivo):
```Bash
pip install -r requirements.txt
```

###5. Configurare la GOOGLE_API_KEY
L'applicazione richiede una chiave API di Google Gemini per funzionare.

#Generare la Chiave API:

1. Vai alla Google AI Studio.

2. Accedi con il tuo account Google.

3. Crea una nuova chiave API.

###Salvare la Chiave API:

1.Nella directory del progetto, apri o crea un file chiamato .env.

2.Aggiungi la tua chiave API in questo formato (sostituisci la_tua_chiave_api_qui con la chiave effettiva):

```Plaintext
GOOGLE_API_KEY="la_tua_chiave_api_qui"
```
3.Salva il file .env.

###6. Eseguire l'Applicazione
Ora sei pronto per avviare il brainstorming!

Per tutti i sistemi (con ambiente virtuale attivo):
```Bash
python brainstorming.py
```




