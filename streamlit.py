import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from  helper.page_layout import PageLayout
from  helper.helper import Helper
from  helper.league_card import LeagueCard
from  helper.team_card import TeamCard


def main():

    ### SETING THE PAGE LAYOUT
    PageLayout.setup_page()

    try:
        # Info
        with st.expander(
                "Streamlit app to fetch insights from the FPL team and mini leagues in a few clicks", expanded=False
        ):
            st.write("Enter your team ID and league ID. Get the following insights")
            app_intro = """
            This app allows you to get crucial insights that can help you be 1st in your mini leagues with just a few clicks.
            * __Insights 1__: TODO.
            * __Insights 2__: TODO 2.
            * __Insights 3__: TODO 3.
            * __Insights 4__: TODO 4. \n
            """

            st.write(app_intro)
        st.write("")

        team_id = st.text_input('Enter your team id:', value='104676')
        league_id = st.text_input('Enter your league id:', value='1252741')

        validated_team_id_input = Helper.validate_api_input(team_id)
        validated_league_id_input = Helper.validate_api_input(league_id)


        if st.button('Confirm'):
            if validated_team_id_input and validated_league_id_input is not None:


                gw, last_updated_at = TeamCard.event_status()
                st.markdown(f'<p2 style="color:black"> <i>Current Gameweek is {gw}, Stats last updated at {last_updated_at}</i> </p2>',
                            unsafe_allow_html=True)
                PageLayout.setup_seperator()

                df_filtered,league_name,team_name = LeagueCard.process_data(team_id, league_id)
                st.markdown(f'<h2>FPL League Insights</h2> <h3 style="color:purple"> <i>{league_name}</i> </h3>', unsafe_allow_html=True)

                st.write(df_filtered)
                PageLayout.setup_seperator()


                st.markdown(f'<h2>Team Insights</h2> <h3 style="color:purple"> <i>{team_name}</i> </h3>', unsafe_allow_html=True)
                TeamCard.process_data(team_id, league_id, gw, last_updated_at)
                PageLayout.setup_footer()
            else:
                st.error("Please enter a valid integer.")
    except Exception as e:
        # Handle any exceptions that occur
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


