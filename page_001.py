import streamlit as st





# --- Streamlit UI ---
st.set_page_config(page_title="Sync CR tool", layout="centered")
st.title("Batch CR - Sync tool")
st.divider()

# --- CR Info ---
#----Step1--
st.subheader("1. Template CR")
default_cr = st.text_input(
    label="Step1. Input your template CR.",  # 标签（必填）
    value="",  # 默认值
    max_chars=5,  # 最大字符数
    type="default",  # 输入类型
    placeholder="CHG0001"  # 占位提示文本
)


if st.button("Search"):
    if default_cr:
        st.success(f"It has been found, here are the details：{default_cr}")
    else:
        st.warning("Please input the template CR ....")

st.divider()


# 创建容器

with st.container(border=True):
    st.markdown ("###### Mode2 DevOps | NON-DISSDFSDFSD SD S| VXCVXCVXCVXCV X | SDFSDFSD F SDF SDFSDF SDFSSDFSD F SDF SDFSDF SDFSSDFSD F SDF SDFSDF SDFSD")
    st.caption("Choose which section you want to sync...")
    col_expander1,col_check1 = st.columns([0.9,0.1])

    with col_check1:
        check1 = st.checkbox("Sync", key="check1")
    with col_expander1:
        with st.expander("Description", expanded=check1):
            st.write("""
                   这是一个可折叠的内容区域，适合展示额外信息但不希望占用太多空间。

                   你可以：
                   - 放置详细说明文本
                   - 添加次要操作按钮
                   - 展示辅助图表或数据
                   """)



    col_expander2, col_check2 = st.columns([0.9, 0.1])
    with col_check2:
        check2 = st.checkbox("Sync", key="check2")
    with col_expander2:
        with st.expander("Implement Plan", expanded=check2):
            st.write("""
                      这是一个可折叠的内容区域，适合展示额外信息但不希望占用太多空间。

                      你可以：
                      - 放置详细说明文本
                      - 添加次要操作按钮
                      - 展示辅助图表或数据
                      """)



    col_expander3, col_check3 = st.columns([0.9, 0.1])
    with col_check3:
        check3 = st.checkbox("Sync", key="check3")
    with col_expander3:
        with st.expander("Backout Plan", expanded=check3):
            st.write("""
                      这是一个可折叠的内容区域，适合展示额外信息但不希望占用太多空间。

                      你可以：
                      - 放置详细说明文本
                      - 添加次要操作按钮
                      - 展示辅助图表或数据
                      """)

    col_expander4, col_check4 = st.columns([0.9, 0.1])
    with col_check4:
        check4 = st.checkbox("Sync", key="check4")
    with col_expander4:
        with st.expander("Verification Plan", expanded=check4):
            st.write("""
                      这是一个可折叠的内容区域，适合展示额外信息但不希望占用太多空间。

                      你可以：
                      - 放置详细说明文本
                      - 添加次要操作按钮
                      - 展示辅助图表或数据
                      """)


#----Step2--
st.subheader("2. Targe CR List")
default_cr = st.text_input(
    label="Step2. Input your CR List",  # 标签（必填）
    value="",  # 默认值
    type="default",  # 输入类型
    placeholder="CHG0001,CHG0002,CHG0003,CHG0004,CHG0005,"  # 占位提示文本
)

if st.button("Sync data"):
    if default_cr:
        st.success(f"It has been found, here are the details：{default_cr}")
    else:
        st.warning("Please input the template CR ....")

st.divider()



# Remove deploy button in page header
hide_streamlit_style = """
             <style>
                div[data-testid="stHeader"] {
                    visibility: hidden;
                    height: 0px;
                    position: fixed;
                }
                div[data-testid="stToolbar"] {
                    visibility: hidden;
                    height: 0px;
                    position: fixed;
                }
                div[data-testid="stDecoration"] {
                    visibility: hidden;
                    height: 0px;
                    position: fixed;
                }
                #MainMenu {
                    visibility: hidden;
                    height: 0px;
                }
                header {
                    visibility: hidden;
                    height: 0px;
                }
                footer {
                    visibility: hidden;
                    height: 0%;
                }
                div[data-testid="stMainBlockContainer"] {
                    padding: 0rem 1rem 10rem
                }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)