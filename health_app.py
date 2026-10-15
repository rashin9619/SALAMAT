import streamlit as st

# --- تنظیمات صفحه و استایل بنفش ---
st.set_page_config(page_title="سیستم ارزیابی سلامت", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #2E0854; 
        color: white;
    }
    [data-testid="stSidebar"] {
        background-color: #4B0082 !important;
    }
    h1, h2, h3 {
        color: #E0B0FF !important;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #8A2BE2;
        color: white;
        border-radius: 10px;
        border: none;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div {
        background-color: #ffffff !important;
        color: #2E0854 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # --- ۱. سایدبار (اطلاعات ضروری کاربر) ---
    st.sidebar.header("👤 اطلاعات شناسایی")
    name = st.sidebar.text_input("نام و نام خانوادگی:")
    age = st.sidebar.number_input("سن:", min_value=0, max_value=120, value=0)
    gender = st.sidebar.selectbox("جنسیت:", ["انتخاب نشده", "زن", "مرد", "سایر"])

    # --- ۲. بخش اصلی: دریافت علائم ---
    st.title("🩺 سیستم ارزیابی علائم سلامت")
    st.write("---")
    
    st.subheader("📋 لیست علائم")
    
    symptoms_list = {
        "آب‌بینی": 15,
        "درد پا": 25,
        "درد گوش": 30,
        "سوزش گلو": 20,
        "ریزش مو": 10,
        "تب بالا": 35,
        "سرفه شدید": 20,
        "درد قفسه سینه": 50,
        "سرگیجه": 15
    }

    selected_symptoms = []
    cols = st.columns(3) 
    
    for i, (symptom, score) in enumerate(symptoms_list.items()):
        with cols[i % 3]:
            if st.checkbox(symptom):
                selected_symptoms.append((symptom, score))

    st.write("---")
    
    # --- ۳. مرحله اعتبارسنجی و ثبت ---
    if st.button("🚀 ثبت علائم و بررسی وضعیت"):
        # اصلاح مورد اول طبق درخواست شما (پیام خطای خاص)
        if not name or age <= 0 or gender == "انتخاب نشده":
            st.error("❌ خطای ورود: لطفاً ابتدا اطلاعات شناسایی را در اطلاعات شناسایی تکمیل کنید!")
        
        elif len(selected_symptoms) == 0:
            st.error("❌ خطا: شما هیچ علامتی را انتخاب نکرده‌اید. لطفا علائم خود را تیک بزنید.")
            
        else:
            total_score = sum(item[1] for item in selected_symptoms)
            symptom_names = [item[0] for item in selected_symptoms]
            
            st.balloons()
            st.success(f"اطلاعات برای {name} با موفقیت ثبت شد.")
            
            st.divider()
            st.subheader("🔍 نتیجه تحلیل هوشمند:")

            # --- ۴. تحلیل بر اساس شدت و اضافه کردن بخش دارو ---
            if total_score >= 60:
                st.error(f"🚨 وضعیت شما: **بسیار حساس!**")
                st.markdown(f"""
                **شدت بیماری:** {total_score}  
                **تحلیل:** با توجه به علائم ({', '.join(symptom_names)})، وضعیت شما جدی است.  
                **⚠️ دستورات پزشکی:**  
                - بلافاصله به پزشک مراجعه کنید.  
                - از فعالیت‌های فیزیکی سنگین خودداری کنید.  
                **💊 داروهای پیشنهادی:**  
                - استفاده از مسکن‌های قوی (تحت نظر پزشک).  
                - داروهای ضد التهاب ضروری هستند.
                """)
            elif total_score >= 30:
                st.warning(f"🟡 وضعیت شما: **نیاز به مراقبت**")
                st.markdown(f"""
                **شدت بیماری:** {total_score}  
                **تحلیل:** علائم شما نشان‌دهنده یک بیماری متوسط است.  
                **💡 توصیه‌ها:**  
                - فعالیت‌های سنگین را کم کنید.  
                - حتماً مایعات گرم مصرف کنید.  
                **💊 داروهای پیشنهادی:**  
                - قرص‌های ضد حساسیت یا قرص‌های ضد تب.
                """)
            else:
                st.info(f"✅ وضعیت شما: **خوب/خفیف**")
                st.markdown(f"""
                **شدت بیماری:** {total_score}  
                **تحلیل:** علائم شما بسیار ناچیز است.  
                **🌿 توصیه‌ها:**  
                - استراحت کافی داشته باشید.  
                - رژیم غذایی سالم‌تر داشته باشید.  
                **💊 داروهای پیشنهادی:**  
                - نیازی به دارو نیست، فقط ویتامین‌های تقویت‌کننده.
                """)

if __name__ == "__main__":
    main()
