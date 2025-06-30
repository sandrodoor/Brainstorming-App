# utils.py

def print_messages(state):
    """
    Stampa una lista di messaggi in un formato leggibile,
    estraendo tipo, nome dell'agente e contenuto.
    Accetta lo 'state' del grafo che contiene una chiave 'messages'.
    """
    print("\n" + "="*60)
    print("                --- Cronologia Messaggi del Grafo ---")
    print("="*60 + "\n")

    # Assicurati che 'state' contenga la chiave 'messages' e che sia una lista
    if "messages" in state and isinstance(state["messages"], list):
        for msg in state["messages"]:
            # LangChain messages are typically instances of HumanMessage, AIMessage, etc.
            # They have a .type and .content attribute. Some might have a .name attribute.
            
            msg_type = msg.type # e.g., 'human', 'ai'
            
            # Check if the message object has a 'name' attribute
            # For HumanMessage, name is often None unless explicitly set.
            # For AIMessage from agents, 'name' should correspond to the agent's name.
            msg_name = getattr(msg, "name", None) 
            
            content = msg.content

            # If the content is structured (e.g., a list of dicts for multimodal output),
            # extract only the text parts.
            if isinstance(content, list):
                extracted_text = "\n".join(
                    block.get("text", "") 
                    for block in content 
                    if isinstance(block, dict) and block.get("type") == "text"
                )
            else:
                extracted_text = content
            
            # Determine the display name
            display_name = f"[{msg_name.capitalize()}]" if msg_name else f"[{msg_type.capitalize()}]"

            print(f"{display_name}:\n{extracted_text}\n{'-'*60}")
    else:
        print("Nessun messaggio trovato nello stato fornito o formato non valido.")
    
    print("\n" + "="*60)
    print("              --- Fine Cronologia Messaggi del Grafo ---")
    print("="*60 + "\n")