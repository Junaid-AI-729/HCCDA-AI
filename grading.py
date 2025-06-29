import streamlit as st
st.title('Corvit system')
marks=st.number_input("Enter obtained marks:",min_value=1)

total= st.number_input("Enter total marks",min_value=1)

p = marks/total * 100

st.subheader(f'Your percentage: :blue[{p} %]')

if p >= 80:
    st.success('Excellent')
elif p >= 60 and p < 80:
    st.info('Pass')
else:
    st.error('Fail')