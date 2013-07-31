# -*- encoding: utf-8 -*-
import unittest
import os
import logging
import tempfile

logging.basicConfig(level=logging.DEBUG)

import camlipy
from camlipy import Camlistore, compute_hash

camlipy.DEBUG = True
CAMLIPY_SERVER = os.environ.get('CAMLIPY_SERVER', 'http://localhost:3179/')


class CamliPyTestCase(unittest.TestCase):
    def setUp(self):
        self.server = Camlistore(CAMLIPY_SERVER)

    def testPutBlobStr(self):
        test_blob_str = os.urandom(4096)
        resp = self.server.put_blobs([test_blob_str])
        self.assertEqual(resp['received'], [{'blobRef': compute_hash(test_blob_str), 'size': 4096}])

    def testPutBlobFileobj(self):
        test_blob_file = tempfile.TemporaryFile()
        test_blob_file.write(os.urandom(4096))
        test_blob_file.seek(0)

        resp = self.server.put_blobs([test_blob_file])
        test_blob_file.seek(0)
        self.assertEqual(resp['received'], [{'blobRef': compute_hash(test_blob_file.read()), 'size': 4096}])

    def testGetBlob(self):
        data_len = (1024 << 10) + (4 << 10)
        blob_data = os.urandom(data_len)
        blob_br = compute_hash(blob_data)
        self.server.put_blobs([blob_data])

        fileobj = self.server.get_blob(blob_br)
        self.assertTrue(isinstance(fileobj, tempfile.SpooledTemporaryFile))
        self.assertEqual(len(fileobj.read()), data_len)
        fileobj.seek(0)
        self.assertEqual(fileobj.read(), blob_data)

    def testGetBlobSchema(self):
        pass

if __name__ == '__main__':
    unittest.main()
