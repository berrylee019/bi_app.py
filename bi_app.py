import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API 설정 (본인의 API 키 입력)
import streamlit as st
genai.configure(api_key=st.secrets["MY_API_KEY"])

# 2. 페이지 설정 및 브랜딩
st.set_page_config(page_title="Microhard BI 전략가", page_icon="📊", layout="centered")

st.title("📊 BI 전략가: 데이터 기반 경영 컨설팅")
st.caption("microhard.co.kr - 1인 기업을 위한 데이터 분석 에이전트")
st.markdown("---")

# 3. 서비스 안내
st.info("💡 매출 차트, 영수증, 또는 경영 대시보드 스크린샷을 업로드하세요. AI가 비즈니스 인사이트를 도출합니다.")

# 4. 파일 업로드
# --- 영상 업로드 가이드 섹션 ---
st.title("✨ AI 퍼스널 스타일 가이드")
st.markdown("### 🤳 당신의 스타일을 10초 만에 분석해 드립니다")

with st.expander("🎥 **더 정확한 분석을 위한 영상 촬영 꿀팁 (필독!)**", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **1. 전신 샷은 필수!** 머리부터 발끝까지 화면에 다 들어와야  
        정확한 비율 분석이 가능해요.
        
        **2. 천천히 360도 회전** 앞, 옆, 뒤태를 모두 보여주시면  
        입체적인 핏 가이드를 드립니다.
        """)
    with col2:
        st.markdown("""
        **3. 밝은 곳에서 촬영** 조명이 밝아야 옷의 질감과  
        퍼스널 컬러를 정확히 잡아내요.
        
        **4. 5~15초 내외 권장** 너무 길면 업로드 시간이 오래 걸려요!
        """)

# 실제 업로드 버튼
uploaded_file = st.file_uploader("분석할 쇼핑/스타일 영상을 업로드하세요.", type=["mp4", "mov", "avi"])
uploaded_file = st.file_uploader("분석할 경영 자료를 업로드하세요.", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드된 분석 자료", use_container_width=True)
    
    if st.button("🚀 비즈니스 인사이트 추출"):
        try:
            with st.spinner("전문 전략가가 데이터를 분석 중입니다..."):
                model = genai.GenerativeModel("gemini-2.5-flash")
                
                # BI 전용 시스템 프롬프트
                system_prompt = """
                너는 전문 경영 컨설턴트이자 데이터 분석가다. 이미지를 분석하여 다음을 수행하라:
                1. 현재 경영 상황 요약 (매출 트렌드, 비용 규모 등)
                2. 데이터에서 발견된 주요 문제점 또는 기회 요소
                3. 경영자가 즉시 실행할 수 있는 전략적 액션 아이템 3가지 제안
                친절하면서도 전문적인 톤으로 답변해줘.
                """
                
                response = model.generate_content([system_prompt, image])
                
                st.success("✅ 분석 완료!")
                st.markdown("---")
                st.markdown(response.text)
                
                # 리포트 다운로드
                st.download_button(
                    label="📄 경영 리포트 저장",
                    data=response.text,
                    file_name="BI_Strategy_Report.md",
                    mime="text/markdown"
                )
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
# --- 피드백을 받습니다. ---
st.markdown("---")
st.subheader("💬 여러분의 의견이 궁금해요!")
st.write("서비스가 도움이 되셨나요? 더 나은 서비스를 위해 짧은 의견을 남겨주세요.")
contact_form = """
<form action="https://formsubmit.co/bslee@yahoo.com" method="POST">
     <input type="text" name="name" placeholder="성함/닉네임" required>
     <input type="email" name="email" placeholder="이메일 주소" required>
     <textarea name="message" placeholder="피드백을 자유롭게 남겨주세요"></textarea>
     <button type="submit">의견 보내기</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# 5. 하단 푸터 (다른 서비스로의 연결)
st.markdown("---")
st.write("🔧 다른 서비스가 필요하신가요?")

st.link_button("Error 해결사 바로가기", "https://error-doctor.streamlit.app") # 기존 앱 주소 입력












