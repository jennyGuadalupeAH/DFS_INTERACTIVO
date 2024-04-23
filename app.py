from flask import Flask, render_template, jsonify
import dfs_interactivo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dfs-interactivo', methods=['GET'])
def dfs():
    resultado_dfs_interactivo= dfs_interactivo.imprimir()
    return jsonify({"resultado": resultado_dfs_interactivo})

if __name__ == '__main__':
    app.run(debug=True)
