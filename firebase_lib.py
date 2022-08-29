from firebase_admin import credentials, db, initialize_app, delete_app # install with 'pip install firebase_admin'

class firebase_database():
	def __init__(self, key_file, database_url, name="default_firebase_app"):
		""" Constructeur de la classe 
			key_file : Fichier de clé
			database_url : url de la db
		"""
		firebase_credentials = credentials.Certificate(key_file)
		self.db = initialize_app(firebase_credentials, {"databaseURL":database_url}, name)


	def write(self, noeud, data, prevent_erase = True):
		""" Ecriture d'une donnée sur un noeud spécifié 
			Ecrit tout le noeud
			noeud : chemin du noeud depuis la racine
			data : données à écrire (dictionnaire)
			prevent_erase : si True, n'écrase pas le noeud s'il existe déjà
		"""

		# On définit le noeud
		fb_noeud = self.db.reference(noeud)

		# On regarde si le noeud existe déjà
		if prevent_erase and fb_noeud.get() is not None:
			# S'il existe déjà, on s'arrête là
			return False

		# On écrit les données
		fb_noeud.update(data)

		return True

	def update(self, noeud, data):
		""" Ecriture (mise à jour) d'une donnée sur un noeud spécifié 
			noeud : chemin du noeud depuis la racine
			data : données à écrire (dictionnaire)
		"""

		if type(data) != dict:
			raise TypeError("Data doit être un dictionnaire, pour écrire une valeur unique, utilisez la méthode 'write'")

		# On défini le noeud
		fb_noeud = self.db.reference(noeud)
		# On récupère le contenu du noeud
		noeud_data = fb_noeud.get()
		# On modifie les valeurs du noeud
		for key, item in data.items():
			noeud_data[key] = item
		# On renvoie le noeud
		fb_noeud.update(noeud_data)

		return True


	def read(self, noeud=""):
		""" Lecture des données à partir du noeud spécifié """

		# On défini le noeud
		fb_noeud = self.db.reference(noeud)
		return fb_noeud.get()


	def close(self):
		""" Détruire l'objet """

		delete_app(self.db)