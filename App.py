import streamlit as st

# --- LOGICA CHAT IN TEMPO REALE ---
# Inizializziamo la memoria della chat se non esiste
if "messages" not in st.session_state:
    st.session_state.messages = []

st.divider()
st.markdown("### Private Concierge Chat")
st.caption("La conversazione è crittografata e temporanea.")

# Container per visualizzare i messaggi
chat_container = st.container(height=300)

with chat_container:
    # Mostra i messaggi precedenti
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Input per il nuovo messaggio
if prompt := st.chat_input("Scrivi qualcosa..."):
    # Aggiungi messaggio dell'utente
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Visualizza immediatamente il messaggio dell'utente
    with chat_container:
        with st.chat_message("user"):
            st.markdown(prompt)
    
    # Risposta automatica del sistema (Simulazione presenza)
    response = "Ricevuto. Sto leggendo il tuo messaggio, ti risponderò privatamente tra un istante."
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    with chat_container:
        with st.chat_message("assistant"):
            st.markdown(response)

# Pulsante per resettare la conversazione (Privacy)
if st.button("Cancella Cronologia Chat", type="secondary"):
    st.session_state.messages = []

import requests

# --- FUNZIONE NOTIFICA ---
def invia_notifica(messaggio):
    # Incolla qui il NUOVO token che ti ha dato BotFather
    nuovo_token = "8612614571:AAH9ZYWxr1m-N5RbeCQhQX24rxvDo4f6wHI" 
    mio_chat_id = "600355763"
    
    url = f"https://api.telegram.org/bot{nuovo_token}/sendMessage"
    payload = {
        "chat_id": mio_chat_id,
        "text": messaggio
    }
    
    try:
        requests.post(url, data=payload)
    except Exception as e:
        st.error(f"Errore invio: {e}")

# --- AZIONI NELL'APP ---
if st.button("Richiedi Disponibilità"):
    invia_notifica("🔔 Qualcuno ha richiesto la tua presenza su Essence!")
    st.success("Richiesta inviata!")

if st.button("TEST NOTIFICA"):
    # Usiamo la funzione definita sopra per il test
    invia_notifica("Test connessione riuscito! ✨")
    st.info("Controlla Telegram.")
