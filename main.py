import streamlit as st

# -------------------------------------------------------------
# 0. Petites données de base
# -------------------------------------------------------------
# Une liste de dictionnaires : chaque dictionnaire représente une campagne.
campagnes = [
    {
        "nom": "Les Brumes de Valombre",
        "type": "Fantasy médiévale",
        "jeu": "D&D 5e",
        "personnage": "Cérène, rôdeur humain",
        "mj": "Thomas",
        "jour": "Vendredi soir",
        "joueurs": 5,
        "quete": "Explorer la Moria.",
        "derniere_partie": "29/05/2026",
        "image": "🧙‍♂️🌲"
    },
    {
        "nom": "Chroniques du Néant",
        "type": "Horreur / enquête",
        "jeu": "L'Appel de Cthulhu",
        "personnage": "Émile Caron, médecin militaire",
        "mj": "Lucie",
        "jour": "Dimanche après-midi",
        "joueurs": 4,
        "quete": "Comprendre les rêves étranges des habitants du manoir.",
        "derniere_partie": "22/06/2026",
        "image": "🕯️👁️"
    },
    {
        "nom": "Astres Brisés",
        "type": "Science-fiction",
        "jeu": "Starfinder",
        "personnage": "Nox-17, pilote androïde",
        "mj": "Mehdi",
        "jour": "Mercredi soir",
        "joueurs": 6,
        "quete": "Explorer une station spatiale abandonnée.",
        "derniere_partie": "01/04/2026",
        "image": "🚀🤖"
    },
    {
        "nom": "La Cité sous la Pluie",
        "type": "Urbain / infiltration",
        "jeu": "Blades in the Dark",
        "personnage": "Mara Voss, voleuse négociatrice",
        "mj": "Anaïs",
        "jour": "Samedi soir",
        "joueurs": 3,
        "quete": "Voler un registre secret chez un noble corrompu.",
        "derniere_partie": "15/06/2026",
        "image": "🌃🗡️"
    }
]

# Notes d'évaluation simples.
evaluations = [
    {"Campagne": "Les Brumes de Valombre", "Ambiance": 10, "Roleplay": 8, "Combats": 8, "Fun": 10},
    {"Campagne": "Chroniques du Néant", "Ambiance": 8, "Roleplay": 9, "Combats": 3, "Fun": 7},
    {"Campagne": "Astres Brisés", "Ambiance": 7, "Roleplay": 6, "Combats": 8, "Fun": 8},
    {"Campagne": "La Cité sous la Pluie", "Ambiance": 9, "Roleplay": 10, "Combats": 5, "Fun": 9},
]


# -------------------------------------------------------------
# 1. Un titre et un en-tête
# -------------------------------------------------------------
st.title("🎲 Ma passion : le JDR plateau")
st.image("https://www.jeuxderole.com/wp-content/uploads/2025/02/Daggerheart-JDR-couverture.png.webp")
st.header("Bienvenue dans mon carnet de campagnes")
st.write("Cette page présente les campagnes de jeu de rôle auxquelles je participe.")

st.markdown("---")


# -------------------------------------------------------------
# 2. Un menu déroulant : choisir une campagne
# -------------------------------------------------------------
noms_campagnes = [
    "Les Brumes de Valombre",
    "Chroniques du Néant",
    "Astres Brisés",
    "La Cité sous la Pluie"
]

choix = st.selectbox(
    "Choisis une campagne :",
    noms_campagnes
)

st.write(f"Tu as choisi : **{choix}**")

campagne = None

for element in campagnes:
    if element["nom"] == choix:
        campagne = element


# -------------------------------------------------------------
# 3. Affichage des détails de la campagne
# -------------------------------------------------------------
st.subheader("📖 Détails de la campagne")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"## {campagne['image']}")
    st.write(f"**Type de JDR :** {campagne['type']}")
    st.write(f"**Jeu utilisé :** {campagne['jeu']}")
    st.write(f"**MJ :** {campagne['mj']}")
    st.write(f"**Jour de jeu :** {campagne['jour']}")

with col2:
    st.write(f"**Mon personnage :** {campagne['personnage']}")
    st.write(f"**Nombre de joueurs :** {campagne['joueurs']}")
    st.write(f"**Dernière partie :** {campagne['derniere_partie']}")
    st.write(f"**Quête en cours :** {campagne['quete']}")

st.markdown("---")

# -------------------------------------------------------------
# 4. Un widget de saisie en plus
# -------------------------------------------------------------
st.subheader("⭐ Mon avis génral sur cette campagne")

note = st.slider("Ma note sur 10", 0, 10, 8)
st.write(f"Ta note : **{note}/10**")

recommande = st.checkbox("Je recommande cette campagne")
commentaire = st.text_input("Un petit commentaire :", placeholder="Ex : super ambiance, combats épiques...")

st.markdown("---")

# -------------------------------------------------------------
# 5. Un petit tableau d'évaluations
# -------------------------------------------------------------
st.subheader("📊 Notes moyennes du groupe sur ces campagnes")

st.dataframe(evaluations)

st.markdown("---")

# -------------------------------------------------------------
# 6. Mes recommandations de jeux
# -------------------------------------------------------------
st.subheader("🎯 Mes recommandations de jeux")

style = st.radio(
    "Tu veux plutôt jouer à :",
    ["Une aventure épique", "Une enquête inquiétante", "De la science-fiction", "Un casse / infiltration"]
)

if style == "Une aventure épique":
    st.success("Je recommande : **D&D 5e** 🧙‍♂️")
elif style == "Une enquête inquiétante":
    st.success("Je recommande : **L'Appel de Cthulhu** 🕯️")
elif style == "De la science-fiction":
    st.success("Je recommande : **Starfinder** 🚀")
else:
    st.success("Je recommande : **Blades in the Dark** 🌃")

st.markdown("---")

# -------------------------------------------------------------
# 7. Un bouton
# -------------------------------------------------------------
st.subheader("✅ Validation")

if st.button("Valider"):
    st.success("Bravo, ton app Streamlit JDR tourne ! 🎉")

    if recommande:
        st.write("Tu recommandes cette campagne 👍")

    if commentaire:
        st.write(f"Ton commentaire : {commentaire}")

else:
    st.info("Clique sur le bouton pour valider.")


# --- Idées pour aller un peu plus loin (facultatif) ---
# st.image("une_image.jpg")          # afficher une vraie image locale
# st.sidebar.selectbox(...)          # mettre les filtres dans une sidebar
# st.bar_chart(...)                  # afficher un graphique simple
# st.text_area(...)                  # écrire un avis plus long
