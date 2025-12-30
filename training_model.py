import mlflow
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

# mi crea un Log in cui saranno anche salvati alcuni file e informazioni
mlflow.sklearn.autolog()
# scarico i dati
db = load_diabetes()
# solito delle esercitazioni
x_train, x_test, y_train, y_test = train_test_split( db.data, db.target )
# creo il modello
model = RandomForestRegressor( n_estimators=10,
                               max_depth=5,
                               random_state=10 )
# addestro il mio modello
model.fit( x_train, y_train )