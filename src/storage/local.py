from pathlib import Path

from src.storage.base import StorageBackend


class LocalStorage(StorageBackend):
    """本地文件系统存储驱动。"""

    def __init__(self, root_dir: str = "/tmp/demo_storage"):
        self.root = Path(root_dir)
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, name: str, content: bytes) -> str:
        target = self.root / name
        target.write_bytes(content)
        return str(target)

    def read(self, name: str) -> bytes:
        target = self.root / name
        if not target.exists():
            raise FileNotFoundError(f"文件不存在: {name}")
        return target.read_bytes()

    def exists(self, name: str) -> bool:
        return (self.root / name).exists()
