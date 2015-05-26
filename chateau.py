def lieu(liste, position):
	print (liste[position])

liste_direction = [[8, 8, 8, 3], [8, 8, 2, 4], [1, 8, 8, 5], [8, 0, 4, 8], [3, 1, 5, 6], [4, 2, 8, 8], [8, 4, 8, 8]]
liste_noms = [""" ________________
|                |
|    Chambre     |
|_______  _______|""""\n", """ ________________
|                |
|    Débaras     
|_______  _______|""""\n", """ ________________
|                |
     Cuisine     |
|_______  _______|""""\n", """ _______  _______
|                |
|  Bibliothèque     
|________________|""""\n", """ _______  _______
|                |
       Hall      
|_______  _______|""""\n", """ _______  _______
|                |
      Salon      |
|________________|""", """ _______  _______
|                |
|     Jardin     |
|________________|""" "\n"]




place_actuelle = 0
direction = 0

while direction != 6:
	print (""" ________________ ________________ _________________
|                |                |                 |
|    chambre     |    Débarras          Cuisine     |    
|_______  _______|_______  _______|________  _______|
|                |                |                 |
|  Bibliothèque         Hall             Salon      |
|________________|_______  _______|_________________|
|                                                   |
|                      Jardin                       |
|___________________________________________________|""")
	lieu(liste_noms, place_actuelle)
	direction = int(input("Ou voulez vous aller ? : \n   1 - Gauche \n   2 - Haut \n   3 - Droite \n   4 - Bas \n   5 - Sortir \n    "))
	
	if direction == 5:
		print ("A bientôt !")
		exit ()
		
	direction = direction - 1
	
	if direction < 5:
		
		if liste_direction[place_actuelle][direction] != 8:
			place_actuelle = liste_direction[place_actuelle][direction]
			
	else:
		print ("Valeur impossible !")
		
		
		
		
		
		
		
		
		
		
		
		
		
