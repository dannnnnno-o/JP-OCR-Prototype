import sys
import mss
from PIL import Image
import pytesseract
import pyperclip
import keyboard
import time

from PyQt5 import QtWidgets, QtGui, QtCore

class SnipWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snip Capture")
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.setWindowOpacity(0.3)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setCursor(QtCore.Qt.CrossCursor)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor("red"), 2))
        qp.setBrush(QtGui.QColor(255, 0, 0, 50))
        rect = QtCore.QRect(self.begin, self.end)
        qp.drawRect(rect)

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        self.close()

    def get_rect(self):
        return QtCore.QRect(self.begin, self.end)

def capture_region(rect):
    """Capture selected region using mss."""
    with mss.mss() as sct:
        monitor = {
            "top": rect.top(),
            "left": rect.left(),
            "width": rect.width(),
            "height": rect.height(),
        }
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return img

def ocr_image(img):
    """Run OCR on image using Japanese language and clean up spaces."""
    text = pytesseract.image_to_string(img, lang="jpn")
    # Remove all whitespace (spaces, tabs, newlines)
    text = "".join(text.split())
    return text.strip()

def run_capture_ocr():
    print("\n[Hotkey Triggered] Select region...")
    app = QtWidgets.QApplication(sys.argv)
    snip = SnipWidget()
    snip.show()
    app.exec_()

    rect = snip.get_rect()
    if rect.width() > 0 and rect.height() > 0:
        img = capture_region(rect)
        print("Running OCR (Japanese)...")
        text = ocr_image(img)

        if text:
            print("Recognized text:\n", text)
            pyperclip.copy(text)
            print("Text copied to clipboard ✅")
        else:
            print("No text detected.")
    else:
        print("No region selected.")

def main():
    hotkey = "ctrl+alt+shift+f12"
    print(f"Running in background... Press {hotkey} to snip + OCR Japanese text.")
    keyboard.add_hotkey(hotkey, run_capture_ocr)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
