# JP-OCR Snipping Tool

## 📖 Summary
This Python script lets you **snip a region of your screen and run OCR (Optical Character Recognition) on Japanese text**.  
The recognized text is automatically cleaned (spaces removed) and copied to your clipboard for easy pasting anywhere.  

It’s especially useful for quickly extracting Japanese text from images, PDFs, or applications that don’t allow text selection.

---

## 🔧 Prerequisites

Before running the script, make sure you have the following installed:

- **Python 3.7+** (tested with Python 3.14 in development)
- **Tesseract OCR**
  - Download from [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki) (Windows).
  - Ensure the installation path (e.g. `C:\Program Files\Tesseract-OCR`) is added to your system `PATH`.
  - Confirm installation with:
    ```bash
    tesseract --version
    ```
- **Japanese language data for Tesseract**
  - Usually included in the installer. Check that `jpn.traineddata` exists in `Tesseract-OCR\tessdata`.

- **Python packages** (install via pip):
  ```bash
  pip install pytesseract pillow mss pyperclip keyboard pyqt
## ▶️ How to Run

1. Save the script as `main.py` (or any filename you prefer).
2. Open a terminal in the script’s folder.
3. Run:
   ```bash
   python main.py
   ```
4. The script will run in the background and wait for a hotkey.

---

## 🎮 How to Use

- Press **Ctrl + Alt + Shift + F12** to trigger the snipping tool.
- Select a rectangular region on your screen with the mouse.
- The script will:
  1. Capture the selected region.
  2. Run OCR using Tesseract (Japanese mode).
  3. Clean up the text (remove unwanted spaces).
  4. Copy the recognized text to your clipboard.
- Paste the text anywhere (e.g., editor, browser, chat).

---

## ⚠️ Notes

- OCR accuracy depends on image quality and font clarity. For best results, use high-resolution captures.
- If you see the warning `QApplication was not created in the main() thread`, it’s due to PyQt being launched from a hotkey callback. The script still works, but restructuring to run Qt in the main thread can remove the warning.
- You can change the hotkey by editing:
  ```python
  hotkey = "ctrl+alt+shift+f12"
  ```

---

## 🛠️ Troubleshooting

- **TesseractNotFoundError**  
  → Make sure Tesseract OCR is installed and added to PATH. PATH must contain the folder (e.g. `C:\Program Files\Tesseract-OCR`), not the `.exe` file.

- **Japanese not recognized**  
  → Check that `jpn.traineddata` exists in the `tessdata` folder inside your Tesseract installation.

- **Clipboard contains spaces**  
  → The script already strips spaces using `text = "".join(text.split())`. If you want to preserve line breaks, replace with `text.replace(" ", "")`.

---

## ✅ Example

Snipped text:
```
禁ぎろら学開参ナタヌア統月エシ工18毎オル橋寺つほト関引フアイテ
```

Clipboard result:
```
禁ぎろら学開参ナタヌア統月エシ工18毎オル橋寺つほト関引フアイテ
```

---

## 📌 License

This script is provided as-is for personal use.  
Tesseract OCR is licensed under the Apache License 2.0.