"""
==========================================================
Stitches By S AI Chatbot
Main Application
==========================================================
"""

import gradio as gr

from graph.workflow import app as workflow
from memory.conversation import ConversationMemory
from utils.logger import logger

# --------------------------------------------------------
# Initialize Memory
# --------------------------------------------------------

memory = ConversationMemory()


# --------------------------------------------------------
# Chat Function
# --------------------------------------------------------

def chatbot(message, history):

    if history is None:
        history = []

    logger.info(f"User Question : {message}")

    try:

        history_text = memory.format_history()

        result = workflow.invoke(
            {
                "question": message,
                "history": history_text,
                "route": "",
                "answer": "",
            }
        )

        answer = result["answer"]

        memory.add("User", message)
        memory.add("Assistant", answer)

        # New Gradio message format
        history.append(
            {
                "role": "user",
                "content": message,
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        logger.info("Response Generated Successfully")

        return "", history

    except Exception as e:

        logger.error(f"Error : {e}")

        history.append(
            {
                "role": "assistant",
                "content": f"❌ Error: {str(e)}",
            }
        )

        return "", history


# --------------------------------------------------------
# Clear Chat
# --------------------------------------------------------

def clear_chat():

    memory.clear()

    logger.info("Conversation Cleared")

    return "", []


# --------------------------------------------------------
# Gradio UI
# --------------------------------------------------------

with gr.Blocks(
    title="Stitches By S AI Chatbot"
) as demo:

    gr.Markdown(
        """
# 👗 Stitches By S AI Chatbot

### AI-Powered Multi-Agent Tailoring Knowledge Assistant

### 👩‍💼 Expert AI Agents

- 🧵 Fabric Expert
- ✂️ Tailoring Expert
- 💼 Business Expert

Ask anything about fabrics, tailoring, stitching,
measurements, pricing, or tailoring business.
"""
    )

    chatbot_ui = gr.Chatbot(
        height=500,
        label="Chat",
        type="messages",
    )

    message = gr.Textbox(
        placeholder="Ask your tailoring question...",
        label="Your Question",
    )

    clear = gr.Button("🗑️ Clear Chat")

    message.submit(
        chatbot,
        inputs=[
            message,
            chatbot_ui,
        ],
        outputs=[
            message,
            chatbot_ui,
        ],
    )

    clear.click(
        clear_chat,
        outputs=[
            message,
            chatbot_ui,
        ],
    )


# --------------------------------------------------------
# Launch
# --------------------------------------------------------

if __name__ == "__main__":

    logger.info("Starting Stitches By S AI Chatbot...")

    demo.launch(
        share=True,
        debug=True,
        show_error=True,
    )
