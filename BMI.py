import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Obesity Calculator",
    page_icon="⚖️",
    layout="centered"
)

# Title and description
st.title("⚖️ Obesity Calculator")
st.markdown("Calculate your BMI and check your weight status")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Weight input
    weight = st.number_input(
        "Enter your weight (kg):", 
        min_value=1.0, 
        max_value=300.0, 
        value=70.0,
        step=0.1
    )

with col2:
    # Height input
    height = st.number_input(
        "Enter your height (m):", 
        min_value=0.5, 
        max_value=2.5, 
        value=1.75,
        step=0.01
    )

# Calculate button
if st.button("Calculate BMI", type="primary"):
    if height > 0:
        BMI = weight / (height ** 2)
        
        # Display results
        st.subheader("Results:")
        
        # Show BMI value
        st.metric("Your BMI", f"{BMI:.2f}")
        
        # Determine category with color coding
        if BMI > 40:
            st.error("OBESE - Category III")
            st.warning("🚨 Please consult a healthcare professional")
        elif BMI > 35:
            st.error("OBESE - Category II")
            st.warning("⚠️ Consider seeking medical advice")
        elif BMI > 30:
            st.error("OBESE - Category I")
        elif BMI > 25:
            st.warning("OVERWEIGHT")
        elif BMI > 18.5:
            st.success("NORMAL WEIGHT ✅")
        elif BMI > 17:
            st.warning("UNDERWEIGHT - Mild")
        elif BMI > 16:
            st.warning("UNDERWEIGHT - Moderate")
        else:
            st.error("UNDERWEIGHT - Severe")
            st.warning("🚨 Please consult a healthcare professional")
        
        # BMI chart for reference
        st.subheader("BMI Categories Reference:")
        st.markdown("""
        | Category | BMI Range |
        |----------|-----------|
        | Severe Underweight | < 16 |
        | Moderate Underweight | 16 - 17 |
        | Mild Underweight | 17 - 18.5 |
        | Normal Weight | 18.5 - 25 |
        | Overweight | 25 - 30 |
        | Obese I | 30 - 35 |
        | Obese II | 35 - 40 |
        | Obese III | > 40 |
        """)
        
    else:
        st.error("Height must be greater than 0!")

# Additional features
st.markdown("---")
st.subheader("💡 Tips for Healthy Weight")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Nutrition**")
    st.markdown("""
    - Balanced diet
    - Portion control
    - Stay hydrated
    """)

with col2:
    st.markdown("**Exercise**")
    st.markdown("""
    - 150 mins/week
    - Strength training
    - Stay active
    """)

with col3:
    st.markdown("**Lifestyle**")
    st.markdown("""
    - Quality sleep
    - Stress management
    - Regular check-ups
    """)

# Disclaimer
st.markdown("---")
st.caption("""
**Disclaimer:** This calculator provides general information only. 
For medical advice, please consult with a healthcare professional. 
BMI may not accurately reflect body composition for athletes, elderly, or certain ethnic groups.
""")
