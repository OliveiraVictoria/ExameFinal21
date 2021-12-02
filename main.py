from env import Flask # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def main():
  return 'index.html'

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação
