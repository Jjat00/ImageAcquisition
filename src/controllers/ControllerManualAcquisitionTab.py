from PySide2 import QtWidgets
from EventsManualAcquisition import *

class ControllerManualAcquisitionTab():
    def __init__(self, window):
        super(ControllerManualAcquisitionTab).__init__()
        self.window = window
        self.event = EventsManualAcquisition()

    def handlerTurnOnRGBCamera(self):
        rgbImage = self.event.turnOnCamera('RGB')
        self.window.displayManual.addWidget(rgbImage)

    def handlerTurnOnDepthCamera(self):
        depthImage = self.event.turnOnCamera('DEPTH')
        self.window.displayManual.addWidget(depthImage)

    def handlerTurnOnThermalCamera(self):
        thermalImage = self.event.turnOnCamera('THERMAL')
        self.window.displayManual.addWidget(thermalImage)

    def handlerCaptureRGBImage(self):
        rgbImage = self.event.captureImage('RGB')
        self.window.displayManual.addWidget(rgbImage)

    def handlerCaptureDepthmage(self):
        depthImage = self.event.captureImage('DEPTH')
        self.window.displayManual.addWidget(depthImage)

    def handlerCaptureThermalImage(self):
        thermalImage = self.event.captureImage('THERMAL')
        self.window.displayManual.addWidget(thermalImage)
        
    def handlerSaveRgbImage(self):
        nameImage = self.saveDialog()
        self.event.saveImage('RGB', nameImage)

    def handlerSaveDepthImage(self):
        nameImage = self.saveDialog()
        self.event.saveImage('DEPTH', nameImage)

    def handlerSaveThermalImage(self):
        nameImage = self.saveDialog()
        self.event.saveImage('THERMAL', nameImage)

    def handlerTurnOffCamera(self):
        self.event.turnOffCamera()

    def handlerNone(self):
        print("NONE")

    def saveDialog(self):
        nameImage = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        nameImage = "%s.png" % nameImage[0]
        return nameImage
