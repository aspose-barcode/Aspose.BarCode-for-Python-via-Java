import unittest
from datetime import datetime

from asposebarcode import Recognition, Generation, Assist
from examples.utilities import ExampleAssist as ea


class BarcodeResultExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ea.set_license()

    def testBarcodeResultsParameters(self):
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.DATABAR_EXPANDED, "12345678")
        reader = Recognition.BarCodeReader(generator.generateBarCodeImage(), None, Recognition.DecodeType.DATABAR_EXPANDED)
        results = reader.readBarCodes()
        self.assertTrue(len(results) > 0)

        ReadingQuality = results[0].getReadingQuality()
        self.assertTrue(abs(99.99 - ReadingQuality) < 0.01)

        Confidence = results[0].getConfidence()
        self.assertEqual(Confidence, Recognition.BarCodeConfidence.MODERATE)

        CodeBytes = results[0].getCodeBytes()
        self.assertEqual(CodeBytes, ["40", "49", "50", "41", "51", "52", "53", "54", "55", "56"])

        CodeType = results[0].getCodeType()
        self.assertEqual(CodeType, Recognition.DecodeType.DATABAR_EXPANDED)

        CodeTypeName = results[0].getCodeTypeName()
        self.assertEqual(CodeTypeName, "DatabarExpanded")

    def testBarCodeRegionParameters(self):
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.DATABAR_EXPANDED, "12345678")
        reader = Recognition.BarCodeReader(generator.generateBarCodeImage(), None, Recognition.DecodeType.DATABAR_EXPANDED)
        results = reader.readBarCodes()
        self.assertTrue(len(results) > 0)

        Quadrangle = results[0].getRegion().getQuadrangle()
        self.assertTrue(Quadrangle.getLeftTop().__eq__(Assist.Point(11, 7)))
        self.assertTrue(Quadrangle.getRightTop().__eq__(Assist.Point(206, 7)))
        self.assertTrue(Quadrangle.getRightBottom().__eq__(Assist.Point(206, 63)))
        self.assertTrue(Quadrangle.getLeftBottom().__eq__(Assist.Point(11, 63)))

        Angle = results[0].getRegion().getAngle()
        self.assertEqual(Angle, 0)

        Points = results[0].getRegion().getPoints()
        self.assertTrue(Points[0].__eq__(Assist.Point(11, 7)))
        self.assertTrue(Points[1].__eq__(Assist.Point(206, 7)))
        self.assertTrue(Points[2].__eq__(Assist.Point(206, 63)))
        self.assertTrue(Points[3].__eq__(Assist.Point(11, 63)))

        Rectangle = results[0].getRegion().getRectangle()
        self.assertEqual(Rectangle.getX(), 11)
        self.assertEqual(Rectangle.getY(),7)
        self.assertEqual(Rectangle.getWidth(), 196)
        self.assertEqual(Rectangle.getHeight(), 57)


    def testDataBarExtendedParameters(self):
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.DATABAR_EXPANDED, "12345678")
        reader = Recognition.BarCodeReader(generator.generateBarCodeImage(), None, Recognition.DecodeType.DATABAR_EXPANDED)
        results = reader.readBarCodes()
        self.assertTrue(len(results) > 0)

        is2DCompositeComponent = results[0].getExtended().getDataBar().is2DCompositeComponent()
        self.assertFalse(is2DCompositeComponent)

        is2DCompositeComponent = results[0].getExtended().getDataBar().is2DCompositeComponent()
        self.assertFalse(is2DCompositeComponent)

    def testOneDParameters(self):
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODE_39, "12345678")
        reader = Recognition.BarCodeReader(generator.generateBarCodeImage(), None, Recognition.DecodeType.CODE_39)
        results = reader.readBarCodes()
        self.assertTrue(len(results) > 0)

        value = results[0].getExtended().getOneD().getValue()
        expectedValue = "12345678"
        self.assertEqual(expectedValue, value)

        checkSum = results[0].getExtended().getOneD().getCheckSum()
        expectedCheckSum = ""
        self.assertEqual(expectedCheckSum, checkSum)

        isEmpty = results[0].getExtended().getOneD().isEmpty()
        self.assertFalse(isEmpty)

    def testCode128ExtendedParameters(self):
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODE_128, "12345")
        reader = Recognition.BarCodeReader(generator.generateBarCodeImage(), None, Recognition.DecodeType.CODE_128)
        results = reader.readBarCodes()
        self.assertTrue(len(results) > 0)

        code128DataPortions = results[0].getExtended().getCode128().getCode128DataPortions()
        self.assertTrue(len(code128DataPortions) == 2)

        isEmpty = results[0].getExtended().getCode128().isEmpty()
        self.assertFalse(isEmpty)

    def testQRExtendedParameters(self):
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.QR, "12345")
        generator.getParameters().getBarcode().getQR().getStructuredAppend().setParityByte(1)
        generator.getParameters().getBarcode().getQR().getStructuredAppend().setSequenceIndicator(2)
        generator.getParameters().getBarcode().getQR().getStructuredAppend().setTotalCount(3)
        reader = Recognition.BarCodeReader(generator.generateBarCodeImage(), None, Recognition.DecodeType.QR)
        results = reader.readBarCodes()
        self.assertTrue(len(results) > 0)

        QRStructuredAppendModeBarCodesQuantity = results[0].getExtended().getQR().getQRStructuredAppendModeBarCodesQuantity()
        self.assertEqual(QRStructuredAppendModeBarCodesQuantity, 3)

        QRStructuredAppendModeBarCodeIndex = results[0].getExtended().getQR().getQRStructuredAppendModeBarCodeIndex()
        self.assertEqual(QRStructuredAppendModeBarCodeIndex, 2)

        QRStructuredAppendModeParityData = results[0].getExtended().getQR().getQRStructuredAppendModeParityData()
        self.assertEqual(QRStructuredAppendModeParityData, 1)

        isEmpty = results[0].getExtended().getQR().isEmpty()
        self.assertFalse(isEmpty)

    def testPdf417ExtendedParameters(self):
        expectedDate = datetime.fromisoformat('2021-02-01')
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.MACRO_PDF_417, "12345")
        pdf417Parameters = generator.getParameters().getBarcode().getPdf417()
        pdf417Parameters.setPdf417MacroAddressee("ABC")
        pdf417Parameters.setPdf417MacroFileName("ZYX")
        pdf417Parameters.setPdf417MacroFileID(7)
        pdf417Parameters.setPdf417MacroSegmentID(6)
        pdf417Parameters.setPdf417MacroSegmentsCount(5)
        pdf417Parameters.setPdf417MacroChecksum(4)
        pdf417Parameters.setPdf417MacroSender("KLM")
        pdf417Parameters.setPdf417MacroTimeStamp(expectedDate)
        pdf417Parameters.setPdf417MacroFileSize(99)
        reader = Recognition.BarCodeReader(generator.generateBarCodeImage(), None, Recognition.DecodeType.MACRO_PDF_417)
        results = reader.readBarCodes()
        self.assertTrue(len(results) > 0)

        MacroPdf417FileID = results[0].getExtended().getPdf417().getMacroPdf417FileID()
        self.assertEqual(MacroPdf417FileID, "7")

        MacroPdf417SegmentID = results[0].getExtended().getPdf417().getMacroPdf417SegmentID()
        self.assertEqual(MacroPdf417SegmentID, 6)

        MacroPdf417SegmentsCount = results[0].getExtended().getPdf417().getMacroPdf417SegmentsCount()
        self.assertEqual(MacroPdf417SegmentsCount, 5)

        MacroPdf417FileName = results[0].getExtended().getPdf417().getMacroPdf417FileName()
        self.assertEqual(MacroPdf417FileName, "ZYX")

        MacroPdf417FileSize = results[0].getExtended().getPdf417().getMacroPdf417FileSize()
        self.assertEqual(MacroPdf417FileSize, 99)

        MacroPdf417Sender = results[0].getExtended().getPdf417().getMacroPdf417Sender()
        self.assertEqual(MacroPdf417Sender, "KLM")

        MacroPdf417Addressee = results[0].getExtended().getPdf417().getMacroPdf417Addressee()
        self.assertEqual(MacroPdf417Addressee, "ABC")

        MacroPdf417TimeStamp = results[0].getExtended().getPdf417().getMacroPdf417TimeStamp()
        self.assertEqual(MacroPdf417TimeStamp.timetuple(), expectedDate.timetuple())

        MacroPdf417Checksum = results[0].getExtended().getPdf417().getMacroPdf417Checksum()
        self.assertEqual(MacroPdf417Checksum, 4)