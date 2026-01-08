import streamlit as st
from datetime import datetime, time

# ==================== 페이지 설정 ====================
st.set_page_config(page_title="Streamlit 요소 가이드", layout="wide")

# ==================== 제목 섹션 ====================
st.title("📚 Streamlit 단일 페이지 요소 완벽 가이드")
st.markdown(
    "이 페이지는 Streamlit에서 사용할 수 있는 모든 요소들을 실제로 보고 배울 수 있는 교육용 페이지입니다."
)

# ==================== 구분선 ====================
st.divider()

# ==================== 1. 텍스트 표시 요소 ====================
st.header("1️⃣ 텍스트 표시 요소")

# st.title() - 페이지의 가장 큰 제목
st.subheader("📌 st.title() - 페이지 제목")
st.write("페이지의 가장 상단에 큰 제목을 표시합니다. 일반적으로 페이지당 하나만 사용합니다.")
with st.echo():
    st.title("이것이 제목입니다")

st.divider()

# st.header() - 섹션 헤더
st.subheader("📌 st.header() - 섹션 헤더")
st.write("페이지 내 주요 섹션을 구분할 때 사용합니다. title보다 작은 크기입니다.")
with st.echo():
    st.header("이것이 헤더입니다")

st.divider()

# st.subheader() - 서브 헤더
st.subheader("📌 st.subheader() - 서브 헤더")
st.write("header의 하위 항목을 구분할 때 사용합니다.")
with st.echo():
    st.subheader("이것이 서브헤더입니다")

st.divider()

# st.write() - 다목적 쓰기 함수
st.subheader("📌 st.write() - 다목적 쓰기")
st.write("텍스트, 숫자, 마크다운, 데이터프레임, 차트 등 다양한 형태의 데이터를 표시할 수 있습니다.")
with st.echo():
    st.write("이것은 일반 텍스트입니다")
    st.write(42)  # 숫자도 표시 가능
    st.write({"이름": "철수", "나이": 25})  # 딕셔너리도 표시 가능

st.divider()

# st.text() - 일반 텍스트
st.subheader("📌 st.text() - 일반 텍스트")
st.write("마크다운 포매팅을 적용하지 않은 순수 텍스트를 표시합니다.")
with st.echo():
    st.text("이것은 일반 텍스트입니다\n포매팅이 적용되지 않습니다")

st.divider()

# st.markdown() - 마크다운
st.subheader("📌 st.markdown() - 마크다운 텍스트")
st.write("마크다운 문법을 사용하여 포매팅된 텍스트를 표시합니다.")
with st.echo():
    st.markdown("**굵은 텍스트**, *기울임 텍스트*, `코드`, [링크](https://streamlit.io)")

st.divider()

# st.code() - 코드 표시
st.subheader("📌 st.code() - 코드 블록")
st.write("프로그래밍 코드를 문법 하이라이팅과 함께 표시합니다.")
with st.echo():
    code = """
def hello_world():
    print("안녕하세요!")
    return True
"""
    st.code(code, language="python")

st.divider()

# st.caption() - 작은 텍스트
st.subheader("📌 st.caption() - 캡션 (작은 텍스트)")
st.write("이미지나 기타 요소를 설명하는 작은 텍스트입니다.")
with st.echo():
    st.caption("이것은 캡션입니다. 매우 작은 크기입니다.")

st.divider()

# st.metric() - 메트릭 표시
st.subheader("📌 st.metric() - 핵심 수치 표시")
st.write("중요한 수치를 강조해서 표시합니다. 이전 값 대비 변화를 시각적으로 보여줄 수 있습니다.")
with st.echo():
    col1, col2, col3 = st.columns(3)
    col1.metric(label="온도", value="25°C", delta="1.2°C")
    col2.metric(label="매출", value="$1,000,000", delta="+12%")
    col3.metric(label="방문자", value="12,345", delta="-2%")

st.divider()

# ==================== 2. 입력 요소 ====================
st.header("2️⃣ 사용자 입력 요소")

# st.button() - 버튼
st.subheader("📌 st.button() - 버튼")
st.write("클릭할 수 있는 버튼입니다. 버튼을 클릭하면 True를 반환합니다.")
with st.echo():
    if st.button("클릭해보세요!"):
        st.success("버튼이 클릭되었습니다!")

st.divider()

# st.checkbox() - 체크박스
st.subheader("📌 st.checkbox() - 체크박스")
st.write("사용자가 선택/취소할 수 있는 체크박스입니다. True/False를 반환합니다.")
with st.echo():
    agree = st.checkbox("약관에 동의합니다")
    if agree:
        st.write("감사합니다!")

st.divider()

# st.radio() - 라디오 버튼
st.subheader("📌 st.radio() - 라디오 버튼")
st.write("여러 옵션 중 하나만 선택할 수 있습니다.")
with st.echo():
    choice = st.radio("좋아하는 과일을 선택하세요", ["🍎 사과", "🍌 바나나", "🍊 오렌지"])
    st.write(f"선택된 항목: {choice}")

st.divider()

# st.selectbox() - 셀렉트박스
st.subheader("📌 st.selectbox() - 드롭다운 셀렉트")
st.write("드롭다운 메뉴에서 하나의 항목을 선택합니다.")
with st.echo():
    selected = st.selectbox("도시를 선택하세요", ["서울", "부산", "대구", "인천"])
    st.write(f"선택된 도시: {selected}")

st.divider()

# st.multiselect() - 멀티셀렉트
st.subheader("📌 st.multiselect() - 복수 선택")
st.write("여러 개의 항목을 동시에 선택할 수 있습니다.")
with st.echo():
    options = st.multiselect("좋아하는 색상들을 선택하세요", ["빨강", "초록", "파랑", "노랑", "보라"])
    st.write(f"선택된 색상: {options}")

st.divider()

# st.slider() - 슬라이더
st.subheader("📌 st.slider() - 슬라이더")
st.write("마우스로 드래그하여 값을 선택합니다.")
with st.echo():
    age = st.slider("나이를 선택하세요", 0, 100, 25)
    st.write(f"선택된 나이: {age}")

st.divider()

# st.text_input() - 텍스트 입력
st.subheader("📌 st.text_input() - 한 줄 텍스트 입력")
st.write("사용자가 텍스트를 입력할 수 있습니다.")
with st.echo():
    name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")
    if name:
        st.write(f"안녕하세요, {name}님!")

st.divider()

# st.number_input() - 숫자 입력
st.subheader("📌 st.number_input() - 숫자 입력")
st.write("숫자만 입력할 수 있는 입력 필드입니다.")
with st.echo():
    number = st.number_input("숫자를 입력하세요", min_value=0, max_value=100, step=1)
    st.write(f"입력된 숫자: {number}")

st.divider()

# st.text_area() - 텍스트 영역
st.subheader("📌 st.text_area() - 여러 줄 텍스트 입력")
st.write("여러 줄의 텍스트를 입력할 수 있습니다.")
with st.echo():
    text = st.text_area("의견을 입력하세요", placeholder="여기에 입력하세요...", height=100)
    if text:
        st.write(f"입력하신 내용: {text}")

st.divider()

# st.date_input() - 날짜 입력
st.subheader("📌 st.date_input() - 날짜 선택")
st.write("캘린더에서 날짜를 선택합니다.")
with st.echo():
    date = st.date_input("날짜를 선택하세요", value=datetime.now().date())
    st.write(f"선택된 날짜: {date}")

st.divider()

# st.time_input() - 시간 입력
st.subheader("📌 st.time_input() - 시간 선택")
st.write("시간을 선택합니다.")
with st.echo():
    selected_time = st.time_input("시간을 선택하세요", value=time(12, 0))
    st.write(f"선택된 시간: {selected_time}")

st.divider()

# st.file_uploader() - 파일 업로드
st.subheader("📌 st.file_uploader() - 파일 업로드")
st.write("사용자가 파일을 업로드할 수 있습니다.")
with st.echo():
    uploaded_file = st.file_uploader("파일을 선택하세요", type=["txt", "csv", "xlsx"])
    if uploaded_file:
        st.success(f"파일이 업로드되었습니다: {uploaded_file.name}")

st.divider()

# ==================== 3. 메시지 요소 ====================
st.header("3️⃣ 메시지 표시 요소")

# st.success() - 성공 메시지
st.subheader("📌 st.success() - 성공 메시지")
st.write("작업이 성공적으로 완료되었을 때 표시합니다.")
with st.echo():
    st.success("✅ 저장되었습니다!")

st.divider()

# st.info() - 정보 메시지
st.subheader("📌 st.info() - 정보 메시지")
st.write("사용자에게 추가 정보를 제공할 때 표시합니다.")
with st.echo():
    st.info("ℹ️ 이것은 정보 메시지입니다")

st.divider()

# st.warning() - 경고 메시지
st.subheader("📌 st.warning() - 경고 메시지")
st.write("주의가 필요한 상황을 알릴 때 표시합니다.")
with st.echo():
    st.warning("⚠️ 이것은 경고 메시지입니다")

st.divider()

# st.error() - 에러 메시지
st.subheader("📌 st.error() - 에러 메시지")
st.write("오류 상황을 알릴 때 표시합니다.")
with st.echo():
    st.error("❌ 이것은 에러 메시지입니다")

st.divider()

# ==================== 4. 레이아웃 요소 ====================
st.header("4️⃣ 레이아웃 요소")

# st.columns() - 컬럼
st.subheader("📌 st.columns() - 여러 컬럼 배치")
st.write("화면을 여러 개의 컬럼으로 나누어 요소를 배치합니다.")
with st.echo():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("첫 번째 컬럼")
        st.button("버튼 1")
    with col2:
        st.write("두 번째 컬럼")
        st.button("버튼 2")
    with col3:
        st.write("세 번째 컬럼")
        st.button("버튼 3")

st.divider()

# st.tabs() - 탭
st.subheader("📌 st.tabs() - 탭 네비게이션")
st.write("여러 탭으로 콘텐츠를 구성합니다.")
with st.echo():
    tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])
    
    with tab1:
        st.write("탭 1의 콘텐츠입니다")
    
    with tab2:
        st.write("탭 2의 콘텐츠입니다")
    
    with tab3:
        st.write("탭 3의 콘텐츠입니다")

st.divider()

# st.expander() - 확장 가능한 섹션
st.subheader("📌 st.expander() - 확장/축소 섹션")
st.write("클릭하여 펼칠 수 있는 숨겨진 컨텐츠입니다.")
with st.echo():
    with st.expander("더 보기"):
        st.write("숨겨진 컨텐츠가 여기에 표시됩니다!")

st.divider()

# st.container() - 컨테이너
st.subheader("📌 st.container() - 컨테이너")
st.write("여러 요소를 하나의 컨테이너로 그룹화할 수 있습니다.")
with st.echo():
    with st.container(border=True):
        st.write("이 요소들은 테두리로 감싸져 있습니다")
        st.button("컨테이너 내 버튼")

st.divider()

# st.divider() - 구분선
st.subheader("📌 st.divider() - 구분선")
st.write("콘텐츠를 시각적으로 구분할 때 사용합니다.")
with st.echo():
    st.write("구분선 위")
    st.divider()
    st.write("구분선 아래")

st.divider()

# ==================== 5. 사이드바 요소 ====================
st.header("5️⃣ 사이드바 요소")
st.write("사이드바에도 모든 입력 요소들을 사용할 수 있습니다.")

with st.echo():
    # 사이드바에 요소 추가하기
    st.sidebar.title("⚙️ 설정")
    st.sidebar.subheader("사이드바 예제")
    sidebar_choice = st.sidebar.selectbox("옵션을 선택하세요", ["옵션 1", "옵션 2", "옵션 3"])
    sidebar_slider = st.sidebar.slider("슬라이더", 0, 100)
    st.write(f"사이드바에서 선택된 옵션: {sidebar_choice}")
    st.write(f"사이드바 슬라이더 값: {sidebar_slider}")

st.divider()

# ==================== 하단 정보 ====================
st.info("💡 **팁**: 모든 Streamlit 요소는 단일 페이지에서 결합하여 사용할 수 있으며, 마크다운 포매팅도 지원합니다.")
