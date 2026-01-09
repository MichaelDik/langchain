from IPython.display import Image, display
import operator
from typing import Annotated, List, Literal, TypedDict
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class State(TypedDict):
    nlist: List[str]
    
def node_a(state: State) -> State:
    print(f"node a is receiving {state['nlist']}")
    note = "\nHello World from Node a"
    return(State(nlist = [note]))

def node_b(state: State) -> State: 
    print(f"Node b is receiving {state['nlist']}")
    note ="Sup"
    return(State(nlist = [note]))

builder = StateGraph    (State)
builder.add_node("a", node_a)
builder.add_edge(START, "a")
builder.add_edge("a", END)
graph = builder.compile()

initial_state = State(
    nlist = ["Goodbye?"]
)

display(Image(graph.get_graph().draw_mermaid_png))
