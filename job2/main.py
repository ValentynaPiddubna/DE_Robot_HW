from flask import Flask, request, jsonify
from bll.sales_avro import process_data
# from dal.local_disk import get_directories

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    input_data = request.json
    raw_dir = input_data.get('raw_dir')
    stg_dir = input_data.get('stg_dir')

    if not raw_dir or not stg_dir:
        return jsonify({"error": "raw_dir and stg_dir are required."}), 400

    result, status_code = process_data(raw_dir, stg_dir)

    return jsonify({"result": result}), status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)
