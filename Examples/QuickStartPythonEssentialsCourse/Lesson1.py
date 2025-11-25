from IPython.display import Image, display
import operator
from typing import Annotated, List, Literal, TypedDict
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt
""" 

Lesson 1 from courses, building state, nodes, edges. Very Simple

"""

class State(TypedDict):
    nlist: List[str]
    
def node_a(state: State) -> State:
    print(f"node a is receiving {state['nlist']}")
    note = "\nHello World from Node B"
    return(State(nlist = [note]))

builder = StateGraph(State)
builder.add_node("a", node_a)
builder.add_edge(START, "a")
builder.add_edge("a", END)
graph = builder.compile()


#display(Image(graph.get_graph().draw_mermaid_png()))
print(graph.get_graph().draw_mermaid())

initial_state = State(
    nlist = ["Hello Node a, how are you?"]
)
#graph.invoke(initial_state)
print(type(builder))