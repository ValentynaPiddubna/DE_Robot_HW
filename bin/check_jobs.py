import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

RAW_DIR = os.getenv("RAW_DIR")
STG_DIR = os.getenv("STG_DIR")
JOB1_PORT = 8081
JOB2_PORT = 8082


def run_job1():
    print("Starting job1:")
    resp = requests.post(
        url=f'http://localhost:{JOB1_PORT}/',
        json={
            "start_date": "2022-08-09",
            "raw_dir": RAW_DIR
        }
    )
    print("Response status code:", resp.status_code)
    print("Response content:", resp.content)
    assert resp.status_code == 201
    print("job1 completed!")


def run_job2():
    print("Starting job2:")
    resp = requests.post(
        url=f'http://localhost:{JOB2_PORT}/',
        json={
            "raw_dir": RAW_DIR,
            "stg_dir": STG_DIR
        }
    )
    assert resp.status_code == 201
    print("job2 completed!")


if __name__ == '__main__':
    run_job1()
    time.sleep(3)
    run_job2()