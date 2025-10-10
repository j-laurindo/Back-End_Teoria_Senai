# # CRIAÇÃO DO SERVIDOR COM O SIMPLE REQUEST HANDLER ##

# # Importação do HTTP Server
# from http.server import SimpleHTTPRequestHandler, HTTPServer

# # Definindo a porta do servidor
# port = 8000

# # Definindo o gerenciador/manipulador de requisições
# handler = SimpleHTTPRequestHandler

# # Criação da instância do servidor
# server = HTTPServer(("localhost", port), handler)

# # Impressão da mensagem
# print(f"Server Initiated in http://localhost:{port}")

# server.serve_forever()

####################################################################

## CRIAÇÃO DO SERVIDOR COM AS TRATATIVAS DE MÉTODOS ##

import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "senai"
)

# Definição e configuração do Handler 
class MyHandler(SimpleHTTPRequestHandler):

    # Método da listagem e exibição do index.html como default
    def list_directory(self, path):
        try:
            f = open(os.path.join(path, 'index.html'), encoding='utf-8')
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode('UTF-8'))

            f.close()
            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)
    
    def load_filme(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Site_Filmes.Filmes")
        movie_result = cursor.fetchall()

        for mov in movie_result:
            id_filme = res[0]
            titulo = res[1]
            orcamento = res[2]
            duracao = res[3]
            ano = res[4]
            poster = res[5]
            print(id_filme, titulo, orcamento, duracao, ano, poster)

        
        
        
        

    # Método para verificar o email e a senha
    def account_user(self, login, password):
        login_correto = "juliaroberts@gmail.com"
        senha = 123

        if(login == login_correto and senha == password):
            return "Usuário logado"
        else:
            return "Usuário não existe"
    
    # Método GET para enviar as páginas do projeto
    def do_GET(self):

        # Definição do caminho de login
        if(self.path == "/login"):
            self.load_filme()
            try:
                with open(os.path.join(os.getcwd(), "login.html"), encoding='utf-8') as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('UTF-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                pass

        # Definição do caminho de cadastro de filmes
        elif(self.path =="/cadastro"):
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), encoding='utf-8') as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('UTF-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                pass

        # Definição do caminho da lista de filmes
        elif(self.path == "/listarFilmes"):
            try:
                with open(os.path.join(os.getcwd(), "listarFilmes.html"), encoding='utf-8') as listaFilmes:
                    content = listaFilmes.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content.encode('UTF-8'))
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                pass

        # Resposta da lista 
        elif (self.path == "/get_lista"):

            arquivo = "data.json"

            if os.path.exists(arquivo):
                with open(arquivo, encoding="utf-8") as listagem:
                    try:
                        filmes = json.load(listagem)
                    except json.JSONDecodeError:
                        filmes = []
            else:
                filmes = []

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filmes).encode("utf-8"))

        else:
            super().do_GET()
    
    def do_POST(self):
        #  Tratativa de dados para o envio/autenticação do login
        if self.path == '/send_login':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('UTF-8')
            form_data = parse_qs(body)

            print("Data form: ")
            print("Username: ",form_data.get('nomeUsuario', [""])[0])
            print("Password: ",form_data.get('senha', [""])[0])

            login = form_data.get('nomeUsuario', [""])[0]
            password = int(form_data.get('senha', [""])[0])

            entrada = self.account_user(login, password)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(entrada.encode('UTF-8'))
        
        # Tratativa de dados para o envio do cadastro de filmes
        elif self.path == '/send_register':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            id_novo = 1

            if os.path.exists(arquivo):
                with open(arquivo, "r", encoding="utf-8") as lista:
                    try:
                        filmes = json.load(lista)
                        if filmes:
                            id_novo = max(f["id"] for f in filmes) + 1
                    except json.JSONDecodeError:
                        filmes = []
            else:
                filmes = []

            jsum = {
                "id": id_novo,
                "nome": form_data.get('nomeFilme', [""])[0],
                "atores":form_data.get('atores', [""])[0],
                "diretor": form_data.get('diretor', [""])[0],
                "ano": str(form_data.get('anoFilme', ["0"])[0]),
                "generos": form_data.get('genero', [""])[0],
                "sinopse": form_data.get('sinopse', [""])[0],
                "produtora": form_data.get('produtora', [""])[0]
            }

            arquivo = "data.json"
            if os.path.exists(arquivo):
                with open(arquivo,  "r", encoding="utf-8") as lista:
                    try:
                        filmes = json.load(lista)
                    except json.JSONDecodeError:
                        filmes = []
                filmes.append(jsum)
            else:
                filmes = [jsum]

            with open(arquivo, "w", encoding="utf-8") as lista:
                json.dump(filmes, lista, indent=4, ensure_ascii=False)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(str(jsum).encode('utf-8'))

        else:
            super(MyHandler, self).do_POST()
    
    # Fazer método DELETE com remove
    def do_DELETE(self):
        if self.path.startswith("/send_delete/"):
            id_filme = self.path.split("/")[-1]
            arquivo = "data.json"

            if os.path.exists(arquivo):
                with open(arquivo, "r", encoding="utf-8") as f:
                    try:
                        filmes = json.load(f)
                    except json.JSONDecodeError:
                        filmes = []

                # Remove o filme com id correspondente
                filmes = [filme for filme in filmes if str(filme.get("id")) != id_filme]

                with open(arquivo, "w", encoding="utf-8") as f:
                    json.dump(filmes, f, indent=4, ensure_ascii=False)

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(b'{"mensagem": "Filme deletado com sucesso"}')
            else:
                self.send_error(404, "Arquivo de filmes não encontrado.")
        else:
            self.send_error(404, "Rota não encontrada.")
    
    def do_PUT(self):
        if self.path.startswith("/send_edit/"):
            id_filme = self.path.split("/")[-1]
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')
            novo_dado = json.loads(body)

            arquivo = "data.json"
            if os.path.exists(arquivo):
                with open(arquivo, "r", encoding="utf-8") as f:
                    try:
                        filmes = json.load(f)
                    except json.JSONDecodeError:
                        filmes = []

                for filme in filmes:
                    if str(filme.get("id")) == id_filme:
                        filme.update(novo_dado)  # Atualiza os campos passados
                        break

                with open(arquivo, "w", encoding="utf-8") as f:
                    json.dump(filmes, f, indent=4, ensure_ascii=False)

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(b'{"mensagem": "Filme atualizado com sucesso"}')
            else:
                self.send_error(404, "Arquivo de filmes não encontrado.")
        else:
            self.send_error(404, "Rota não encontrada.")




# Função Main para iniciar o servidor
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server Initiated in http://localhost:8000")
    httpd.serve_forever()

# Chamada da Função Main
main()

