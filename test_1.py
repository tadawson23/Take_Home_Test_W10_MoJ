"""Cleans log file and returns dict"""

import re

VALID_ERRORS = ['WARNING', 'INFO', 'TRACE']
ERR_POSITION = 2
MSG_POSITION = 3


def is_log_line(line: str) -> bool:
    """Takes a log line and returns True if it is a valid log line 
    and returns nothing if it is not.
    """

    columns = line.split()
    valid_timestamp = r'\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}'
    match = bool(re.search(valid_timestamp, line))

    if len(columns) > 3:
        if match and columns[ERR_POSITION] in VALID_ERRORS and ':' in columns[MSG_POSITION]:
            return True


def get_dict(line: str) -> dict:
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    columns = line.split()

    timestamp = " ".join(columns[:ERR_POSITION])

    error_type = columns[ERR_POSITION]

    message = " ".join(columns[MSG_POSITION:])

    return {'timestamp': timestamp, 'log_level': error_type, 'message': message}


if __name__ == "__main__":

    def log_parser_step_1(log_file):
        """Log parser 1"""
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        """Log parser 2"""
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    def test_step_1():
        """Test 1"""
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        """Test 2"""
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
