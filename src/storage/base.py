from abc import ABC, abstractmethod


class StorageBackend(ABC):
    """存储抽象基类。"""

    @abstractmethod
    def save(self, name: str, content: bytes) -> str:
        """保存文件并返回文件路径或访问链接。"""
        pass

    @abstractmethod
    def read(self, name: str) -> bytes:
        """读取文件内容。"""
        pass

    @abstractmethod
    def exists(self, name: str) -> bool:
        """判断文件是否存在。"""
        pass
