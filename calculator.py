import streamlit as st

# Title and Author
st.set_page_config(page_title="Calculator by Junaid Akbar", layout="centered")
st.markdown("## 🔢 Calculator App")
st.markdown("### Developed by *Junaid Akbar*")

# Session State to maintain expression
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display the current expression
st.text_input("Expression", st.session_state.expression, key="display", disabled=True)

# Button Layout
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "⌫"]
]

# Function to handle button clicks
def click(btn):
    if btn == "C":
        st.session_state.expression = ""
    elif btn == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]
    elif btn == "=":
        try:
            # Replace symbols with Python equivalents
            result = eval(st.session_state.expression.replace("×", "*").replace("÷", "/"))
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += btn

# Display Buttons
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        with cols[i]:
            st.button(btn, on_click=click, args=(btn,), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("🧮 **Basic Calculator using Python & Streamlit**")