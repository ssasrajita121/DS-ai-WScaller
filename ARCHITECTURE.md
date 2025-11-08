# 🏗️ SnapSkill AI Caller - Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER (Browser)                       │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │         Streamlit UI (app.py)                   │   │
│  │                                                 │   │
│  │  Language Selection: [Telugu ▼]                │   │
│  │  Phone Number: [+91 __________]                │   │
│  │                                                 │   │
│  │  [Make Call Now]                               │   │
│  └─────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              Backend (vapi_caller.py)                   │
│                                                         │
│  1. Get Language Config                                │
│     ├─ Telugu → Telugu voice + Telugu prompt          │
│     ├─ English → English voice + English prompt       │
│     └─ Hindi → Hindi voice + Hindi prompt             │
│                                                         │
│  2. Create Vapi Assistant                              │
│     ├─ Model: GPT-4o                                   │
│     ├─ Voice: ElevenLabs                               │
│     └─ Prompt: Fixed SnapSkill course reminder         │
│                                                         │
│  3. Make Call via Vapi API                             │
│                                                         │
│  4. Return Results                                     │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  Vapi Platform                          │
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐             │
│  │   OpenAI        │  │  ElevenLabs     │             │
│  │   GPT-4o        │  │  Voice          │             │
│  │  (AI Brain)     │  │  (Speech)       │             │
│  └─────────────────┘  └─────────────────┘             │
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐             │
│  │   Deepgram      │  │   Twilio        │             │
│  │  (Listen)       │  │  (Phone)        │             │
│  └─────────────────┘  └─────────────────┘             │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                Customer Phone                           │
│                                                         │
│  📞 Call received                                       │
│  🎤 AI speaks in selected language                     │
│  👂 Customer responds                                   │
│  🤖 AI understands and replies                         │
└─────────────────────────────────────────────────────────┘
```

---

## Data Flow

### 1. User Input
```python
{
    "language": "Telugu (తెలుగు)",
    "phone": "+91 9876543210"
}
```

### 2. Language Config Selection
```python
{
    "voice_id": "telugu_voice_id",
    "language_code": "te",
    "prompt": "నమస్కారం! నేను SnapSkill నుండి..."
}
```

### 3. Vapi Assistant Creation
```python
{
    "name": "SnapSkill Caller - Telugu",
    "model": {
        "provider": "openai",
        "model": "gpt-4o",
        "messages": [{"role": "system", "content": "Telugu prompt"}]
    },
    "voice": {
        "provider": "11labs",
        "voiceId": "telugu_voice_id"
    }
}
```

### 4. Call Initiation
```python
{
    "assistantId": "asst_xxx",
    "phoneNumberId": "pn_xxx",
    "customer": {"number": "+91 9876543210"}
}
```

### 5. Call Result
```python
{
    "status": "completed",
    "duration": "1m 45s",
    "cost": 8.67,
    "call_id": "call_xxx",
    "recording_url": "https://..."
}
```

---

## Component Breakdown

### Frontend (app.py)
- **Technology**: Streamlit
- **Purpose**: Simple UI for user input
- **Features**:
  - Language dropdown
  - Phone input with validation
  - Call button
  - Result display

### Backend (vapi_caller.py)
- **Technology**: Python + Requests
- **Purpose**: Vapi API integration
- **Functions**:
  - `validate_phone_number()` - Input validation
  - `create_assistant()` - Create language-specific assistant
  - `make_vapi_call()` - Initiate outbound call
  - `calculate_cost()` - Calculate call charges

### External Services
1. **Vapi**: Call orchestration
2. **OpenAI GPT-4o**: Conversation AI
3. **ElevenLabs**: Voice synthesis
4. **Deepgram**: Speech recognition
5. **Twilio**: Phone infrastructure

---

## Security Flow

```
User Input → Validation → Sanitization → API Call → Result
     ↓           ↓             ↓            ↓         ↓
  .env      Phone format   Remove chars  HTTPS    Display
```

**Security Features:**
- ✅ Environment variables for secrets
- ✅ Phone number validation
- ✅ HTTPS for all API calls
- ✅ No sensitive data in logs
- ✅ Input sanitization

---

## Cost Calculation Flow

```
Call Duration (seconds)
        ↓
Convert to minutes
        ↓
Multiply by rate (₹4.565/min)
        ↓
Round to 2 decimals
        ↓
Display to user
```

**Cost Components:**
- VAPI Platform: ₹4.20
- Twilio: ₹2.52 (2 min avg)
- GPT-4o: ₹0.42
- ElevenLabs: ₹0.00 (free tier)
- Deepgram: ₹0.72
- Phone rental: ₹1.27
- **Total: ₹9.13**

---

## Language Processing Flow

```
User Selects "Telugu"
        ↓
System Fetches Telugu Config
        ↓
┌─────────────────────────────┐
│ Voice: Telugu Female Voice  │
│ Code: te-IN                 │
│ Prompt: Telugu script       │
└─────────────────────────────┘
        ↓
Creates Vapi Assistant
        ↓
Makes Call in Telugu
        ↓
Customer Hears Telugu Voice
```

---

## Error Handling Flow

```
User Input
    ↓
┌─ Validation ─┐
│ Phone valid? │─ NO → Show Error
└──────────────┘
    ↓ YES
┌─ API Call ───┐
│ Success?     │─ NO → Show Error + Retry
└──────────────┘
    ↓ YES
┌─ Result ─────┐
│ Show to User │
└──────────────┘
```

**Error Types:**
1. **Validation Errors**: Invalid phone format
2. **API Errors**: Vapi connection issues
3. **Call Errors**: Failed to connect
4. **Network Errors**: Timeout, no internet

---

## Scalability Considerations

### Current (Single Call)
```
1 User → 1 Call → 1 Result
Time: ~2 minutes per call
```

### Future (Batch Calling)
```
1 User → Upload CSV → 100 Calls → 100 Results
Time: All calls in parallel
```

### Production Scale
```
Multiple Users → Queue System → Async Processing → Dashboard
```

---

## File Dependencies

```
app.py
├── imports streamlit
├── imports vapi_caller
│   ├── imports requests
│   ├── imports os
│   └── imports re
└── uses .env
    ├── VAPI_API_KEY
    └── VAPI_PHONE_NUMBER_ID
```

---

## Deployment Architecture

### Local Development
```
Developer PC
├── Python 3.11
├── Streamlit (localhost:8501)
├── .env (secrets)
└── Internet → Vapi API
```

### Production (Streamlit Cloud)
```
Streamlit Cloud
├── app.py
├── vapi_caller.py
├── requirements.txt
└── Secrets (in dashboard)
    ↓
Internet → Vapi API
    ↓
Twilio → Customer Phone
```

---

## Key Design Decisions

1. **Fixed Purpose**: Hardcoded prompts for consistency
2. **Simple UI**: Only 2 inputs to minimize user errors
3. **Language First**: Support local languages
4. **No Customization**: Prevents spam/abuse
5. **Immediate Feedback**: Show results instantly
6. **Cost Transparency**: Display cost before calling

---

**This architecture ensures:**
- ✅ Simple user experience
- ✅ Reliable call quality
- ✅ Cost predictability
- ✅ Easy maintenance
- ✅ Secure operations
