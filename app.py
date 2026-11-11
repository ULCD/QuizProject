import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# Page Configuration
st.set_page_config(page_title="Multiple Intelligences Quiz", page_icon="🧠", layout="centered")

# CUSTOM CSS: Making questions and clickable radio circles much bigger and centered
st.markdown("""
<style>
    /* Make question text larger and bolder */
    .question-text {
        font-size: 22px !important;
        font-weight: 700;
        color: #111111;
        margin-bottom: 8px;
        line-height: 1.4;
    }
    
    /* Center the horizontal radio buttons container */
    div[data-testid="stRadio"] > div {
        justify-content: center;
        gap: 35px;
    }
    
    /* Make the 1 to 5 number labels larger */
    div[data-testid="stRadio"] label {
        font-size: 20px !important;
        font-weight: 600;
    }
    
    /* Make the actual radio circles significantly bigger */
    input[type="radio"] {
        transform: scale(2.0);
        margin-right: 8px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Gardner's Multiple Intelligences Quiz")
st.markdown("Rate each statement from **1 (Strongly Disagree)** to **5 (Strongly Agree)** by clicking the circles below.")
st.markdown("All questions must be answered to generate your profile. You can change your answers at any time!")
st.markdown("---")

# The Full Question Bank (40 questions total, 5 per intelligence)
base_questions = [
    # --- 1. LINGUISTIC ---
    {"text": "I enjoy reading books, articles, or poetry in my free time.", "category": "Linguistic"},
    {"text": "I find it easy to express my thoughts clearly through writing or speaking.", "category": "Linguistic"},
    {"text": "I enjoy word games, puns, or learning new vocabulary words.", "category": "Linguistic"},
    {"text": "I remember things best when I write them down or read them repeatedly.", "category": "Linguistic"},
    {"text": "I can easily tell engaging stories or explain complex ideas with words.", "category": "Linguistic"},

    # --- 2. LOGICAL-MATHEMATICAL ---
    {"text": "I love solving puzzles, brain teasers, or working with numbers.", "category": "Logical-Math"},
    {"text": "I prefer to look for patterns, cause-and-effect relationships, or logical structures.", "category": "Logical-Math"},
    {"text": "I enjoy planning steps, organizing data, or doing math problems.", "category": "Logical-Math"},
    {"text": "I like asking 'how' and 'why' things work mechanically or abstractly.", "category": "Logical-Math"},
    {"text": "I find comfort in clear rules, categories, and systematic problem-solving.", "category": "Logical-Math"},

    # --- 3. SPATIAL ---
    {"text": "I can easily visualize objects from different angles or read maps without getting lost.", "category": "Spatial"},
    {"text": "I enjoy drawing, doodling, designing things, or working with visual arts.", "category": "Spatial"},
    {"text": "I have a good sense of color, composition, and space when decorating or arranging things.", "category": "Spatial"},
    {"text": "I prefer visual diagrams, charts, or blueprints over heavy blocks of text.", "category": "Spatial"},
    {"text": "I easily notice shapes, designs, and visual details in my surroundings.", "category": "Spatial"},

    # --- 4. BODILY-KINESTHETIC ---
    {"text": "I learn best by doing, building, or participating in physical hands-on activities.", "category": "Bodily-Kin."},
    {"text": "I have good physical coordination and enjoy sports, dancing, acting, or crafting.", "category": "Bodily-Kin."},
    {"text": "I get restless or fidgety if I have to sit still for too long without moving.", "category": "Bodily-Kin."},
    {"text": "I use body language, hand gestures, or physical expression when talking.", "category": "Bodily-Kin."},
    {"text": "I excel at fine motor tasks like repairing things, sculpting, or assembling items.", "category": "Bodily-Kin."},

    # --- 5. MUSICAL ---
    {"text": "I easily notice rhythms, melodies, and pitches in the music around me.", "category": "Musical"},
    {"text": "I often find myself humming, tapping tunes, or playing a musical instrument.", "category": "Musical"},
    {"text": "I remember songs, jingles, or musical themes easily after hearing them a few times.", "category": "Musical"},
    {"text": "I often use music to shift, enhance, or match my mood.", "category": "Musical"},
    {"text": "I am sensitive to environmental sounds, tones of voice, and auditory cues.", "category": "Musical"},

    # --- 6. INTERPERSONAL ---
    {"text": "People often come to me for advice or to talk through their problems.", "category": "Interpersonal"},
    {"text": "I work very well in teams and can easily sense other people's moods and feelings.", "category": "Interpersonal"},
    {"text": "I enjoy meeting new people, networking, and group social events.", "category": "Interpersonal"},
    {"text": "I can look at a situation from another person's point of view with empathy.", "category": "Interpersonal"},
    {"text": "I am good at resolving conflicts and mediating disagreements between friends or peers.", "category": "Interpersonal"},

    # --- 7. INTRAPERSONAL ---
    {"text": "I spend time reflecting on my own goals, emotions, and personal growth.", "category": "Intrapersonal"},
    {"text": "I am very self-aware and prefer working independently to understand myself.", "category": "Intrapersonal"},
    {"text": "I have a clear sense of my personal strengths, weaknesses, and values.", "category": "Intrapersonal"},
    {"text": "I enjoy journaling, meditating, or having quiet time alone to think.", "category": "Intrapersonal"},
    {"text": "I am highly motivated from within rather than needing external praise.", "category": "Intrapersonal"},

    # --- 8. NATURALIST ---
    {"text": "I feel a deep connection to nature, plants, animals, and the outdoors.", "category": "Naturalist"},
    {"text": "I easily notice details in the natural environment that others miss, like weather patterns or animal species.", "category": "Naturalist"},
    {"text": "I love gardening, hiking, camping, or spending time exploring natural landscapes.", "category": "Naturalist"},
    {"text": "I am fascinated by ecology, environmental science, and how living things interact.", "category": "Naturalist"},
    {"text": "I can easily classify and categorize different types of plants, animals, or natural phenomena.", "category": "Naturalist"}
]

# Randomize the question order once per session
if "shuffled_questions" not in st.session_state:
    shuffled = base_questions.copy()
    random.shuffle(shuffled)
    st.session_state.shuffled_questions = shuffled

questions = st.session_state.shuffled_questions
user_answers = {}

# Display questions with larger fonts and centered clickable option circles
for i, q in enumerate(questions):
    st.markdown(f'<p class="question-text">{i+1}. {q["text"]}</p>', unsafe_allow_html=True)
    
    user_answers[i] = st.radio(
        label=f"Rating for question {i+1}",
        options=[1, 2, 3, 4, 5],
        index=None,
        horizontal=True,
        key=f"q_{i}",
        label_visibility="collapsed"
    )
    st.write("") # Spacing between questions

st.markdown("---")

# When the user clicks the submission button
if st.button("🚀 Generate My Octagon Profile", type="primary", use_container_width=True):
    
    unanswered_count = sum(1 for i in range(len(questions)) if user_answers[i] is None)
    
    if unanswered_count > 0:
        st.warning(f"⚠️ Please answer all questions before generating your profile! ({unanswered_count} questions remaining)")
    else:
        scores = {
            "Linguistic": 0,
            "Logical-Math": 0,
            "Spatial": 0,
            "Bodily-Kin.": 0,
            "Musical": 0,
            "Interpersonal": 0,
            "Intrapersonal": 0,
            "Naturalist": 0
        }
        
        for i, q in enumerate(questions):
            cat = q["category"]
            scores[cat] += user_answers[i]
            
        categories = list(scores.keys())
        values = list(scores.values())
        N = len(categories)
        
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        values.append(values[0])
        angles.append(angles[0])
        
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.plot(angles, values, linewidth=2.5, linestyle='solid', color='#ff4b4b')
        ax.fill(angles, values, color='#ff4b4b', alpha=0.3)
        
        plt.xticks(angles[:-1], categories, color='#111111', size=10, weight='bold')
        plt.yticks([5, 10, 15, 20, 25], ['5', '10', '15', '20', '25'], color='grey', size=8)
        ax.set_rlim(0, 25)
        
        plt.title('Your Multiple Intelligences Profile', size=14, weight='bold', y=1.1)
        plt.tight_layout()
        
        st.success("🎉 Here is your Multiple Intelligences Octagon Profile!")
        st.pyplot(fig)