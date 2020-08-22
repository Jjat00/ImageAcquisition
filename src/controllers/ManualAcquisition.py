from PySide2 import  *
from ControllerManualAcquisition import *

class ManualAcquisition():
    def __init__(self, window):
        super(ManualAcquisition).__init__()
        self.window = window
        self.controller = ControllerManualAcquisition()

    def handlerTurnOnRGBCamera(self):
        rgbImage = self.controller.turnOnCamera(0)
        self.window.displayManual.addWidget(rgbImage)

    def handlerTurnOnDepthCamera(self):
        depthImage = self.controller.turnOnCamera(1)
        self.window.displayManual.addWidget(depthImage)

    def handlerTurnOnThermalCamera(self):
        thermalImage = self.controller.turnOnCamera(2)
        self.window.displayManual.addWidget(thermalImage)

    def handlerCaptureRGBImage(self):
        rgbImage = self.controller.captureImage(0)
        self.window.displayManual.addWidget(rgbImage)

    def handlerCaptureDepthmage(self):
        depthImage = self.controller.captureImage(1)
        self.window.displayManual.addWidget(depthImage)

    def handlerCaptureThermalImage(self):
        thermalImage = self.controller.captureImage(2)
        self.window.displayManual.addWidget(thermalImage)
        
    def handlerSaveRgbImage(self):
        nameImage = self.saveDialog()
        self.controller.saveImage(0, nameImage)

    def handlerSaveDepthImage(self):
        nameImage = self.saveDialog()
        self.controller.saveImage(1, nameImage)

    def handlerSaveThermalImage(self):
        nameImage = self.saveDialog()
        self.controller.saveImage(2, nameImage)

    def handlerTurnOffCamera(self):
        self.controller.turnOffCamera()

    def handlerNone(self):
        print("NONE")

    def saveDialog(self):
        nameImage = QtWidgets.QFileDialog.getSaveFileName(
            self.window, 'Save as', '../data/images', selectedFilter='*.png')
        nameImage = nameImage[0]+".png"
        return nameImage
