# create main file that launches the login page
from log_in_window import LogInWindow
import database_func as db


if __name__ == "__main__":
    import sys
    db.create_database()
    LogInWindow()
    sys.exit(0)