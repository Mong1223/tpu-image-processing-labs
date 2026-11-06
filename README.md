# Методы и алгоритмы обработки изображений (ТПУ, магистратура, 3 семестр)

Лабораторные работы по цифровой обработке изображений на Python (NumPy, OpenCV, PIL, PyQt5).

| Лаба | Тема | Файлы |
|---|---|---|
| lab1-color-spaces | GUI-приложение (PyQt5) для перевода изображений между цветовыми пространствами RGB / YUV / HSL — собственная реализация преобразований | `res/LAB.py`, `res/yuv_lib.py`, `res/hsl_lib.py` |
| lab2 | Выделение границ: перевод в оттенки серого, операторы Собеля и др. свёрточные фильтры | `Lab2.ipynb` |
| lab3-wavelets | Вейвлет-преобразования Хаара и Добеши (прямое и обратное, многоуровневое) | `1/HaarTansformation.py`, `1/main.py` |
| lab4 | Бинаризация и обработка бинарных изображений | `lab4.ipynb` |
| lab5 | Текстурный анализ изображений | `lab5.ipynb` |

## Запуск
```bash
pip install numpy opencv-python pillow matplotlib pyqt5
python lab1-color-spaces/res/LAB.py
cd lab3-wavelets/1 && python main.py
```
Ноутбуки lab2/lab4/lab5 писались в Google Colab — пути к картинкам (`/content/drive/...`) нужно заменить на локальные.
