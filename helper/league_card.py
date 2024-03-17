import streamlit as st
import requests
import pandas as pd

class LeagueCard:

    @staticmethod
    def process_data(team_id, league_id):
        league_api = f'https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/'
        response = requests.get(f"{league_api}").json()
        league_name = (response['league']['name'])

        top_n_players = []
        finding_top_player = 50
        my_team_name = ''
        # Iterate over the dictionary
        for key, value in response.items():

            if key == 'standings':
                current_player_rank = 0
                while current_player_rank < finding_top_player:

                    if current_player_rank == 0:
                        top_player_points = (value['results'][current_player_rank]['total'])

                    rank = (value['results'][current_player_rank]['rank_sort'])
                    entry = (value['results'][current_player_rank]['entry'])
                    entry_name = (value['results'][current_player_rank]['entry_name'])
                    total_points = (value['results'][current_player_rank]['total'])
                    last_gw_pts = (value['results'][current_player_rank]['event_total'])
                    last_rank = (value['results'][current_player_rank]['last_rank'])

                    if str(entry) == str(team_id):
                        my_team_name = entry_name


                    new_map = {'Current Rank': rank, 'Team Id': entry, 'Team Name': entry_name, 'Total Points': total_points, 'Last GW Points': last_gw_pts,
                               'Points From The Top': top_player_points - total_points, 'Rank Delta': last_rank - rank}

                    top_n_players.append(new_map)
                    current_player_rank = current_player_rank + 1

        df = pd.DataFrame(top_n_players)
        return (df, league_name, my_team_name)