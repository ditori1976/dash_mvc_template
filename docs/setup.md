# Setup

## Virtuelle Umgebung

Anlegen einer virtuellen Umgebung mit unterschiedlicher Python Version

```
virtualenv venv -p <path/to/python>
# e.g. virtualenv venv -p D:\PyInstalls\Python388\python.exe
```

## Python Module

Die benötigten Python-Module werden in requirements.txt gelistet. Zur Installation folgendende Befehle ausführen:

```
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
```

Bei veralteter PIP Version:

```
python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pip
```
