# Innovaccer Off-Campus

Problem Statement for SDE (Platform) Summer Intern 2019 at Innovaccer.

# Project Details

Run SMTP server to send reminder emails to localhost:
```
python -m smtpd -n -c DebuggingServer localhost:1025
```

Install project requirements:
```
pip install -r requirements.txt
```

Run the main program:
```
python3 main.py
```

**NOTE**: *Make sure the main program `main.py` and SMTP server should be running at the same time. If SMTP server not started then, it'll throw `ConnectionError` and hence program will fail to run.

Status: Working successfully as per problem statement.

If user input has to be stored in MySQL database, run MySQL server:
```
python3 sqlconnect.py
```



