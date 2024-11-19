import streamlit as st
import openai

# Replace with your actual OpenAI API key
openai.api_key = st.secrets["mykey"]

# Define electronic product categories, features, benefits, and use cases
product_categories = ["Smartphones", "Laptops", "Smartwatches", "Headphones", "Gaming Consoles"]
product_features = [
    "Long battery life", 
    "High-resolution display", 
    "Fast charging", 
    "Lightweight design", 
    "Advanced noise cancellation"
]
product_benefits = [
    "Improved productivity", 
    "Seamless entertainment", 
    "Enhanced health tracking", 
    "Immersive gaming", 
    "Clearer communication"
]
use_cases = ["Work from home", "Fitness tracking", "Travel", "Gaming", "Daily communication"]
budget_options = ["Budget-friendly", "Mid-range", "Premium", "Luxury"]
tones = ["Professional", "Friendly", "Tech-savvy", "Enthusiastic"]

# Function to generate product recommendation
def generate_recommendation(category, features, benefits, use_case, budget, tone):
    prompt = f"""
    You're a virtual assistant helping users find the best electronic product for their needs.

    **Product category:** {category}
    **Key features:** {', '.join(features)}
    **Benefits:** {', '.join(benefits)}
    **Use case:** {use_case}
    **Budget preference:** {budget}
    **Tone:** {tone}

    Provide a personalized product recommendation with a detailed explanation of why it matches their preferences.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a product recommendation expert."},
            {"role": "user", "content": prompt}
        ]
    )
    recommendation = response['choices'][0]['message']['content']
    return recommendation

# Streamlit UI
st.title("Virtual Electronic Product Recommender")

selected_category = st.selectbox("Product Category:", product_categories)
selected_features = st.multiselect("Key Features:", product_features)
selected_benefits = st.multiselect("Product Benefits:", product_benefits)
selected_use_case = st.selectbox("Use Case:", use_cases)
selected_budget = st.selectbox("Budget Preference:", budget_options)
selected_tone = st.selectbox("Tone:", tones)

if st.button("Get Recommendation"):
    recommendation = generate_recommendation(
        selected_category, selected_features, selected_benefits, selected_use_case, selected_budget, selected_tone
    )
    st.subheader("Recommended Product:")
    st.write(recommendation)
