"""
import http.server
import socketserver
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
    
"""

from flask import Flask
import mysql.connector

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def galaxy():
    cnx = mysql.connector.connect(user="root",password="root",host="mysql",database="test")
    cursor = cnx.cursor()

    # Execute a query
    query = 'SHOW DATABASES'
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Iterate through the results and print them
#     for result in results:
#         print(result)

    # Close the cursor and connection
    cursor.close()
    cnx.close()
    return results

if __name__ == '__main__':
    #app.run(threaded=True, port=5000)
    app.run(host='0.0.0.0', port=5000)
