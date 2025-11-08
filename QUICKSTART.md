# 🚀 Quick Start Guide - SnapSkill AI Caller

## ⚡ 5-Minute Setup

### 1. Install Python Packages
```bash
py -3.11 -m pip install -r requirements.txt
```

### 2. Setup Environment Variables
Create `.env` file:
```env
VAPI_API_KEY=your_key_here
VAPI_PHONE_NUMBER_ID=your_phone_id_here
```

### 3. Run the App
```bash
py -3.11 -m streamlit run app.py
```

### 4. Make Your First Call
1. Open browser: http://localhost:8501
2. Select language: Telugu/English/Hindi
3. Enter phone: +91 9876543210
4. Click "Make Call Now"
5. View results!

---

## 📋 Where to Get API Keys

### Vapi API Key
1. Go to: https://dashboard.vapi.ai
2. Login/Signup
3. Settings → API Keys
4. Copy "Private API Key"

### Vapi Phone Number ID
1. Dashboard → Phone Numbers
2. If no number: Click "Buy Phone Number"
3. Select India (+91)
4. Copy the Phone Number ID

---

## 🎯 What It Does

**Fixed Purpose:** SnapSkill Course Reminders

**Calls students in their language to remind them about:**
- Python programming course
- Tomorrow at 10 AM
- At JNTU campus
- Confirms attendance

**Cost:** ₹9.13 per call (~2 minutes)

---

## 🔧 Common Commands

```bash
# Install dependencies
py -3.11 -m pip install -r requirements.txt

# Run app
py -3.11 -m streamlit run app.py

# Test backend only
py -3.11 vapi_caller.py

# Check Python version
py -3.11 --version

# Upgrade packages
py -3.11 -m pip install -r requirements.txt --upgrade
```

---

## ❌ Troubleshooting

**Problem:** Module not found
```bash
py -3.11 -m pip install streamlit requests python-dotenv
```

**Problem:** Can't find .env
- Make sure `.env` file is in same folder as `app.py`
- Copy from `.env.example` template

**Problem:** Invalid phone number
- Format: `+91 9876543210` (with +91)
- Must be 10 digits after +91
- First digit: 6, 7, 8, or 9

**Problem:** Call fails
- Check VAPI_API_KEY in .env
- Check VAPI_PHONE_NUMBER_ID in .env
- Ensure Twilio has balance

---

## 📊 File Overview

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI (RUN THIS) |
| `vapi_caller.py` | Backend logic |
| `.env` | Your API keys (SECRET!) |
| `requirements.txt` | Python packages |

---

## 🎨 Customization

### Change the prompts:
Edit `vapi_caller.py` → `LANGUAGE_CONFIG` → `prompt`

### Change voice:
Edit `vapi_caller.py` → `LANGUAGE_CONFIG` → `voice_id`

### Add language:
Add new entry in `LANGUAGE_CONFIG` dict

---

## 💡 Tips

- ✅ Test with your own number first
- ✅ ElevenLabs free tier = 6-7 calls/month
- ✅ After free tier, costs jump to ₹46.93/call
- ✅ Use Azure TTS to reduce to ₹11.14/call
- ✅ Keep calls under 2 minutes to control costs

---

**Ready to make calls!** 🚀

Just run:
```bash
py -3.11 -m streamlit run app.py
```
