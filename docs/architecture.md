# MVC Architektur

```
components/
layout/ <-- Grundstruktur Seite
pages/
    home/
        __init__ <-- View
        data <-- Model
        callbacks <-- Controller
    admin/
        __init__
        data
        callbacks
assets/
utils/
app <-- app separieren, um circular imports zu vermeiden
index/__main__ <-- Aufruf Seite
routes
```
