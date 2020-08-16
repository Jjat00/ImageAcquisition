import sys
sys.path.append('../src/controllers')
from ManualAcquisition import *

class ViewManualAcquisition():
    def __init__(self, window):
        super(ViewManualAcquisition).__init__()
        self.window = window
        self.controllerManualAcq = ManualAcquisition(self.window)

    def connectButtonsRgbCamera(self):
        try:
            self.disconnectButtons()
            self.connectButtonsRgb()
        except:
            self.connectButtonsRgb()

    def connectButtonsDepthCamera(self):
        try:
            self.disconnectButtons()
            self.connectButtonsDepth()
        except:
            self.connectButtonsDepth()

    def connectButtonsThermalCamera(self):
        try:
            self.disconnectButtons()
            self.conncetButtonsThermal()
        except:
            self.conncetButtonsThermal()

    def stopCamera(self):
            self.window.offButton.clicked.connect(
                self.controllerManualAcq.handlerTurnOffCamera)

    def connectButtonsRgb(self):
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnRGBCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureRGBImage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveRgbImage)

    def connectButtonsDepth(self):
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnDepthCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureDepthmage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveDepthImage)

    def conncetButtonsThermal(self):
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnThermalCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureThermalImage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveThermalImage)

    def disconnectButtons(self):
        self.window.onButton.clicked.disconnect()
        self.window.captureButton.clicked.disconnect()
        self.window.saveButton.clicked.disconnect()
