import unittest
import os
from dotenv import load_dotenv
from Lesson_02.job2.bll.sales_avro import process_data


load_dotenv()


class ProcessDataTestCase(unittest.TestCase):
    def test_process_data(self):
        raw_dir = os.getenv('raw_dir')
        stg_dir = os.getenv('stg_dir')

        result, status_code = process_data(raw_dir, stg_dir)

        self.assertEqual(result, "Data processing completed successfully.")
        self.assertEqual(status_code, 200)


if __name__ == '__main__':
    unittest.main()
