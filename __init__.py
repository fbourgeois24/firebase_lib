import os

try:
	# On importe tout
	from firebase_lib.firebase_lib import firebase_database
except ModuleNotFoundError:
	# Si module non trouvé, on installe les dépendances
	os.popen(f"pip install --no-cache-dir -r {os.path.dirname(os.path.realpath(__file__))}/requirements.txt").read()
	from firebase_lib.firebase_lib import firebase_database
