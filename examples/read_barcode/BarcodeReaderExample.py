import os
import unittest
from unittest.mock import Mock

from asposebarcode import Assist
from asposebarcode.Assist import Point
from asposebarcode.Generation import BarcodeGenerator, EncodeTypes, Unit
from asposebarcode.Recognition import BarCodeReader, DecodeType, QualitySettings, BarcodeQualityMode
from ..utilities import ExampleAssist as ta

class BarCodeReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # install the license once for the entire class of tests
        ta.setLicense()
        cls.image_path_code128 = os.path.join(ta.testdata_root, "Comments", "code128.jpg")
        cls.image_path_code39 = os.path.join(ta.testdata_root, "Comments", "code39.jpg")
        cls.xml_file1 = os.path.join(ta.testdata_root, "Comments", "test.xml")
        cls.xml_file2 = os.path.join(ta.testdata_root, "Wrong", "test.xml")

    def setUp(self):
        self.barcodeReader = BarCodeReader(self.__class__.image_path_code128,None, DecodeType.CODE_128)


    def test_exportToXml_raises_barcode_exception(self):
        self.assertTrue(self.barcodeReader.exportToXml(self.xml_file1))
        # check that the method raises BarcodeException when an exception occurs
        with self.assertRaises(Assist.BarCodeException) as context:
            self.barcodeReader.exportToXml(self.xml_file2)
        # Make sure the exception contains the original message
        self.assertIn("No such file or directory", str(context.exception))

    def test_importFromXml_raises_barcode_exception(self):
        self.assertTrue(self.barcodeReader.importFromXml(self.xml_file1))
        # check that the method raises BarcodeException when an exception occurs
        with self.assertRaises(Assist.BarCodeException) as context:
            self.barcodeReader.importFromXml(self.xml_file2)
        # Make sure the exception contains the original message
        self.assertIn("No such file or directory", str(context.exception))

    def testGetMaxQuality(self):
        qualitySettings = QualitySettings.getMaxQuality()
        self.assertEqual(qualitySettings.getBarcodeQuality(),BarcodeQualityMode.LOW)
        self.barcodeReader.setQualitySettings(qualitySettings)
        results = self.barcodeReader.readBarCodes()
        for result in results:
            self.assertEqual(result.getCodeTypeName(), "Code128")
            self.assertEqual(result.getCodeText(), "CODE128A")
