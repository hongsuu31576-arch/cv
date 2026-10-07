import streamlit as st
from PIL import Image
import os

# Biến WSGI bắt buộc để Vercel không bị lỗi build "Missing app / handler"
app = st

# ==========================================
# 1. CẤU HÌNH TRANG WEB
# ==========================================
st.set_page_config(
    page_title="Nguyễn Thành Huy | Personal Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CUSTOM CSS GIAO DIỆN HIỆN ĐẠI
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .header-box {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 30px;
        border-radius: 16px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    .main-title {
        font-size: 2.6rem;
        font-weight: 700;
        margin-bottom: 5px;
        color: #FFFFFF;
    }
    .sub-title {
        font-size: 1.25rem;
        color: #E0E7FF;
        font-weight: 400;
        margin-bottom: 15px;
    }
    .bio-text {
        font-size: 1rem;
        line-height: 1.6;
        color: #F3F4F6;
    }

    .custom-card {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .custom-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.08);
    }
    .card-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 8px;
    }
    .card-desc {
        color: #4B5563;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    .tag {
        display: inline-block;
        background-color: #EFF6FF;
        color: #2563EB;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        margin-top: 8px;
    }

    .skill-badge {
        background-color: #F3F4F6;
        border-left: 4px solid #2563EB;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
        font-weight: 600;
        color: #1F2937;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. PHẦN THANH BÊN (SIDEBAR)
# ==========================================
with st.sidebar:
    st.title("📌 Danh Mục")
    menu = st.radio(
        "Đi đến:",
        ["🏠 Trang Chủ", "🛠️ Kỹ Năng", "📂 Dự Án", "📜 Học Vấn & Kinh Nghiệm", "📩 Liên Hệ"]
    )
    
    st.divider()
    st.markdown("### 🌐 Mạng Xã Hội")
    st.link_button("🌐 Facebook", "https://www.facebook.com/share/1DGH51fJh9/", use_container_width=True)
    st.link_button("💻 GitHub", "https://github.com/thanh", use_container_width=True)
    st.link_button("💼 LinkedIn", "https://linkedin.com/in/thanh", use_container_width=True)
    
    st.divider()
    st.caption("© 2026 Designed with ❤️ by Python & Streamlit")

# ==========================================
# 4. TRANG CHỦ (HERO SECTION)
# ==========================================
if menu == "🏠 Trang Chủ":
    col_img, col_info = st.columns([1, 2.2], gap="large")

    with col_img:
        image_path = None
        for ext in ["assets/avatar.png", "assets/avatar.PNG", "assets/avatar.jpg", "assets/avatar.jpeg"]:
            if os.path.exists(ext):
                image_path = ext
                break

        if image_path:
            avatar = Image.open(image_path)
            st.image(avatar, use_container_width=True)
        else:
            st.info("💡 Chưa tìm thấy ảnh đại diện! Vui lòng kiểm tra thư mục `assets/avatar.png`.")

    with col_info:
        st.markdown("""
            <div class="header-box">
                <div class="main-title">Nguyễn Thành Huy</div>
                <div class="sub-title">Lập Trình Viên Ô Tô | Automotive Programmer</div>
                <div class="bio-text">
                    Xin chào! Tôi là một kỹ sư lập trình viên nhúng đam mê phát triển phần cứng trên ô tô, 
                    tự động hóa quy trình làm việc và tối ưu hóa hệ thống dữ liệu. 
                    Tôi luôn chủ động tìm tòi công nghệ mới để đưa ra các giải pháp công nghệ hiệu quả và tối ưu.
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("📍 **Địa chỉ:** Khu Phố 2, Phường Đông Hòa, TP. Tuy Hòa, Việt Nam")
        st.markdown("✉️ **Email:** nguyenthanhhuy16122005@gmail.com")
        st.markdown("📞 **SĐT:** 0337-340-448")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric(label="Kinh Nghiệm", value="4+ Năm")
    c2.metric(label="Dự Án Hoàn Thành", value="9+")
    c3.metric(label="Công Nghệ Sử Dụng", value="C++, Python")
    c4.metric(label="Trạng Thái", value="Sẵn sàng")

# ==========================================
# 5. TRANG KỸ NĂNG (SKILLS)
# ==========================================
elif menu == "🛠️ Kỹ Năng":
    st.header("🛠️ Kỹ Năng & Công Nghệ Trên Ô Tô")
    st.write("Các kỹ năng chuyên môn và công cụ tôi sử dụng thành thạo trong quá trình phát triển:")

    col_s1, col_s2, col_s3 = st.columns(3)

    with col_s1:
        st.subheader("💻 Lập Trình Backend")
        st.markdown('<div class="skill-badge">🐍 Python (Advanced)</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-badge">⚡ FastAPI / Flask</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-badge">🛢️ AUTOCAD</div>', unsafe_allow_html=True)

    with col_s2:
        st.subheader("🌐 Web & Frontend")
        st.markdown('<div class="skill-badge">🚀 Streamlit</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-badge">🎨 HTML5 & CSS3 Custom</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-badge">📜 JavaScript Basic</div>', unsafe_allow_html=True)

    with col_s3:
        st.subheader("⚙️ Công Cụ & Khác")
        st.markdown('<div class="skill-badge">🐙 Git & GitHub Workflow</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-badge">💻 VS Code & Terminal</div>', unsafe_allow_html=True)
        st.markdown('<div class="skill-badge">📊 Pandas & Data Processing</div>', unsafe_allow_html=True)

# ==========================================
# 6. TRANG DỰ ÁN (PROJECTS)
# ==========================================
elif menu == "📂 Dự Án":
    st.header("📂 Các Dự Án Nổi Bật")
    st.write("Một số sản phẩm phần mềm tiêu biểu mà tôi đã nghiên cứu và phát triển:")

    col_p1, col_p2 = st.columns(2)

    with col_p1:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🌐 1. Trang Web Portfolio Cá Nhân Interactive</div>
            <div class="card-desc">Xây dựng ứng dụng web giới thiệu bản thân trực quan, hỗ trợ tùy biến giao diện và hiển thị dự án.</div>
            <span class="tag">Python</span><span class="tag">Streamlit</span><span class="tag">HTML/CSS</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🤖 3. Công Cụ Tự Động Hóa Dữ Liệu Excel</div>
            <div class="card-desc">Phần mềm giúp tự động đọc, lọc và tổng hợp dữ liệu từ các file Excel phức tạp thành báo cáo đồ họa.</div>
            <span class="tag">Python</span><span class="tag">Pandas</span><span class="tag">OpenPyXL</span>
        </div>
        """, unsafe_allow_html=True)

    with col_p2:
        st.markdown("""
        <div class="custom-card">
            <div class="card-title">📊 2. Dashboard Phân Tích Dữ Liệu Realtime</div>
            <div class="card-desc">Hệ thống bảng điều khiển thông minh hiển thị doanh thu và dự báo xu hướng thị trường.</div>
            <span class="tag">Python</span><span class="tag">Plotly</span><span class="tag">SQL</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="custom-card">
            <div class="card-title">🔗 4. API Service Quản Lý Người Dùng</div>
            <div class="card-desc">Xây dựng hệ thống RESTful API kết nối cơ sở dữ liệu, hỗ trợ xác thực tài khoản.</div>
            <span class="tag">FastAPI</span><span class="tag">SQLite</span><span class="tag">JWT</span>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 7. HỌC VẤN & KINH NGHIỆM
# ==========================================
elif menu == "📜 Học Vấn & Kinh Nghiệm":
    st.header("📜 Hành Trình Phát Triển")

    st.subheader("🎓 Học Vấn")
    st.markdown("""
    - **Kỹ Sư Lập Trình Ô Tô / Khoa học Máy tính**
      - *Chuyên ngành:* Công Nghệ Kỹ Thuật Ô Tô
      - *Tốt nghiệp:* Loại Khá, Trường Đại Học Lạc Hồng `(2023 - 2026)`
    """)

    st.divider()

    st.subheader("💼 Kinh Nghiệm Làm Việc")
    st.markdown("""
    - **Software Developer (Kỹ sư thiết kế, lập trình ô tô)** — *Công ty Công nghệ Việt Nhân* `(2025 - Hiện tại)`
      - Trực tiếp phát triển và thiết kế các tính năng ứng dụng ô tô và vẽ sơ đồ bằng Python và AutoCAD.
    - **Lập trình ô tô Thực Tập (Python automation)** — *Tập đoàn Hyundai Việt Nam* `(2025 - 2026)`
      - Tham gia xây dựng các kịch bản tự động hóa quy trình dữ liệu ô tô.
    """)

# ==========================================
# 8. TRANG LIÊN HỆ (CONTACT FORM)
# ==========================================
elif menu == "📩 Liên Hệ":
    st.header("📩 Gửi Lời Nhắn Đến Tôi")

    with st.form("contact_form", clear_on_submit=True):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            name = st.text_input("Họ và Tên (*)")
        with col_f2:
            email = st.text_input("Địa chỉ Email (*)")
            
        subject = st.text_input("Tiêu đề tin nhắn")
        message = st.text_area("Nội dung lời nhắn (*)", height=150)
        
        submitted = st.form_submit_button("🚀 Gửi Lời Nhắn")

        if submitted:
            if name and email and message:
                st.success(f"🎉 Cảm ơn {name}! Lời nhắn đã được gửi đi thành công. Tôi sẽ phản hồi qua {email} sớm nhất!")
            else:
                st.error("⚠️ Vui lòng điền đầy đủ các thông tin bắt buộc (*).")