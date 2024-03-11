import streamlit as st


class PageLayout:
    @staticmethod
    def setup_page():

        # Define the CSS style for the card background
        card_style = """
            <style>
            .card {
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
                background: linear-gradient(to right, #e6ccff, #cc99ff); /* Light purple gradient background */
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .card:hover {
                transform: translateY(-4px);
                box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.1);
            }
            .stTextInput>div>div>div>input {
                width: 100%;
                font-size: 20px;
                text-align: center;
            }
            </style>
        """

        title = "🏆 FPL DATA CARD"


        st.set_page_config(
            page_title=title,
            page_icon="🏆",
            # layout="wide",
            # initial_sidebar_state="expanded"
        )
        # st.title('FPL DATA CARD')

        # Render the card background using st.markdown
        st.markdown(f'<div class="card">{card_style}'
                    f'<h1>🏆 FPL DATA CARD</h1>'
                    f'</div>',
                    unsafe_allow_html=True)

    @staticmethod
    def setup_footer():
        st.markdown("---")
        st.markdown(
            "Please feel free to connect if you'd like to discuss further. I'm available and eager to chat! : [LinkedIn](https://www.linkedin.com/in/nishant-bahri/)")