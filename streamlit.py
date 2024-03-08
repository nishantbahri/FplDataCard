import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from st_aggrid import AgGrid

def _format_arrow(val):

    val = int(val)
    return f"{'↑' if val > 0 else '↓'} {abs(val):.0f}%" if val != 0 else f"{val:.0f}%"

def _color_arrow(val):
    val = int(val)
    return "color: green" if val > 0 else "color: red" if val < 0 else "color: black"

def setup_footer():
    st.markdown(
        """
        ---
        Made with ❤️ from India
        """
    )

def setup_basic():
    title = "🏆 FPL DATA CARD"


    st.set_page_config(
        page_title=title,
        page_icon="🏆",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title('FPL DATA CARD')

    st.markdown(
        "Trying to pave my way to the top in mini leagues"
    )

def process_data(team_id, league_id):
    # print("league_id is ", league_id)
    league_api = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/'
    # print(f"league_api is {league_api}")
    response = requests.get(f"{league_api}").json()
    league_name = (response['league']['name'])
    # Drop rows with missing values for simplicity
    # df.dropna(inplace=True)
    # df_filtered = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]
    # df_filtered = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]
    # df_filtered = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]

    top_n_players = []
    finding_top_player = 10
    # Iterate over the dictionary
    for key, value in response.items():

        if key == 'standings':
            # print(key, ":", value)
            current_player_rank = 0
            while current_player_rank < finding_top_player:

                if current_player_rank == 0:
                    top_player_points = (value['results'][current_player_rank]['total'])

                # print(current_player_rank)
                rank = (value['results'][current_player_rank]['rank_sort'])
                entry = (value['results'][current_player_rank]['entry'])
                entry_name = (value['results'][current_player_rank]['entry_name'])
                total_points = (value['results'][current_player_rank]['total'])
                last_rank = (value['results'][current_player_rank]['last_rank'])
                # print(f"rank -> {rank}, entry -> {entry}, entry_name -> {entry_name}")

                # Create a map (dictionary)
                new_map = {'Current Rank': rank, 'Team Id': entry, 'Team Name': entry_name, 'Total Points': total_points,
                           'Points From The Top': top_player_points - total_points, 'Rank Delta': last_rank - rank}

                # print(f"Adding map {new_map}")

                # Append the map to the list
                top_n_players.append(new_map)



                current_player_rank = current_player_rank + 1


    # print(f"\n{top_n_players}")
    df = pd.DataFrame(top_n_players)
    return (df, league_name)

def visualize_data(df):
    # Plot histogram of passenger ages
    fig, ax = plt.subplots()
    ax.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Histogram of Passenger Ages')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Function to highlight a specific row
def highlight_row(row):
    print("row ", row)
    color = 'purple'
    # color = 'purple' if row.entry_id == '101' else ''
    return [f'background-color: {color}'] if color else []


def main():
    setup_basic()


    # Load dataset

    try:
        # User input for age range
        team_id = st.text_input('Enter your team id:', value='104676')
        league_id = st.text_input('Enter your league id:', value='1252741')
        if st.button('Confirm'):
            # team_id = float(team_id)
            # league_id = float(league_id)
            # Process dataset based on age range
            df_filtered,league_name = process_data(team_id, league_id)

            # styled_df = df_filtered.style.format(_format_arrow).applymap(_color_arrow)


            # Show DataFrame
            # st.subheader(f'FPL LEAGUE : {league_name} INSIGHTS')
            # AgGrid(df_filtered)

            st.subheader(f'FPL LEAGUE : {league_name} INSIGHTS')
            st.write(df_filtered)

            # html_string = df_filtered.to_html(index=False)
            # st.write(html_string, unsafe_allow_html=True)

            # st.write(df_filtered.style.applymap(highlight_row))
            #st.dataframe(df_filtered.style.apply(highlight_row, name_to_highlight=team_id, axis=1), unsafe_allow_html=True)


            # Visualize data
            # st.subheader('Data Visualization')
            # visualize_data(df_filtered)

            setup_footer()
    except Exception as e:
        # Handle any exceptions that occur
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


