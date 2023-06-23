# My basic preset of .nuke folder for NukeX and Nuke Studio customization.


### Вся кастомизация Nuke происходит через папку “.nuke”:
- Windows: “C:/Users/user/.nuke”  
- macOS: “/Users/user/.nuke”
- Linux: “/home/user/.nuke”


### Мой шаблон папки .nuke:
```python
- /.nuke
        - /_other
                    - /icons  # папка для иконок
                    - /start_nuke_bat  # папка для .bat файлов (запуск Nuke в safe и terminal)
                    - /set_nuke_reg  # установить для Windows дефолтный запуск Nuke через .reg
        - /Gizmos  # папка с гизмами (может включать подпапки)
        - /Python  # папка с плагинами
                - /3DE4  # папка для импорта линз 3DEqualizer4 в Nuke
                - /Startup  # папка для работы с модулями hiero.ui и hiero.core (NukeStudio)
        - /PythonConstruct  # папка для кастомизации
                - /custom_autolabel.py  # кастомные autolabel для нод
                - /custom_callbacks.py  # кастомные callbacks для Nuke
                - /custom_favorite.py  # кастомные favorite для Nuke
                - /custom_gizmos.py  # модуль, который импортирует гизмы из /.nuke/Gizmos
                - /custom_guides.py  # кастомные форматы
                - /set_nuke_hot_keys.py  # кастомизация дополнительных хоткеев,
                                         # основные заводим через VP Lord of Nodes
                - /set_nuke_knobs_default.py # кастомизация дополнительных дефолтных кнобов,
                                             # основные заводим через VP Lord of Nodes
                - /set_nuke_plugin_paths.py  # импорт модулей из /.nuke/Python
        - /init.py  # импортируем /.nuke/PythonConstruct/set_nuke_plugin_paths.py
        - /menu.py  # импортируем остальное из папки /.nuke/PythonConstruct
