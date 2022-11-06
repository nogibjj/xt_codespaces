import calendar  # Core Python Module
from datetime import datetime  # Core Python Module

import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
from dblib.querydb import querydb
from dblib.querydb import amount_year_category
import pandas as pd
# -------------- SETTINGS --------------
page_title = "Netflix Data Hub"
page_icon = ":dvd:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
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
    st.header("Add new data into Netflix")
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month:", months, key="month")
        col2.selectbox("Select Year:", years, key="year")

        # read input
        with st.expander("Name"):
            name = st.text_area("", placeholder="Enter a movie/TV show name here ...")
        with st.expander("Age Rating"):
            age_rating = st.text_area("", placeholder="Enter age rating here ...(7+, 15+, 18+, all)")
        with st.expander("Duration"):
            duration = st.text_area("", placeholder="Enter duration here in the format of h/m such as 1h30m")
        with st.expander("Category"):
            category = st.selectbox('Select category:',('Kids & Family Movies', 'Action & Adventure', 'Anime Movies', 'Documentary Films', 'Dramas', 'Romantic Movies'), 3)

        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            insert_sql = "INSERT INTO default.netflix_1_csv VALUES ('" + name + "', '" + period + "', '"+ age_rating + "', '" + duration + "', '" + category +"', 'null"+ "')"
            querydb(insert_sql)
            st.success("Data saved!")


# --- PLOT PERIODS ---
if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("category_form", clear_on_submit=True):
        with st.expander("Choose first Category"):
            first = st.selectbox('Select category:',('Kids & Family Movies', 'Action & Adventure', 'Anime Movies', 'Documentary Films', 'Dramas', 'Romantic Movies'), 1)
        with st.expander("Choose second Category"):
            second = st.selectbox('Select category:',('Kids & Family Movies', 'Action & Adventure', 'Anime Movies', 'Documentary Films', 'Dramas', 'Romantic Movies'), 2)
        submitted = st.form_submit_button("Submit Data")
        if submitted:
            st.success("Data submitted!")
            list1 = []
            for i in range(10):
                time = 2010+i
                num = amount_year_category(time, first)
                list1.append(num)

            list2 = []
            for i in range(10):
                time = 2010+i
                num = amount_year_category(time, second)
                list2.append(num)
            #print(list2)
            # dataframe = pd.DataFrame(np.random.randn(10, 5),
            # columns = ('col %d' % i for i in range(5)))
            # dataframe
            # st.write('This is a line_chart.')
            # st.line_chart(dataframe
            data = {first:list1, second:list2}
            # dataframe = pd.DataFrame(list1,
            # columns = [first])
            dataframe = pd.DataFrame(data)
            dataframe.index = ('%d' % (i+2010) for i in range(10))
            st.dataframe(dataframe)
            st.write('This is a line_chart.')
            st.line_chart(dataframe)