import sys
sys.path.append('../src/views')
from DataAcquisitionWidget import *
from PySide2 import *
import cv2

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionIntrinsicCalibration = DataAcquisitionWidget()
    acquisitionIntrinsicCalibration.show()
    app.exec_()
