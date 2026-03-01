import streamlit as st
import random
from few_shot import FewShotPosts
from post_generator import generate_post, generate_hashtags

st.set_page_config(page_title="LinkedIn Post Generator", layout="wide")

def main():
    if "history" not in st.session_state:
        st.session_state["history"] = []
    if "generated_count" not in st.session_state:
        st.session_state["generated_count"] = 0

    st.title("LinkedIn Post Generator")

    # ---------------- SIDEBAR -------------------
    st.sidebar.markdown("## 🎛 Dashboard")

    quotes = [
        "Believe you can, and you're halfway there.",
        "Work hard in silence, let success make the noise.",
        "Discipline is choosing what you want most over what you want now.",
        "You don’t need to be perfect, just be consistent.",
        "Push yourself, because no one else is going to do it for you.",
        "Action is the antidote to fear.",
        "Don’t stop until you’re proud.",
        "Every day is a second chance.",
        "Success is built from small daily efforts.",
        "Dream it. Wish it. Do it.",
        "You become what you believe.",
        "Growth happens outside your comfort zone.",
        "Your future depends on what you do today.",
        "Great things never come from comfort zones.",
        "Start where you are. Use what you have. Do what you can.",
    ]

    st.sidebar.info(random.choice(quotes))

    st.sidebar.metric("Posts Generated", st.session_state["generated_count"])

    st.sidebar.markdown("### 📜 History")

    # Collapsible short previews
    for idx, item in enumerate(st.session_state["history"], start=1):
        preview_line = item.split("\n")[0][:60] + "..."
        with st.sidebar.expander(f"Post {idx}: {preview_line}"):
            st.sidebar.write(item)

    st.sidebar.markdown("## 👩‍💻 About Me")
    st.sidebar.write("### **Nandini Pathange**")
    st.sidebar.write("I love learning new things and exploring anything interesting ✨")
    st.sidebar.success("Funny fact: I learn new things every day… mostly because I forget them by tomorrow! 😄")

    # ---------------- MAIN UI -------------------
    fs = FewShotPosts()

    st.write("### Select Post Requirements")

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("Topic", options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length", ["Short", "Medium", "Long"])

    with col3:
        selected_language = st.selectbox("Language", ["English", "Hinglish"])

    selected_tone = st.selectbox(
        "Tone",
        ["Motivational", "Professional", "Funny", "Emotional", "Inspirational"]
    )

    st.write("---")

    if st.button("Generate Post"):
        post = generate_post(selected_length, selected_language, selected_tag, selected_tone)
        hashtags = generate_hashtags(post)

        # Update history & counter
        st.session_state["history"].append(post)
        st.session_state["generated_count"] += 1

        st.write("## Generated Post")
        st.success(post)

        st.write("## Hashtags")
        st.info(hashtags)

        st.download_button(
            label="Download Post as TXT",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
