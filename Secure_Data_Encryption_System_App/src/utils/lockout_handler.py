# src/utils/lockout_handler.py

import time
import streamlit as st

LOCKOUT_DURATION = 10  # seconds
MAX_ATTEMPTS = 3

def handle_lockout():
    """Checks if user is under lockout and handles countdown + reset."""
    if st.session_state.get('lockout_time', 0) > time.time():
        remaining = int(st.session_state.lockout_time - time.time())
        st.warning(f"⏳ Too many failed attempts. Please wait {remaining} seconds to re-login.")
        st.stop()
    elif st.session_state.get('lockout_time', 0) != 0 and st.session_state.lockout_time <= time.time():
        # Reset lockout when timer ends
        st.session_state.lockout_time = 0
        st.session_state.failed_attempts = 0
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.info("✅ You can now log in again.")

def process_failed_attempt():
    """Increments failed attempts and triggers lockout if limit reached."""
    st.session_state.failed_attempts = st.session_state.get('failed_attempts', 0) + 1
    if st.session_state.failed_attempts >= MAX_ATTEMPTS:
        st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
        st.warning(f"🔒 Locked out for {LOCKOUT_DURATION} seconds due to multiple failed attempts.")
