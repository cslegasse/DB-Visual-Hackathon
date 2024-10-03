# Import main classes or functions that should be available when importing the package
from .main_module import MainClass
from .utils import utility_function

# You can also define __all__ to specify what gets imported with "from package import *"
__all__ = ['MainClass', 'utility_function']

# Optionally, you can set the version of your package
__version__ = '0.1.0'

# You can also include any initialization code that needs to run when the package is imported
# For example:
# print("Initializing package")