import unittest

from asposebarcode import Generation
from asposebarcode.Generation import BarCodeImageFormat

from examples.utilities import ExampleAssist as ea

class BarcodeParametersExample(unittest.TestCase):

 def testSetParameters(self):
        print("---\ntestSetParameters")
        ea.set_license()
        newCodeText = "UPDATED_NEW"
        barColor = (255, 0, 0)
        autoSizeMode = Generation.AutoSizeMode.NEAREST
        barCodeHeight = 91
        barCodeWidth = 133
        barHeight = 1
        barcodeGenerator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODE_128, "1234567891")
        baseGenerationParameters = barcodeGenerator.getParameters()
        barcodeParameters = baseGenerationParameters.getBarcode()
        barcodeGenerator.setCodeText(newCodeText,"UTF-8")
        print("codeText: " + str(barcodeGenerator.getCodeText()))
        barcodeParameters.setBarColor(barColor)
        print("barColor: " + str(barcodeParameters.getBarColor()))
        baseGenerationParameters.setAutoSizeMode(autoSizeMode)
        print("autoSizeMode: " + str(baseGenerationParameters.getAutoSizeMode()))
        baseGenerationParameters.getImageHeight().setMillimeters(barCodeHeight)
        print("barCodeHeight: " + str(baseGenerationParameters.getImageHeight().getMillimeters()))
        baseGenerationParameters.getImageWidth().setMillimeters(barCodeWidth)
        print("barCodeWidth: " + str(baseGenerationParameters.getImageWidth().getMillimeters()))
        barcodeParameters.getBarHeight().setMillimeters(barHeight)
        print("barHeight: " + str(barcodeParameters.getBarHeight().getMillimeters()))
        path_to_save =  ea.results_root + "barcode_parameters_example.png"
        barcodeGenerator.save(path_to_save, BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

