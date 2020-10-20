from PySide2 import QtWidgets
from EventsAutoAcquisition import EventsAutoAcquisition

class ControllerAutoAcquisitionTab():
    """ 
    Controller for automatic intrinsic acquisition 
    """
    
    def __init__(self, window):
        super(ControllerAutoAcquisitionTab).__init__()
        self.window = window
        self.event = EventsAutoAcquisition(self.window)

    def configAdqcquisition(self):
        NoImages = int(self.window.NoImages.text())
        patternDimension = (int(self.window.cornerX.text()), int(self.window.cornerY.text()))
        self.pathImages = self.saveDialog()
        if self.pathImages != '':
            self.event.setConfigAutoAcq(NoImages, patternDimension, self.pathImages)

    def handlerStartRgbImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.event.turnOnCamera('RGB')
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStartDepthImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.event.turnOnCamera('DEPTH')
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStartThermalImageAcq(self):
        self.configAdqcquisition()
        if self.pathImages != '':
            rgbImage = self.event.turnOnCamera('DEPTH')
            self.window.displayAuto.addWidget(rgbImage)

    def handlerStopAcquisition(self):
        self.event.turnOffCamera()

    def saveDialog(self):
        pathImages, info = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        return pathImages
