import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. ตั้งค่าหน้าจอและ CSS ---
st.set_page_config(page_title="Football Evolution Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1e5d1e; background-image: linear-gradient(rgba(0,0,0,0.3) 1px, transparent 1px), linear-gradient(90deg, rgba(0,0,0,0.3) 1px, transparent 1px); background-size: 50px 50px; }
    .main .block-container { background-color: rgba(0, 0, 0, 0.7) !important; border-radius: 20px; padding: 30px !important; margin-top: 20px; border: 1px solid rgba(255,255,255,0.2); }
    h1, h2, h3, p, span, label, .stMarkdown { color: #ffffff !important; text-shadow: 2px 2px 4px #000000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000 !important; }
    [data-testid="stMetricValue"] { color: #ffff00 !important; font-size: 2.5rem !important; font-weight: bold !important; }
    .stDataFrame { background-color: white; border-radius: 10px; }
    [data-testid="stSidebar"] { background-color: #ffffff !important; }
    [data-testid="stSidebar"] * { color: #000000 !important; text-shadow: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ฐานข้อมูลรหัสผ่าน & โลโก้ ---
ACCOUNTS = {
    "FIFA_ADMIN": "FIFA@2026", "GUEST": "FREE",
    "Man Utd": "MUFC@Scout", "Man City": "MCFC@Etihad", "Liverpool": "LFC@Anfield",
    "Arsenal": "AFC@Gunners", "Chelsea": "CFC@Blues", "Spurs": "THFC@London",
    "Newcastle": "NUFC@Magpies", "Aston Villa": "AVFC@Villa", "Brighton": "BHAFC@Seagulls",
    "West Ham": "WHUFC@Irons", "Wolves": "WWFC@Wolves", "Fulham": "FFC@Cottage",
    "Bournemouth": "AFCB@Cherries", "Crystal Palace": "CPFC@Eagles", "Brentford": "BFC@Bees",
    "Everton": "EFC@Toffees", "Nottm Forest": "NFFC@Forest", "Ipswich Town": "ITFC@Tractor",
    "Southampton": "SFC@Saints", "Leicester City": "LCFC@Foxes"
}

TEAM_LOGOS = {
    "Man Utd": "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg",
    "Man City": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
    "Liverpool": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
    "Arsenal": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
    "Chelsea": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
    "Spurs": "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg",
    "Newcastle": "https://upload.wikimedia.org/wikipedia/en/5/56/Newcastle_United_Logo.svg",
    "Aston Villa": "https://upload.wikimedia.org/wikipedia/en/f/f9/Aston_Villa_FC_crest_%282016%29.svg",
    "Brighton": "https://upload.wikimedia.org/wikipedia/en/f/fd/Brighton_%26_Hove_Albion_logo.svg",
    "West Ham": "https://upload.wikimedia.org/wikipedia/en/c/c2/West_Ham_United_FC_logo.svg",
    "Wolves": "https://upload.wikimedia.org/wikipedia/en/f/fc/Wolverhampton_Wanderers.svg",
    "Fulham": "https://upload.wikimedia.org/wikipedia/en/3/3f/Fulham_FC_%28shield%29.svg",
    "Bournemouth": "https://upload.wikimedia.org/wikipedia/en/e/e5/AFC_Bournemouth_%282013%29.svg",
    "Crystal Palace": "https://upload.wikimedia.org/wikipedia/en/a/a2/Crystal_Palace_FC_logo_%282022%29.svg",
    "Brentford": "https://upload.wikimedia.org/wikipedia/en/2/2a/Brentford_FC_crest.svg",
    "Everton": "https://upload.wikimedia.org/wikipedia/en/7/7c/Everton_FC_logo.svg",
    "Nottm Forest": "https://upload.wikimedia.org/wikipedia/en/e/e5/Nottingham_Forest_F.C._logo.svg",
    "Ipswich Town": "https://upload.wikimedia.org/wikipedia/en/4/43/Ipswich_Town.svg",
    "Southampton": "https://upload.wikimedia.org/wikipedia/en/c/c9/Southampton_FC.svg",
    "Leicester City": "https://upload.wikimedia.org/wikipedia/en/2/2d/Leicester_City_crest.svg"
}

# --- 3. ฟังก์ชันล็อกอิน & ตัดเกรด ---
def get_club_grade(score):
    if score >= 9.0: return "S", "#FFD700", "World Class"
    if score >= 8.0: return "A", "#00FF00", "Elite"
    if score >= 7.0: return "B", "#ADFF2F", "Strong"
    if score >= 6.0: return "C", "#FFFF00", "Average"
    if score >= 5.0: return "D", "#FFA500", "Below Average"
    return "F", "#FF4B4B", "Critical"

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_role = None
    if not st.session_state.logged_in:
        st.markdown("<h1 style='text-align: center; color: #FFD700;'>🛡️ PREMIER LEAGUE ANALYTICS UNIT</h1>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1.2, 1])
        with col2:
            with st.form("login_form"):
                user = st.text_input("Username")
                pw = st.text_input("Access Key", type="password")
                btn = st.form_submit_button("🔐 เข้าสู่ระบบ")
                if btn:
                    if user in ACCOUNTS and pw == ACCOUNTS[user]:
                        st.session_state.logged_in = True
                        st.session_state.user_role = user
                        st.rerun()
                    else: st.error("ข้อมูลไม่ถูกต้อง")
        return False
    return True

# --- 4. ส่วนการทำงานหลัก ---
if check_login():
    user_role = st.session_state.user_role

    with st.sidebar:
        st.header("🔍 ค้นหา & กรอง")
        st.write(f"ผู้ใช้งาน: **{user_role}**")
        if st.button("🚪 ออกจากระบบ"):
            st.session_state.logged_in = False
            st.rerun()
        st.divider()
        uploaded_file = st.file_uploader("📂 อัปโหลดไฟล์ (.xlsx)", type=["xlsx"])
        search_player = st.text_input("👤 ชื่อนักเตะ:")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)

        # การกำหนด search_team เพื่อใช้เช็คเงื่อนไขแสดงโลโก้
        if user_role == "FIFA_ADMIN" or user_role == "GUEST":
            teams_list = ["ทั้งหมด"] + sorted(df['ทีม'].unique().tolist())
            search_team = st.sidebar.selectbox("🏟️ เลือกทีม:", teams_list)
            if search_team != "ทั้งหมด":
                df = df[df['ทีม'] == search_team]
        else:
            search_team = user_role
            df = df[df['ทีม'] == user_role]

        if 'ตำแหน่ง' in df.columns:
            all_pos = sorted(df['ตำแหน่ง'].unique().tolist())
            search_pos = st.sidebar.multiselect("🏃 ตำแหน่ง:", all_pos, default=all_pos)
            df = df[df['ตำแหน่ง'].isin(search_pos)]

        if search_player:
            df = df[df['ชื่อนักเตะ'].str.contains(search_player, case=False)]

        if not df.empty:
            # --- 🛡️ FIFA Secret Grade ---
            if user_role == "FIFA_ADMIN":
                avg_team_score = df['คะแนนรวม'].mean()
                grade, color, label = get_club_grade(avg_team_score)
                st.markdown(f'<div style="background-color: rgba(0,0,0,0.6); border-radius: 15px; padding: 20px; text-align: center; border: 2px solid {color}; margin-bottom: 25px;"><p style="margin: 0; color: #FFD700; font-size: 14px; letter-spacing: 2px;">⚠️ FIFA CONFIDENTIAL RATING</p><h2 style="margin: 5px 0; color: white;">{search_team} Grade: <span style="color:{color};">{grade}</span></h2></div>', unsafe_allow_html=True)

            # --- ⚽ ส่วน Header (ปรับปรุงเพื่อความคลีนของ GUEST) ---
            best_row = df.loc[df['คะแนนรวม'].idxmax()]
            col_txt, col_img = st.columns([2, 1])

            with col_txt:
                if user_role != "GUEST":
                    # โชว์ข้อมูลเต็มเฉพาะ ADMIN หรือ CLUB
                    st.markdown("<p style='margin-bottom: -10px;'>สูงสุดในกลุ่มนี้</p>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size: 4rem;'>{best_row['ชื่อนักเตะ']}</h1>", unsafe_allow_html=True)
                    st.write(f"🏟️ {best_row['ทีม']} | 🏃 {best_row['ตำแหน่ง']} | ⭐ คะแนนวิเคราะห์: {best_row['คะแนนรวม']:.1f}")
                else:
                    # GUEST จะไม่เห็นข้อความใดๆ เลย
                    st.write("")

            with col_img:
                # เงื่อนไข: GUEST จะเห็นโลโก้ก็ต่อเมื่อมีการเลือกทีมแล้วเท่านั้น (ไม่ใช่ "ทั้งหมด")
                if user_role == "GUEST" and search_team == "ทั้งหมด":
                    st.write("")
                else:
                    l_url = TEAM_LOGOS.get(best_row['ทีม'], "https://upload.wikimedia.org/wikipedia/en/f/f2/Premier_League_Logo.svg")
                    st.image(l_url, width=220)

            st.divider()

            if user_role == "GUEST":
                st.markdown(f"### 📋 สถิตินักเตะพรีเมียร์ลีก: {search_team}")
                public_cols = ['ชื่อนักเตะ', 'ทีม', 'ตำแหน่ง', 'ประตู', 'แอสซิสต์', 'เซฟลูก', 'ระยะวิ่ง (กม.)']
                st.dataframe(df[public_cols], use_container_width=True)
                st.warning("🔒 ข้อมูลคะแนนวิเคราะห์และกราฟเปรียบเทียบ สงวนสิทธิ์สำหรับเจ้าหน้าที่")
            else:
                m1, m2, m3 = st.columns(3)
                avg_n, avg_p = df['คะแนนรวม'].mean(), df['คะแนนครั้งก่อน'].mean()
                m1.metric("นักเตะที่พบ", f"{len(df)} คน")
                m2.metric("เฉลี่ยล่าสุด", f"{avg_n:.1f}", f"{avg_n - avg_p:.1f}")
                m3.metric("คะแนนสูงสุด", f"{best_row['คะแนนรวม']:.1f}")

                st.markdown("### 📋 ตารางสถิติและคะแนนวิเคราะห์")
                st.dataframe(df, use_container_width=True)

                st.markdown("### 📈 กราฟเปรียบเทียบฟอร์ม (Internal Use Only)")
                df_p = df.sort_values('คะแนนรวม', ascending=False).head(15)
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_p['ชื่อนักเตะ'], y=df_p['คะแนนครั้งก่อน'], name='ครั้งก่อน', line=dict(color='#FF4B4B', dash='dot')))
                fig.add_trace(go.Scatter(x=df_p['ชื่อนักเตะ'], y=df_p['คะแนนรวม'], name='ล่าสุด', line=dict(color='#FFFF00', width=4)))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0.2)', font=dict(color="white"))
                st.plotly_chart(fig, use_container_width=True)

                if st.button("🏆 MoTM"):
                    st.balloons()
                    st.success(f"ผู้เล่นยอดเยี่ยมคือ {best_row['ชื่อนักเตะ']}! 🎉")
        else: st.error("ไม่พบข้อมูล")
    else: st.info("👈 กรุณาอัปโหลดไฟล์ Excel เพื่อเริ่มการวิเคราะห์")