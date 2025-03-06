from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_cardioguard(age, creatinine, ejection_fraction, sodium):
    """Calculate the Cardioguard Score based on medical parameters."""
    score = (int(age > 65) + int(creatinine > 1.5) +
             int(ejection_fraction < 30) + int(sodium < 135))
    
    if score == 0:
        risk_level = "Low"
        explanation = "The patient has no significant indicators of repeat heart failure."
    elif score == 1:
        risk_level = "Moderate"
        explanation = "The patient has a mild risk factor that may need monitoring."
    elif score == 2:
        risk_level = "Elevated"
        explanation = "The patient shows some indicators of potential heart failure risk."
    elif score == 3:
        risk_level = "High"
        explanation = "The patient has multiple risk factors and requires close monitoring."
    else:
        risk_level = "Severe"
        explanation = "The patient is at severe risk of heart failure recurrence and requires immediate medical attention."
    
    return score, risk_level, explanation

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        age = float(request.form['age'])
        creatinine = float(request.form['creatinine'])
        ejection_fraction = float(request.form['ejection_fraction'])
        sodium = float(request.form['sodium'])
        
        score, risk_level, explanation = calculate_cardioguard(age, creatinine, ejection_fraction, sodium)
        result = f"Cardioguard Score: {score} ({risk_level}) - {explanation}"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
