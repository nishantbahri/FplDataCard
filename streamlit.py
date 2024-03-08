import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
def load_data():
    # Load dataset (you can replace this with your own dataset)
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    return df

def process_data(team_id, league_id):
    league_api = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/'
    response = requests.get(f"{league_api}").json()

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
                total_points = (value['results'][current_player_rank]['total'])
                last_rank = (value['results'][current_player_rank]['last_rank'])
                # print(f"rank -> {rank}, entry -> {entry}, entry_name -> {entry_name}")

                # Create a map (dictionary)
                new_map = {'rank': rank, 'entry_id': entry, 'total_points': total_points,
                           'points_from_top': top_player_points - total_points, 'rank_change': last_rank - rank}


                # Append the map to the list
                top_n_players.append(new_map)

                current_player_rank = current_player_rank + 1

    df = pd.DataFrame(top_n_players)
    return df

def visualize_data(df):
    # Plot histogram of passenger ages
    fig, ax = plt.subplots()
    ax.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Histogram of Passenger Ages')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

def main():
    st.title('FPL DATA CARD')

    # Load dataset


    # User input for age range
    team_id = st.text_input('Enter your team id:')
    league_id = st.text_input('Enter your league id:')
    if st.button('Confirm'):
        # team_id = float(team_id)
        # league_id = float(league_id)
        # Process dataset based on age range
        df_filtered = process_data(team_id, league_id)

        # Show DataFrame
        st.subheader('Filtered Dataset')
        st.write(df_filtered, index=False)

        # Visualize data
        # st.subheader('Data Visualization')
        # visualize_data(df_filtered)

if __name__ == "__main__":
    main()
