from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    likes = float(request.form['likes'])
    saves = float(request.form['saves'])
    comments = float(request.form['comments'])
    shares = float(request.form['shares'])
    profile_visits = float(request.form['profile_visits'])
    follows = float(request.form['follows'])

    features = np.array([[likes, saves, comments, shares, profile_visits, follows]])
    prediction = model.predict(features)

    return render_template('index.html', prediction_text='Estimated Reach: {}'.format(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
