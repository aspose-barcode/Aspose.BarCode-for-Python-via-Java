from asposebarcode import Recognition
import ExampleAssist as ta

class BarcodeReaderExamples():
    def allSupportedTypesExample(self):
        print("\n----\nallSupportedTypesExample")
        ta.set_license()
        full_path = ta.test_data_root + "code128-example-1.jpg"
        image_data_base64 = ta.load_image_base64_from_path(full_path)
        reader = Recognition.BarcodeReader(image_data_base64, None, None)
        recognized_results = reader.readBarCodes()
        for x in recognized_results:
            print(x.getCodeText())
            print(x.getCodeTypeName())

    def setQualitySettingsExample1(self):
        print("\n----\nsetQualitySettingsExample1")
        ta.set_license()
        full_path = ta.test_data_root + "code128-example-2.png"
        reader = Recognition.BarcodeReader(full_path, None, None)
        reader.setQualitySettings(Recognition.QualitySettings.getHighPerformance())
        reader.getQualitySettings().setAllowMedianSmoothing(True)
        reader.getQualitySettings().setMedianSmoothingWindowSize(5)
        results = reader.readBarCodes()
        i = 0
        while (i < len(results)):
            print(i)
            print("code text: " + results[i].getCodeText())
            print("code type: " +  results[i].getCodeTypeName())
            i += 1

    def setQualitySettingsExample2(self):
        print("\n----\nsetQualitySettingsExample2")
        ta.set_license()
        full_path = ta.test_data_root + "datamatrix-example-1.png"
        reader = Recognition.BarcodeReader(full_path, None, None)
        reader.setQualitySettings(Recognition.QualitySettings.getNormalQuality())
        results = reader.readBarCodes()
        i = 0
        while (i < len(results)):
            print(i)
            print("code text: " + results[i].getCodeText())
            print("code type: " + results[i].getCodeTypeName())
            i += 1

    def setQualitySettingsExample3(self):
            print("\n----\nsetQualitySettingsExample3")
            ta.set_license()
            full_path = ta.test_data_root + "barcodes-document-example-1.jpg"
            reader = Recognition.BarcodeReader(full_path, None, None)
            reader.setQualitySettings(Recognition.QualitySettings.getHighQuality())
            results = reader.readBarCodes()
            i = 0
            while (i < len(results)):
                print(i)
                print("code text: " + results[i].getCodeText())
                print("code type: " + results[i].getCodeTypeName())
                i += 1

    def setQualitySettingsExample4(self):
                print("setQualitySettingsExample4")
                ta.set_license()
                full_path = ta.test_data_root + "barcodes-document-example-2.jpg"
                reader = Recognition.BarcodeReader(full_path, None, None)
                reader.setQualitySettings(Recognition.QualitySettings.getHighPerformance())
                results = reader.readBarCodes()
                i = 0
                while (i < len(results)):
                    print(i)
                    print("code text: " + results[i].getCodeText())
                    print("code type: " + results[i].getCodeTypeName(), "\n\n")
                    i += 1




barcodeReaderExamples = BarcodeReaderExamples()
barcodeReaderExamples.allSupportedTypesExample()
barcodeReaderExamples.setQualitySettingsExample1()
barcodeReaderExamples.setQualitySettingsExample2()
barcodeReaderExamples.setQualitySettingsExample3()
barcodeReaderExamples.setQualitySettingsExample4()

