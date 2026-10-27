from pathlib import Path

import streamlit as st

HERE = Path(__file__).parent
VIDEO = HERE / "純情青春夢_動態曲譜_男key伴奏.mp4"
SHEET = HERE / "純情青春夢_數位簡譜.png"

st.set_page_config(page_title="純情青春夢 動態曲譜", page_icon="🎵", layout="wide")

st.title("純情青春夢 · 動態曲譜")
st.caption("男key伴奏版　1=C　4/4")

st.video(str(VIDEO))

with st.expander("數位簡譜（可列印）"):
    st.image(str(SHEET), width="stretch")
    st.download_button("下載簡譜 PNG", SHEET.read_bytes(), file_name=SHEET.name, mime="image/png")
