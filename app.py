from flask import Flask, render_template, url_for,request
import pickle
import numpy as np


app = Flask(__name__)

# load the model from disk

clf = pickle.load(open('nlp_model.pkl', 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        prediction_numeric = clf.predict(vect)[0]

        # Map numeric prediction to class labels
        if prediction_numeric == 0:
            my_prediction = "Given message is ham"
        else:
            my_prediction = "Given message is spam"

    return render_template('home.html', prediction_text=my_prediction)




if __name__ == '__main__':
	app.run(debug=True)
	



