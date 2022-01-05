"""For dynamic usage of Qt Designer files."""
import os
import inspect
import importlib
import subprocess

import PySide6


def get_module(from_path):
    """
    From a __file__-path of another module load according .ui into module.
    Make sure it's up-to-date. Recompile if necessary.
    """
    dirpath, base = os.path.split(from_path)
    name = os.path.splitext(base)[0]
    ui_name = name + '.ui'
    ui_mod_name = name + '_ui'
    py_name = ui_mod_name + '.py'
    py_path = os.path.join(dirpath, py_name)
    ui_path = os.path.join(dirpath, ui_name)
    if os.path.isfile(py_path):
        if os.path.isfile(ui_path) and os.path.getmtime(ui_path) > os.path.getmtime(py_path):
            to_python(dirpath, ui_name, py_name)
    elif os.path.isfile(ui_path):
        to_python(dirpath, ui_name, py_name)
    else:
        raise FileNotFoundError(f'No {py_name} or {ui_name} found! Unable to build ui!')

    return get_ui_class(ui_mod_name)()


def get_ui_class(ui_mod_name):
    module = importlib.import_module(ui_mod_name)
    classes = [obj for name, obj in inspect.getmembers(module, inspect.isclass)
               if obj.__module__ == ui_mod_name]
    if not classes:
        raise AttributeError(f'Could not find own class from module "{module.__name__}"')
    return classes[0]


def to_python(path, ui_name, py_name):
    uic_path = os.path.join(PySide6.__path__[0], 'uic.exe')
    subprocess.call([uic_path, '-g', 'python', ui_name, '-o', py_name], cwd=path)
