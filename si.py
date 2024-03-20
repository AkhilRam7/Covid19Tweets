import streamlit as st

# Set wide layout for the entire app
st.set_page_config(layout="wide")

st.markdown(""" 
<style>
    [data-testid="stAppViewContainer"]{
      background: linear-gradient(to right, #e5e5f7 50%, #ffffff 50%);
    }
    [data-testid="stHeader"]{
      background: linear-gradient(to right, #e5e5f7 50%, #ffffff 50%);
    }
    .block-container {
        padding-top: 5rem;
        padding-bottom: 0rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
    .scrollable-text {
        overflow-y: scroll;
        padding: 10px;
    }
</style>
""" ,unsafe_allow_html=True)

# Create a single wide column
main_column = st.container()

# Create two containers inside the main column for sections
section_1_container, section_2_container = main_column.columns(2)

# Add content to sections
with section_1_container:
    st.subheader("Profile & Team")
    st.write("This is content in section 1.")
    st.divider()

    st.subheader("Notes")
    notes = "This is a long text example that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text example that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text example that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text example that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text example that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text example that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text example that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text element that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content.This is a long text element that will be scrollable within Section 1. You can add any amount of text here, and it will only show a limited portion initially. By using the scrollbar, you can view the entire content."
    text_container_html = st.components.v1.html(
        """
        <div style="height: 300px;overflow-y: scroll;padding: 0px;font-family: ui-sans-serif;line-height: 1.5;"><p>
        """+notes+"""</p>
        </div>
        """, height=150)
    st.divider()

    st.subheader("Engagements")
    st.write("This is content in section 1.")
    eng_tab1, eng_tab2 = st.tabs(["Individual", "BuyingUnit"])
    with eng_tab1:
        st.write("Individual")

    with eng_tab2:
        st.write("BuyingUnit")
    st.divider()

    st.subheader("Sales & Assets")
    st.write("This is content in section 1.")
    st.divider()

    st.subheader("Book of Business")
    st.write("This is content in section 1.")
    st.divider()

with section_2_container:
    st.subheader("Recommendations")
    st.write("This is content in section 2.")



