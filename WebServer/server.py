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
from http.server import SimpleHTTPRequestHandler, HTTPServer

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
    
    # Método GET para enviar as páginas do projeto
    def do_GET(self):

        # Definição do caminho de login
        if(self.path == "/login"):
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
        else:
            super().do_GET()


# Função Main para iniciar o servidor
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Server Initiated in http://localhost:8000")
    httpd.serve_forever()

# Chamada da Função Main
main()

