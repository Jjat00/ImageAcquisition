from PySide2 import  *
import sys
sys.path.append('../src/controllers')
from ControllerAutoAcquisition import *

class AutomaticAcquisition():
    def __init__(self, window):
        super(AutomaticAcquisition).__init__()
        self.window = window
        self.controller = ControllerAutoAcquisition()

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        patternDimension = (int(self.window.cornerX.text()), int(self.window.cornerY.text()))
        pathImages = self.saveDialog()
        self.controller.setConfigAutoAcq(NoImages, patternDimension, pathImages)

    def handlerStartRgbImageAcq(self):
        self.configAdqcquisition()
        rgbImage = self.controller.turnOnCamera(0)
        self.window.displayAuto.addWidget(rgbImage)

    def handlerStartDepthImageAcq(self):
        self.configAdqcquisition()
        rgbImage = self.controller.turnOnCamera(1)
        self.window.displayAuto.addWidget(rgbImage)

    def handlerStartThermalImageAcq(self):
        self.configAdqcquisition()
        rgbImage = self.controller.turnOnCamera(2)
        self.window.displayAuto.addWidget(rgbImage)

    def handlerStopAcquisition(self):
        self.controller.turnOffCamera()

    def saveDialog(self):
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        return pathImages

