import streamlit as st
import os


def main():

  col1, col2, col3 = st.columns(3, vertical_alignment='center')

  with col1:
    st.image('img/datascientest_logo.png', output_format='PNG')    
  with col2:
    st.image("img/NBA-img.jpg")
  with col3:
    st.image("img/kaggle_logo.png", output_format='PNG')

  
  st.title('Analyse des tirs de joueurs NBA')
  st.write(
        """

    Projet d'analyse et de prédiction des tirs de 20 joueurs NBA sur la période 2003-2020.
    Ce projet a été réalisé dans le cadre d'une formation data scientist dispensée par Datascientest.

    Les 20 joueurs sont les suivants. L'année indiquée entre parenthèses est celle où le joueur a démarré son activité dans le championnat NBA.

      - LeBron James (2003)
      - Kevin Durant (2007)
      - Stephen Curry, Jrue Holiday, James Harden, DeMar DeRozan (2009)
      - Paul George (2010)
      - Kawhi Leonard, Kyrie Irving, Jimmy Butler, Klay Thompson (2011)
      - Anthony Davis, Damian Lillard, Khris Middleton, Draymond Green, Bradley Beal, Jonas Valanciunas (2012)
      - Giannis Antetokounmpo, Rudy Gobert, Kentavious Caldwell-Pope (2013)
    
    Les datasets utilisés ont été principalement téléchargés depuis le site Kaggle, plateforme web interactive qui propose des compétitions d'apprentissage automatique en science des données. 

    Auteurs :

      - Dominique Beaufrère ([LinkedIn](https://www.linkedin.com/in/dominiquebeaufrere))
      - Mikaël Jayet ([LinkedIn](https://www.linkedin.com/in/mikael-jayet))

    """
  )
