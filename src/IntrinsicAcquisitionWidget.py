import sys
import os
dirs = ['views','styles', 'controllers', 'models']
for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)

from Styles import *
from ViewManualAcquisition import *
from ViewAutomaticAcquisition import *
from PySide2 import *
import cv2

class IntrinsicAcquisitionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(IntrinsicAcquisitionWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        self.viewAutoAcquisition = ViewAutomaticAcquisition(self.window)
        self.viewManualAcquisition = ViewManualAcquisition(self.window)
        Styles(self)

    def initUI(self):
        self.setWindowTitle("Data Acquisition")
        self.setGeometry(300, 100, 550, 510)
        self.manualAcquisition()
        self.window.comboBoxManual.currentIndexChanged.connect(
            self.manualAcquisition)
        self.automaticAcquisition()
        self.window.comboBoxAuto.currentIndexChanged.connect(
            self.automaticAcquisition)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/dataAcquisition.ui')
        file = QtCore.QFile(formUI)
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

    def manualAcquisition(self):
        chosenCamera = self.window.comboBoxManual.currentText()
        if chosenCamera == "RGB":
            self.viewManualAcquisition.connectButtonsRgbCamera()
        if chosenCamera == "DEPTH":
            self.viewManualAcquisition.connectButtonsDepthCamera()
        if chosenCamera == "THERMAL":
            self.viewManualAcquisition.connectButtonsThermalCamera()
        if chosenCamera == "NONE":
            pass

    def automaticAcquisition(self):
        chosenCamera = self.window.comboBoxAuto.currentText()
        if chosenCamera=="RGB":
            self.viewAutoAcquisition.connectButtonsRgbCamera()
        if chosenCamera=="DEPTH":
            self.viewAutoAcquisition.connectButtonsDepthCamera()
        if chosenCamera=="THERMAL":
            self.viewAutoAcquisition.connectButtonsThermalCamera()
        if chosenCamera=="NONE":
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionIntrinsicCalibration = IntrinsicAcquisitionWidget()
    acquisitionIntrinsicCalibration.show()
    app.exec_()
