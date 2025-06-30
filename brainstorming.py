import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from langgraph.checkpoint.memory import InMemorySaver
# Importa i tipi di messaggio necessari da langchain_core.messages
from langchain_core.messages import HumanMessage, AIMessage

from utils import print_messages # Assicurati che utils.py sia nella stessa directory

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Recupera la chiave API di Google
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Assicurati che la chiave API sia stata caricata correttamente
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY non trovata nel file .env. Assicurati di averla configurata correttamente.")

# Inizializza il modello LLM
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 1. Agente Visionario
visionary_agent = create_react_agent(
    model=model,
    tools=[], # Non useranno strumenti per questo brainstorming iniziale
    prompt="Sei l'agente visionario. Cerchi di offrire risposte fuori dagli schemi alle richieste dell'utente.",
    name="Visionary"
)

# 2. Agente Critico
critical_agent = create_react_agent(
    model=model,
    tools=[],
    prompt="Sei l'agente critico. Analizzi con attenzione tutte le implicazioni di una determinata soluzione.",
    name="Critical"
)

# 3. Agente Pragmatico
pragmatic_agent = create_react_agent(
    model=model,
    tools=[],
    prompt="Sei l'agente pragmatico. Eviti lunghi giri di parole e cerchi di offrire soluzioni sintetiche e concrete.",
    name="Pragmatic"
)

print("Agenti Visionario, Critico e Pragmatico creati con successo con i parametri corretti!")

supervisor_prompt = (
     "Sei il supervisore di un team di brainstorming composto da un Visionario, un Critico e un Pragmatico.\n"
    "Il tuo compito è guidare la conversazione attraverso un ciclo fisso di 3 fasi per ogni nuova idea utente:\n"
    "1. **Generazione Visionaria**: Il Visionario genera idee creative e fuori dagli schemi.\n"
    "2. **Analisi Critica**: Il Critico analizza in dettaglio le implicazioni e le criticità dell'idea visionaria.\n"
    "3. **Soluzione Pragmatica**: Il Pragmatico sintetizza e propone soluzioni concrete e attuabili basate sull'analisi precedente.\n\n"
    "Regole di transizione:\n"
    "**Inizia sempre** passando la richiesta iniziale dell'utente al **Visionario**.\n"
    "**Dopo la risposta del Visionario**, passa sempre il compito al **Critico** per una valutazione approfondita dell'idea appena generata dal Visionario.\n"
    "**Dopo l'analisi del Critico**, passa sempre il compito al **Pragmatico** per convertire le idee e le critiche in soluzioni concrete e attuabili.\n"
    "**Dopo la risposta del Pragmatico**, se il brainstorming per questa specifica idea è concluso, valuta se puoi dare una sintesi all'utente. Altrimenti, se ritieni sia necessario, puoi chiedere di ripassare al Visionario per un'ulteriore iterazione sull'idea, o terminare il flusso per l'idea corrente se non c'è altro da aggiungere.\n"
    "Quando l'utente chiede esplicitamente di 'stop', il tuo compito è fornire una valutazione finale complessiva di tutti i brainstorming precedenti."
)

# Lista degli agenti (le variabili stesse)
members = [visionary_agent, critical_agent, pragmatic_agent]

supervisor = create_supervisor(
    members, # Lista di oggetti agente
    model=model,
    prompt=supervisor_prompt,
)

print("Supervisore creato con successo con la lista corretta degli oggetti agente!")

# Crea un checkpointer in memoria
checkpointer = InMemorySaver()

# Compila il grafo del supervisore
app = supervisor.compile(checkpointer=checkpointer)

print("Checkpointer creato e grafo compilato con successo!")

# Definisci la configurazione per la conversazione, inclusivo del thread ID
config = {"configurable": {"thread_id": "brainstorm_session_1"}}

print("Variabile 'config' con thread ID definita!")

print("Benvenuto nell'app di brainstorming AI interattiva!")
print("Descrivi il problema o l'idea su cui vuoi fare brainstorming.")
print("Per terminare la sessione e ottenere una valutazione finale, digita 'stop'.")

# Inizializza la cronologia dei messaggi come una lista vuota di oggetti BaseMessage
# LangGraph gestisce lo stato interno, noi daremo l'input iniziale come HumanMessage
# e il checkpointer salverà lo stato completo che conterrà tutti gli AIMessage.
# Quindi, la nostra variabile 'messages' locale non sarà più la storia completa,
# ma solo l'input per il turno corrente.

while True:
    user_input = input("\nLa tua idea o problema (o 'stop' per terminare): ")
    
    if user_input.lower() == 'stop':
        print("\nSessione di brainstorming terminata. Sto generando la valutazione finale...")
        
        # Creiamo un HumanMessage specifico per la richiesta di sintesi finale
        final_message = HumanMessage(content="Il brainstorming è concluso. Fornisci una sintesi finale e una valutazione complessiva.")
        
        # Invochiamo il grafo con questo messaggio. Il grafo ha il contesto dal checkpointer.
        # LangGraph si aspetta che l'input al grafo sia un dizionario con la chiave 'messages'
        # e il valore sia una lista di messaggi.
        for s in app.stream({"messages": [final_message]}, config=config):
            if "__end__" not in s:
                # print_messages(s) # Puoi scommentare per vedere tutti gli stati intermedi
                # Cerchiamo il risultato finale del supervisore
                for key, value in s.items():
                    if key == "supervisor" and "messages" in value and value["messages"]:
                        # Il messaggio finale del supervisore è l'ultimo della sua lista
                        final_response_content = value["messages"][-1].content
                        print(f"\n[Supervisore - Valutazione Finale]: {final_response_content}")
                        break # Una volta trovata la risposta del supervisore, usciamo
            else: # Se lo stato è "__end__", significa che il supervisore ha terminato il suo lavoro
                # A questo punto, il checkpointer dovrebbe avere lo stato finale salvato
                pass # Non facciamo nulla qui, la stampa è già stata gestita sopra

        break # Esci dal ciclo principale dopo la sintesi finale
    
    # Prepara l'input dell'utente come HumanMessage per il grafo
    input_message = HumanMessage(content=user_input)

    print("\n--- Inizio Turno ---")
    
    # Invocazione del grafo e streaming delle risposte
    # Il grafo riceve l'input dell'utente e recupera la cronologia dal checkpointer
    # usando il 'config' thread_id.
    
    current_state_output = None
    for s in app.stream({"messages": [input_message]}, config=config):
        # s è l'intero stato del grafo in quel momento,
        # che include la chiave 'messages' aggiornata.
        
        # Utilizza print_messages per visualizzare l'intero stato del grafo,
        # che include i messaggi aggiornati ad ogni passo del turno.
        # Per evitare output troppo verbosi, potresti voler chiamare print_messages
        # solo alla fine di un "turno logico" completo, non ad ogni micro-passaggio.

        # Per il nostro scopo di mostrare l'output di ogni agente,
        # estraiamo il messaggio dell'agente attivo come facevi tu:
        if "__end__" not in s:
            for agent_name, state in s.items():
                # Evitiamo di stampare lo stato del supervisore qui, a meno che non sia l'unico a parlare
                if agent_name != "supervisor" and "messages" in state and state["messages"]:
                    # Il messaggio più recente dell'agente è l'ultimo nella lista
                    agent_response = state["messages"][-1]
                    # 'agent_response' è già un AIMessage, puoi usarlo direttamente per la stampa
                    # o continuare a estrarre il contenuto come facevi per compatibilità visiva
                    print(f"\n[{agent_name}]: {agent_response.content}")
                    # Non è necessario aggiungere a 'messages' locale, il checkpointer lo fa per noi.
                    break # Presupponiamo un solo agente attivo per output per ciclo di stream
        else:
            # Questo blocco viene raggiunto quando il grafo ha completato una sequenza e
            # il supervisore ha deciso il prossimo stato o la terminazione.
            # Qui potremmo volere la stampa completa della cronologia.
            # Ottieni lo stato finale di questo ciclo dal checkpointer per la stampa completa
            # Nota: accedere al checkpointer direttamente qui potrebbe non essere ideale
            # in un ambiente di stream.
            pass
            
    print("--- Fine Turno ---")
    
    # Alla fine di ogni turno, dopo che il grafo ha completato la sua esecuzione
    # per quell'input, possiamo stampare la cronologia completa dallo stato aggiornato.
    # Per fare questo, dobbiamo recuperare lo stato corrente dal checkpointer.
    # Questo è un po' più complesso con stream() poiché lo stato non è 'fermo' fino alla fine del stream.
    # Per ora, la stampa di ogni agente dentro il loop for s in app.stream è sufficiente.
    # Se volessi la stampa finale completa, potresti dover invocare app.get_state(config) dopo il loop.
    
    # Esempio (per debug, scommenta se vuoi vedere lo stato completo dopo ogni turno)
    # current_thread_state = app.get_state(config)
    # print_messages(current_thread_state.values) # .values per accedere al dizionario dello stato

print("\nGrazie per aver usato l'app di brainstorming!")

# Alla fine dell'intera sessione (dopo 'stop'), puoi chiamare print_messages
# per visualizzare la cronologia completa e finale del thread.
# Recupera lo stato finale dal checkpointer
final_thread_state = app.get_state(config)
print_messages(final_thread_state.values) # Passa il dizionario dello stato a print_messages