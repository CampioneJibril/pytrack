import sqlite3
import datetime as dt

from typing import Protocol

# all the code needs for entering data is in this block
class WindowEntryIn:
    """Takes Window Title, Time Started, Time Finished \n
    class for window entry that wil handle the data structure and entry of the data to the database
    """

    def __init__(self, window_title, time_started, time_finished):
        self.window_title = window_title
        self.time_started = time_started
        self.time_finished = time_finished
        self.time_elapsed = self.convert_time_format()

    def record_in_database(self):
        """enter the data to data base"""
        conn = sqlite3.connect("pyTrack.db")

        c = conn.cursor()

        c.execute(
            """
                    INSERT INTO windowTimeEntries VALUES(?,?,?)

        """,
            (self.window_title, self.time_elapsed, str(dt.date.today())),
        )

        conn.commit()

        conn.close()

        print("successfully added to database")

    def convert_time_format(self):
        """subtracts the time started and time finished to get time elapsed"""
        hours = self.time_finished[0] - self.time_started[0]
        minutes = self.time_finished[1] - self.time_started[1]
        seconds = self.time_finished[2] - self.time_started[2]
        time_elapsed = f"{hours}, {minutes}, {seconds}"
        return time_elapsed


# all the code need for querying processing and showing the data in this block


class WindowRecord:
    """class to handle and store data that is retrieved from the database"""

    def __init__(self, entry):
        window_name: str = entry[0]
        time_elapsed: str = entry[1]
        date_entered: str = entry[2]

        split_window_name = window_name.split("- ")

        self.window_short_name: str = split_window_name[-1]
        self.window_full_name: str = window_name
        self.window_time_elapsed = WindowTime(time_elapsed)
        self.window_date_entered = date_entered


class WindowTime:
    """class window time for keeping data(time)"""

    name: str
    full_name: str

    def __init__(self, time_elapsed: str) -> None:
        split_time_elapsed = time_elapsed.split(", ")

        self.hours: float = float(split_time_elapsed[0])
        self.minutes: float = float(split_time_elapsed[1])
        self.seconds: float = float(split_time_elapsed[2])

        self.format_time()

    def get_time(self) -> tuple:
        """returns tuple of time"""
        self.format_time()
        time = (self.hours, self.minutes, self.seconds)
        return time

    def add_time(self, hours=0, minutes=0, seconds=0):
        """adds time"""
        self.hours += hours
        self.minutes += minutes
        self.seconds += seconds

        self.format_time()

    def format_time(self):
        """formats the time to avoid the negatives and time going above 60 \n use this when changing the time value"""
        if self.minutes > 60:
            self.minutes -= 60
            self.hours += 1
        if self.seconds > 60:
            self.seconds -= 60
            self.minutes += 1
        if self.seconds < 0:
            self.seconds += 60
        if self.minutes < 0:
            self.minutes += 60


# all in one class for window record needs
class WindowRecordUtils:
    """all in one class for window record needs"""

    formatted_records = []

    def __init__(self) -> None:
        self.fetch_entries()

    def fetch_entries(self):
        """combination of format_raw_entries and retrieve_raw_entries as one function"""
        self.formatted_records = self.format_raw_entries(self.retrieve_raw_entries())

    def format_raw_entries(self, raw_records: list) -> list[WindowRecord]:
        """format raw entry list\n output: list of Class WindowRecord"""
        formatted_records = []
        for entry in raw_records:
            record = WindowRecord(entry)
            formatted_records.append(record)
        return formatted_records

    def retrieve_raw_entries(self, q=None) -> list:
        """connects to the database and gets all entries as raw list of string"""
        conn = sqlite3.connect("pyTrack.db")
        c = conn.cursor()
        c.execute("SELECT * FROM windowTimeEntries")
        raw_records = c.fetchall()
        conn.commit()
        conn.close
        return raw_records

    def get_total_time_elapsed(self) -> WindowTime:
        """get total time elapsed\n Returns window time"""
        time = WindowTime(f"0, 0, 0")

        # cycle through the formatted entries and format the time
        for entry in self.formatted_records:
            time.hours += entry.window_time_elapsed.hours
            time.minutes += entry.window_time_elapsed.minutes
            time.seconds += entry.window_time_elapsed.seconds

            time.format_time()

        # format and return time
        return time

    def get_time_of_each_window(self):
        """get time elapsed on each window"""
        unique_windows: list[WindowTime] = []

        # loop through the entries
        for entry in self.formatted_records:

            # loop through the unique window list find if there is a match or not
            is_unique: bool = True
            for window in unique_windows:
                # if unique add time elapsed to the object that it matched
                if window.name == entry.window_short_name:
                    is_unique = False
                    time_to_add = entry.window_time_elapsed.get_time()
                    window.add_time(time_to_add[0], time_to_add[1], time_to_add[2])
                else:
                    pass

            # if unique then add a new item in the list
            if is_unique:
                unique_window = entry.window_time_elapsed
                unique_window.full_name = entry.window_full_name
                unique_window.name = entry.window_short_name
                unique_windows.append(unique_window)

        return unique_windows

    def get_percentage_of_time_of_each_window(self):
        total_time = self.get_total_time_elapsed()
        time_of_each_window = self.get_time_of_each_window()

        percentages: list[list] = []

        for window in time_of_each_window:
            percentage = window.seconds / total_time.seconds
            percentage = percentage + window.minutes
            percentage = percentage / total_time.minutes
            percentage = percentage + window.hours
            percentage = percentage / total_time.hours
            percentage = percentage * 100

            percentages.append([window, round(percentage, 2)])

        return percentages


if __name__ == "__main__":
    window_util = WindowRecordUtils()

    total_time_elapsed = window_util.get_total_time_elapsed()
    print(total_time_elapsed.get_time())
    print()

    total_time_of_each_window = window_util.get_time_of_each_window()

    percentage_time_of_each_window = window_util.get_percentage_of_time_of_each_window()

    for window in percentage_time_of_each_window:
        print(f"name: {window[0].full_name}")
        print(f"percentage: {window[1]}")
