import importlib

from src import app

if __name__ == '__main__':
    importlib.import_module('.routes', 'src')

    app.run('localhost', port=3001, debug=True)
