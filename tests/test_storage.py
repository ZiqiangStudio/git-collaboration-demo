import tempfile

import pytest

from src.storage.local import LocalStorage


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
