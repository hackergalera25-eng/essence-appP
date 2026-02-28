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

# Funzione per inviare la notifica
def invia_notifica(testo):
    # INCOLLA QUI IL NUOVO TOKEN
    token_nuovo = "https://core.telegram.org/bots/inline"
    mio_id = "600355763"
    
    url = f"https://api.telegram.org/bot{token_nuovo}/sendMessage"
    payload = {"chat_id": mio_id, "text": testo}
    
    try:
        requests.post(url, data=payload)
    except Exception as e:
        st.error(f"Errore: {e}")

# Pulsante per i clienti
if st.button("Richiedi Disponibilità"):
    invia_notifica("🔔 Qualcuno ha richiesto la tua compagnia su Essence!")
    st.success("Richiesta inviata!")

# Pulsante di TEST (Semplificato)
if st.button("TEST NOTIFICA"):
    invia_notifica("Test connessione riuscito! ✨")
    st.info("Controlla Telegram.")
