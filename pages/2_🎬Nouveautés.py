import streamlit as st
from streamlit_player import st_player

#st.sidebar.markdown("# Nouveautés")
page_title="Nouveautés"
st.title("🎬 Les nouveautés tendances en ce moment :")

with st.sidebar:
    st.image('RAJJ-master\Images\LogoTOP.png')

tab1, tab2, tab3 = st.tabs(["Furiosa", "Bad Boys 4", "Le Comte de Monte-Cristo"])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.image('https://cdn.lesnumeriques.com/optim/news/21/219752/6e969e98-furiosa-une-anya-taylor-joy-vengeresse-dans-un-nouveau-trailer-jubilatoire_png__1200_678__0-96-1816-1120.jpg', width=700)
        st_player("https://www.youtube.com/watch?v=tHJiytWjjSI&pp=ygUYZnVyaW9zYSBiYW5kZSBhbm5vbmNlIHZm")
    with col2:
        st.write('22 mai 2024 en salle')
        st.write('Durée : 2h 28min')
        st.write('Genre : Action, Science Fiction')
        st.write('Réalisé par : George Miller')
        st.write('Avec Anya Taylor-Joy, Chris Hemsworth, Tom Burke')
        st.subheader('Synopsis')
        st.subheader('Interdit - 12 ans')
        st.write('Dans un monde en déclin, la jeune Furiosa est arrachée à la Terre Verte et capturée par une horde de motards dirigée par le redoutable Dementus. Alors qu’elle tente de survivre à la Désolation, à Immortan Joe et de retrouver le chemin de chez elle, Furiosa n’a qu’une seule obsession : la vengeance.')

        

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://www.createur-video-entreprise.com/wp-content/uploads/2024/01/bad-boys-4.jpg")
        st_player("https://www.youtube.com/watch?v=Y7GX3iPk0xE&pp=ygUlYmFkIGJveXMgcmlkZSBvciBkaWUgYmFuZGUgYW5ub25jZSB2Zg%3D%3D")
    with col2:
        
        st.write('Date de sortie : 5 juin 2024 en salle')
        st.write('Durée : 1h 55min')
        st.write('Genre : Action')
        st.write('Réalisé par : Adil El Arbi, Bilall Fallah')
        st.write('Avec : Martin Lawrence, Will Smith, Vanessa Hudgens')
        st.subheader('Synopsis')
        st.write("Cet été, la franchise Bad Boys est de retour avec son mélange iconique d'action explosive et d'humour irrévérencieux. Mais cette fois-ci, les meilleurs flics de Miami deviennent les hommes les plus recherchés d'Amérique.")
with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://www.ecranlarge.com/media/cache/1600x1200/uploads/image/001/510/le-comte-de-monte-cristo-deuxieme-bande-annonce-pour-ladaptation-avec-pierre-niney-du-monument-de-la-litterature-1510173.png")
        st_player("https://www.youtube.com/watch?v=u0YnbsyvGS0&pp=ygUdTGUgQ29tdGUgZGUgTW9udGUtQ3Jpc3RvIDIwMjQ%3D", )
    with col2:
        st.write('Date de sortie : 28 juin 2024 en salle')
        st.write('Durée : 2h 58min')
        st.write('Genre : Aventure, Historique')
        st.write('Réalisé par : Matthieu Delaporte, Alexandre De La Patellière')
        st.write('Avec : Pierre Niney, Bastien Bouillon, Anaïs Demoustier')
        st.subheader('Synopsis')
        st.write("Victime d’un complot, le jeune Edmond Dantès est arrêté le jour de son mariage pour un crime qu’il n’a pas commis. Après quatorze ans de détention au château d’If, il parvient à s’évader. Devenu immensément riche, il revient sous l’identité du comte de Monte-Cristo pour se venger des trois hommes qui l’ont trahi.")