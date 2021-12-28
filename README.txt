INSTALLATION : 
	Téléchargez les dépendances python avec :
	
		pip install -r requirements.txt
	
	Si vous souhaitez utiliser tensorflow GPU :

		pip install tensorflow-gpu
		
	Sinon : 

		pip install tensorflow-cpu


LES CORPUS :
	Ils sont tous situés dans data/
	J'en ai laissé plusieurs à disposition.
	Par défaut tous les codes utilisent Corpus_POETRY.txt
	Mais vous pouvez très bien regarder ce qu'on peut produire avec les autres ;)


COMMENT UTILISER LE CODE :
	Pour lancer le Générateur de Markov (situé dans MarkovGenerator) :
		(NOTE SUR LE GENERATEUR MARKOVIEN) : 
			Il y'a beaucoup de paramètres qui peuvent être modifiés.
			Je conseil de l'utiliser en lançant juste run.py 
			pour voir ce qu'il se passe avant de lire la description de chaque paramètre.


		Configurer les constantes dans run.py:
			- GENERATING : 
				Booléen qui indique si on regénère de nouvelles phrases d'exemple.
				Pour éviter de tout regénérer à chaque fois que l'on veut créer un poème on peut le mettre à false.
				J'ai laissé une génération de 20000 phrases dans out/ngram-pregen-out.txt
				Elle est utilisée si GENERATING est à False 
				Par défaut : False

			- NB_SENTENCES_TO_GENERATE :
				Le nombre de phrases à générer.
				Doit être élevé si on souhaite créer des rimes (solution expliquée dans le rapport)
				Un nombre élevé prend néanmoins beaucoup de temps.
				Si on souhaite juste générer des vers sans essayer de les faire rimer on peut :
					- Mettre NB_SENTENCES_TO_GENERATE = 50
					- Mettre MAKING_RHYMES = False
				Par défaut : 20000

			- MAKING_RHYMES :
				Booléen qui indique si oui on non on essaye de faire des rhymes.
				Par défaut : True
			- SENTENCE_LENGTH_LIMIT :
				Indique le nombre de mot que contiendront au maximum chacune des phrases
				Par défaut : 12

			- NGRAM_SIZE : 
				Correspond au nombre de mots à partir des quels on construit la table.
				Le choix par défaut est 2 car c'est celui qui donne les meilleurs résultats
				sans trop réciter le corpus.
				On peut faire varier NGRAM_SIZE entre 1 et 4 (plus la valeur est élevée, plus 
				on va coller au vrai texte.)
				Par défaut : 7

			- POEM_LINES_NB :
				Utile pour la Post-Generation. Indique la moitié du nombre de vers à créer
				
			- IMPORT_TABLE : 
				Booléen qui indique si on importe une table json déjà existante ou non
				si IMPORT_TABLE est false on va générer une nouvelle table json, 
				ce qui peut prendre du temps.
				Par défaut à False

			- IMPORTED_TABLE_FILENAME :
				Le Path de la Table json utilisée
				Par défaut à ""

			- CORPUS_PATH : 
				Le Path du corpus utilisé.
				Par défaut à "../../data/Corpus_POETRY.txt"
		Une fois que toutes les valeurs ont été configurées, il suffit de lancer le code avec
			
			python3 run.py 
				
	====================================================================================================

	Pour lancer GPT2
		Lien vers la doc de GPT2

	====================================================================================================

	L'utilisation des répertoires : 
		- GRU_SIMPLE
		- GRU_BIFURCATION
		- LSTM_BIFURCATION
		- LSTM_SIMPLE	
	Est la même.
	Dans chacun des des cas il faut :
	(OPTIONEL)- Mettre les drivers CUDA dans le répertoire si on utilise un GPU
		  - Configurer les constantes dans TextGeneration.py :
			- EPOCH :
				Le nombre d'epochs
				Par défaut : 20
			- SEQ_LENGTH :
				Le nombre de caractères qu'on regarde pour s'entrainer
				Par défaut : 100
			- POEM_START :
				correspond à la phrase à partir de laquelle on va générer le poème
				Par défaut : Dépend du générateur

		  - Lancer TextGeneration.py en séléctionnant un des corpus pour entrainer le réseau.
		  - Lancer Main.py pour utiliser le réseau et produire des chaines de caractères.

	====================================================================================================


