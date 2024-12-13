import streamlit as st
import pandas as pd

# Charger les données PERFADOM
data = {
    "Code": [
        "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F17", "F18",
        "F19", "F20", "F27", "F28", "F29", "F30", "F31", "F32", "F33",
        "F34", "F35", "F36", "F37", "F38", "F39", "F40"
    ],
    "Intitulé": [
        "Forfait installation Système Actif",
        "Forfait installation 2ème Système Actif ( > 4jours après)",
        "Forfait installation Système Actif remplissage Etablissement",
        "Forfait installation Diffuseur",
        "Forfait installation 2ème Diffuseur ( > 4jours après)",
        "Forfait installation + Suivi Gravité",
        "Forfait Suivi Système Actif",
        "Forfait Suivi Diffuseur",
        "Forfait Perfuseur/par perfusion/ max 15 perfusions",
        "Forfait Perfuseur 1 perf/jour",
        "Forfait Perfuseur 2 perfs/jour",
        "Forfait Perfuseur > 2 perfs/jour",
        "Forfait consommable SA 1perf/sem",
        "Forfait consommable SA 2 à 3 perf/sem",
        "Forfait consommable SA 4 à 6 perf/sem",
        "Forfait consommable SA 1perf/jour = 7perfs/semaine",
        "Forfait consommable SA 2perf/jour= 14 perfs/semaine",
        "Forfait consommable SA 3perf/jour= 21 perfs/semaine",
        "Forfait consommable SA >3perf/jour",
        "Forfait consommable Diffuseur 1perf/sem",
        "Forfait consommable Diffuseur 2 à 3 perf/sem",
        "Forfait consommable Diffuseur 4 à 6 perf/sem",
        "Forfait consommable Diffuseur 1perf/jour = 7perfs/semaine",
        "Forfait consommable Diffuseur 2perf/jour= 14 perfs/semaine",
        "Forfait consommable Diffuseur 3perf/jour= 21 perfs/semaine",
        "Forfait consommable Diffuseur >3perf/jour"
    ],
    "Fréquence": [
        "1X/Semestre", "1X/Semestre", "1X/Semestre", "1X/Semestre", "1X/Semestre",
        "One shot", "Hebdomadaire", "Hebdomadaire", "Par perfusion", "Hebdomadaire",
        "Hebdomadaire", "Hebdomadaire", "Hebdomadaire", "Hebdomadaire", "Hebdomadaire",
        "Hebdomadaire", "Hebdomadaire", "Hebdomadaire", "Hebdomadaire",
        "Hebdomadaire", "Hebdomadaire", "Hebdomadaire", "Hebdomadaire",
        "Hebdomadaire", "Hebdomadaire", "Hebdomadaire"
    ],
    "Tarif_TTC": [
        357.2, 164.86, 164.86, 228.97, 105.33, 45.79, 100.75, 45.79, 10.8, 76.02,
        143.8, 204.24, 34.76, 69.51, 156.4, 240.15, 454.97, 647.27, 815.18, 31.27,
        62.55, 140.75, 216.12, 409.47, 582.54, 733.66
    ],
    "Tarif_HT": [
        285.76, 131.89, 131.89, 183.18, 84.26, 36.63, 80.60, 36.63, 8.64, 60.82,
        115.04, 163.39, 27.81, 55.61, 125.12, 192.12, 363.98, 517.82, 652.14, 25.02,
        50.04, 112.6, 172.9, 327.58, 466.03, 586.93
    ]
}

perfadom_data = pd.DataFrame(data)

# Titre de l'application
st.image("logo.png", width=150)
st.title("Calculette PERFADOM")

# Informations du patient
st.header("Informations du patient")
nom = st.text_input("Nom du patient :")
prenom = st.text_input("Prénom du patient :")
date_naissance = st.date_input("Date de naissance (jj/mm/aaaa) :")

if nom and prenom and date_naissance:
    st.write(f"Patient : {nom} {prenom}, né(e) le {date_naissance.strftime('%d/%m/%Y')}")

# Sélection des prestations pour une ordonnance
st.header("Calcul du montant d'une ordonnance")
selected_items = st.multiselect(
    "Sélectionnez des prestations par leur intitulé :", options=perfadom_data["Intitulé"].tolist()
)

if selected_items:
    selected_data = perfadom_data[perfadom_data["Intitulé"].isin(selected_items)]
    selected_data["Quantité"] = st.number_input(
        "Indiquez la quantité totale pour ces prestations", min_value=1, step=1, value=1
    )
    selected_data["Montant_TTC"] = selected_data["Tarif_TTC"] * selected_data["Quantité"]
    st.write("Détails de l'ordonnance :", selected_data)
    st.write("Montant total TTC :", selected_data["Montant_TTC"].sum())
else:
    st.write("Aucune prestation sélectionnée.")

# Footer
st.write("\n---\nCréé avec ❤️ pour simplifier la gestion des forfaits PERFADOM.")
