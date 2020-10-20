from PySide2 import QtWidgets
from controllers.ControllerAutoAcquisitionTab import ControllerAutoAcquisitionTab
from controllers.ControllerManualAcquisitionTab import ControllerManualAcquisitionTab


class MainControllerIntrisicAcqWidget():
    """
    Main controller app Deptherm Inspection
    """

    def __init__(self, intrinsicAcquisitionWidget):
        super(MainControllerIntrisicAcqWidget).__init__()
        self.window = intrinsicAcquisitionWidget.window
        self.connectComboBox()
        intrinsicAcquisitionWidget.exec()

    def connectComboBox(self):
        """
        Connect comboBox
        """
        self.connectButtonsManualAcquisition()
        self.window.comboBoxManual.currentIndexChanged.connect(
            self.connectButtonsManualAcquisition)
        self.connectButtonsAtomaticAcquisition()
        self.window.comboBoxAuto.currentIndexChanged.connect(
            self.connectButtonsAtomaticAcquisition)

    #Connect  buttons manual acquisition tab
    def connectButtonsManualAcquisition(self):
        self.controllerManualAcq = ControllerManualAcquisitionTab(self.window)
        chosenCamera = self.window.comboBoxManual.currentText()
        if chosenCamera == "RGB":
            try:
                self.cleanWorkspaceManualAcq()
                self.disconnectButtonsManualAcqTab()
                self.buttonsManualAcqRgbCamera()
            except:
                self.cleanWorkspaceManualAcq()
                self.buttonsManualAcqRgbCamera()
        if chosenCamera == "DEPTH":
            try:
                self.cleanWorkspaceManualAcq()
                self.disconnectButtonsManualAcqTab()
                self.buttonsManualAcqDepthCamera()
            except:
                self.cleanWorkspaceManualAcq()
                self.buttonsManualAcqDepthCamera()
        if chosenCamera == "THERMAL":
            try:
                self.cleanWorkspaceManualAcq()
                self.disconnectButtonsManualAcqTab()
                self.buttonsManualAcqThermalCamera()
            except:
                self.cleanWorkspaceManualAcq()
                self.buttonsManualAcqThermalCamera()
        if chosenCamera == "NONE":
            pass

    def buttonsManualAcqRgbCamera(self):
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnRGBCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureRGBImage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveRgbImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def buttonsManualAcqDepthCamera(self):
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnDepthCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureDepthmage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveDepthImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def buttonsManualAcqThermalCamera(self):
        self.window.onButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOnThermalCamera)
        self.window.captureButton.clicked.connect(
            self.controllerManualAcq.handlerCaptureThermalImage)
        self.window.saveButton.clicked.connect(
            self.controllerManualAcq.handlerSaveThermalImage)
        self.window.offButton.clicked.connect(
            self.controllerManualAcq.handlerTurnOffCamera)

    def disconnectButtonsManualAcqTab(self):
        self.window.onButton.clicked.disconnect()
        self.window.captureButton.clicked.disconnect()
        self.window.saveButton.clicked.disconnect()

    #Connect  buttons automatic acquisition tab
    def connectButtonsAtomaticAcquisition(self):
        self.controllerAutoAcq = ControllerAutoAcquisitionTab(self.window)
        chosenCamera = self.window.comboBoxAuto.currentText()
        if chosenCamera == "RGB":
            try:
                self.cleanWorkspaceAutoAcqManualAcq()
                self.window.startButton.clicked.disconnect()
                self.buttonsAutoAcqRgbCamera()
            except:
                self.cleanWorkspaceAutoAcqManualAcq()
                self.buttonsAutoAcqRgbCamera()
        if chosenCamera == "DEPTH":
            try:
                self.cleanWorkspaceAutoAcqManualAcq()
                self.window.startButton.clicked.disconnect()
                self.buttonsAutoAcqDepthCamera()
            except:
                self.cleanWorkspaceAutoAcqManualAcq()
                self.buttonsAutoAcqDepthCamera()
        if chosenCamera == "THERMAL":
            try:
                self.cleanWorkspaceAutoAcqManualAcq()
                self.window.startButton.clicked.disconnect()
                self.buttonsAutoAcqThermalCamera()
            except:
                self.cleanWorkspaceAutoAcqManualAcq()
                self.buttonsAutoAcqThermalCamera()
        if chosenCamera == "NONE":
            pass

    def buttonsAutoAcqRgbCamera(self):
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartRgbImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def buttonsAutoAcqDepthCamera(self):
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartDepthImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def buttonsAutoAcqThermalCamera(self):
        self.window.startButton.clicked.connect(
            self.controllerAutoAcq.handlerStartThermalImageAcq)
        self.window.stopButton.clicked.connect(
            self.controllerAutoAcq.handlerStopAcquisition)

    def cleanWorkspaceManualAcq(self):
        """
        Clean worksspace remove all widget
        """
        for index in reversed(range(self.window.displayManual.count())):
            layoutItem = self.window.displayManual.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.displayManual.removeWidget(widgetToRemove)

    def cleanWorkspaceAutoAcqManualAcq(self):
        """
        Clean worksspace remove all widget
        """
        for index in reversed(range(self.window.displayAuto.count())):
            layoutItem = self.window.displayAuto.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.displayAuto.removeWidget(widgetToRemove)
