import os
import unittest
from io import BytesIO
from PIL import Image
from asposebarcode import ComplexBarcode, Assist
from asposebarcode.ComplexBarcode import ComplexBarcodeGenerator
from asposebarcode.Generation import BarCodeImageFormat
from examples.utilities import ExampleAssist as ea

# Assuming you already have a working JPype setup
class ComplexBarcodeGeneratorExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ea.set_license()

    def setUp(self):
        swissQRCodetext = ComplexBarcode.SwissQRCodetext(None)
        swissQRCodetext.getBill().setAccount("CH450023023099999999A")
        swissQRCodetext.getBill().getCreditor().setName("Name")
        swissQRCodetext.getBill().getCreditor().setCountryCode("NL")
        swissQRCodetext.getBill().setBillInformation("BillInformation")
        self.complexBarcodeGenerator = ComplexBarcodeGenerator(swissQRCodetext)


    def test_save_image(self):
        # Save the image in memory (BytesIO) instead of disk
        image_source = BytesIO()
        output_file_path = os.path.join(ea.results_root ,"image_to_save1.png")
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
        """Exception is raised when the imageSource is invalid."""
        with self.assertRaises(ValueError) as context:
            image_source = 34567 #incorrect image_source
            self.complexBarcodeGenerator.save(image_source, BarCodeImageFormat.PNG)
        self.assertEqual(str(context.exception),"Parameter imageSource must be a string path or a BytesIO object.")

    def test_save_image_to_file(self):
        output_file_path = os.path.join(ea.results_root, "image_to_save2.png")
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        self.assertFalse(os.path.exists(output_file_path), "Output file still exists before test starts.")
        self.complexBarcodeGenerator.save(output_file_path, BarCodeImageFormat.PNG)
        self.assertTrue(os.path.exists(output_file_path))

if __name__ == '__main__':
    unittest.main()
