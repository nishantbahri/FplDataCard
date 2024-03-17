import streamlit as st
import requests
import pandas as pd
import altair as alt
import plotly.express as px

class TeamCard:

    @staticmethod
    def event_status():
        test = "https://fantasy.premierleague.com/api/event-status/"
        response = requests.get(f"{test}")
        gw = response.json()["status"][-1]["event"]
        last_updated_at = response.json()["status"][-1]["date"]
        return gw,last_updated_at

    @staticmethod
    def process_data(team_id, league_id, gw,last_updated_at):
        gw_transfer_api = f'https://fantasy.premierleague.com/api/entry/{team_id}/event/{gw}/picks/'
        response = requests.get(f"{gw_transfer_api}").json()

        element_ids = [pick['element'] for pick in response['picks']]
        print(f"Currently the team_id {team_id} on the gw {gw} has the players with id's {element_ids}")

        url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

        data = requests.get(f"{url}").json()

        print('\n--- element type ---\n')

        # print(data['element_types'][0])
        for item in data['element_types']:
            print(item['id'], item['plural_name'])

        '''
        --- element type ---
        1 Goalkeepers
        2 Defenders
        3 Midfielders
        4 Forwards
        '''

        # Mapping position numbers to positions
        position_mapping = {'1': 'GK', '2': 'DEF', '3': 'MID', '4': 'FWD'}

        my_fpl_team = element_ids
        player_name = []

        for item in data['elements']:
            if item['id'] in my_fpl_team:
                player_name.append(
                    f"{item['element_type']}/{item['web_name']}/{data['teams'][item['team'] - 1]['name']}")

        sorted_list = sorted(player_name)

        print("\n")
        print(sorted_list)

        transformed_data = []
        for entry in sorted_list:
            position, player_name, club_name = entry.split('/')
            transformed_data.append(
                {'Position': position_mapping[position], 'Player': player_name, 'Club': club_name})

        # Creating DataFrame
        df = pd.DataFrame(transformed_data)

        response = requests.get(f"https://fantasy.premierleague.com/api/entry/{team_id}/history/").json()

        line_chart_pts = {}
        d = []

        for i in range(0, gw):
            gw = response['current'][i]['event']
            pts = response['current'][i]['points']

            line_chart_pts[gw] = pts
            d.append(
                {
                    'Gameweek': gw,
                    'Points': pts
                }
            )

        df = pd.DataFrame(d)

        # Plot line chart using Plotly
        fig = px.line(df.reset_index(), x='Gameweek', y='Points', title='Points acquired Each Gameweek')
        fig.update_traces(mode='lines+markers', line=dict(color='#800080'))
        fig.update_layout(hovermode='x')
        fig.update_xaxes(tickmode='linear', dtick=1)
        st.plotly_chart(fig)

        return df

