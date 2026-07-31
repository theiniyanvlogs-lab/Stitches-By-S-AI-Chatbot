"""
==========================================================
Stitches By S AI Chatbot
LangGraph Workflow
==========================================================
"""

from langgraph.graph import StateGraph, END

from graph.state import ChatState

from graph.nodes import (
    supervisor_node,
    fabric_node,
    tailoring_node,
    business_node,
)


workflow = StateGraph(ChatState)

workflow.add_node(
    "supervisor",
    supervisor_node,
)

workflow.add_node(
    "fabric",
    fabric_node,
)

workflow.add_node(
    "tailoring",
    tailoring_node,
)

workflow.add_node(
    "business",
    business_node,
)

workflow.set_entry_point("supervisor")


def router(state: ChatState):

    route = state["route"]

    if "fabric" in route:
        return "fabric"

    if "tailoring" in route:
        return "tailoring"

    return "business"


workflow.add_conditional_edges(
    "supervisor",
    router,
    {
        "fabric": "fabric",
        "tailoring": "tailoring",
        "business": "business",
    },
)

workflow.add_edge("fabric", END)
workflow.add_edge("tailoring", END)
workflow.add_edge("business", END)

app = workflow.compile()
