import pandas as pd
import matplotlib.pyplot as plt

# %pip install openpyxl   #pour lire les fichiers Excel

# Chemin du fichier Excel
file_path = r"C:\Users\Lenovo\Desktop\CC3-Projet\medical_sales.xlsx"

# Phase 1 : Préparation et Nettoyage

# 1. Charger les feuilles Excel : Transactions, Products, Customers
df_transactions = pd.read_excel(file_path, sheet_name="Transactions")  # Feuille Transactions
df_products = pd.read_excel(file_path, sheet_name="Products")          # Feuille Products
df_customers = pd.read_excel(file_path, sheet_name="Customers")        # Feuille Customers

# Afficher les 5 premières lignes 
df_transactions.head()

# 2. Identifier les colonnes avec des valeurs manquantes dans df_transactions
df_transactions.isna().sum()  # Vérifie le nombre de NaN par colonne

# Supprimer les lignes contenant des NaN 
df_transactions = df_transactions.dropna()

# Vérifier les aleurs manquantes
df_transactions.isna().sum()

# 3. Fusionner les trois tables pour créer un DataFrame unique df_drug_sales
df_drug_sales = (
    df_transactions
    .merge(df_products, on="DrugID", how="left")     # Fusion Transactions + Products sur DrugID
    .merge(df_customers, on="CustomerID", how="left") # Fusion + Customers sur CustomerID
)

# Afficher les 5 premières lignes du DataFrame final
df_drug_sales.head()

# 4. Ajouter les colonnes de performance
df_drug_sales["total_sales"] = df_drug_sales["UnitsSold"] * df_drug_sales["UnitSalesPrice"]  # Total ventes
df_drug_sales["total_costs"] = df_drug_sales["UnitsSold"] * df_drug_sales["CostOfProduction"] # Total coûts
df_drug_sales["gross_profit"] = df_drug_sales["total_sales"] - df_drug_sales["total_costs"]   # Profit brut

# 5. Vérifier les types de données (notamment SaleDate)
df_drug_sales["SaleDate"] = pd.to_datetime(df_drug_sales["SaleDate"])  # Convertir en datetime
df_drug_sales.dtypes  # Affiche les types de colonnes

# Ajouter une colonne Year pour les analyses annuelles
df_drug_sales["Year"] = df_drug_sales["SaleDate"].dt.year

# Phase 2 : Analyse Statistique et Visualisation

# 6. Regrouper par année et calculer le profit brut total
df_yearly_profit = (
    df_drug_sales
    .groupby("Year")["gross_profit"]
    .sum()
    .reset_index()
)

# Afficher le DataFrame annuel
df_yearly_profit

# Tracer un graphique en ligne pour l'évolution annuelle du profit brut
plt.figure()
plt.plot(
    df_yearly_profit["Year"],        # Axe X : Année
    df_yearly_profit["gross_profit"],# Axe Y : Profit brut total
    marker='o'                       # Marqueur pour chaque point
)
plt.xlabel("Année")                  # Label axe X
plt.ylabel("Profit Brut Total")      # Label axe Y
plt.title("Évolution annuelle du profit brut")  # Titre du graphique
plt.xticks(df_yearly_profit["Year"])           # Afficher toutes les années sur l'axe X
plt.grid(True,alpha=0.3)                        # Ajouter une grille légère
plt.show()

# 7. Regrouper par pays et calculer la moyenne des ventes
df_country_sales = (
    df_drug_sales
    .groupby("Country")["total_sales"]
    .mean()
    .reset_index()
)

# Afficher le DataFrame par pays
df_country_sales

# Tracer un graphique en barres pour la moyenne des ventes par pays
plt.figure()
plt.bar(
    df_country_sales["Country"],    # Axe X : Pays
    df_country_sales["total_sales"] # Axe Y : Moyenne des ventes
)
plt.xlabel("Pays")                  # Label axe X
plt.ylabel("Moyenne des ventes")    # Label axe Y
plt.title("Moyenne des ventes par pays") # Titre du graphique
plt.xticks(rotation=45)             # Faire pivoter les labels de l'axe X pour lisibilité
plt.show()


# Phase 3 : Développement de l'Application Dash

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Initialiser l'application Dash
app = dash.Dash(__name__)

# 8. Layout de l'application
app.layout = html.Div([

    # Titre principal
    html.H3("Ventes de médicaments par pays"),

    # Sélecteur de dates pour filtrer les résultats
    dcc.DatePickerRange(
        id="date",
        start_date=df_drug_sales["SaleDate"].min(),  # Date de début par défaut
        end_date=df_drug_sales["SaleDate"].max()     # Date de fin par défaut
    ),

    # Menu déroulant pour sélectionner un pays
    dcc.Dropdown(
        id="country",
        options=[
            {"label": c, "value": c}               # Chaque pays comme option
            for c in df_drug_sales["Country"].unique()
        ],
        value=df_drug_sales["Country"].unique()[0]  # Valeur par défaut
    ),

    # Graphique dynamique
    dcc.Graph(id="graph")
])

# 9. Callback pour générer le graphique en barres empilées dynamique
@app.callback(
    Output("graph", "figure"),
    Input("country", "value"),
    Input("date", "start_date"),
    Input("date", "end_date")
)
def update(country, start, end):

    # Filtrer les données selon le pays et la période sélectionnés
    df = df_drug_sales[
        (df_drug_sales["Country"] == country) &
        (df_drug_sales["SaleDate"] >= start) &
        (df_drug_sales["SaleDate"] <= end)
    ]

    # Créer le graphique en barres empilées par genre
    fig = px.bar(
        df,
        x="SaleDate",         # Axe X : Date de vente
        y="gross_profit",     # Axe Y : Profit brut
        color="Gender",       # Empiler par genre Male/Female
        barmode="stack"       # Barres empilées
    )

    # Formater l'axe Y pour afficher les valeurs en millions
    fig.update_yaxes(tickformat=".1fM", title="Profit Brut (M)")

    # Mettre à jour le titre dynamiquement selon le pays sélectionné
    fig.update_layout(title=f"Profit Brut pour {country}")

    return fig

# Lancer l'application Dash
if __name__ == "__main__":
    app.run(port=8051, debug=False)
