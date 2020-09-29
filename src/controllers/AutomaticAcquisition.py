from PySide2 import  *
from ControllerAutoAcquisition import *

class AutomaticAcquisition():
    def __init__(self, window):
        super(AutomaticAcquisition).__init__()
        self.window = window
        self.controller = ControllerAutoAcquisition(self.window)

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        patternDimension = (int(self.window.cornerX.text()), int(self.window.cornerY.text()))
        self.pathImages = self.saveDialog()
        if self.pathImages != '':
            self.controller.setConfigAutoAcq(NoImages, patternDimension, self.pathImages)

    def handlerStartRgbImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.controller.turnOnCamera(0)
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStartDepthImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.controller.turnOnCamera(1)
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStartThermalImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.controller.turnOnCamera(2)
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStopAcquisition(self):
        self.controller.turnOffCamera()

    def saveDialog(self):
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        return pathImages
