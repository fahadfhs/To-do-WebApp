import streamlit as st
import functions

accessed_list = functions.get_todo_list()


def add_todo():
    local_todo = st.session_state["new_todo"] + "\n"
    accessed_list.append(local_todo)
    functions.write_todo_list(accessed_list)


st.title("Todo list tracker App")
st.subheader("This is my todo app")
st.write("This app is to increase your day to day <b>productivity</b>.",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add a new todo item",
              on_change=add_todo, key='new_todo')

for index, item in enumerate(accessed_list):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        accessed_list.pop(index)
        """Once the item is popped, the new list is written
        again using the write function below """
        functions.write_todo_list(accessed_list)
        del st.session_state[item]
        st.experimental_rerun()

# """ The below code is just for checking how our
# code works in the webapp and the processess behind
# it"""
# print("Hello")
# st.session_state
