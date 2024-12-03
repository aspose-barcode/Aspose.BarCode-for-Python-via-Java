import os
import unittest
import jpype
from io import BytesIO

import pytest
from PIL import Image
from asposebarcode import ComplexBarcode, Assist
from asposebarcode.ComplexBarcode import ComplexBarcodeGenerator
from asposebarcode.Generation import BarCodeImageFormat

from testassist import TestAssist as ta

# Assuming you already have a working JPype setup
class ComplexBarcodeGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ta.setLicense()
        cls.image_path_to_save1 = os.path.join(ta.testdata_root, "Comments", "image_to_save1.png")


    def setUp(self):
        swissQRCodetext = ComplexBarcode.SwissQRCodetext(None)
        swissQRCodetext.getBill().setAccount("CH450023023099999999A")
        swissQRCodetext.getBill().getCreditor().setName("Name")
        swissQRCodetext.getBill().getCreditor().setCountryCode("NL")
        swissQRCodetext.getBill().setBillInformation("BillInformation")
        self.complexBarcodeGenerator = ComplexBarcodeGenerator(swissQRCodetext)


    # @unittest.skip(reason="in developing")
    def test_generator_initialization(self):
        """Test that the ComplexBarcodeGenerator is initialized correctly."""
        with self.assertRaises(Assist.BarCodeException) as context:
            generator = ComplexBarcodeGenerator(ComplexBarcode.SwissQRCodetext(None))
        self.assertIn("IBAN", str(context.exception))

    # @unittest.skip(reason="in developing")
    def test_generate_barcode_image(self):
        """Test the barcode generation method."""
        image = self.complexBarcodeGenerator.generateBarCodeImage()
        self.assertIsInstance(image, Image.Image)

    # TODO BARCODEPYTHON-613 The 'save' method in the ComplexBarcodeGenerator class should accept both str and BytesIO types
    def test_save_image1(self):
        # Save the image in memory (BytesIO) instead of disk for test purposes
        image_source = BytesIO()
        output_file_path = os.path.join(ta.testdata_root, "Comments", "image_to_save2.png")
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        self.assertFalse(os.path.exists(output_file_path), "Output file still exists before test starts.")

        self.complexBarcodeGenerator.save(image_source, BarCodeImageFormat.PNG)
        image_source.seek(0)
        img = Image.open(image_source)
        self.assertIsInstance(img, Image.Image)
        img.save(output_file_path, format="PNG")
        self.assertTrue(os.path.exists(output_file_path))

    def test_save_image_incorrect(self):
        """Test that an exception is raised when the imageSource is invalid."""
        with self.assertRaises(ValueError) as context:
            image_source = 34567 #incorrect image_source
            self.complexBarcodeGenerator.save(image_source, BarCodeImageFormat.PNG)
        self.assertEqual(str(context.exception),"Parameter imageSource must be a string path or a BytesIO object.")

    def test_save_image_to_file(self):
        output_file_path = os.path.join(ta.testdata_root, "Comments", "image_to_save3.png")
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        self.assertFalse(os.path.exists(output_file_path), "Output file still exists before test starts.")
        self.complexBarcodeGenerator.save(output_file_path, BarCodeImageFormat.PNG)
        self.assertTrue(os.path.exists(output_file_path))

if __name__ == '__main__':
    unittest.main()
