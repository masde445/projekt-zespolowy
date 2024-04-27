# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from wycena_dxf import analyze_dxf

app = Flask(__name__)
CORS(app)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
 
    material = request.form['material']
    thickness = request.form['thickness']
    require_material = bool(request.form['requireMaterial'])
    file = request.files['file']

    # Zapisanie przeslanego pliku DXF
    file_path = 'temp.dxf'
    file.save(file_path)

    # Wywolanie funkcji z Twojej aplikacji do analizy pliku DXF
    total_perimeter, total_area = analyze_dxf(file_path)

    # Usuniecie tymczasowego pliku DXF
    os.remove(file_path)

    # Zwrocenie wynikow jako odpowied� JSON
    return jsonify({
        'total_perimeter': round(total_perimeter, 1),
        'total_area': round(total_area, 1)
        'total_cost': total_cost
    })

if __name__ == '__main__':
    app.run(debug=True)
