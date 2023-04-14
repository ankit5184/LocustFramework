import subprocess
import datetime
import os
import webbrowser

if __name__ == '__main__':
    test_files = ["testCases/"]
    processes = []
    timestamp = datetime.datetime.now().strftime('%m-%d-%Y___%I-%M-%S-%p')
    report_folder = "Reports"
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)
    for test_file in test_files:
        report_file = os.path.join(report_folder, f"report_{timestamp}.html")
        processes.append(subprocess.Popen(
            ["locust", "-f", test_file, "--headless", "-u", "10", "-r", "1", "-t", "10s", "--html", report_file,
             "--logfile", "locust.log"]))

    for process in processes:
        process.wait()

    report_files = [os.path.join(report_folder, f) for f in os.listdir(report_folder) if f.endswith('.html')]
    latest_report = max(report_files, key=os.path.getctime)

    # Open the latest report in the default web browser
    webbrowser.open_new_tab(latest_report)
