# import multiprocessing
# import datetime
# import os
# import subprocess
#
# def run_test(test_file):
#     timestamp = datetime.datetime.now().strftime('%m-%d-%Y___%I-%M-%S-%p')
#     report_folder = "Reports"
#     if not os.path.exists(report_folder):
#         os.makedirs(report_folder)
#     report_file = os.path.join(report_folder, f"report_{timestamp}.html")
#     subprocess.run(
#         ["locust", "-f", test_file, "--headless", "-u", "2", "-r", "1", "-t", "15", "--html", report_file])
#
# if __name__ == '__main__':
#     test_files = ["testCases/firstTest.py", "testCases/reqres.py"]
#     with multiprocessing.Pool(processes=len(test_files)) as pool:
#         pool.map(run_test, test_files)


import multiprocessing
import datetime
import os
import subprocess
import webbrowser

def run_test(test_file):
    timestamp = datetime.datetime.now().strftime('%m-%d-%Y___%I-%M-%S-%p')
    report_folder = "Reports"
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    report_file = os.path.join(report_folder, f"report_{timestamp}.html")
    print(f"Starting test file: {test_file}")
    subprocess.run(
        ["locust", "-f", test_file, "--headless", "-u", "10", "-r", "1", "-t", "10s", "--html", report_file])
    print(f"Finished test file: {test_file}")

    report_files = [os.path.join(report_folder, f) for f in os.listdir(report_folder) if f.endswith('.html')]
    latest_report = max(report_files, key=os.path.getctime)

    # Open the latest report in the default web browser
    webbrowser.open_new_tab(latest_report)

if __name__ == '__main__':
    test_files = ["testCases/"]
    with multiprocessing.Pool(processes=len(test_files)) as pool:
        pool.map(run_test, test_files)