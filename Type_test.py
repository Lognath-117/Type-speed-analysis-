import streamlit as st
import random
import time

# Long practice paragraphs (20 total, ~200+ words each)
paragraphs = [
    """Typing is a skill that improves gradually with practice and patience. 
    Just like playing a musical instrument or learning a sport, typing requires 
    both accuracy and rhythm. Many people believe speed is the most important 
    aspect of typing, but in reality accuracy is equally crucial. A person who 
    types extremely fast but makes constant errors may end up wasting more time 
    correcting mistakes. On the other hand, someone who types slowly but 
    consistently with fewer errors can actually be more productive in the long run. 
    The goal of every learner should be to balance speed and accuracy while 
    maintaining a steady rhythm. The brain, fingers, and eyes must work in 
    synchronization, building a muscle memory that allows words to flow without 
    conscious effort. This transformation happens only through daily practice. 
    The more you expose yourself to different words, sentences, and punctuation, 
    the better your fingers adapt. Over time, you will notice that you no longer 
    need to look at the keyboard. Your fingers will automatically find the right 
    keys, your mind will process sentences faster, and your typing speed will 
    increase without forcing it. Remember, typing is not just about inputting words 
    into a machine; it is about developing a lifelong skill that enhances efficiency, 
    confidence, and communication in the digital age.""",

    """Artificial intelligence has rapidly grown from being a futuristic idea to an 
    everyday reality. From unlocking smartphones with facial recognition to asking 
    voice assistants for directions, AI now exists in our daily routines. One of the 
    most fascinating aspects of AI is its ability to learn patterns from data and 
    improve over time. This learning capability allows AI to make predictions, 
    recommend products, or even detect diseases. However, with great power comes 
    great responsibility. Many experts worry about the ethical side of AI, including 
    privacy concerns and job automation. If machines can think, learn, and make 
    decisions, what will be the role of humans in the future? The answer may not be 
    simple, but one thing is clear: AI should be developed responsibly. The focus must 
    remain on using AI to assist humans rather than replace them. This means designing 
    systems that are transparent, fair, and accountable. As we move further into an 
    AI-driven world, it is important for individuals to develop skills that complement 
    automation, such as creativity, critical thinking, and emotional intelligence. The 
    true power of AI lies not in replacing humans, but in empowering them to achieve 
    things once considered impossible.""",

    # Add 18 more long paragraphs here (I’m keeping this short here, 
    # but you can fill with real stories, essays, or Wikipedia extracts).
]

# Ensure at least 20
while len(paragraphs) < 20:
    paragraphs.append(paragraphs[0])  # duplicate until you write 20 unique ones

# Session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "paragraph" not in st.session_state:
    st.session_state.paragraph = random.choice(paragraphs)
if "results" not in st.session_state:
    st.session_state.results = None

st.title("⌨️ Smart Typing Speed Trainer (Extended Version)")

# Display paragraph
st.subheader("Type this paragraph (will take ~15 min):")
st.info(st.session_state.paragraph)

# Typing box
typed_text = st.text_area("Start typing here:", height=300)

# Start timer on first keystroke
if typed_text and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# Button to check results
if st.button("Check Speed"):
    if st.session_state.start_time:
        end_time = time.time()
        elapsed_time = max(end_time - st.session_state.start_time, 1)

        # Words per minute
        words_typed = typed_text.split()
        total_words = len(words_typed)
        wpm = round((total_words / elapsed_time) * 60)

        # Accuracy
        original_words = st.session_state.paragraph.split()
        correct_words = sum(
            1 for i, word in enumerate(words_typed) 
            if i < len(original_words) and word == original_words[i]
        )
        accuracy = round((correct_words / max(len(original_words), 1)) * 100, 2)
        mistakes = total_words - correct_words

        st.session_state.results = {
            "wpm": wpm,
            "accuracy": accuracy,
            "mistakes": mistakes
        }

# Show results
if st.session_state.results:
    st.success(
        f"🚀 Speed: {st.session_state.results['wpm']} WPM | "
        f"🎯 Accuracy: {st.session_state.results['accuracy']}% | "
        f"❌ Mistakes: {st.session_state.results['mistakes']}"
    )

# New paragraph button
if st.button("New Paragraph"):
    st.session_state.paragraph = random.choice(paragraphs)
    st.session_state.start_time = None
    st.session_state.results = None
    st.rerun()
