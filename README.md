# 🌍 TravelGuideAI - Custom Itineraries for Your Next Journey

An AI-powered travel itinerary generator that creates personalized travel plans using Google's Gemini Pro LLM and Streamlit.

## 🎯 Project Overview

TravelGuideAI solves the complex and time-consuming process of travel planning by providing:
- **Automated itinerary generation** based on destination, duration, and preferences
- **Personalized recommendations** for attractions, dining, and activities
- **Professional travel planning** for agencies and individual travelers
- **Interactive web interface** built with Streamlit

## ✨ Features

- 🤖 **AI-Powered Planning**: Uses Google Gemini 1.5 Flash for intelligent itinerary generation
- 🎨 **Customizable Preferences**: Add personal interests and travel style preferences
- 📱 **User-Friendly Interface**: Clean, responsive Streamlit web application
- 📥 **Export Functionality**: Download generated itineraries as text files
- 🌟 **Comprehensive Details**: Includes attractions, dining, accommodation, and travel tips

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **Google Gemini Pro (1.5 Flash)** - Generative AI model
- **Google Generative AI API** - AI model integration
- **python-dotenv** - Environment variable management

## 📁 Project Structure

```
TravelGuideAI/
│
├── travel.py              # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # Project documentation
└── .env                  # Your API keys (create this file)
```

## ⚙️ Setup Instructions

### Step 1: Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd TravelGuideAI

# Or download and extract the files
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Get Google Gemini API Key
1. Visit [Google AI Studio](https://developers.generativeai.google/)
2. Click "Get API Key"
3. Create a new API key
4. Copy the API key securely

### Step 4: Configure Environment Variables
1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
2. Edit `.env` and add your API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### Step 5: Run the Application
```bash
streamlit run travel.py
```

The application will open in your browser at `http://localhost:8501`

## 🚀 Usage

1. **Enter Destination**: Type your desired travel destination
2. **Set Duration**: Specify the number of days and nights
3. **Add Preferences** (Optional): Include interests like "museums, food, adventure"
4. **Generate**: Click "Generate Itinerary" to create your custom plan
5. **Download**: Save the itinerary as a text file for offline use

## 📋 Sample Output

The AI generates comprehensive itineraries including:

- **Destination Overview**: Introduction and travel basics
- **Day-by-Day Schedule**: Morning, afternoon, and evening activities
- **Dining Recommendations**: Local cuisine and restaurant suggestions
- **Accommodation Options**: Hotels across different budget ranges
- **Transportation Tips**: Getting around and airport transfers
- **Travel Essentials**: Packing lists, cultural tips, and safety advice

## 🎯 Use Cases

### Individual Travelers
- Quick trip planning without extensive research
- Personalized recommendations based on interests
- Structured itineraries for better time management

### Travel Agencies
- Automated itinerary creation for clients
- Time-saving tool for travel consultants
- Professional-quality travel plans

### Content Creators
- Generate travel guides for websites
- Create engaging travel blog content
- Produce destination-specific recommendations

## 🔧 Customization

You can modify the AI prompt in `travel.py` to:
- Change the output format
- Add specific types of recommendations
- Include budget considerations
- Adjust the level of detail

## 🚨 Troubleshooting

**API Key Issues:**
- Ensure your `.env` file contains the correct API key
- Verify the API key is active in Google AI Studio

**Installation Problems:**
- Use `pip install --upgrade pip` before installing requirements
- Try creating a virtual environment first

**Streamlit Issues:**
- Clear browser cache if the app doesn't load properly
- Check that port 8501 is available

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for improvements.

## 📞 Support

For questions or support, please open an issue in the project repository.

---

**Happy Travels! ✈️🌟**