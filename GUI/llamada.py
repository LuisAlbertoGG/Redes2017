#! /usr/bin/env python
# coding=utf8


# Copyright (C) 2011 Saúl Ibarra Corretgé <saghul@gmail.com>
#

# Some inspiration taken from: http://www.morethantechnical.com/2009/03/05/qt-opencv-combined-for-face-detecting-qwidgets/


#from cv2.cv import *
import sys
sys.path.append('/usr/local/opencv-2.4.13')
import cv2.cv as cv
from PyQt4.QtCore import QPoint, QTimer
from PyQt4.QtGui import QApplication, QImage, QPainter, QWidget


class IplQImage(QImage):
    """
    http://matthewshotton.wordpress.com/2011/03/31/python-opencv-iplimage-to-pyqt-qimage/
    A class for converting iplimages to qimages
    """

    def __init__(self,iplimage):
        # Rough-n-ready but it works dammit
        alpha = cv.CreateMat(iplimage.height,iplimage.width, cv.CV_8UC1)
        cv.Rectangle(alpha, (0, 0), (iplimage.width,iplimage.height), cv.ScalarAll(255) ,-1)
        rgba = cv.CreateMat(iplimage.height, iplimage.width, cv.CV_8UC4)
        cv.Set(rgba, (1, 2, 3, 4))
        cv.MixChannels([iplimage, alpha],[rgba], [
        (0, 0), # rgba[0] -> bgr[2]
        (1, 1), # rgba[1] -> bgr[1]
        (2, 2), # rgba[2] -> bgr[0]
        (3, 3)  # rgba[3] -> alpha[0]
        ])
        self.__imagedata = rgba.tostring()
        super(IplQImage,self).__init__(self.__imagedata, iplimage.width, iplimage.height, QImage.Format_RGB32)


class VideoWidget(QWidget):
    """ A class for rendering video coming from OpenCV """

    def __init__(self, parent=None):
        QWidget.__init__(self)
        self._capture = cv.CreateCameraCapture(0)
        # Take one frame to query height
        frame = cv.QueryFrame(self._capture)
        #if(frame != None):
        self.setMinimumSize(frame.width, frame.height)
        self.setMaximumSize(self.minimumSize())
        self._frame = None
        self._image = self._build_image(frame)# Paint every 50 ms
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.queryFrame)
        self._timer.start(50)
        #else:
        #	self.setMinimumSize(100, 100)
	    #    self.setMaximumSize(self.minimumSize())
	    #    self._frame = None
	    #    self._image = self._build_image(frame)
	        # Paint every 50 ms
	    #    self._timer = QTimer(self)
	    #    self._timer.timeout.connect(self.queryFrame)
	    #    self._timer.start(50)
	     
	    	

    def _build_image(self, frame):
        if not self._frame:
            self._frame = cv.CreateImage((frame.width, frame.height), cv.IPL_DEPTH_8U, frame.nChannels)
        if frame.origin == cv.IPL_ORIGIN_TL:
            cv.Copy(frame, self._frame)
        else:
            cv.Flip(frame, self._frame, 0)
        return IplQImage(self._frame)



    def queryFrame(self):
        frame = cv.QueryFrame(self._capture)
        self._image = self._build_image(frame)
        self.update()
