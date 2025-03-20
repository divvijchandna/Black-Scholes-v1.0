import streamlit as st
import heatmap
import options_calculator

from streamlit_option_menu import option_menu

PAGES = {
    "Options Pricing Calculator": options_calculator,
    "Call and Put Heatmap": heatmap,
}

with st.sidebar:
    selected = option_menu(
        menu_title = "📈 Black-Scholes",
        menu_icon="a",
        options = list(PAGES.keys()),
        default_index = 0
    )

page = PAGES[selected]
page.app()