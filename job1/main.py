import os
from flask import Flask, request
from flask import typing as flask_typing
from dotenv import load_dotenv
from datetime import datetime

from bll.sales_service import save_sales_to_local_disk


load_dotenv()

AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")

# raw_dir = os.getenv('RAW_DIR')

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    triggers the business logic layer

    Proposed POST body in JSON:
    {
      "start_date": "2022-08-09",
      "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
    }
    """

    input_data: dict = request.json
    start_date = input_data.get('start_date')
    raw_dir = input_data.get('raw_dir')

    if not start_date:
        return {
            "message": "start_date or end_date parameter is missing",
        }, 400

    save_sales_to_local_disk(start_date=start_date, raw_dir=raw_dir)

    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)
