from dotenv import load_dotenv
import random
import os
load_dotenv()

champions = [
	"Musclor : Le Défenseur d’Eternia, un guerrier puissant qui manie l’Épée de Pouvoir et protège les secrets du Château des Ombres.",
	"Starlion : Le Seigneur des Cosmocats, un héros noble armé de l’Épée d’Omens et guidé par un profond sens de la justice.",
	"Cobra : L’Aventurier de l’Espace, un aventurier rusé avec un Psychogun et un talent pour déjouer ses ennemis.",
	"She-Ra : La Princesse du Pouvoir, une championne intrépide avec l’Épée de Protection, en mission pour libérer Etheria.",
	"Duke : Le Leader de G.I. Joe, un commandant courageux qui lutte pour la liberté contre les forces de Cobra.",
	"Optimus Prime : Le Chef des Autobots, un robot sage et puissant qui se transforme pour défendre la Terre contre les Decepticons.",
	"Capitaine Flam : Le Protecteur de l’Univers, un stratège brillant qui défend la galaxie contre les menaces interstellaires.",
	"Albator : Le Corsaire de l’Espace, un capitaine audacieux de l’Arcadia qui combat la tyrannie pour protéger la liberté de la Terre.",
	"Jem : La Star Glamour, une chanteuse aux pouvoirs holographiques qui inspire et protège avec son groupe, les Holograms.",
	"Seiya : Le Chevalier de Pégase, un guerrier courageux qui canalise la puissance du cosmos pour combattre l’injustice.",
	"Goldorak : Le Protecteur Cosmique, un robot géant piloté par Actarus pour défendre la Terre contre les forces de Véga."
]

def pick_random_description():
    return random.choice(champions)