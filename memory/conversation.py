"""
==========================================================
Stitches By S AI Chatbot
Conversation Memory
==========================================================
"""

from collections import deque


class ConversationMemory:
    """
    Stores recent conversation history.
    """

    def __init__(self, max_history=10):

        self.history = deque(maxlen=max_history)

    def add(self, role, message):

        self.history.append(
            {
                "role": role,
                "message": message,
            }
        )

    def get_history(self):

        return list(self.history)

    def clear(self):

        self.history.clear()

    def format_history(self):

        if not self.history:
            return ""

        text = []

        for item in self.history:

            text.append(
                f"{item['role']}: {item['message']}"
            )

        return "\n".join(text)
