import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My to-do app")
st.subheader("This is a to-do app.")

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label= "", placeholder= "Add new todo", on_change=add_todo, key='new todo')