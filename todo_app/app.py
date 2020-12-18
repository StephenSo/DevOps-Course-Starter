from flask import Flask, render_template, session

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

_DEFAULT_ITEMS = [
    { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
    { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' }
]

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    return session.get('items', _DEFAULT_ITEMS)

@app.route('/')
def index():
    return render_template('index.html', items=get_items())

if __name__ == '__main__':
    app.run()
