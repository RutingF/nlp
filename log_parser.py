import re 
import os

def parse_log_to_dict(logdata):

    # Regex pattern to match the log format
    pattern = re.compile(
        r'(?P<host>\S+) - (?P<user_name>\S+) \[(?P<time>[^\]]+)\] "(?P<request>[^"]+)" \d+ \d+'
    )

    # Empty list to store log entries
    log_entries = [] 

    for line in logdata.strip().split('\n'):
        match = pattern.match(line)
        if match:
            entry = match.groupdict()
            log_entries.append(entry)

    return log_entries


with open(f"{os.path.dirname(os.path.abspath(__file__))}/data/logdata.txt", "r") as file:
    logdata = file.read()

log_entries = parse_log_to_dict(logdata)
print(log_entries[:5])