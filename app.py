from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    selection = request.form.get('selection')
    conn = sqlite3.connect('MovieRental.db')
    cursor = conn.cursor()

    # Fetch the column names and data for the selected table
    query = f"SELECT * FROM {selection}"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Retrieve column names
    column_names = [description[0] for description in cursor.description]

    conn.close()

    return render_template('result.html', column_names=column_names, rows=rows, table_name=selection)

if __name__ == '__main__':
    app.run(debug=True)
