__version__ = "0.0.1"  # 与 pyproject.toml 中的版本保持一致

from .document import MdDocument
from .document import make_md

__all__ = [
    "MdDocument",
    "make_md",
    " __version__",
]
