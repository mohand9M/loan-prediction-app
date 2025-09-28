from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Charger le modèle depuis le chemin relatif
model_path = os.path.join(os.getcwd(), 'model', 'rf_model.pkl')
try:
    with open(model_path, 'rb') as f:
        rf_model = pickle.load(f)
    print("Modèle chargé avec succès !")
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")


@app.route('/')
def index():
    """Route pour la page d'accueil."""
    return render_template('index.html')


@app.route('/loan')
def loan():
    """Route pour la page de demande de prêt avec le formulaire."""
    return render_template('loan_form.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Route pour gérer la prédiction après soumission du formulaire."""
    try:
        # Collecter les valeurs du formulaire
        loan_term = int(request.form['loan_term'])
        loan_amount = float(request.form['loan_amount'])
        cibil_score = float(request.form['cibil_score'])
        income_annum = float(request.form['income_annum'])
        no_of_dependents = int(request.form['no_of_dependents'])
        education = int(request.form['education'])
        self_employed = int(request.form['self_employed'])
        residential_assets_value = float(request.form['residential_assets_value'])
        luxury_assets_value = float(request.form['luxury_assets_value'])
        commercial_assets_value = float(request.form['commercial_assets_value'])
        bank_asset_value = float(request.form['bank_asset_value'])

        # Construire les caractéristiques pour la prédiction
        features = [
            0,
            loan_term,
            loan_amount,
            income_annum,
            no_of_dependents,
            education,
            self_employed,
            cibil_score,
            residential_assets_value,
            luxury_assets_value,
            commercial_assets_value,
            bank_asset_value,
        ]
        
        # Prédire avec le modèle
        prediction = rf_model.predict([features])
        result_text = "Approuvé" if prediction[0] == 0 else "Rejeté"

        return render_template('result.html', result=result_text)
    except Exception as e:
        print(f"Erreur dans la prédiction : {e}")
        return render_template('result.html', result="Erreur lors de la prédiction")


if __name__ == '__main__':
    app.run(debug=True)
