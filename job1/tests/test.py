import unittest
from unittest.mock import patch, MagicMock

from Lesson_02.job1.bll import sales_service


import os
from dotenv import load_dotenv

load_dotenv()


class SalesServiceTestCase(unittest.TestCase):
    def test_save_sales_to_local_disk(self):
        start_date = "2022-08-09"
        raw_dir = os.getenv('RAW_DIR')

        with patch('sales_service.local_disk.clear_directory', new=MagicMock()) as mock_clear_directory:
            with patch('sales_service.sales_api.get_sales_data') as mock_get_sales_data:
                mock_sales_data = {"sales": []}
                mock_get_sales_data.return_value = mock_sales_data

                with patch('sales_service.local_disk.save_data_to_file', new=MagicMock()) as mock_save_data_to_file:
                    result = sales_service.save_sales_to_local_disk(start_date, raw_dir)

                    mock_clear_directory.assert_called_once_with(raw_dir)

                    expected_calls = [
                        ((start_date, 1),),
                        ((start_date, 2),),
                        ((start_date, 3),),
                        # ... and so on
                    ]
                    self.assertEqual(mock_get_sales_data.call_args_list, expected_calls)

                    expected_save_calls = [
                        (mock_sales_data, start_date, raw_dir, 1),
                        (mock_sales_data, start_date, raw_dir, 2),
                        (mock_sales_data, start_date, raw_dir, 3),
                        # ... and so on
                    ]
                    self.assertEqual(mock_save_data_to_file.call_args_list, expected_save_calls)

                    self.assertEqual(result, 'Data extraction completed')


if __name__ == '__main__':
    unittest.main()
