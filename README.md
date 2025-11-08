# 📞 DS AI Caller

Automated course reminder calling system with multi-language support (Telugu, English, Hindi).

## 🎯 Features

- ✅ **Multi-language Support**: Telugu, English, Hindi
- ✅ **Simple UI**: Just select language and enter phone number
- ✅ **Fixed Purpose**: Course reminder calls (hardcoded prompts)
- ✅ **Real-time Results**: View call status, duration, and cost
- ✅ **Cost Tracking**: ~₹9.13 per call
- ✅ **Professional Voice**: ElevenLabs AI voices
- ✅ **Smart AI**: GPT-4o powered conversations

## 📁 Project Structure

```
AI_caller/
├── app.py                 # Streamlit UI (main file to run)
├── vapi_caller.py         # Backend logic with Vapi integration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🚀 Setup Instructions

### Step 1: Prerequisites

- Python 3.9 or higher
- Vapi account with API key
- Twilio phone number (via Vapi)

### Step 2: Clone/Download Project

```bash
# Navigate to project directory
cd AI_caller
```

### Step 3: Install Dependencies

```bash
# For Python 3.11
py -3.11 -m pip install -r requirements.txt

# Or for default Python
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Copy `.env.example` to `.env`:
```bash
copy .env.example .env
```

2. Edit `.env` and fill in your values:
```env
VAPI_API_KEY=your_actual_vapi_api_key
VAPI_PHONE_NUMBER_ID=your_actual_phone_number_id
```

**Where to get these values:**
- **VAPI_API_KEY**: Login to https://dashboard.vapi.ai → Settings → API Keys
- **VAPI_PHONE_NUMBER_ID**: Dashboard → Phone Numbers → Copy ID

### Step 5: Run the Application

```bash
# For Python 3.11
py -3.11 -m streamlit run app.py

# Or for default Python
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📱 How to Use

### Making a Call

1. **Select Language**: Choose Telugu, English, or Hindi
2. **Enter Phone Number**: Format `+91 9876543210`
3. **Click "Make Call Now"**
4. **View Results**: Status, duration, cost displayed immediately

### Call Flow

```
User Opens App
    ↓
Selects Language (Telugu/English/Hindi)
    ↓
Enters Phone Number (+91 XXXXXXXXXX)
    ↓
Clicks "Make Call"
    ↓
System:
  - Creates language-specific assistant
  - Makes call via Vapi
  - Uses fixed course reminder script
    ↓
Shows Results:
  - Status (Answered/Not Answered)
  - Duration (e.g., 1m 45s)
  - Cost (e.g., ₹8.67)
  - Call details
```

## 💰 Cost Breakdown

| Component | Cost per Call |
|-----------|---------------|
| VAPI Platform | ₹4.20 |
| Twilio (2 min) | ₹2.52 |
| GPT-4o | ₹0.42 |
| ElevenLabs (free tier) | ₹0.00 |
| Deepgram STT | ₹0.72 |
| Phone Number | ₹1.27 |
| **Total** | **₹9.13** |

**Note**: Costs may vary based on:
- Call duration
- Voice provider (free tier has limits)
- Number of calls per month

## 🎨 Customization

### Changing the Purpose

Edit the prompts in `vapi_caller.py`:

```python
LANGUAGE_CONFIG = {
    "English": {
        "prompt": """Your custom prompt here..."""
    }
}
```

### Adding New Languages

1. Add new language config in `vapi_caller.py`:
```python
"Tamil (தமிழ்)": {
    "voice_id": "tamil_voice_id",
    "language_code": "ta",
    "voice_name": "Tamil Voice",
    "prompt": "Your Tamil prompt..."
}
```

2. Add to dropdown in `app.py`:
```python
language = st.selectbox(
    "Choose language",
    ["Telugu", "English", "Hindi", "Tamil"]
)
```

### Changing Voice

Get ElevenLabs voice IDs from: https://api.elevenlabs.io/v1/voices

Update `voice_id` in `LANGUAGE_CONFIG`

## 🔧 Troubleshooting

### Issue: "Failed to create assistant"
**Solution**: Check if `VAPI_API_KEY` is correct in `.env`

### Issue: "Failed to make call"
**Solution**: 
- Verify `VAPI_PHONE_NUMBER_ID` is correct
- Ensure phone number format is `+91XXXXXXXXXX`
- Check Twilio account has sufficient balance

### Issue: "Invalid phone number"
**Solution**: 
- Must start with `+91`
- Must have exactly 10 digits after +91
- First digit should be 6, 7, 8, or 9

### Issue: Module not found
**Solution**:
```bash
py -3.11 -m pip install -r requirements.txt --upgrade
```

## 📊 Production Deployment

### Option 1: Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your repo
4. Add secrets (VAPI_API_KEY, etc.) in settings
5. Deploy!

### Option 2: Local Deployment

```bash
# Run on specific port
streamlit run app.py --server.port 8080

# Run in background
nohup streamlit run app.py &
```

## 🔐 Security Notes

- ✅ Never commit `.env` file to Git
- ✅ `.env` is in `.gitignore` by default
- ✅ All API calls use HTTPS
- ✅ Phone numbers are validated before calling
- ✅ All calls are logged for audit

## 📞 Call Script (Fixed Purpose)

### Telugu Script:
```
నమస్కారం! నేను SnapSkill నుండి కాల్ చేస్తున్నాను.
మీ Python programming కోర్సు గురించి గుర్తు చేయడానికి...
రేపు ఉదయం 10 గంటలకు JNTU క్యాంపస్‌లో క్లాస్ ఉంది.
మీరు క్లాస్‌కి రాగలరా?
```

### English Script:
```
Hello! I'm calling from SnapSkill.
I'm calling to remind you about your Python programming course.
The class is scheduled for tomorrow at 10 AM at JNTU campus.
Will you be able to attend the class?
```

### Hindi Script:
```
नमस्ते! मैं SnapSkill से बात कर रही हूं।
मैं आपको Python programming कोर्स के बारे में याद दिलाने के लिए...
कल सुबह 10 बजे JNTU कैंपस में क्लास है।
क्या आप क्लास में आ पाएंगे?
```

## 🎯 Use Cases

- **Educational Institutions**: Course reminders, exam alerts
- **Training Centers**: Class notifications
- **Coaching Centers**: Batch schedule reminders
- **Online Courses**: Live session reminders

## 📈 Future Enhancements

- [ ] Batch calling (multiple numbers at once)
- [ ] Google Sheets integration
- [ ] Call scheduling (call at specific time)
- [ ] SMS backup (if call not answered)
- [ ] Call analytics dashboard
- [ ] Export call logs to Excel

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Vapi documentation: https://docs.vapi.ai
3. Check ElevenLabs voice IDs: https://api.elevenlabs.io/v1/voices

## 📝 Version History

- **v1.0.0** (Current)
  - Initial release
  - 3 languages supported
  - Fixed course reminder purpose
  - Simple 2-input UI

## 📄 License

This project is for internal use by SnapSkill.

---

**Built with ❤️ **  
