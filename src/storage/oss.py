from src.storage.base import StorageBackend


class AliyunOssStorage(StorageBackend):
    """阿里云 OSS 对象存储驱动模拟实现。"""

    def __init__(self, bucket_name: str = "demo-bucket", endpoint: str = "oss-cn-hangzhou.aliyuncs.com"):
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self._mock_cloud_store: dict[str, bytes] = {}

    def save(self, name: str, content: bytes) -> str:
        self._mock_cloud_store[name] = content
        return f"https://{self.bucket_name}.{self.endpoint}/{name}"

    def read(self, name: str) -> bytes:
        if name not in self._mock_cloud_store:
            raise FileNotFoundError(f"OSS 中不存在文件: {name}")
        return self._mock_cloud_store[name]

    def exists(self, name: str) -> bool:
        return name in self._mock_cloud_store
