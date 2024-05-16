from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

def convert_numeric_columns(df):
    numeric_columns = ['gross']
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')  
    return df

def get_unique_values(df, column):
    return sorted(df[column].dropna().unique())


@app.route('/')
def redirect_to_login():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_submit():
    
    return redirect(url_for('main'))


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_submit():
   
    username = request.form['username']
    password = request.form['password']
  
    print(f"Username: {username}, Password: {password}")
   
    return redirect(url_for('main'))

@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/select_star', methods=['GET', 'POST'])
def select_star():
    if request.method == 'POST':
        df = pd.read_csv('C:/Users/Bhavana/OneDrive/Desktop/MovieRecommendationSystem/data/preprocessed_movies.csv')
        df = convert_numeric_columns(df)
        star_names = get_unique_values(df, 'star')
        return render_template('select_star.html', star_names=star_names)
    else:
        return redirect(url_for('main'))

@app.route('/get_details', methods=['POST'])
def get_details():
    selected_star = request.form['star']
    df = pd.read_csv('C:/Users/Bhavana/OneDrive/Desktop/MovieRecommendationSystem/data/preprocessed_movies.csv')
    df = convert_numeric_columns(df)
    selected_movies = df[df['star'] == selected_star]
  
    rating_map = {1: 'R', 2: 'PG', 3: 'PG-13', 4: 'NC-17', 5: 'G', 6: 'Not Rated', 7: 'Unrated', 8: 'Other'}
    selected_movies['rating'] = selected_movies['rating'].map(rating_map)
    
   
    genre_map = {0: 'Action', 1: 'Adventure', 2: 'Animation', 3: 'Biography', 4: 'Comedy', 5: 'Crime', 6: 'Drama', 7: 'Family', 8: 'Fantasy', 9: 'History', 10: 'Horror', 11: 'Music', 12: 'Musical', 13: 'Mystery', 14: 'Romance', 15: 'Sci-Fi', 16: 'Sport', 17: 'Thriller', 18: 'War', 19: 'Western'}
    selected_movies['genre'] = selected_movies['genre'].map(genre_map)
    
    selected_movies['rating'].fillna('Unknown', inplace=True)
    selected_movies['country'].fillna('Unknown', inplace=True)
    
    return render_template('details.html', movies=selected_movies.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
