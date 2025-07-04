
import streamlit as st
import pandas as pd
import random
from quizbrain import QuizBrain

def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    
    # Add tracking for current question set
    if 'current_set_index' not in st.session_state:
        st.session_state.current_set_index = 0
        
    # Initialize questions if needed
    if 'questions' not in st.session_state or 'quiz_brain' not in st.session_state:
        st.session_state.quiz_brain = QuizBrain()
        # Get the current question set based on the index
        st.session_state.questions = st.session_state.quiz_brain.get_question_set(st.session_state.current_set_index).copy()
        # Optional: randomize questions
        random.shuffle(st.session_state.questions)
    
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = len(st.session_state.questions)

def start_quiz():
    """Start the quiz."""
    st.session_state.quiz_started = True
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.quiz_completed = False

def submit_answer(answer):
    """Process the user's answer."""
    q = st.session_state.questions[st.session_state.current_question]
    correct = answer == q["correct"]
    
    if correct:
        st.session_state.score += 1
    
    st.session_state.user_answers.append({
        "question_num": st.session_state.current_question + 1,
        "category": q["category"],
        "question": q["question"],
        "user_answer": answer,
        "user_answer_text": q["options"][answer],
        "correct_answer": q["correct"],
        "correct_answer_text": q["options"][q["correct"]],
        "is_correct": correct
    })
    
    # Move to next question or finish quiz
    if st.session_state.current_question < st.session_state.total_questions - 1:
        st.session_state.current_question += 1
    else:
        st.session_state.quiz_completed = True

def restart_quiz():
    """Restart the quiz by returning to the welcome screen for set selection."""
    # Reset quiz state but don't automatically select next question set
    st.session_state.quiz_started = False
    st.session_state.quiz_completed = False
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.user_answers = []

def display_welcome():
    """Display welcome screen."""
    set_names = st.session_state.quiz_brain.get_set_names()
    
    st.title("🧠 BRAZE KNOWLEDGE CHECK: MULTIPLE CHOICE QUIZ 🧐")
    st.markdown("---")
    st.markdown(f"### Test your knowledge of the Braze marketing platform!")
    
    st.markdown("<h5 style='color:blue;'>Choose your question set:</h5>", unsafe_allow_html=True)
    
    # Add question set selection as vertical radio buttons
    selected_set_index = st.radio(
        "",  # Empty label since we're using a header above
        options=range(len(set_names)),
        format_func=lambda x: f"{set_names[x]} (Set {x+1} of {st.session_state.quiz_brain.get_total_sets()})",
        horizontal=False,  # Make it vertical
        label_visibility="collapsed"  # Hide the empty label completely
    )
    
    # Update current set index based on user selection
    st.session_state.current_set_index = selected_set_index
    
    # Get the current question set based on selection
    st.session_state.questions = st.session_state.quiz_brain.get_question_set(st.session_state.current_set_index).copy()
    random.shuffle(st.session_state.questions)
    st.session_state.total_questions = len(st.session_state.questions)
    
    current_set = set_names[st.session_state.current_set_index]
    
    # Modified to make the variable text blue
    st.markdown(f"Selected question set: <span style='color:blue;font-weight:bold;'>{current_set}</span> (Set {st.session_state.current_set_index + 1} of {st.session_state.quiz_brain.get_total_sets()})", unsafe_allow_html=True)
    
    # Split into two separate writes with paragraph break
    st.write(f"There are {st.session_state.total_questions} questions in total covering various Braze topics.")
    st.write(f"If you retry the quiz after completion, you will receive a different set of questions next time!!")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Start Quiz", use_container_width=True):
            start_quiz()
            st.rerun()

def display_question():
    """Display the current question."""
    # Add a safety check to prevent index out of range errors
    if st.session_state.current_question >= len(st.session_state.questions):
        st.session_state.quiz_completed = True
        st.rerun()
        return
    
    q = st.session_state.questions[st.session_state.current_question]
    
    st.subheader(f"Question {st.session_state.current_question + 1} of {st.session_state.total_questions}")
    st.caption(f"Category: {q['category']}")
    
    st.markdown(f"### {q['question']}")
    
    # Convert options to format for radio button
    options = []
    for key, value in q['options'].items():
        options.append(f"{key}: {value}")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        answer = st.radio(
            "Select your answer:",
            options=options,
            key=f"q_{st.session_state.current_question}",
            label_visibility="collapsed"
        )
    
    with col2:
        if st.button("Submit Answer", use_container_width=True):
            # Extract just the letter (A, B, C or D) from the selected option
            selected_letter = answer.split(":")[0].strip()
            submit_answer(selected_letter)
            st.rerun()

def display_results():
    """Display quiz results."""
    score_percentage = (st.session_state.score / st.session_state.total_questions) * 100
    
    st.title("🏆 QUIZ RESULTS")
    st.markdown("---")
    
    # Display score with colored background based on performance
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if score_percentage == 100:
            score_color = "green"
            emoji = "🎉"
        elif score_percentage >= 80:
            score_color = "green"
            emoji = "🌟"
        elif score_percentage >= 60:
            score_color = "orange"
            emoji = "👍"
        else:
            score_color = "red"
            emoji = "📚"
            
        st.markdown(
            f"""
            <div style="padding: 10px; border-radius: 10px; background-color: {score_color}; color: white; text-align: center;">
                <h2>{emoji} You scored: {st.session_state.score}/{st.session_state.total_questions} ({score_percentage:.1f}%)</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Performance message
    if score_percentage == 100:
        st.success("Perfect score! You're a Braze expert!")
    elif score_percentage >= 80:
        st.success("Great job! You have strong knowledge of Braze.")
    elif score_percentage >= 60:
        st.warning("Good effort! Consider reviewing the topics you missed.")
    else:
        st.error("You might need more study time with Braze documentation.")
    
    # Answer summary
    st.subheader("Answer Summary")
    
    # Convert answers to DataFrame for better display
    answers_df = pd.DataFrame(st.session_state.user_answers)
    
    # Group questions by category and show performance per category
    if not answers_df.empty:
        st.subheader("Performance by Category")
        category_performance = answers_df.groupby('category')['is_correct'].agg(['sum', 'count'])
        category_performance['percentage'] = (category_performance['sum'] / category_performance['count'] * 100).round(1)
        category_performance.columns = ['Correct', 'Total', 'Percentage (%)']
        st.dataframe(category_performance, use_container_width=True)
    
    # Show detailed answers
    st.subheader("Your Answers")
    for answer in st.session_state.user_answers:
        with st.expander(f"Q{answer['question_num']}: {answer['question']}"):
            status = "✅ CORRECT" if answer["is_correct"] else "❌ INCORRECT"
            status_color = "green" if answer["is_correct"] else "red"
            
            st.markdown(f"**Category:** {answer['category']}")
            st.markdown(f"**Your answer:** {answer['user_answer']} - {answer['user_answer_text']}")
            st.markdown(f"**Correct answer:** {answer['correct_answer']} - {answer['correct_answer_text']}")
            st.markdown(f"<span style='color:{status_color};font-weight:bold;'>{status}</span>", unsafe_allow_html=True)
    
    # Restart button
    if st.button("Return to Question Set Selection", use_container_width=True):
        restart_quiz()
        st.rerun()

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Braze Knowledge Quiz",
        page_icon="🅑𝐑🅰️𝐙🅔",
        layout="centered"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Navigation based on app state - added extra safety check
    if st.session_state.quiz_completed:
        display_results()
    elif not st.session_state.quiz_started:
        display_welcome()
    else:
        display_question()

if __name__ == "__main__":
    main()