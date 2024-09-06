from flask import Flask, render_template, send_from_directory
import os
import csv 

app = Flask(__name__)

# Path to the folder containing CSV reports
REPORTS_FOLDER = 'analyze_data/csv_reports'

@app.route('/')
def index():
    # List all CSV files in the folder
    csv_files = [f for f in os.listdir(REPORTS_FOLDER) if f.endswith('.csv')]
    
    # Read data from each CSV file
    file_data = {}
    for file in csv_files:
        with open(os.path.join(REPORTS_FOLDER, file), 'r') as f:
            reader = csv.reader(f)
            headers = next(reader, None)  # Get headers
            rows = [row for row in reader]
            file_data[file] = {'headers': headers, 'rows': rows}
    
    return render_template('index.html', file_data=file_data)

@app.route('/csv/<filename>')
def get_csv(filename):
    return send_from_directory(REPORTS_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
