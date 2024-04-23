from flask import Flask, render_template
import pickle
import pandas as pd


app = Flask(__name__)
popular_df = pickle.load(open("popular_movies_df.pkl",'rb'))
movies = popular_df.sort_values(by='avg_vote',ascending=False)[:50]

@app.route('/')
def top_movies():
    top_movies = movies.to_dict('records')
    return render_template('home.html',movies = top_movies)
if __name__=='__main__':
    app.run(debug=True)
