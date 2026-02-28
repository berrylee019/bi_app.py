import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API 설정 (본인의 API 키 입력)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# 2. 페이지 설정 및 브랜딩
st.set_page_config(page_title="Microhard BI 전략가", page_icon="📊", layout="centered")

st.title("📊 BI 전략가: 데이터 기반 경영 컨설팅")
st.caption("microhard.co.kr - 1인 기업을 위한 데이터 분석 에이전트")
st.markdown("---")

# 3. 서비스 안내
st.info("💡 매출 차트, 영수증, 또는 경영 대시보드 스크린샷을 업로드하세요. AI가 비즈니스 인사이트를 도출합니다.")

# 4. 파일 업로드
uploaded_file = st.file_uploader("분석할 경영 자료를 업로드하세요.", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드된 분석 자료", use_container_width=True)
    
    if st.button("🚀 비즈니스 인사이트 추출"):
        try:
            with st.spinner("전문 전략가가 데이터를 분석 중입니다..."):
                model = genai.GenerativeModel("gemini-1.5-flash")
                
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

# 5. 하단 푸터 (다른 서비스로의 연결)
st.markdown("---")
st.write("🔧 다른 서비스가 필요하신가요?")
st.link_button("Error 해결사 바로가기", "https://error-doctor.streamlit.app") # 기존 앱 주소 입력