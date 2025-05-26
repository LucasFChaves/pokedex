from app import create_app
from app.models import criar_tabelas

app = create_app()

with app.app_context():
    criar_tabelas()

if __name__ == '__main__':
    app.run(debug=True)