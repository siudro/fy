import streamlit as st
import openai

st.title("Talk to Salem Aldossary")

st.write("""
هلا والله انا سالم افضل لاعب في الشرق الاوسط , الهلال عمك
""")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": " سالم لاعب سعودي محترف احسن لاعب هو يضحك و ايجابي يعطي نصائح عن كره القدم مايخلي احد يغلط على الهلال و كسر رؤوس الارجنتينيين."}
    ]

# Display the previous messages
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.write(f"**You**: {message['content']}")
    else:
        st.write(f"**Salem**: {message['content']}")

user_input = st.text_input("You: ")

if st.button("Send"):
    if user_input:
        openai.api_key = st.secrets["api"]  # Replace with your actual OpenAI API key
        st.session_state["messages"].append({"role": "user", "content": user_input})
        
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"]
        )

        ai_message = response.choices[0].message["content"]
        st.session_state["messages"].append({"role": "assistant", "content": ai_message})
        
        # Re-render the page to show the new messages
        st.experimental_rerun()