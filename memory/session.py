"""
==========================================================
Stitches By S AI Chatbot
Conversation Session
==========================================================
"""

from uuid import uuid4


DEFAULT_SESSION = str(uuid4())


class SessionManager:
    """
    Handles chat sessions.
    """

    def __init__(self):

        self.session_id = DEFAULT_SESSION

    def get_session(self):

        return self.session_id

    def new_session(self):

        self.session_id = str(uuid4())

        return self.session_id
