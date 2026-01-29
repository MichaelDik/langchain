from IPython.display import Image, display
import operator
from typing import Annotated, List, Literal, TypedDict
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class State(TypedDict):
    nlist: List[str]
    value2: str
    
def node_a(state: State) -> Command[Literal["b", "c", END]]:
   #So this would get most recent item appended 
    select = state["nlist"][-1]

    if select == "b": 
        next_node = "b"
    elif select == "c": 
         next_node = "c"
    elif select =="q":
         next_node = END
    else: 
        next_node = END
    return Command (
        #Ok so state holds the next node 
        update = State(nlist = [select]), 
        goto = next_node 
    )


def node_b(state: State) -> State: 
    #print(f"Node b is receiving {state['nlist']}")
    return (State(nlist = ["B"]) ) 
def node_c(state: State) -> State: 
    return(State(nlist = ["C"])) 

#Create Conditional Edge

def conditional_edge(state: State) -> Literal["b" ,"c", END]:
    #So this would get most recent item appended 
    select = state["nlist"][-1]

    if select == "b": 
        return"b"
    elif select == "c": 
        return "c"
    elif select =="q":
        return END
    else: 
        return END



# Instantiate StateGraph 
builder = StateGraph(State)

#Add nodes 
builder.add_node("a", node_a)
builder.add_node("b", node_b ) # this Registers the node
builder.add_node("c", node_c)
#Add Edges 
builder.add_edge(START, "a")
builder.add_edge("b" ,END)
builder.add_edge("c", END)
#Add Conditional Edge
#builder.add_conditional_edges("a", conditional_edge)

#Compile Graph
graph = builder.compile()

initial_state = State(
    nlist = ["Goodbye?"]
)


# print()
# result = graph.invoke(initial_state)
# print(result)

# print(graph.get_graph().draw_mermaid())


user = input('b,c,or q to quit: ')

input_state = State(
    nlist = [user]
)

print(graph.invoke(input_state)) 
