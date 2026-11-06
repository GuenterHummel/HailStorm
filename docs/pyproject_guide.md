# Python Packaging Guide: pyproject.toml & Projektverwaltung

Dieser Leitfaden fasst die wichtigsten Grundlagen, Befehle und Architekturmuster für modernes Python-Packaging mit `pyproject.toml` und `uv` zusammen.

---

## 1. Warum `pyproject.toml`? (PEP 517 / PEP 621)

Frühere Python-Projekte nutzten oft eine Kombination aus `setup.py`, `setup.cfg` und `requirements.txt`.
Mit **PEP 517** und **PEP 621** wurde ein einheitlicher, deklarativer Standard geschaffen:

- **Einheitlich:** Metadaten, Abhängigkeiten und Tool-Konfigurationen (wie `pytest`, `ruff`) liegen in **einer** Datei.
- **Kein ausführbarer Code beim Installieren:** Keine Sicherheitsrisiken oder Nebeneffekte durch Ausführung von `setup.py`.
- **Ersatz für `requirements.txt`:** Alle Produktions- und Entwicklungsabhängigkeiten werden direkt im Build-Manifest gepflegt.

---

## 2. Struktur von `pyproject.toml` (anhand dieses Projekts)

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "hailstorm"
version = "0.1.0"
description = "Learning Python stuff"
readme = "README.md"
requires-python = ">=3.10"

# Produktions-Abhängigkeiten (früher requirements.txt)
dependencies = [
    "cirq~=1.5.0",
    "numpy>=2.2.5",
    "pandas>=2.2.3",
    "regex>=2024.11.6",
    "scipy>=1.15.3",
]

# Optionale Entwicklungs-Abhängigkeiten
[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
]

# Erzeugt ausführbare Terminalbefehle (CLI Entrypoints)
[project.scripts]
hailstorm = "hailstorm:main"

# Automatische Paketerkennung für Python-Module
[tool.setuptools.packages.find]
where = ["."]
include = ["hailstorm*"]
exclude = ["test*"]

# Test-Runner Konfiguration
[tool.pytest.ini_options]
testpaths = ["test"]
python_files = ["test_*.py", "*_test.py"]
```

---

## 3. Versionsangaben & Operatoren

| Operator | Beispiel | Bedeutung |
|---|---|---|
| `~=` (Compatible Release) | `cirq ~= 1.5.0` | `>= 1.5.0, < 1.6.0` (erlaubt sichere Bugfixes/Patches, verhindert Breaking Changes) |
| `>=` | `numpy >= 2.2.5` | Jede Version ab 2.2.5 (auch Version 3.0+) |
| `==` | `pandas == 2.2.3` | Fixiert exakt auf diese Version (keine Updates) |

---

## 4. Wichtige Terminal-Befehle (Cheatsheet)

### Virtuelle Umgebung aktivieren (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

### Installation & Abhängigkeiten verwalten

| Aufgabe | Mit `uv` (Schnell & Modern) | Mit klassischem `pip` |
|---|---|---|
| **Projekt editierbar installieren** | `uv pip install -e .` | `pip install -e .` |
| **Inklusive Dev-Tools (z. B. pytest)** | `uv pip install -e ".[dev]"` | `pip install -e ".[dev]"` |
| **Alle Pakete aktualisieren** | `uv pip install --upgrade -e ".[dev]"` | `pip install --upgrade -e ".[dev]"` |
| **Einzelnes Paket aktualisieren** | `uv pip install --upgrade numpy` | `pip install --upgrade numpy` |
| **Distribution bauen (Wheel & sdist)** | `uv build` | `python -m build` |

---

## 5. Programm und installierte Pakete ausführen

Sobald die virtuelle Umgebung aktiviert ist (`(.venv)` im Prompt):

1. **Direkt als Konsolenbefehl:**
   ```powershell
   hailstorm
   ```
   *(Greift auf den in `[project.scripts]` definierten Einstiegspunkt zu).*

2. **Als Modul über den Python-Launcher `py`:**
   ```powershell
   py -m hailstorm
   py -m pytest
   ```
   > **Hinweis:** Damit ein eigenes Modul mit `py -m <name>` aufgerufen werden kann, benötigt das Modul eine `__main__.py`, welche den Einstiegspunkt aufruft:
   > ```python
   > from hailstorm import main
   > 
   > if __name__ == "__main__":
   >     main()
   > ```

3. **Per Kurz-Befehl (Einzeiler):**
   ```powershell
   py -c "import hailstorm; hailstorm.main()"
   ```

---

## 6. Projektstrukturen & Unterprojekte (Vergleich zu Java/Gradle)

### Variante A: Submodule im selben Projekt
Alle Ordner mit einer `__init__.py` werden als Subpakete erkannt und mitinstalliert:
```text
HailStorm/
├── pyproject.toml
├── hailstorm/
│   ├── __init__.py
│   ├── hailstorm.py
│   └── math_utils/          # Import: from hailstorm.math_utils import ...
│       └── __init__.py
```

### Variante B: Multi-Projekt / Monorepo (Workspace)
Entspricht exakt einem **Gradle Multi-Project Build** in Java/Kotlin:

| Konzept | Gradle (Kotlin DSL) | Python (`uv` Workspace) |
|---|---|---|
| **Root-Konfiguration** | `settings.gradle.kts` (`include(...)`) | Root `pyproject.toml` (`[tool.uv.workspace]`) |
| **Subprojekt-Buildfile** | `subproject/build.gradle.kts` | `packages/subproject/pyproject.toml` |
| **Interne Abhängigkeit** | `implementation(project(":core"))` | `dependencies = ["core"]` mit `{ workspace = true }` |
| **Zentraler Sync** | `./gradlew build` | `uv sync` |
