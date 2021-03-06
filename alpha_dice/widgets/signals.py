from PyQt5.QtCore import (pyqtSignal, QObject)


class PrimitiveSignals(QObject):
    """
    Standard set of pyqtSignals.
    """
    signal_str = pyqtSignal(str)
    signal_int = pyqtSignal(int)
    signal_float = pyqtSignal(float)
    signal_list = pyqtSignal(list)
    signal_tuple = pyqtSignal(tuple)
    signal_dict = pyqtSignal(dict)
    signal_object = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)
