import sys
sys.path.append('../src/controllers')
from AutomaticAcquisition import *

class viewAutomaticAcquisition():
    def __init__(self, window):
        super(viewAutomaticAcquisition).__init__()
        self.window = window
        self.controllerAutoAcq = AutomaticAcquisition(self.window)

    def connectButtonsRgbCamera(self):
        try:
            self.window.startButton.clicked.disconnect()
            self.conncetButtonsRgb()
        except:
            self.conncetButtonsRgb()

    def connectButtonsDepthCamera(self):
        try:
            self.window.startButton.clicked.disconnect()
            self.conncetButtonsDepth()
        except:
            self.conncetButtonsDepth()

    def connectButtonsThermalCamera(self):
        try:
            self.window.startButton.clicked.disconnect()
            self.connectButtonsThermal()
        except:
            self.connectButtonsThermal()

    def conncetButtonsRgb(self):
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartRgbImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def conncetButtonsDepth(self):
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartDepthImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def connectButtonsThermal(self):
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartThermalImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)
