import tempfile

import pytest

from src.storage.local import LocalStorage
from src.storage.oss import AliyunOssStorage


def test_local_storage_lifecycle():
    with tempfile.TemporaryDirectory() as tmpdir:
        storage = LocalStorage(root_dir=tmpdir)
        filename = "test.txt"
        data = b"Hello Ziqiang Studio"

        assert not storage.exists(filename)
        path = storage.save(filename, data)
        assert storage.exists(filename)
        assert storage.read(filename) == data
        assert filename in path


def test_local_storage_file_not_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        storage = LocalStorage(root_dir=tmpdir)
        with pytest.raises(FileNotFoundError):
            storage.read("non_existent.txt")


def test_aliyun_oss_storage():
    oss = AliyunOssStorage(bucket_name="zq-test-bucket")
    filename = "report.csv"
    payload = b"id,name,score\n1,alice,100"

    assert not oss.exists(filename)
    url = oss.save(filename, payload)
    assert oss.exists(filename)
    assert url == "https://zq-test-bucket.oss-cn-hangzhou.aliyuncs.com/report.csv"
    assert oss.read(filename) == payload

    with pytest.raises(FileNotFoundError):
        oss.read("unknown.csv")
