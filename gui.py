from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread

from UI.main import icons_rc
from UI.main.ui_main import Ui_MainWindow

from PyTrackMain import PyTrackWorker


class PytrackMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pytrack")
        self.main_loop_active = False

        self.pytrack_worker = PyTrackWorker(self)
        self.pytrack_worker_thread = QThread()

        # setting text and placeholder texts
        self.button_activate_deactivate_main_loop.setText("Activate")
        self.line_edit_point_threshold_break.setPlaceholderText(
            str(self.pytrack_worker.point_tracker.POINT_THRESHOLD_TAKE_A_BREAK)
        )
        self.line_edit_point_threshold_warning.setPlaceholderText(
            str(self.pytrack_worker.point_tracker.POINT_THRESHOLD_GET_BACK_TO_WORK)
        )

        # setting the button signals to slots
        self.button_go_to_home.clicked.connect(self.go_to_home_page)  # type: ignore
        self.button_go_to_analytics.clicked.connect(self.go_to_analytics_page)  # type: ignore
        self.button_go_to_settings.clicked.connect(self.go_to_settings_page)  # type: ignore
        self.button_activate_deactivate_main_loop.clicked.connect(self.activate_deactivate_main_loop)  # type: ignore
        self.button_activate_deactivate_main_loop.clicked.connect(self.pytrack_worker.main_loop)  # type: ignore
        self.button_settings_general.clicked.connect(self.go_to_settings_general)  # type: ignore
        self.button_settings_window.clicked.connect(self.go_to_settings_window)  # type: ignore
        self.button_settings_about.clicked.connect(self.go_to_settings_about)  # type: ignore

        # setting the text edit signal to slots
        self.line_edit_point_threshold_break.editingFinished.connect(self.edit_point_threshold_break)  # type: ignore
        self.line_edit_point_threshold_warning.editingFinished.connect(self.edit_point_threshold_warning)  # type: ignore

        # move workers to their threads and start the threads
        self.pytrack_worker.moveToThread(self.pytrack_worker_thread)
        self.pytrack_worker_thread.start()

        # show the window
        self.show()

    def go_to_home_page(self):
        print("to home page")
        self.stackedWidget.setCurrentWidget(self.page_home)

    def go_to_analytics_page(self):
        print("to analytics page")
        self.stackedWidget.setCurrentWidget(self.page_analytics)

    def go_to_settings_page(self):
        print("go to settings page")
        self.stackedWidget.setCurrentWidget(self.page_settings)

    def go_to_settings_general(self):
        print("go to general settings")
        self.page_settings_stacked_widget.setCurrentWidget(
            self.page_settings_stacked_widget_page_general
        )

    def go_to_settings_window(self):
        print("go to window settings")
        self.page_settings_stacked_widget.setCurrentWidget(
            self.page_settings_stacked_widget_page_window
        )

    def go_to_settings_about(self):
        print("go to about settings")
        self.page_settings_stacked_widget.setCurrentWidget(
            self.page_settings_stacked_widget_page_about
        )

    def edit_point_threshold_break(self):
        """edit the point threshold of break"""
        # TODO: add the functionality to change the config file. dont forget to update the point tracker's values to the updated config file
        print(
            f"changing point threshold for break to {self.line_edit_point_threshold_break.text()}"
        )
        self.line_edit_point_threshold_break.clear()
        self.line_edit_point_threshold_break.setPlaceholderText(
            str(self.pytrack_worker.point_tracker.POINT_THRESHOLD_TAKE_A_BREAK)
        )

    def edit_point_threshold_warning(self):
        """edit the point threshold of warning"""
        # TODO: add the functionality to change the config file. dont forget to update the point tracker's values to the updated config file
        print(
            f"changing point threshold for warning to {self.line_edit_point_threshold_warning.text()}"
        )
        self.line_edit_point_threshold_break.clear()
        self.line_edit_point_threshold_warning.setPlaceholderText(
            str(self.pytrack_worker.point_tracker.POINT_THRESHOLD_GET_BACK_TO_WORK)
        )

    def activate_deactivate_main_loop(self):
        if not self.main_loop_active:
            print("Activated")
            self.main_loop_active = True
            self.button_activate_deactivate_main_loop.setText("Deactivate")
        elif self.main_loop_active:
            print("Deactivated")
            self.main_loop_active = False
            self.button_activate_deactivate_main_loop.setText("Activate")


if __name__ == "__main__":
    app = QApplication()
    window = PytrackMainWindow()
    app.exec()
