import unittest

from PIL import ImageColor
from asposebarcode.Generation import BarCodeImageFormat, BarcodeGenerator, EncodeTypes, FontStyle

from examples.utilities import ExampleAssist as ea

class BarcodeGeneratorExamples(unittest.TestCase):
    def test_generateBarcodeImageExample1(self):
        print("---\ngenerateBarcodeImageExample1")
        ea.set_license()
        encode_type = EncodeTypes.CODE_128
        generator = BarcodeGenerator(encode_type, None)
        generator.setCodeText("123ABC", None)
        path_to_save = ea.results_root + "code128_1.png"
        generator.save(path_to_save, BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def test_generateBarcodeImageExample2(self):
        print("---\ngenerateBarcodeImageExample2")
        ea.set_license()
        generator = BarcodeGenerator(EncodeTypes.CODABAR, "123456789")
        path_to_save = ea.results_root + "codabar.png"
        generator.save(path_to_save, BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def test_generateBarcodeImageExample3(self):
        print("---\ngenerateBarcodeImageExample3")
        ea.set_license()
        generator = BarcodeGenerator(EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ea.results_root + "datamatrix.png"
        image_base_64 = generator.generateBarCodeImage()
        print("Image was saved to " + path_to_save)

    def test_setBarcodeTypeExample(self):
        print("---\nsetBarcodeTypeExample")
        ea.set_license()
        generator = BarcodeGenerator(EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ea.results_root + "barcode_type.png"
        new_type = EncodeTypes.CODABAR
        generator.setBarcodeType(new_type)
        generator.save(path_to_save, BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def test_backColorExample(self):
            print("---\nbackColorExample")
            ea.set_license()
            back_color = ImageColor.getrgb("#FF0000")
            generator = BarcodeGenerator(EncodeTypes.CODE_39, '01234567')
            params = generator.getParameters()
            back_color_default = generator.getParameters().getBackColor()
            print("Default back color: " + str(back_color_default))
            params.setBackColor(back_color)
            back_color_actual = generator.getParameters().getBackColor()
            print('new back color: ' + str(back_color_actual))
            path_to_save = ea.results_root + "backColorExample.png"
            generator.save(path_to_save, BarCodeImageFormat.PNG)
            print("Image was saved to " + path_to_save)

    def test_barColorExample(self):
        print("---\nbarColorExample")
        bar_color = ImageColor.getrgb("#0000FF")
        generator = BarcodeGenerator(EncodeTypes.CODE_39, '01234567')
        bar_color_default = generator.getParameters().getBarcode().getBarColor()
        print("Default bar color: " + str(bar_color_default))
        generator.getParameters().getBarcode().setBarColor(bar_color)
        bar_color= generator.getParameters().getBarcode().getBarColor()
        print('new bar color: ' + str(bar_color))
        path_to_save = ea.results_root + "barColorExample.png"
        generator.save(path_to_save, BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def test_fontExample(self):
        print("---\nfontExample")
        generator = BarcodeGenerator(EncodeTypes.CODE_128, None)
        generator.getParameters().getCaptionAbove().setText("CAPTION ABOVE")
        generator.getParameters().getCaptionAbove().setVisible(True)
        generator.getParameters().getCaptionAbove().getFont().setStyle(FontStyle.ITALIC)
        generator.getParameters().getCaptionAbove().getFont().getSize().setPoint(5)
        generator.getParameters().getCaptionBelow().setText("CAPTION BELOW")
        generator.getParameters().getCaptionBelow().setVisible(True)
        generator.getParameters().getCaptionBelow().getFont().setStyle(FontStyle.BOLD)
        generator.getParameters().getCaptionBelow().getFont().getSize().setPixels(15)
        generator.getParameters().getCaptionAbove().getFont().setFamilyName("Verdana")
        path_to_save = ea.results_root + "fontExample.bmp"
        generator.save(path_to_save, BarCodeImageFormat.BMP)
        print("Image was saved to " + path_to_save)

if __name__ == '__main__':
    unittest.main()


