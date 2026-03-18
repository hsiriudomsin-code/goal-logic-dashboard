import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. ตั้งค่าหน้าจอ ---
st.set_page_config(page_title="Football Evolution Dashboard", layout="wide")

# --- 2. CSS ---
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

# --- 3. ACCOUNT DATABASE ---
ACCOUNTS = {
    "FIFA_ADMIN": "FIFA@2026", "GUEST": "FREE", "Man Utd": "MUFC@Scout", "Man City": "MCFC@Etihad",
    "Liverpool": "LFC@Anfield", "Arsenal": "AFC@Gunners", "Chelsea": "CFC@Blues", "Spurs": "THFC@London",
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
    "Spurs": "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Spurs_2017_badge.svg/250px-Spurs_2017_badge.svg.png",
    "Newcastle": "https://upload.wikimedia.org/wikipedia/en/5/56/Newcastle_United_Logo.svg",
    "Aston Villa": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Aston_Villa_FC_new_crest.svg/960px-Aston_Villa_FC_new_crest.svg.png",
    "Brighton": "https://upload.wikimedia.org/wikipedia/en/f/fd/Brighton_%26_Hove_Albion_logo.svg",
    "West Ham": "https://upload.wikimedia.org/wikipedia/en/c/c2/West_Ham_United_FC_logo.svg",
    "Wolves": "https://upload.wikimedia.org/wikipedia/en/f/fc/Wolverhampton_Wanderers.svg",
    "Fulham": "https://upload.wikimedia.org/wikipedia/en/e/eb/Fulham_FC_%28shield%29.svg",
    "Bournemouth": "https://upload.wikimedia.org/wikipedia/en/e/e5/AFC_Bournemouth_%282013%29.svg",
    "Crystal Palace": "https://upload.wikimedia.org/wikipedia/en/a/a2/Crystal_Palace_FC_logo_%282022%29.svg",
    "Brentford": "https://upload.wikimedia.org/wikipedia/en/2/2a/Brentford_FC_crest.svg",
    "Everton": "https://upload.wikimedia.org/wikipedia/en/7/7c/Everton_FC_logo.svg",
    "Nottm Forest": "https://r2.thesportsdb.com/images/media/team/badge/bk4qjs1546440351.png",
    "Ipswich Town": "https://upload.wikimedia.org/wikipedia/en/4/43/Ipswich_Town.svg",
    "Southampton": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c9/FC_Southampton.svg/1280px-FC_Southampton.svg.png",
    "Leicester City": "https://upload.wikimedia.org/wikipedia/en/2/2d/Leicester_City_crest.svg"
}

def get_club_grade(score):
    if score >= 100:
        if score >= 300: return "S", "#FFD700"
        if score >= 250: return "A", "#00FF00"
        if score >= 200: return "B", "#ADFF2F"
    else:
        if score >= 9: return "S", "#FFD700"
        if score >= 8: return "A", "#00FF00"
        if score >= 7: return "B", "#ADFF2F"
        if score >= 6: return "C", "#FFFF00"
    return "D", "#FFA500"

def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.session_state.username = None
    if "REGISTERED_USERS" not in st.session_state:
        st.session_state.REGISTERED_USERS = {}

    if not st.session_state.logged_in:
        st.markdown("<h1 style='text-align:center;color:#FFD700'>🛡️ PREMIER LEAGUE ANALYTICS UNIT</h1>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])
        with tab1:
            col1, col2, col3 = st.columns([1, 1.2, 1])
            with col2:
                with st.form("login_form"):
                    user = st.text_input("Username")
                    pw = st.text_input("Access Key", type="password")
                    if st.form_submit_button("🔐 เข้าสู่ระบบ"):
                        if user in ACCOUNTS and pw == ACCOUNTS[user]:
                            st.session_state.logged_in = True
                            st.session_state.user_role = user
                            st.session_state.username = user
                            st.rerun()
                        elif user in st.session_state.REGISTERED_USERS and pw == st.session_state.REGISTERED_USERS[user]:
                            st.session_state.logged_in = True
                            st.session_state.user_role = "GUEST"
                            st.session_state.username = user
                            st.rerun()
                        else:
                            st.error("Username หรือ Password ไม่ถูกต้อง")
        with tab2:
            col1, col2, col3 = st.columns([1, 1.2, 1])
            with col2:
                with st.form("register_form"):
                    new_user = st.text_input("สร้าง Username")
                    new_pw = st.text_input("สร้าง Password", type="password")
                    confirm_pw = st.text_input("Confirm Password", type="password")
                    if st.form_submit_button("📝 สมัครสมาชิก"):
                        if new_user in ACCOUNTS or new_user in st.session_state.REGISTERED_USERS:
                            st.error("Username นี้มีอยู่แล้ว")
                        elif new_pw != confirm_pw:
                            st.error("Password ไม่ตรงกัน")
                        else:
                            st.session_state.REGISTERED_USERS[new_user] = new_pw
                            st.success("สมัครสมาชิกสำเร็จ")
        return False
    return True

if check_login():
    user_role = st.session_state.user_role
    username = st.session_state.username

    with st.sidebar:
        st.header("🔍 ค้นหา & กรอง")
        st.write(f"ผู้ใช้งาน: **{username}**")
        if st.button("🚪 ออกจากระบบ"):
            st.session_state.logged_in = False
            st.rerun()
        st.divider()
        uploaded_file = st.file_uploader("📂 อัปโหลดไฟล์ (.xlsx)", type=["xlsx"])
        search_player = st.text_input("👤 ชื่อนักเตะ:")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        if "คะแนนรวมทั้งฤดูกาล" in df.columns: target_col = "คะแนนรวมทั้งฤดูกาล"
        elif "คะแนนรวม" in df.columns: target_col = "คะแนนรวม"
        else:
            st.error("❌ ไม่พบคอลัมน์คะแนน")
            st.stop()

        if user_role in ["FIFA_ADMIN", "GUEST"]:
            teams_list = ["ทั้งหมด"] + sorted(df["ทีม"].unique().tolist())
            search_team = st.sidebar.selectbox("🏟️ เลือกทีม:", teams_list)
            if search_team != "ทั้งหมด": df = df[df["ทีม"] == search_team]
        else:
            search_team = user_role
            df = df[df["ทีม"] == user_role]

        if "ตำแหน่ง" in df.columns:
            pos_list = sorted(df["ตำแหน่ง"].unique())
            search_pos = st.sidebar.multiselect("🏃 ตำแหน่ง", pos_list, default=pos_list)
            df = df[df["ตำแหน่ง"].isin(search_pos)]

        if search_player:
            df = df[df["ชื่อนักเตะ"].str.contains(search_player, case=False)]

        if not df.empty:
            if user_role == "FIFA_ADMIN":
                avg_team_score = df[target_col].mean()
                grade, color = get_club_grade(avg_team_score)
                st.markdown(f'<div style="background-color: rgba(0,0,0,0.6); border-radius: 15px; padding: 20px; text-align: center; border: 2px solid {color}; margin-bottom: 25px;"><p style="margin: 0; color: #FFD700; font-size: 14px; letter-spacing: 2px;">⚠️ FIFA CONFIDENTIAL RATING</p><h2 style="margin: 5px 0; color: white;">{search_team} Grade: <span style="color:{color};">{grade}</span></h2></div>', unsafe_allow_html=True)

            best_row = df.loc[df[target_col].idxmax()]

            col_txt, col_img = st.columns([2, 1])
            with col_txt:
                if user_role != "GUEST":
                    st.markdown("<p style='margin-bottom: -10px;'>สูงสุดในกลุ่มนี้</p>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size: 4rem;'>{best_row['ชื่อนักเตะ']}</h1>", unsafe_allow_html=True)
                    st.write(f"🏟️ {best_row['ทีม']} | 🏃 {best_row['ตำแหน่ง']} | ⭐ คะแนนวิเคราะห์: {best_row[target_col]:.1f}")

            with col_img:
                if not (user_role == "GUEST" and search_team == "ทั้งหมด"):
                    l_url = TEAM_LOGOS.get(best_row['ทีม'], "https://upload.wikimedia.org/wikipedia/en/f/f2/Premier_League_Logo.svg")
                    st.image(l_url, width=220)

            st.divider()

            if user_role == "GUEST":
                st.markdown(f"### 📋 สถิตินักเตะ: {search_team}")
                all_possible = ["ชื่อนักเตะ", "ทีม", "ตำแหน่ง", "ประตู", "แอสซิสต์", "เซฟลูก", "ระยะวิ่ง (กม.)"]
                guest_cols = [c for c in all_possible if c in df.columns]
                st.dataframe(df[guest_cols], use_container_width=True)
                st.warning("🔒 ข้อมูลกราฟวิเคราะห์ทางสถิติขอสงวนสิทธิ์สำหรับเจ้าหน้าที่")
            else:
                m1, m2, m3 = st.columns(3)
                avg_n = df[target_col].mean()
                avg_p = df['คะแนนครั้งก่อน'].mean() if 'คะแนนครั้งก่อน' in df.columns else avg_n
                m1.metric("นักเตะที่พบ", f"{len(df)} คน")
                m2.metric("เฉลี่ยล่าสุด", f"{avg_n:.1f}", f"{avg_n - avg_p:.1f}")
                m3.metric("คะแนนสูงสุด", f"{best_row[target_col]:.1f}")

                st.markdown("### 📋 ตารางสถิติและคะแนนวิเคราะห์")
                st.dataframe(df, use_container_width=True)

                st.markdown("### 📈 กราฟเปรียบเทียบฟอร์ม (Internal Use Only)")
                df_p = df.sort_values(target_col, ascending=False).head(15)
                fig = go.Figure()
                if 'คะแนนครั้งก่อน' in df.columns:
                    fig.add_trace(go.Scatter(x=df_p['ชื่อนักเตะ'], y=df_p['คะแนนครั้งก่อน'], name='ครั้งก่อน', line=dict(color='#FF4B4B', dash='dot')))
                fig.add_trace(go.Scatter(x=df_p['ชื่อนักเตะ'], y=df_p[target_col], name='ล่าสุด', line=dict(color='#FFFF00', width=4)))
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0.2)', font=dict(color="white"))
                st.plotly_chart(fig, use_container_width=True)

                st.markdown(f"### 🕸️ โครงสร้างความสามารถรายบุคคล (Radar Chart)")
                p_list = sorted(df["ชื่อนักเตะ"].unique())
                sel_p = st.selectbox("🎯 เลือกนักเตะเพื่อดู Radar Chart:", p_list, index=p_list.index(best_row['ชื่อนักเตะ']))
                p_data = df[df["ชื่อนักเตะ"] == sel_p].iloc[0]

                categories = ['ประตู', 'แอสซิสต์', 'เซฟลูก', 'ใบเหลืองสะสม', 'ลงสนาม (นัด)']
                categories = [c for c in categories if c in df.columns]

                if categories:
                    fig_radar = go.Figure()
                    fig_radar.add_trace(go.Scatterpolar(
                        r=[p_data[c] for c in categories],
                        theta=categories,
                        fill='toself',
                        name=sel_p,
                        line_color='#FFFF00'
                    ))
                    fig_radar.update_layout(
                        polar=dict(
                            bgcolor="rgba(0,0,0,0.5)",
                            radialaxis=dict(visible=True, range=[0, 40], color="white", gridcolor="rgba(255,255,255,0.2)"),
                            angularaxis=dict(color="white")
                        ),
                        showlegend=False,
                        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                        margin=dict(l=80, r=80, t=20, b=20)
                    )
                    st.plotly_chart(fig_radar, use_container_width=True)

            # --- แก้ไข: ตรวจสอบสิทธิ์ก่อนแสดงปุ่ม MoTM ---
            if user_role != "GUEST":
                if st.button("🏆 MoTM"):
                    st.balloons()
                    st.success(f"ผู้เล่นยอดเยี่ยมคือ {best_row['ชื่อนักเตะ']}")
        else: st.error("ไม่พบข้อมูล")
    else: st.info("👈 กรุณาอัปโหลดไฟล์ Excel")
