from firebase_admin import credentials, db, initialize_app # install with 'pip install firebase_admin'

class firebase_database():
	def __init__(self, key_file, database_url):
		""" Constructeur de la classe 
			key_file : Fichier de clé
			database_url : url de la db
		"""
		firebase_credentials = credentials.Certificate(key_file)
		initialize_app(firebase_credentials, {"databaseURL":database_url})


	def write(self, noeud, data, prevent_erase = True):
		""" Ecriture d'une donnée sur un noeud spécifié 
			noeud : chemin du noeud depuis la racine
			data : données à écrire (dictionnaire)
			prevent_erase : si True, n'écrase pas le noeud s'il existe déjà
		"""

		# On définit le noeud
		fb_noeud = db.reference(noeud)

		# On regarde si le noeud existe déjà
		if prevent_erase and fb_noeud.get() is not None:
			# S'il existe déjà, on s'arrête là
			return False

		# On écrit les données
		fb_noeud.update(data)

		return True


	def read(self, noeud=""):
		""" Lecture des données à partir du noeud spécifié """

		# On défini le noeud
		fb_noeud = db.reference(noeud)
		return fb_noeud.get()