import streamlit as st

def clear_form():
    st.session_state.image_input_key += 1  # Change the key to force reset
    st.session_state.question_key += 1
    st.session_state.option_keys = [k + 1 for k in st.session_state.option_keys]
    st.session_state.answer_input_key += 1

def main():
    st.set_page_config(
        layout="wide",
    )
    # Initialize the dynamic key if it doesn't exist
    if "image_input_key" not in st.session_state:
        st.session_state.image_input_key = 0
    if "question_key" not in st.session_state:
        st.session_state.question_key = 0
    if "option_keys" not in st.session_state:   
        st.session_state.option_keys = [0, 0, 0, 0]  # For A, B, C, D
    if "answer_input_key" not in st.session_state:
        st.session_state.answer_input_key = 0

    st.title("Smart Exam Preperation")
    option= st.radio("Choose an option",options=["IOE", "IOM"], horizontal=True, index= None)
    with st.form("exam_form"):
        if option == "IOE":
            st.radio("Select Subject", options=["Mathematics", "Physics", "Chemistry", "English"] , horizontal=True, index=None)
            st.radio("Choose Section", options=["Secton 1", "Section 2"], horizontal=True, index=None)
        if option == "IOM":
            st.radio("Select Subject", options=["Zoology", "Botany", "Chemistry", "Physics", "MAT"] , horizontal=True, index=None)

        q_col, f_col = st.columns([3, 1])
        with q_col:
            question = st.text_area("Enter your question",height= 130, key=f"question_key_{st.session_state.question_key}")
            options_labels = ["A", "B", "C", "D"]
            option_dict = {}
            for i, label in enumerate(options_labels):
                label_col, input_col, spacer_col= st.columns([1, 30, 10])
                with label_col:
                    st.markdown(f"**{label}**")
                with input_col:
                    option_text = st.text_input(
                        f"{label}",
                        key=f"option_{label}_{st.session_state.option_keys[i]}",
                        label_visibility="collapsed"
                    )
                option_dict[label] = option_text
        with f_col:
            uploaded_file = st.file_uploader(
                "Upload your exam notes",
                key=f"image_input_{st.session_state.image_input_key}",
                type=["jpg", "jpeg", "png"]
            )
        answer = st.selectbox(
            "Select the correct anser",
            options= options_labels,
            index=None,
            key=f"answer_select_{st.session_state.answer_input_key}"
        )
        submitted = st.form_submit_button("Submit", type="primary")
        # cleared = st.form_submit_button("Clear", on_click=clear_form)

    if submitted:
        st.write("Form submitted successfully!")
        st.session_state.image_input_key += 1 # Reset after submit
        st.session_state.question_key += 1
        st.session_state.option_keys = [k + 1 for k in st.session_state.option_keys]
        st.session_state.answer_input_key += 1
        st.rerun()

if __name__ == "__main__":
    main()
