from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Serve the front-end files
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'Index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)

# API endpoint to handle feedback form submission
@app.route('/api/feedback', methods=['POST'])
def handle_feedback():
    data = request.json
    # Handle the feedback data (e.g., send an email, save to a database, etc.)
    print('Feedback received:', data)
    return jsonify({'status': 'success', 'message': 'Feedback received'})

# API endpoint to handle job search
@app.route('/api/search', methods=['GET'])
def search_jobs():
    title = request.args.get('title', '').lower()
    location = request.args.get('location', '').lower()
    salary = request.args.get('salary', '').lower()
    company = request.args.get('company', '').lower()

    conn = sqlite3.connect('prod_database.db')
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    if title:
        query += " AND LOWER(title) LIKE ?"
        params.append(f'%{title}%')
    if location:
        query += " AND LOWER(location) LIKE ?"
        params.append(f'%{location}%')
    if salary:
        query += " AND LOWER(salary) LIKE ?"
        params.append(f'%{salary}%')
    if company:
        query += " AND LOWER(company) LIKE ?"
        params.append(f'%{company}%')

    cursor.execute(query, params)
    jobs = cursor.fetchall()
    conn.close()

    jobs_list = []
    for job in jobs:
        jobs_list.append({
            'id': job[0],
            'title': job[1],
            'company': job[2],
            'location': job[3],
            'salary': job[4],
            'created_date': job[5],
            'closing_date': job[6]
        })

    return jsonify(jobs_list)

if __name__ == '__main__':
    app.run(debug=True)