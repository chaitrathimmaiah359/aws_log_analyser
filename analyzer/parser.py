import re

def extract_errors(log_text):

    errors = []

    patterns = [
        r'ERROR.*',
        r'Exception.*',
        r'Timeout.*',
        r'Failed.*'
    ]

    for line in log_text.splitlines():

        for pattern in patterns:

            if re.search(pattern, line, re.IGNORECASE):
                errors.append(line)

    return errors