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

def invia_notifica(messaggio):
    token = "8612614571:AAFFtoqMbU1KquWat6Mzh1lHXU-uUs31dxY"
    chat_id = "600355763"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={messaggio}"
    requests.get(url)

# Nel punto in cui il cliente prenota o scrive:
if st.button("Richiedi Disponibilità"):
    invia_notifica(f"Nuova richiesta da Essence! Orario: {ora}")
    st.success("Richiesta inviata!")
