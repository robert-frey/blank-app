import streamlit as st
import pandas as pd

# Google Sheet info
SHEET_ID = "1W4kSomg1hRHVAgperK4FtedsgCmeYFJx0Iw_BoKe3Jc"
BASE_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet="

# Load sheets
@st.cache_data
def load_sheet(sheet_name):
    url = BASE_URL + sheet_name.replace(" ", "%20")
    return pd.read_csv(url)

d2_commits_df = load_sheet("D2 Commits")
leaving_d2_df = load_sheet("Leaving D2")

# --- TAB UI ---
st.title("D2 Transfer Portal Tracker")

tab1, tab2 = st.tabs(["D2 Commits","Leaving D2"])


# --- TAB 2: D2 COMMITS ---
with tab1:
    st.header("D2 Commits")

    commit_sort_df = d2_commits_df.sort_values(by="New School", ascending=True)


    st.dataframe(
        commit_sort_df.iloc[:, 0:5],
        use_container_width=True,
        height=700,
        column_config={
            "Name": st.column_config.Column("Player Name"),
            "Prev School": st.column_config.Column("Previous School"),
            "New School": st.column_config.Column("New School"),
            "Level": st.column_config.Column("Level"),
            "Pos": st.column_config.Column("Position"),
            "Source": st.column_config.Column("Source")
        },
        hide_index=True
    )

# --- TAB 5: LEAVING D2 ---
with tab2:
    st.header("Players Leaving D2")

    st.dataframe(
        leaving_d2_df.iloc[:, 0:5],
        use_container_width=True,
        height=700,
        column_config={
            "Name": st.column_config.Column("Player Name"),
            "Prev School": st.column_config.Column("Previous School"),
            "New School": st.column_config.Column("New School"),
            "Level": st.column_config.Column("Level"),
            "Pos": st.column_config.Column("Position")
        },
        hide_index=True
    )