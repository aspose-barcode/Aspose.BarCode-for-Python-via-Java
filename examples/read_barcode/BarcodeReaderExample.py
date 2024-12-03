import os
import unittest

from asposebarcode import Assist, Recognition
from asposebarcode.Generation import BarcodeGenerator, EncodeTypes
from asposebarcode.Recognition import BarCodeReader, DecodeType, QualitySettings, BarcodeQualityMode
from examples.utilities import ExampleAssist as ea

class BarCodeReaderExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # install the license once for the entire class of tests
        ea.set_license()
        cls.recognition_path_root = "../../resources/recognition/"
        cls.image_path_code128 = os.path.join(cls.recognition_path_root,  "code128.jpg")
        cls.image_path_code39 = os.path.join(cls.recognition_path_root,  "code39.jpg")
        cls.night_street_file_path = os.path.join(cls.recognition_path_root,"NightStreet.png")

    def testExampleAllSupportedTypes(self):
        file_path = self.recognition_path_root + "NightStreet.png"
        reader = Recognition.BarCodeReader(file_path, None, None)
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"CodeText = {result.getCodeText()}")
            
    def testExampleSetMaxQuality(self):
        reader = Recognition.BarCodeReader(self.night_street_file_path, None, None)
        reader.setQualitySettings(QualitySettings.getMaxQuality())
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"CodeText = {result.getCodeText()}")
            
    def testExampleSetNormalQuality(self):
        reader = Recognition.BarCodeReader(self.night_street_file_path, None, None)
        reader.setQualitySettings(QualitySettings.getNormalQuality())
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"CodeText = {result.getCodeText()}")
            
    def testExampleSetHighQuality(self):
        reader = Recognition.BarCodeReader(self.night_street_file_path, None, None)
        reader.setQualitySettings(QualitySettings.getHighQuality())
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"CodeText = {result.getCodeText()}")

    def testExampleSetHighPerformance(self):
        reader = Recognition.BarCodeReader(self.night_street_file_path, None, None)
        reader.setQualitySettings(QualitySettings.getHighPerformance())
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"CodeText = {result.getCodeText()}")

    def testExampleChecksumValidation(self):
        reader = Recognition.BarCodeReader(self.night_street_file_path, None, None)
        reader.getBarcodeSettings().setChecksumValidation(Recognition.ChecksumValidation.OFF)
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"CodeText = {result.getCodeText()}")

    def testExampleStripFNC(self):
        reader = Recognition.BarCodeReader(self.night_street_file_path, None, None)
        print(f"reader.getBarcodeSettings().getStripFNC() = {reader.getBarcodeSettings().getStripFNC()}")
        reader.getBarcodeSettings().setStripFNC(True)
        print(f"reader.getBarcodeSettings().getStripFNC() = {reader.getBarcodeSettings().getStripFNC()}")
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"CodeText = {result.getCodeText()}")

    def testExampleChecksum(self):
        file_path = os.path.join(self.recognition_path_root,"mzl.jpg")
        # checksum = "a"
        reader = Recognition.BarCodeReader(file_path, None, None)
        results = reader.readBarCodes()
        for result in results:
            print(f"CodeText = {result.getCodeText()}")
            print(f"CodeTypeName = {result.getCodeTypeName()}")
            print(f"checksum = {result.getExtended().getOneD().getCheckSum()}")


    def testExampleSetBarCodeImage(self):
        reader = Recognition.BarCodeReader(None, None,Recognition.DecodeType.ALL_SUPPORTED_TYPES)
        reader.setBarCodeImage(self.night_street_file_path, None)
        self.assertEqual("Code128", reader.readBarCodes()[0].getCodeTypeName())
        self.assertEqual("Night. Street. Lamp.", reader.readBarCodes()[0].getCodeText())

    def testExampleRecognitionSetBarCodeImageWithArea(self):
        file_path = os.path.join(self.recognition_path_root, "mzl.jpg")
        reader = Recognition.BarCodeReader(self.image_path_code128, None, Recognition.DecodeType.ALL_SUPPORTED_TYPES)
        rect1 = Assist.Rectangle(20, 210, 230, 120)
        reader.setBarCodeImage(file_path, rect1)
        results = reader.readBarCodes()
        for result in results:
            print(f"\nCodeText = {result.getCodeText()}")
            print(f"CodeTypeName = {result.getCodeTypeName()}")

    def testExampleRecognitionArea(self):
        rect1 = Assist.Rectangle(20, 210, 230, 120)
        rect2 = Assist.Rectangle(5, 2300, 240, 150)
        reader = Recognition.BarCodeReader(self.image_path_code128, [rect1, rect2], [Recognition.DecodeType.AZTEC, Recognition.DecodeType.AUSTRALIA_POST])
        results = reader.readBarCodes()
        for result in results:
            print(f"\nCodeText = {result.getCodeText()}")
            print(f"CodeTypeName = {result.getCodeTypeName()}")

    def testExampleRecognitionSetBarCodeImageWithAreas(self):
        file_path = os.path.join(self.recognition_path_root, "mzl.jpg")
        rect1 = Assist.Rectangle(30, 40, 260, 300)
        rect2 = Assist.Rectangle(480, 620, 190, 200)
        reader = Recognition.BarCodeReader(None, None, DecodeType.ALL_SUPPORTED_TYPES)
        reader.setBarCodeImage(file_path, [rect1, rect2])
        results = reader.readBarCodes()
        for result in results:
            print(f"\nCodeText = {result.getCodeText()}")
            print(f"CodeTypeName = {result.getCodeTypeName()}")

    def testExampleDetectEncodingEnabled(self):
        gen = BarcodeGenerator(EncodeTypes.QR, None)
        gen.setCodeText("Слово", None)
        image = gen.generateBarCodeImage()
        reader = Recognition.BarCodeReader(image, None, Recognition.DecodeType.QR)
        reader.getBarcodeSettings().setDetectEncoding(True)
        results = reader.readBarCodes()
        i = 0
        while (i < len(results)):
            print("\nCodeText:" + results[i].getCodeText())
            print()
            print("CodeType:" + results[i].getCodeTypeName())
            i += 1

    def testExampleCustomerInformationInterpretingType1(self):
        generator = BarcodeGenerator(EncodeTypes.AUSTRALIA_POST, None)
        generator.setCodeText("59123456781234567", None)
        generator.getParameters().getBarcode().getAustralianPost().setAustralianPostEncodingTable(
            Recognition.CustomerInformationInterpretingType.N_TABLE)
        image = generator.generateBarCodeImage()
        reader = Recognition.BarCodeReader(image, None, Recognition.DecodeType.AUSTRALIA_POST)
        reader.getBarcodeSettings().getAustraliaPost().setCustomerInformationInterpretingType(
            Recognition.CustomerInformationInterpretingType.N_TABLE)
        results = reader.readBarCodes()
        i = 0
        while (i < len(results)):
            print("\nCodeText:" + results[i].getCodeText())
            print()
            print("CodeType:" + results[i].getCodeTypeName())
            i += 1

    def testExampleCustomerInformationInterpretingType2(self):
        generator = BarcodeGenerator(EncodeTypes.AUSTRALIA_POST, None)
        generator.setCodeText("6212345678ABCdef123#", None)
        generator.getParameters().getBarcode().getAustralianPost().setAustralianPostEncodingTable(
            Recognition.CustomerInformationInterpretingType.C_TABLE)
        image = generator.generateBarCodeImage()
        reader = Recognition.BarCodeReader(image, None,
                                           [Recognition.DecodeType.AUSTRALIA_POST, Recognition.DecodeType.AZTEC])
        reader.getBarcodeSettings().getAustraliaPost().setCustomerInformationInterpretingType(
            Recognition.CustomerInformationInterpretingType.C_TABLE)
        results = reader.readBarCodes()
        i = 0
        while (i < len(results)):
            print("\nCodeText:" + results[i].getCodeText())
            print()
            print("CodeType:" + results[i].getCodeTypeName())
            self.assertEqual(results[i].getCodeText(), "6212345678ABCdef123#")
            self.assertEqual("AustraliaPost", results[i].getCodeTypeName())
            i += 1
