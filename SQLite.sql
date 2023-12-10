-- Calcul du chiffre d'affaires total

SELECT SUM(prix * qte) AS chiffre_daffaires_total FROM ventes;
-- Chiffre d'affaires total = 44825

-- Calcul des ventes par produit

SELECT produit, SUM(prix * qte) AS ventes_par_produit FROM ventes GROUP BY produit;
-- Ventes par produit | Produit_A= 17500 | Produit_B= 15825v | Produit_C = 11500 |

-- Calcul des ventes par région

SELECT region, SUM(prix * qte) AS ventes_par_region FROM ventes GROUP BY region;
-- Nord = 20725 | Sud = 24100