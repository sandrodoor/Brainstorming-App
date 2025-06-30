# Progetto personale relativo al corso Agenti Intelligenti e Machine Learning by Aitho, UNICT 2024/2025


# Brainstorming AI Interattivo

Questa applicazione, realizzata in vibe coding grazie a Gemini 2.5 flash, ti permette di fare brainstorming su un problema o un'idea con un gruppo di agenti AI che possiedono diverse personalità: il Visionario, il Critico e il Pragmatico. Un Supervisore coordina il loro lavoro, guidando la discussione attraverso un ciclo di turni per ciascuna idea.

## Come Funziona

L'applicazione segue un flusso conversazionale intuitivo:

1. Tu inserisci un'idea o un problema.
2. Il Visionario propone idee creative e fuori dagli schemi.
3. Il Critico analizza le implicazioni e le criticità dell'idea.
4. Il Pragmatico sintetizza e offre soluzioni concrete e attuabili.

Il ciclo si ripete per ogni tua nuova idea.

Quando digiti "esci", la sessione di brainstorming termina.

## Requisiti

- Python 3.9+
- Una chiave API Google Gemini

## Setup del Progetto

### 1. Clona il repository

```bash
git clone <url_del_tuo_repository>
cd <nome_della_directory>
```

### 2. Crea un ambiente virtuale

È buona pratica creare un ambiente virtuale per gestire le dipendenze del progetto in modo isolato.

#### Windows

```bash
python -m venv venv
```

Per creare un ambiente virtuale su macOS o Linux:

```bash
python3 -m venv venv
```

### 3. Accedere all'Ambiente Virtuale

Dopo aver creato l'ambiente virtuale, devi attivarlo in base al sistema operativo e alla shell che stai usando.

#### Windows (CMD)

```bash
.\venv\Scripts\activate
```
#### Windows (PowerShell)
```PowerShell
.\venv\Scripts\Activate.ps1
```

#### MacOS/Linux/WSL
```bash
source venv/bin/activate
```

### 4. Installare le Dipendenze

Con l'ambiente virtuale attivo, puoi installare tutte le librerie richieste per il progetto usando `pip` e il file `requirements.txt`.

Esegui il comando:

```bash
pip install -r requirements.txt
```


### 5. Configurare la `GOOGLE_API_KEY`

L'applicazione richiede una chiave API di **Google Gemini** per poter generare idee attraverso il modello LLM.

#### 🔑 Come ottenere la chiave API

1. Vai su [Google AI Studio](https://makersuite.google.com/app).
2. Accedi con il tuo account Google.
3. Crea una nuova chiave API dalla sezione delle impostazioni (API Key).
4. Copia la chiave generata.

#### 📁 Inserire la chiave API nel progetto

1. Nella root del progetto, crea un file chiamato `.env` (se non esiste già).
2. Aggiungi al file questa riga, sostituendo `la_tua_chiave_api_qui` con la tua vera chiave:

```dotenv
GOOGLE_API_KEY="la_tua_chiave_api_qui"
```
3.Salva il file.

4. Non condividere mai questo file pubblicamente o su GitHub senza proteggerlo.


### 6. Eseguire l'Applicazione

Con tutte le configurazioni pronte e l'ambiente virtuale attivo, puoi avviare il sistema di brainstorming AI multi-agente.

Esegui il comando:

```bash
python brainstorming.py
```

### 7. Terminare la Sessione e Visualizzare il Risultato Finale

Durante la sessione di brainstorming, puoi digitare `stop` per terminare la discussione e ricevere un riepilogo finale delle idee e delle valutazioni generate dagli agenti.


