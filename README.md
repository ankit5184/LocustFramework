# Locust-Framework

1. Running all test cases     locust -f testCases/  --host=https://reqres.in
2. single test         locust -f testCases/demo.py  --host=https://reqres.in
3. Csv and Report     locust -f testCases/ --headless --print-stats --csv Run.csv --csv-full-history -L CRITICAL --html my_report.html -u 100 -t 25s
4. --logfile Logging.log
5. locust -f testCases/ --host=https://reqres.in --class-picker