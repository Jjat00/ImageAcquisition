from PySide2 import *
from SharedController import *

class ControllerAutoAcquisition():
    def __init__(self, window):
        super(ControllerAutoAcquisition).__init__()
        self.window = window
        self.sharedController = SharedController()
        self.countNoImageAutoAcq = 0
        self.scalaImage = 70
        self.clicStart = False
        self.dimensionsCamera = np.array([640, 480])*(self.scalaImage/100)
        self.criteria = (cv2.TERM_CRITERIA_EPS +
            cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    def setConfigAutoAcq(self, NoImages, patternDimension, pathImages):
        self.patternDimension = patternDimension
        self.NoImagesAutoAcq = NoImages
        self.pathImages = pathImages

    def chooseCamera(self, whichCamera):
        if (whichCamera == 0):
            self.whichCamera = 0
        if (whichCamera == 1):
            self.whichCamera = 1
        if (whichCamera == 2):
            self.sharedController.initThermalCamera()
            self.whichCamera = 2

    def turnOnCamera(self, whichCamera):
        self.chooseCamera(whichCamera)
        if (self.clicStart):
            self.viewCamera.deleteLater()
        self.initCamera()
        self.initCounter()
        return self.viewCamera

    def turnOffCamera(self):
        if (self.clicStart):
            self.viewCamera.deleteLater()
        self.timerCamera.stop()
        self.countNoImageAutoAcq = 0
        self.clicStart = False

    def initCamera(self):
        self.timerCamera = QtCore.QTimer()
        self.timerCamera.setInterval(30)
        self.timerCamera.timeout.connect(self.getFrameDrawPattern)
        self.timerCamera.start()
        self.viewCamera = QtWidgets.QGraphicsView()
        scene = QtWidgets.QGraphicsScene()
        self.imagePixmap = QtGui.QPixmap(*self.dimensionsCamera)
        self.imagePixmapItem = scene.addPixmap(self.imagePixmap)
        self.viewCamera.setScene(scene)
        self.clicStart = True

    def initCounter(self):
        self.timerCounter = QtCore.QTimer()
        self.timerCounter.setInterval(30)
        self.timerCounter.timeout.connect(self.setValueProgressBar)
        self.timerCounter.start()

    def setValueProgressBar(self):
        value = (self.countNoImageAutoAcq/self.NoImagesAutoAcq)*100
        self.window.progressBarAcq.setValue(value)
        self.window.labelNoImage.setText(str(self.countNoImageAutoAcq))

    def getFrameDrawPattern(self):
        if self.countNoImageAutoAcq < self.NoImagesAutoAcq:
            if (self.whichCamera == 0):
                frame = self.detectPattern(self.sharedController.getFrame(0))
            if (self.whichCamera == 1):
                frame = self.detectPattern(self.sharedController.getFrame(1))
            if (self.whichCamera == 2):
                frame = self.detectPattern(self.sharedController.getFrame(2))
            frame = self.sharedController.imageResize(frame, self.scalaImage)
            image = QtGui.QImage(
                frame, *self.dimensionsCamera, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.imagePixmap = QtGui.QPixmap.fromImage(image)
            self.imagePixmapItem.setPixmap(self.imagePixmap)
        else:
            self.timerCamera.stop()

    def detectPattern(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        patternDimension = (self.patternDimension[1], self.patternDimension[0])
        findCorners, corners = cv2.findChessboardCorners(
            gray, patternDimension, flags=cv2.CALIB_CB_NORMALIZE_IMAGE)
        if findCorners:
            corners = cv2.cornerSubPix(
                gray, corners, (11, 11), (-1, -1), self.criteria)
            nameImage = self.pathImages+str(self.countNoImageAutoAcq)+'.png'
            cv2.imwrite(nameImage, image)
            image = cv2.drawChessboardCorners(
                image, patternDimension, corners, findCorners)
            self.countNoImageAutoAcq += 1
            cv2.waitKey(200)
        return image
