import sys
from PyQt4 import QtCore, QtGui
from windowUI import Ui_MainWindow

from save_msgs.msg import tsr
from std_msgs.msg import Int32
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

TOPIC_NAME = ["Mission_number","Vision_light", "lidar1/scan", "lidar2/scan","lidar3/scan","lidar4/scan"]
TOPIC_TYPE = [Int32, tsr, LaserScan, LaserScan,LaserScan ,LaserScan]
TOPIC_DATA = [Int32(), tsr(), LaserScan(), LaserScan(), LaserScan(), LaserScan()]


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    ui = Ui_MainWindow(TOPIC_NAME, TOPIC_TYPE, TOPIC_DATA)
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())