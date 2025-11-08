"""
SnapSkill AI Caller - Streamlit App
Simple UI for making course reminder calls in multiple languages
"""

import streamlit as st
import time
import os
from datetime import datetime
from vapi_caller import make_call_with_language, validate_phone_number

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="SnapSkill AI Caller",
    page_icon="📞",
    layout="centered"
)

# ==========================================
# SIDEBAR - EXCEL DOWNLOAD
# ==========================================
with st.sidebar:
    st.header("📊 Call Summaries")
    
    # Check if Excel file exists
    excel_file = "call_summaries.xlsx"
    if os.path.exists(excel_file):
        # Get file size and modification time
        file_size = os.path.getsize(excel_file) / 1024  # KB
        mod_time = datetime.fromtimestamp(os.path.getmtime(excel_file))
        
        st.success(f"✅ Excel file available")
        st.caption(f"Size: {file_size:.1f} KB")
        st.caption(f"Last updated: {mod_time.strftime('%Y-%m-%d %H:%M')}")
        
        # Download button
        with open(excel_file, "rb") as file:
            st.download_button(
                label="📥 Download Excel File",
                data=file,
                file_name=f"call_summaries_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        
        st.info("💡 Excel contains all call summaries with transcripts")
    else:
        st.info("📝 No calls yet. Excel file will be created after first call.")
    
    st.markdown("---")
    st.caption("SnapSkill AI Caller v1.0")


# ==========================================
# HEADER
# ==========================================
st.title("📞 SnapSkill AI Caller")
st.markdown("**Automated Course Reminder Calls**")
st.markdown("---")

# ==========================================
# LANGUAGE SELECTION
# ==========================================
st.subheader("🌍 Select Language")
language = st.selectbox(
    "Choose the language for the call",
    ["English", "Telugu (తెలుగు)",  "Hindi (हिंदी)"],
    label_visibility="collapsed"
)

# ==========================================
# PHONE NUMBER INPUT
# ==========================================
st.subheader("📱 Phone Number")
phone = st.text_input(
    "Enter phone number with country code",
    placeholder="+91 9876543210",
    max_chars=15,
    help="Format: +91 followed by 10-digit number",
    label_visibility="collapsed"
)

# ==========================================
# COST DISPLAY
# ==========================================
st.caption("⚠️ Estimated cost: ₹9.13 per call | Duration: ~2 minutes")

# ==========================================
# MAKE CALL BUTTON
# ==========================================
st.markdown("---")

if st.button("📞 Make Call Now", type="primary", use_container_width=True):
    
    # Validate phone number
    is_valid, error_message = validate_phone_number(phone)
    
    if not is_valid:
        st.error(f"❌ {error_message}")
    
    else:
        # Show calling status
        with st.spinner(f"📞 Calling {phone} in {language}..."):
            try:
                # Make the call
                result = make_call_with_language(
                    language=language,
                    phone=phone
                )
                
                # Simulate call processing
                time.sleep(2)
                
            except Exception as e:
                st.error(f"❌ Call failed: {str(e)}")
                st.stop()
        
        # ==========================================
        # DISPLAY CALL RESULTS
        # ==========================================
        
        # Status with appropriate emoji
        if result['status'] in ['ended', 'completed']:
            st.success("✅ Call Completed Successfully!")
        elif result['status'] == 'busy':
            st.warning("📵 Customer was busy")
        elif result['status'] == 'no-answer':
            st.warning("📞 No answer - Customer didn't pick up")
        elif result['status'] == 'failed':
            st.error("❌ Call failed")
        else:
            st.info(f"ℹ️ Call status: {result['status']}")
        
        # Metrics Row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            # Status with proper emoji
            status_display = result['status'].replace('-', ' ').title()
            if result['status'] in ['ended', 'completed']:
                status_emoji = "✅"
            elif result['status'] in ['busy', 'no-answer']:
                status_emoji = "⚠️"
            else:
                status_emoji = "❌"
            st.metric("Status", f"{status_emoji} {status_display}")
        
        with col2:
            st.metric("Duration", result['duration'])
        
        with col3:
            st.metric("Cost", f"₹{result['cost']}")
        
        with col4:
            st.metric("Language", language.split(" ")[0])
        
        # ==========================================
        # DETAILED CALL INFORMATION
        # ==========================================
        st.markdown("---")
        
        with st.expander("📊 Detailed Call Report", expanded=True):
            st.markdown("#### Call Information")
            
            info_col1, info_col2 = st.columns(2)
            
            with info_col1:
                st.write(f"**Call ID:** `{result['call_id'][:20]}...`")
                st.write(f"**Phone:** {phone}")
                st.write(f"**Purpose:** Feedback Collection")
                st.write(f"**End Reason:** {result.get('end_reason', 'N/A')}")
            
            with info_col2:
                st.write(f"**Started:** {result['start_time']}")
                st.write(f"**Ended:** {result['end_time']}")
                st.write(f"**Voice:** {result['voice_name']}")
                st.write(f"**Actual Cost:** ₹{result['cost']} (real duration)")
            
            # Recording (if available)
            if result.get('recording_url'):
                st.markdown("#### 🎧 Call Recording")
                st.audio(result['recording_url'])
            
            # Summary (if available)
            if result.get('summary'):
                st.markdown("#### 📝 Call Summary")
                st.info(result['summary'])
            
            # Transcript (if available)
            if result.get('transcript'):
                st.markdown("#### 💬 Full Transcript")
                st.text_area(
                    "Conversation",
                    value=result['transcript'],
                    height=200,
                    label_visibility="collapsed"
                )
            
            # Full JSON data
            if st.checkbox("Show raw data"):
                st.json(result)
        
        # ==========================================
        # ACTION BUTTONS
        # ==========================================
        st.markdown("---")
        
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            if st.button("📞 Make Another Call", use_container_width=True):
                st.rerun()
        
        with btn_col2:
            if st.button("📥 Download Report", use_container_width=True):
                # Create downloadable report
                report = f"""
SnapSkill Call Report
====================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Phone: {phone}
Language: {language}
Status: {result['status']}
Duration: {result['duration']}
Cost: ₹{result['cost']}
Call ID: {result['call_id']}
                """
                st.download_button(
                    label="Download TXT Report",
                    data=report,
                    file_name=f"call_report_{result['call_id'][:8]}.txt",
                    mime="text/plain"
                )

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.caption("SnapSkill AI Caller v1.0")
