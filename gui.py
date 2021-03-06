import pkgutil
import logging
from PyQt4 import QtCore, QtGui

__author__ = "Roman Budnik"
__copyright__ = "Copyright 2014-2016"
__credits__ = ["Roman Budnik"]
__license__ = "LGPL"
__version__ = "0.9.9"
__maintainer__ = "Roman Budnik"
__status__ = "Development"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 320)
        icon = QtGui.QPixmap()
        icon.loadFromData(pkgutil.get_data(__name__, 'resources/gui.ico'), "ico")
        MainWindow.setWindowIcon(QtGui.QIcon(icon))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.titleInfoBox = QtGui.QGroupBox(self.centralwidget)
        self.titleInfoBox.setObjectName(_fromUtf8("titleInfoBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.titleInfoBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tPathLabel = QtGui.QLabel(self.titleInfoBox)
        self.tPathLabel.setObjectName(_fromUtf8("tPathLabel"))
        self.horizontalLayout_6.addWidget(self.tPathLabel)
        self.vPathLabel = QtGui.QLabel(self.titleInfoBox)
        self.vPathLabel.setObjectName(_fromUtf8("vPathLabel"))
        self.horizontalLayout_6.addWidget(self.vPathLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tTitleLabel = QtGui.QLabel(self.titleInfoBox)
        self.tTitleLabel.setObjectName(_fromUtf8("tTitleLabel"))
        self.horizontalLayout_5.addWidget(self.tTitleLabel)
        self.vTitleLabel = QtGui.QLabel(self.titleInfoBox)
        self.vTitleLabel.setObjectName(_fromUtf8("vTitleLabel"))
        self.horizontalLayout_5.addWidget(self.vTitleLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tNumLabel = QtGui.QLabel(self.titleInfoBox)
        self.tNumLabel.setObjectName(_fromUtf8("tNumLabel"))
        self.horizontalLayout_4.addWidget(self.tNumLabel)
        self.vNumLabel = QtGui.QLabel(self.titleInfoBox)
        self.vNumLabel.setObjectName(_fromUtf8("vNumLabel"))
        self.horizontalLayout_4.addWidget(self.vNumLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tBitLabel = QtGui.QLabel(self.titleInfoBox)
        self.tBitLabel.setObjectName(_fromUtf8("tBitLabel"))
        self.horizontalLayout_3.addWidget(self.tBitLabel)
        self.vBitLabel = QtGui.QLabel(self.titleInfoBox)
        self.vBitLabel.setObjectName(_fromUtf8("vBitLabel"))
        self.horizontalLayout_3.addWidget(self.vBitLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tAudioLabel = QtGui.QLabel(self.titleInfoBox)
        self.tAudioLabel.setObjectName(_fromUtf8("tAudioLabel"))
        self.horizontalLayout_2.addWidget(self.tAudioLabel)
        self.vAudioLabel = QtGui.QLabel(self.titleInfoBox)
        self.vAudioLabel.setObjectName(_fromUtf8("vAudioLabel"))
        self.horizontalLayout_2.addWidget(self.vAudioLabel)
        self.tSubLabel = QtGui.QLabel(self.titleInfoBox)
        self.tSubLabel.setObjectName(_fromUtf8("tSubLabel"))
        self.horizontalLayout_2.addWidget(self.tSubLabel)
        self.vSubLabel = QtGui.QLabel(self.titleInfoBox)
        self.vSubLabel.setObjectName(_fromUtf8("vSubLabel"))
        self.horizontalLayout_2.addWidget(self.vSubLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.titleInfoBox)
        self.settingsTabs = QtGui.QTabWidget(self.centralwidget)
        self.settingsTabs.setObjectName(_fromUtf8("settingsTabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.videoLayout = QtGui.QHBoxLayout()
        self.videoLayout.setObjectName(_fromUtf8("videoLayout"))
        self.convertVideoCheck = QtGui.QCheckBox(self.tab)
        self.convertVideoCheck.setObjectName(_fromUtf8("convertVideoCheck"))
        self.videoLayout.addWidget(self.convertVideoCheck)
        self.eightBitButton = QtGui.QRadioButton(self.tab)
        self.eightBitButton.setObjectName(_fromUtf8("eightBitButton"))
        self.videoLayout.addWidget(self.eightBitButton)
        self.tenBitButton = QtGui.QRadioButton(self.tab)
        self.tenBitButton.setObjectName(_fromUtf8("tenBitButton"))
        self.videoLayout.addWidget(self.tenBitButton)
        self.verticalLayout_3.addLayout(self.videoLayout)
        self.audioLayout = QtGui.QHBoxLayout()
        self.audioLayout.setObjectName(_fromUtf8("audioLayout"))
        self.audioCheck = QtGui.QCheckBox(self.tab)
        self.audioCheck.setObjectName(_fromUtf8("audioCheck"))
        self.audioLayout.addWidget(self.audioCheck)
        self.audioBox = QtGui.QComboBox(self.tab)
        self.audioBox.setObjectName(_fromUtf8("audioBox"))
        self.audioLayout.addWidget(self.audioBox)
        self.audioPreviewButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioPreviewButton.sizePolicy().hasHeightForWidth())
        self.audioPreviewButton.setSizePolicy(sizePolicy)
        self.audioPreviewButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.audioPreviewButton.setObjectName(_fromUtf8("audioPreviewButton"))
        self.audioLayout.addWidget(self.audioPreviewButton)
        self.verticalLayout_3.addLayout(self.audioLayout)
        self.subtitlesLayout = QtGui.QHBoxLayout()
        self.subtitlesLayout.setObjectName(_fromUtf8("subtitlesLayout"))
        self.subCheck = QtGui.QCheckBox(self.tab)
        self.subCheck.setObjectName(_fromUtf8("subCheck"))
        self.subtitlesLayout.addWidget(self.subCheck)
        self.subBox = QtGui.QComboBox(self.tab)
        self.subBox.setObjectName(_fromUtf8("subBox"))
        self.subtitlesLayout.addWidget(self.subBox)
        self.verticalLayout_3.addLayout(self.subtitlesLayout)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.rangeFromLabel = QtGui.QLabel(self.tab)
        self.rangeFromLabel.setObjectName(_fromUtf8("rangeFromLabel"))
        self.horizontalLayout_7.addWidget(self.rangeFromLabel)
        self.startBox = QtGui.QSpinBox(self.tab)
        self.startBox.setMinimum(1)
        self.startBox.setObjectName(_fromUtf8("startBox"))
        self.horizontalLayout_7.addWidget(self.startBox)
        self.rangeToLabel = QtGui.QLabel(self.tab)
        self.rangeToLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rangeToLabel.setObjectName(_fromUtf8("rangeToLabel"))
        self.horizontalLayout_7.addWidget(self.rangeToLabel)
        self.endBox = QtGui.QSpinBox(self.tab)
        self.endBox.setMinimum(1)
        self.endBox.setObjectName(_fromUtf8("endBox"))
        self.horizontalLayout_7.addWidget(self.endBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.settingsTabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        #self.settingsTabs.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        #self.settingsTabs.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.settingsTabs)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bakeButton = QtGui.QPushButton(self.centralwidget)
        self.bakeButton.setObjectName(_fromUtf8("bakeButton"))
        self.horizontalLayout.addWidget(self.bakeButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.progressLabel = QtGui.QLabel(self.centralwidget)
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.horizontalLayout.addWidget(self.progressLabel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.folderButton = QtGui.QPushButton(self.centralwidget)
        self.folderButton.setObjectName(_fromUtf8("folderButton"))
        self.horizontalLayout.addWidget(self.folderButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.totalProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.totalProgressBar.setProperty("value", 24)
        self.totalProgressBar.setTextVisible(False)
        self.totalProgressBar.setObjectName(_fromUtf8("totalProgressBar"))
        self.verticalLayout_2.addWidget(self.totalProgressBar)
        self.episodeProgressBar = QtGui.QProgressBar(self.centralwidget)
        self.episodeProgressBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.episodeProgressBar.setValue(0)
        self.episodeProgressBar.setTextVisible(False)
        self.episodeProgressBar.setMaximum(100)
        self.episodeProgressBar.setObjectName(_fromUtf8("episodeProgressBar"))
        self.verticalLayout_2.addWidget(self.episodeProgressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMore = QtGui.QMenu(self.menubar)
        self.menuMore.setObjectName(_fromUtf8("menuMore"))
        MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtGui.QStatusBar(MainWindow)
        #self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuMore.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMore.menuAction())

        self.retranslateUi(MainWindow)
        self.settingsTabs.setCurrentIndex(0)
        self.convertVideoCheck.toggled.connect(lambda l: self.set_convert(l))
        self.audioCheck.toggled.connect(lambda l: self.set_audio(l))
        self.subCheck.toggled.connect(lambda l: self.set_subs(l))
        self.bakeButton.clicked.connect(self.bake)
        self.folderButton.clicked.connect(self.open)
        self.startBox.valueChanged.connect(lambda l: self.endBox.setMinimum(l))
        self.actionAbout.triggered.connect(self.about)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tTitleLabel.hide()
        self.vTitleLabel.hide()
        self.tAudioLabel.hide()
        self.vAudioLabel.hide()
        self.tSubLabel.hide()
        self.vSubLabel.hide()
        self.eightBitButton.hide()
        self.tenBitButton.hide()
        self.audioBox.hide()
        self.audioPreviewButton.hide()
        self.subBox.hide()
        self.tab_2.hide()
        self.tab_3.hide()
        self.totalProgressBar.hide()
        self.episodeProgressBar.hide()
        self.progressLabel.hide()

    def about(self):
        Dialog = QtGui.QDialog()
        dui = aboutDialog()
        dui.setupUi(Dialog)
        Dialog.exec_()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Baker", None))
        self.titleInfoBox.setTitle(_translate("MainWindow", "Title info", None))
        self.tPathLabel.setText(_translate("MainWindow", "Path:", None))
        self.vPathLabel.setText(_translate("MainWindow", "?", None))
        self.tTitleLabel.setText(_translate("MainWindow", "Title:", None))
        self.vTitleLabel.setText(_translate("MainWindow", "?", None))
        self.tNumLabel.setText(_translate("MainWindow", "Number of episodes:", None))
        self.vNumLabel.setText(_translate("MainWindow", "?", None))
        self.tBitLabel.setText(_translate("MainWindow", "Pixel color depth:", None))
        self.vBitLabel.setText(_translate("MainWindow", "?", None))
        self.tAudioLabel.setText(_translate("MainWindow", "Audio tracks availiable:", None))
        self.vAudioLabel.setText(_translate("MainWindow", "?", None))
        self.tSubLabel.setText(_translate("MainWindow", "Subtitles availiable:", None))
        self.vSubLabel.setText(_translate("MainWindow", "?", None))
        self.convertVideoCheck.setText(_translate("MainWindow", "Convert video", None))
        self.eightBitButton.setText(_translate("MainWindow", "to 8-bit", None))
        self.tenBitButton.setText(_translate("MainWindow", "to10-bit", None))
        self.audioCheck.setText(_translate("MainWindow", "Add audio track", None))
        self.audioPreviewButton.setText(_translate("MainWindow", "Preview", None))
        self.subCheck.setText(_translate("MainWindow", "Add subtitles", None))
        self.rangeFromLabel.setText(_translate("MainWindow", "Process episodes from", None))
        self.rangeToLabel.setText(_translate("MainWindow", "to", None))
        self.settingsTabs.setTabText(self.settingsTabs.indexOf(self.tab), _translate("MainWindow", "General", None))
        self.settingsTabs.setTabText(self.settingsTabs.indexOf(self.tab_2), _translate("MainWindow", "Video", None))
        self.settingsTabs.setTabText(self.settingsTabs.indexOf(self.tab_3), _translate("MainWindow", "Other", None))
        self.bakeButton.setText(_translate("MainWindow", "Bake!", None))
        self.progressLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.folderButton.setText(_translate("MainWindow", "Choose folder", None))
        self.menuMore.setTitle(_translate("MainWindow", "More", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    def open(self, tooldir, collection=QtCore.QDir.currentPath()):
        from title import Anime
        from baker import Converter

        logging.debug("> gui.open")
        folder = QtGui.QFileDialog.getExistingDirectory(None, "Choose folder", collection)
        if not folder:
            logging.error("You must choose a folder with video files!")
            exit(1)
        global anime
        anime = Anime(folder, tooldir)
        self.vPathLabel.setText(folder)
        self.vNumLabel.setText(str(anime.n()))
        self.vBitLabel.setText("{}bit".format(anime.bit_depth))
        self.startBox.setMaximum(anime.n())
        self.startBox.setValue(1)
        self.endBox.setMaximum(anime.n())
        self.endBox.setValue(anime.n())
        self.converter = Converter(anime)
        self.converter.update.connect(self.progress, QtCore.Qt.QueuedConnection)
        self.convertVideoCheck.setChecked(False)
        self.audioCheck.setChecked(False)
        self.subCheck.setChecked(False)
        self.bakeButton.setDisabled(True)
        logging.debug("< gui.open")

    def checksoft(self, workdir):
        import urllib.request
        from os import path, remove, makedirs
        global dir_path

        logging.debug("> gui.checksoft")
        if not path.exists(workdir):
            makedirs(workdir)

        splash_pix = QtGui.QPixmap()
        splash_pix.loadFromData(pkgutil.get_data(__name__, 'resources/splash'), "png")
        splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setBold(True)
        font.setPointSize(10)
        splash.setFont(font)
        splash.showMessage("{}Starting...".format('\n'*11),
                           QtCore.Qt.AlignAbsolute, QtCore.Qt.white)
        splash.show()
        if not (path.exists('{}\\ffprobe.exe'.format(workdir))
                or path.exists('{}\\mkvmerge.exe'.format(workdir))
                or path.exists('{}\\x264.exe'.format(workdir))):
            splash.showMessage("{}Downloading necessary tools...".format('\n'*11),
                               QtCore.Qt.AlignAbsolute, QtCore.Qt.white)
            splash.show()
            urllib.request.urlretrieve("https://drive.google.com/uc?export=download&id=0BzO4LREgLV3SUW5NbkNYYUIzb2M",
                                       "{}\\baker_tools.zip".format(workdir))
            from zipfile import ZipFile
            with ZipFile('{}\\baker_tools.zip'.format(workdir), "r") as z:
                z.extractall(workdir)
            remove("{}\\baker_tools.zip".format(workdir))
        else:
            splash.showMessage("{}Welcome to bakery!".format('\n'*11),
                               QtCore.Qt.AlignAbsolute, QtCore.Qt.white)
            import time
            time.sleep(1)
        splash.finish(None)
        logging.debug("< gui.checksoft")

    def set_convert(self, need):
        logging.debug("> gui.set_convert")
        self.converter.need_convert = need
        self.bakeButton.setEnabled(need)
        logging.debug("< gui.convert")

    def set_audio(self, need):
        logging.debug("> gui.set_audio")
        if need:
            self.audioBox.show()
            self.audioBox.addItems(list(anime.audio.keys()))
        else:
            self.audioBox.hide()
            self.audioBox.clear()
            self.converter.audio = [False, '', '']
        self.bakeButton.setEnabled(need)
        logging.debug("< gui.set_audio")

    def set_subs(self, need):
        logging.debug("> gui.set_subs")
        if need:
            self.subBox.show()
            self.subBox.addItems(list(anime.subtitles.keys()))
        else:
            self.subBox.hide()
            self.subBox.clear()
            self.converter.subs = [False, '', '']
        self.bakeButton.setEnabled(need)
        logging.debug("< gui.set_subs")

    def bake(self):
        logging.debug("> gui.bake")
        if self.audioBox.currentText() != '':
            self.converter.audio = [True,
                                    anime.audio[self.audioBox.currentText()]["path"],
                                    anime.audio[self.audioBox.currentText()]["items"]]
        if self.subBox.currentText() != '':
            self.converter.subs = [True,
                                   anime.subtitles[self.subBox.currentText()]["path"],
                                   anime.subtitles[self.subBox.currentText()]["items"]]
        self.totalProgressBar.setMaximum(0)
        self.totalProgressBar.setValue(-1)
        self.totalProgressBar.setTextVisible(False)
        self.totalProgressBar.setVisible(True)
        self.convertVideoCheck.setDisabled(True)
        self.audioCheck.setDisabled(True)
        self.subCheck.setDisabled(True)
        self.bakeButton.setDisabled(True)
        self.startBox.setDisabled(True)
        self.endBox.setDisabled(True)
        self.episodeProgressBar.setValue(0)
        self.episodeProgressBar.show()
        self.converter.first = self.startBox.value()
        self.converter.last = self.endBox.value()
        self.converter.finished.connect(self.unlock, QtCore.Qt.QueuedConnection)
        self.converter.start()
        logging.debug("< gui.bake")

    def progress(self, counters):
        logging.debug("> gui.progress")
        if counters[0] is not None:
            if self.totalProgressBar.value() == -1:
                self.totalProgressBar.setFormat('%v/{}'.format(self.endBox.value() + 1 - self.startBox.value()))
                self.totalProgressBar.setTextVisible(True)
                self.totalProgressBar.setMaximum(self.endBox.value() - self.startBox.value() + 1)
                logging.debug('\tSet bar length to {}'.format(self.endBox.value()))
                self.totalProgressBar.setValue(0)
            self.totalProgressBar.setValue(counters[0])
            logging.debug('\tUpdated bar to {}'.format(self.totalProgressBar.value()))
        if counters[1] is not None:
            self.episodeProgressBar.setValue(counters[1])
        logging.debug("< gui.progress")

    def unlock(self):
        logging.debug("> gui.unlock")
        self.convertVideoCheck.setDisabled(False)
        self.audioCheck.setDisabled(False)
        self.subCheck.setDisabled(False)
        self.bakeButton.setDisabled(False)
        self.startBox.setValue(self.endBox.value())
        self.startBox.setDisabled(False)
        self.endBox.setValue(anime.n())
        self.endBox.setDisabled(False)
        logging.debug("< gui.unlock")

    def abort(self):
        logging.debug("> gui.abort")
        self.convertVideoCheck.setChecked(False)
        self.audioCheck.setChecked(False)
        self.subCheck.setChecked(False)
        logging.debug("< gui.abort")

class aboutDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setMinimumSize(250, 200)
        Dialog.setMaximumSize(250, 200)
        icon = QtGui.QPixmap()
        icon.loadFromData(pkgutil.get_data(__name__, 'resources/gui.ico'), "ico")
        Dialog.setWindowIcon(QtGui.QIcon(icon))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ico = QtGui.QLabel(Dialog)
        self.ico.setObjectName(_fromUtf8("ico"))
        self.ico.setAlignment(QtCore.Qt.AlignCenter)
        icon = icon.scaledToHeight(128)
        self.ico.setPixmap(icon)
        self.verticalLayout.addWidget(self.ico)
        self.app = QtGui.QLabel(Dialog)
        self.app.setObjectName(_fromUtf8("app"))
        self.verticalLayout.addWidget(self.app)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.author = QtGui.QLabel(Dialog)
        self.author.setObjectName(_fromUtf8("author"))
        self.verticalLayout_3.addWidget(self.author)
        self.github = QtGui.QLabel(Dialog)
        self.github.setObjectName(_fromUtf8("github"))
        self.verticalLayout_3.addWidget(self.github)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.authorName = QtGui.QLabel(Dialog)
        self.authorName.setObjectName(_fromUtf8("authorName"))
        self.verticalLayout_2.addWidget(self.authorName)
        self.githubLink = QtGui.QLabel(Dialog)
        self.githubLink.setObjectName(_fromUtf8("githubLink"))
        self.verticalLayout_2.addWidget(self.githubLink)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.license = QtGui.QLabel(Dialog)
        self.license.setMaximumSize(QtCore.QSize(16777215, 21))
        self.license.setObjectName(_fromUtf8("license"))
        self.gridLayout.addWidget(self.license, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About", None))
        self.app.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Baker v.{}</p></body></html>"
                                    .format(__version__), None))
        self.author.setText(_translate("Dialog", "Author", None))
        self.github.setText(_translate("Dialog", "GitHub link", None))
        self.authorName.setText(_translate("Dialog", "<html><head/><body><p align=\"right\">{}</p></body></html>"
                                           .format(__author__), None))
        self.githubLink.setText(_translate("Dialog",
                                           "<html><head/><body><p align=\"right\"><a href=\"https://github.com/budrom/Baker\">"
                                           "<span style=\" text-decoration: underline; color:#0000ff;\">"
                                           "github.com/budrom/Baker</span></a></p></body></html>", None))
        self.license.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Licensed under {}, {}"
                                                  "</p></body></html>".format(__license__,__copyright__), None))
