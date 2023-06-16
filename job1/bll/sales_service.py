from datetime import datetime, timedelta
from Lesson_02.job1.dal import local_disk, sales_api


def save_sales_to_local_disk(start_date: str, raw_dir: str) -> str:
    local_disk.clear_directory(raw_dir)

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.now().date()
    delta = timedelta(days=1)

    while start_date.date() <= end_date:
        date_str = start_date.strftime('%Y-%m-%d')
        page = 1
        file_index = 1

        while True:
            sales_data = sales_api.get_sales_data(date_str, page)

            if not sales_data:
                break

            local_disk.save_data_to_file(sales_data, date_str, raw_dir, file_index)
            file_index += 1
            page += 1

        start_date += delta

    return 'Data extraction completed'




