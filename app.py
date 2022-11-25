import calendar  # Core Python Module
from datetime import datetime  # Core Python Module

import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from request import get_activity
# from dblib.querydb import querydb
# from dblib.querydb import amount_year_category


# -------------- SETTINGS --------------
page_title = "Search API Hub"
page_icon = ":full_moon:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# # --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

# --- INPUT & SAVE PERIODS ---
if selected == "Data Entry":
    st.header("Request from boredAPI")
    with st.form("entry_form", clear_on_submit=True):
        # col1, col2 = st.columns(2)
        # col1.selectbox("Select Month:", months, key="month")
        # col2.selectbox("Select Year:", years, key="year")

        # read input
        with st.expander("API name"):
            name = st.text_area("", placeholder="Enter API name here ...")
        # with st.expander("Age Rating"):
        #     age_rating = st.text_area("", placeholder="Enter age rating here ...(7+, 15+, 18+, all)")
        # with st.expander("Duration"):
        #     duration = st.text_area("", placeholder="Enter duration here in the format of h/m such as 1h30m")
        # with st.expander("Category"):
        #     category = st.selectbox('Select category:',('Kids & Family Movies', 'Action & Adventure', 'Anime Movies', 'Documentary Films', 'Dramas', 'Romantic Movies'), 3)

        submitted = st.form_submit_button("Search")
        if submitted:
            # period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            # insert_sql = "INSERT INTO default.netflix_1_csv VALUES ('" + name + "', '" + period + "', '"+ age_rating + "', '" + duration + "', '" + category +"', 'null"+ "')"
            # querydb(insert_sql)
            data = get_activity(name)
            print(data)
            st.json(data)
            st.success("Success!")