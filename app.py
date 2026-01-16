from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

app = Flask(__name__)

# Load dataset and train model (simple example)
df = pd.read_csv('1.csv')

# Encode categorical columns
le_gender = LabelEncoder()
le_eye = LabelEncoder()
df['Gender'] = le_gender.fit_transform(df['Gender'])
df['EyeColor'] = le_eye.fit_transform(df['EyeColor'])

# Features and target
X = df[['Age', 'Gender']]
y = df['EyeColor']

# Train regression model
model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        gender = request.form['gender']
        
        # Encode gender
        gender_num = le_gender.transform([gender])[0]
        
        # Make prediction
        pred = model.predict([[age, gender_num]])[0]
        pred_rounded = round(pred)
        
        # Convert back to eye color name
        prediction = le_eye.inverse_transform([pred_rounded])[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
    