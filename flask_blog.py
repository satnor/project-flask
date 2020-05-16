from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Haakon Skaare',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'May 15, 2020'
    },
    {
        'author': 'Mordi',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'May 16, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


## DEBUG
if __name__ == '__main__':
    app.run(debug=True)
