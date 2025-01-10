import sys
from pathlib import Path

class AutoImporter:
    def __init__(self, base_dir=None):
        """
        Constructor para la clase AutoImporter.
        :param base_dir: Ruta base desde donde buscar subdirectorios. Si no se especifica, se usa el directorio actual.
        """
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.add_to_sys_path()

    def add_to_sys_path(self):
        """
        Añade recursivamente todos los subdirectorios de base_dir a sys.path.
        """
        if not self.base_dir.is_dir():
            raise ValueError(f"La ruta base '{self.base_dir}' no es un directorio válido.")
        
        for subdir in self.base_dir.rglob("*"):
            if subdir.is_dir() and str(subdir) not in sys.path:
                sys.path.append(str(subdir))