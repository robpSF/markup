import streamlit as st

def main():
    st.title("Markup Display App")
    st.write("Enter your markup text below:")

    # Text area for user input
    markup_text = st.text_area("Markup Input", height=200)

    if markup_text:
        st.write("Formatted Output:")
        st.markdown(markup_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
