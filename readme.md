# firebase_lib

## Import
```python
import firebase_lib
```

## Instanciation
```python
firebase = firebase_lib.firebase_database("chemin_vers_la_clé.json", "lien_vers_la_realtime_database", name)
# Name est utilisé si plusieurs instances différentes
```

## Ecriture de données
```python
firebase.write("noeud", données, prevent_erase=False)
# prevent_erase si faux, ne prévient pas avant d'effacer
```

## Lire les données
```python
firebase.read("noeud")
```