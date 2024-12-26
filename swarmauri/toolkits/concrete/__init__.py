import importlib

# Define a lazy loader function with a warning message if the module or class is not found
def _lazy_import(module_name, class_name):
    try:
        # Import the module
        module = importlib.import_module(module_name)
        # Dynamically get the class from the module
        return getattr(module, class_name)
    except ImportError:
        # If module is not available, print a warning message
        print(f"Warning: The module '{module_name}' is not available. "
              f"Please install the necessary dependencies to enable this functionality.")
        return None
    except AttributeError:
        # If class is not found, print a warning message
        print(f"Warning: The class '{class_name}' was not found in module '{module_name}'.")
        return None

# List of toolkit names (file names without the ".py" extension) and corresponding class names
toolkit_files = [
    ("swarmauri.toolkits.concrete.AccessibilityToolkit", "AccessibilityToolkit"),
    ("swarmauri.toolkits.concrete.Toolkit", "Toolkit"),
]

# Lazy loading of toolkit modules, storing them in variables
for module_name, class_name in toolkit_files:
    globals()[class_name] = _lazy_import(module_name, class_name)

# Adding the lazy-loaded toolkit modules to __all__
__all__ = [class_name for _, class_name in toolkit_files]
