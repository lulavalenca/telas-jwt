from src.telas_login import server

if __name__ == '__main__':
    server.run(debug=True, port=8080, ssl_context='adhoc')