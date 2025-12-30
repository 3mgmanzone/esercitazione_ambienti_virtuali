# Questo è il File README
Questo è il file Readme
In questo progetto andremo ad addestrare un Modello di ML con MLFlow


# creo il File .GITIGNORE
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ touch .gitignore
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git add .gitignore
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git commit -m "aggiunta file .gitignore"
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git push


# creo un ambiente virtuale di nome VENV
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ python -m venv venv
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ source venv/bin/activate
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ deactivate
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ 


# installo la libreria MLFLOW
@3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ pip install mlflow
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ python
>>> import mlflow
>>> mlflow.__version__
>>> quit()
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ pip list


# adesso si parte con l'addestramento del Modello di ML
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ touch training_model.py
# abbiamo scritto il codice in python e adesso lanciamo
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ python training_model.py
# viene creata una cartella con un sacco di informazioni "MLRUNS"


# carichiamo tutto quanto sul Repository Remoto
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git add training_model.py
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git add mlruns
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git commit -m "aggiunta codice python + cartella mlruns"
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git push
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git add mlflow.db
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git commit -m "aggiunta ultimo file dimenticato"
(venv) @3mgmanzone ➜ /workspaces/esercitazione_ambienti_virtuali (main) $ git push