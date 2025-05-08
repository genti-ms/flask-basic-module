from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def lade_posts():
    with open('posts.json', 'r') as file:
        return json.load(file)

def speichere_posts(posts):
    with open('posts.json', 'w') as file:
        json.dump(posts, file, indent=4)

@app.route('/')
def index():
    posts = lade_posts()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = lade_posts()

        # Neues Post-Daten aus dem Formular holen
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Eine neue eindeutige ID erstellen
        new_id = max([post['id'] for post in posts], default=0) + 1

        # Neues Post-Dict erstellen
        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }

        # Neues Post zur Liste hinzufügen
        posts.append(new_post)

        # Liste in JSON-Datei speichern
        speichere_posts(posts)

        # Zur Startseite umleiten
        return redirect(url_for('index'))

    return render_template('add.html')
