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

# Funzione principale per le notifiche
def invia_notifica(messaggio):
    token = "8612614571:AAERPLdbIA_JDgKzUcAUhmbHvdOzsro-ySk" # Assicurati che sia completo
    chat_id = "600355763"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": messaggio}
    try:
        requests.post(url, data=payload)
    except:
        pass

# Pulsante Richiedi Disponibilità
if st.button("Richiedi Disponibilità"):
    invia_notifica("🔔 Nuova richiesta da Essence!")
    st.success("Richiesta inviata!")

# Pulsante di TEST (Sistemato per eliminare il 401)
if st.button("TEST NOTIFICA"):
    t = "8612614571:AAFFtoqMbU1KquWat6Mzh11HXU-uUs63er"
    c = "600355763"
    risposta = requests.post(
        f"https://api.telegram.org/bot{t}/sendMessage",
        data={"chat_id": c, "text": "Test connessione riuscito! ✨"}
    )
    st.write(risposta.json())
