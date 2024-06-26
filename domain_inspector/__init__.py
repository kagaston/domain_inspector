import importlib
import os
import pkgutil

package_dir = os.path.dirname(__file__)
for _, module_name, _ in pkgutil.iter_modules([package_dir]):
    module = importlib.import_module(f"{__name__}.{module_name}")
    for attr in dir(module):
        if not attr.startswith("_"):
            globals()[attr] = getattr(module, attr)
