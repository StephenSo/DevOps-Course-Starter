from flask import Flask, render_template, session, request

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

def add_item(title):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    items = get_items()

    # Determine the ID for the item based on that of the previously added item
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': 'Not Started' }

    # Add the item to the list
    items.append(item)
    session['items'] = items

    return item

@app.route('/',methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        result = request.form.get('newItem')
        add_item(title=result)
        return render_template('index.html', items=get_items())
        
    if request.method == 'GET':
        return render_template('index.html', items=get_items())

if __name__ == '__main__':
    app.run()
