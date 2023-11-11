#!/usr/bin/python3
"""__init__ majic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
