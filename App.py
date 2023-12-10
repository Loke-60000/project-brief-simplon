import pandas as pd
import plotly.express as px

# Lecture du fichier CSV
df = pd.read_csv('ventes.csv')



# Part 1: Chiffre d'Affaires par Produit
# Calcul du montant des ventes
df['montant'] = df['prix'] * df['qte']

# Graphique du chiffre d'affaires par produit
ca_par_produit = df.groupby('produit')['montant'].sum().reset_index()
fig1 = px.bar(ca_par_produit, x='produit', y='montant', title='Chiffre d\'Affaires par Produit')

# Export du graphique en HTML
fig1.write_html('Chiffre-d-affaires-par-produit.html')
print('Chiffre-d-affaires-par-produit.html généré avec succès !')


# Part 2: Quantité Vendue par Région
# Création d'un graphique en camembert pour la quantité vendue par région
figure = px.pie(df, values='qte', names='region', title='Quantité Vendue par Région')

# Export du graphique en HTML
figure.write_html('ventes-par-region.html')
print('ventes-par-region.html généré avec succès !')


# Part 3: Chiffre d'Affaires Total
# Calcul du chiffre d'affaires total
chiffre_affaires_total = df['montant'].sum()

# Création d'un DataFrame pour le graphique
data = {'Chiffre d\'Affaires': ['Total'], 'Montant': [chiffre_affaires_total]}
df_total = pd.DataFrame(data)

# Création du graphique pour le chiffre d'affaires total
fig2 = px.bar(df_total, x='Chiffre d\'Affaires', y='Montant', title='Chiffre d\'Affaires Total')

# Export du graphique en HTML
fig2.write_html('chiffre-d-affaires-total.html')
print('chiffre-d-affaires-total.html généré avec succès !')
