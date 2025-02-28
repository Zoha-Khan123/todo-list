import streamlit as st 


st.title("To-Do List")

# Initialize session state to store tasks
if 'tasks' not in st.session_state:
    st.session_state["tasks"] = []
add = st.session_state["tasks"]

# Input field for adding tasks
task = st.text_input("Add a task", key=f"add_task{add}")
click = st.button("Add Task")

# Button to add a task
if click:
        st.session_state["tasks"].append(task)
        st.rerun()

# Display task 
for idx,i in enumerate(st.session_state["tasks"]):
    st.write(idx,i)

    # Remove task
    if st.button("Remove",idx):
        st.session_state["tasks"].pop(idx)
        st.rerun()