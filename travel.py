import streamlit as st
import google.generativeai as genai

# ------------------------------
# PAGE CONFIGURATION
# ------------------------------
st.set_page_config(
    page_title="TravelGuideAI - Custom Itineraries",
    page_icon="✈️",
    layout="wide"
)

# ------------------------------
# INITIALIZE GEMINI MODEL
# ------------------------------
def initialize_model():
    """Initialize the Gemini model using Streamlit secrets"""
    try:
        if "GOOGLE_API_KEY" not in st.secrets:
            st.error("⚠️ GOOGLE_API_KEY not found in secrets.toml")
            st.stop()

        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)

        generation_config = {
            "temperature": 0.4,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        
        model = genai.GenerativeModel(
            model_name="models/gemini-flash-lite-latest",
            generation_config=generation_config,
        )


        # Quick test
        model.generate_content("Hello")
        return model

    except Exception as e:
        st.error(f"Error initializing model: {str(e)}")
        return None


# ------------------------------
# GENERATE ITINERARY FUNCTION
# ------------------------------
def generate_itinerary(model, destination, days, nights, interests=""):
    """Generate travel itinerary using Gemini AI"""
    try:
        prompt = f"""
        Create a comprehensive and detailed travel itinerary for a trip to {destination} 
        for {days} days and {nights} nights.

        {f"Special interests/preferences: {interests}" if interests else ""}

        Please structure the itinerary as follows:

        🌟 **DESTINATION OVERVIEW**
        - Brief introduction to {destination}
        - Best time to visit
        - Currency and basic travel info

        📅 **DAY-BY-DAY ITINERARY**
        For each day, include:
        - Morning activities
        - Afternoon attractions
        - Evening recommendations
        - Estimated costs (budget-friendly options)

        🍽️ **DINING RECOMMENDATIONS**
        - Local cuisine highlights
        - Must-try restaurants
        - Street food suggestions

        🏨 **ACCOMMODATION SUGGESTIONS**
        - Different budget ranges
        - Best areas to stay

        🚗 **TRANSPORTATION TIPS**
        - Getting around the city
        - Airport transfers
        - Local transport options

        💡 **TRAVEL TIPS & ESSENTIALS**
        - What to pack
        - Cultural etiquette
        - Safety considerations
        - Money-saving tips

        Make it engaging, practical, and well-organized!
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"Error generating itinerary: {str(e)}")
        return None

# ------------------------------
# LIST AVAILABLE MODELS (DEBUG)
# ------------------------------
def list_available_models():
    """List available Gemini models for debugging"""
    try:
        models = genai.list_models()
        available_models = []
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                available_models.append(model.name)
        return available_models
    except Exception as e:
        st.error(f"Error listing models: {str(e)}")
        return []

# ------------------------------
# MAIN STREAMLIT APP
# ------------------------------
def main():
    # Header
    st.title("🌍 TravelGuideAI")
    st.subheader("Custom Itineraries for Your Next Journey")
    st.markdown("---")

    # Initialize model
    model = initialize_model()
    if not model:
        return

    # Layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 📝 Trip Details")

        # Debug section
        with st.expander("🔧 Debug Info", expanded=False):
            if st.button("List Available Models"):
                available_models = list_available_models()
                if available_models:
                    st.write("Available models:")
                    for model_name in available_models:
                        st.write(f"- {model_name}")
                else:
                    st.write("No models found or error occurred")

        # Input fields
        destination = st.text_input(
            "🎯 Destination:",
            placeholder="e.g., Paris, France"
        )

        col_days, col_nights = st.columns(2)
        with col_days:
            days = st.number_input("📅 Days:", min_value=1, max_value=30, value=3)
        with col_nights:
            nights = st.number_input("🌙 Nights:", min_value=0, max_value=29, value=2)

        interests = st.text_area(
            "🎨 Interests (Optional):",
            placeholder="e.g., museums, food, adventure sports, nightlife",
            height=100
        )

        generate_btn = st.button(
            "✨ Generate Itinerary",
            type="primary",
            use_container_width=True
        )

    with col2:
        st.markdown("### 📋 Your Custom Itinerary")

        if generate_btn:
            if destination.strip() and days > 0 and nights >= 0:
                with st.spinner("🤖 AI is crafting your perfect itinerary..."):
                    itinerary = generate_itinerary(model, destination, days, nights, interests)

                if itinerary:
                    st.markdown(itinerary)

                    # Download option
                    st.download_button(
                        label="📥 Download Itinerary",
                        data=itinerary,
                        file_name=f"{destination.replace(' ', '_')}_itinerary.txt",
                        mime="text/plain"
                    )
            else:
                st.error("⚠️ Please provide a valid destination and trip duration.")

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
            <p>🚀 Powered by Google Gemini AI | Built with Streamlit</p>
            <p>✈️ Happy Travels! 🌟</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
