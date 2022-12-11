import sqlite3


def check_app_type(title: str) -> str:
    '''Takes a window checks and returns string "bad" or "good"'''

    productive_apps = ["Visual Studio Code"]
    bad_apps = ["Opera"]
    app_type = ""

    separated_title: list[str] = title.split("- ")
    for app in productive_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is an productive app {str(separated_title)}")
            app_type = "good"
    for app in bad_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is a bad app {str(separated_title)}")
            app_type = "bad"

    return app_type


class WindowType:
    """Class window type use to store name type and rating of window"""

    window_name: str
    window_type: str
    window_rating: int

    def __init__(self, window_name: str, window_type: str, window_rating: int) -> None:
        self.window_name = window_name
        self.window_type = window_type
        self.window_rating = int(window_rating)

    def __str__(self) -> str:
        return f"name: {self.window_name}\ntype: {self.window_type}\nrating: {self.window_rating}"


class WindowTypeIn(WindowType):
    """inherits from class window type have functions to enter data in database"""

    def record_in_database(self):
        """enter the data to data base"""
        conn = sqlite3.connect("pyTrack.db")
        c = conn.cursor()
        c.execute(
            """INSERT INTO windowTypes(windowName, windowType, windowRating) VALUES(?,?,?)""",
            (self.window_name, self.window_type, self.window_rating),
        )
        conn.commit()
        conn.close()
        print("successfully added to database")


def find_window_on_database_by_name(query_name: str) -> WindowType:
    """find window on data base by name returns windowType object"""
    conn = sqlite3.connect("pyTrack.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM windowTypes WHERE windowName = ?""", (query_name,))
    results = c.fetchall()
    window = WindowType(results[0][1], results[0][2], results[0][3])
    conn.commit()
    conn.close()
    return window


class PointTracker:
    points: int

    def __init__(self) -> None:
        self.points = 0

    def add_points(self, point_to_add: int):
        self.points += point_to_add

    def subtract_points(self, point_to_add: int):
        self.points -= point_to_add


if __name__ == "__main__":
    # window_type = WindowTypeIn("Discord", "bad", 5)
    # window_type.record_in_database()

    results = find_window_on_database_by_name("Visual Studio Code")
    print(results)