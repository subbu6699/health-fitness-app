import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2563EB;
        text-align: center;
        margin-bottom: 1rem;
    }
    .hero {
        background-color: #2563EB;
        color: white;
        padding: 2rem;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .hero p {
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
    }
    .hero button {
        background-color: white;
        color: #2563EB;
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
    }
    .feature {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .feature img {
        width: 100%;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .feature h3 {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .feature p {
        font-size: 1rem;
        color: #666;
    }
    .login-form {
        background-color: #F3F4F6;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        margin: 0 auto;
    }
    .login-form label {
        font-size: 1rem;
        font-weight: bold;
        color: #333;
    }
    .login-form input {
        width: 100%;
        padding: 0.5rem;
        margin-bottom: 1rem;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .login-form button {
        background-color: #2563EB;
        color: white;
        width: 100%;
        padding: 0.8rem;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header">HealthFit</div>', unsafe_allow_html=True)

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h1>Take Control of Your Health</h1>
        <p>Track your activity, monitor your diet, and improve your overall well-being.</p>
        <button>Get Started</button>
    </div>
    """,
    unsafe_allow_html=True,
)

# Features Section
st.markdown("## Key Features")
col1, col2, col3, col4 = st.columns(4)

# Feature 1: Activity Tracking
with col1:
    st.markdown('<div class="feature">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/300x200.png?text=Activity+Tracking", use_container_width=True)
    st.markdown("<h3>Activity Tracking</h3>", unsafe_allow_html=True)
    st.markdown("<p>Monitor your steps, calories burned, and more.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Feature 2: Diet & Nutrition
with col2:
    st.markdown('<div class="feature">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/300x200.png?text=Diet+%26+Nutrition", use_container_width=True)
    st.markdown("<h3>Diet & Nutrition</h3>", unsafe_allow_html=True)
    st.markdown("<p>Log your meals and track your nutrient intake.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Feature 3: Mental Health
with col3:
    st.markdown('<div class="feature">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/300x200.png?text=Mental+Health", use_container_width=True)
    st.markdown("<h3>Mental Health</h3>", unsafe_allow_html=True)
    st.markdown("<p>Access meditation guides and stress management tools.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Feature 4: Sleep Analysis
with col4:
    st.markdown('<div class="feature">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/300x200.png?text=Sleep+Analysis", use_container_width=True)
    st.markdown("<h3>Sleep Analysis</h3>", unsafe_allow_html=True)
    st.markdown("<p>Track your sleep patterns and improve sleep quality.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Login Section
st.markdown("## Login to Your Account")
with st.form("login_form"):
    st.markdown(
        """
        <div class="login-form">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Submit Button
    submit_button = st.form_submit_button("Login")
    if submit_button:
        st.success("Logged in successfully!")  # Placeholder for login logic

    st.markdown(
        """
        <p style="text-align: center; margin-top: 1rem;">
            <a href="#forgot-password" style="color: #2563EB;">Forgot Password?</a>
        </p>
        <p style="text-align: center;">
            Don't have an account? <a href="#signup" style="color: #2563EB;">Sign Up</a>
        </p>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    """
    <div class="footer">
        <p>&copy; 2023 HealthFit. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
