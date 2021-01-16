from asposebarcode import Generation

import TestAssist as ta

class BarcodeGeneratorExamples():
    def generateBarcodeImageExample1(self):
        print("---\ngenerateBarcodeImageExample1")
        ta.set_license()
        encode_type = Generation.EncodeTypes.CODE_128
        generator = Generation.BarcodeGenerator(encode_type, None)
        generator.setCodeText("123ABC")
        path_to_save = ta.results_root + "code128_1.png"
        generator.save(path_to_save, "PNG")
        print("Image was saved to " + path_to_save)

    def generateBarcodeImageExample2(self):
        print("---\ngenerateBarcodeImageExample2")
        ta.set_license()
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODABAR, "123456789")
        path_to_save = ta.results_root + "codabar.png"
        generator.save(path_to_save, "PNG")
        print("Image was saved to " + path_to_save)

    def generateBarcodeImageExample3(self):
        print("---\ngenerateBarcodeImageExample3")
        ta.set_license()
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ta.results_root + "datamatrix.png"
        image_base_64 = generator.generateBarcodeImage("PNG")
        print("Image was saved to " + path_to_save)

    def setBarcodeTypeExample(self):
        print("---\nsetBarcodeTypeExample")
        ta.set_license()
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ta.results_root + "barcode_type.png"
        new_type = Generation.EncodeTypes.CODABAR
        generator.setBarcodeType(new_type)
        generator.save(path_to_save, "PNG")
        print("Image was saved to " + path_to_save)

    def backColorExample(self):
            print("---\nbackColorExample")
            ta.set_license()
            back_color = "#FF0000"
            generator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODE_39_STANDARD, '01234567')
            params = generator.getParameters()
            back_color_default = generator.getParameters().getBackColor()
            print("Default back color: " + str(back_color_default))
            params.setBackColor(back_color)
            back_color_actual = generator.getParameters().getBackColor()
            print('new back color: ' + str(back_color_actual))
            path_to_save = ta.results_root + "backColorExample.png"
            generator.save(path_to_save, "PNG")
            print("Image was saved to " + path_to_save)

    def barColorExample(self):
        print("---\nbarColorExample")
        bar_color = "#0000FF"
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODE_39_STANDARD, '01234567')
        bar_color_default = generator.getParameters().getBarcode().getBarColor()
        print("Default bar color: " + str(bar_color_default))
        generator.getParameters().getBarcode().setBarColor(bar_color)
        bar_color= generator.getParameters().getBarcode().getBarColor()
        print('new bar color: ' + str(bar_color))
        path_to_save = ta.results_root + "barColorExample.png"
        generator.save(path_to_save, "PNG")
        print("Image was saved to " + path_to_save)

    def fontExample(self):
        print("---\nfontExample")
        generator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODE_128, None)
        generator.getParameters().getCaptionAbove().setText("CAPTION ABOVE")
        generator.getParameters().getCaptionAbove().setVisible(True)
        generator.getParameters().getCaptionAbove().getFont().setStyle(Generation.FontStyle.ITALIC)
        generator.getParameters().getCaptionAbove().getFont().getSize().setPoint(5)
        generator.getParameters().getCaptionBelow().setText("CAPTION BELOW")
        generator.getParameters().getCaptionBelow().setVisible(True)
        generator.getParameters().getCaptionBelow().getFont().setStyle(Generation.FontStyle.BOLD)
        generator.getParameters().getCaptionBelow().getFont().getSize().setPixels(15)
        generator.getParameters().getCaptionAbove().getFont().setFamilyName("Verdana")
        path_to_save = ta.results_root + "fontExample.bmp"
        generator.save(path_to_save, "BMP")
        print("Image was saved to " + path_to_save)

barcodeGeneratorExamples = BarcodeGeneratorExamples()
barcodeGeneratorExamples.generateBarcodeImageExample1()
barcodeGeneratorExamples.generateBarcodeImageExample2()
barcodeGeneratorExamples.generateBarcodeImageExample3()
barcodeGeneratorExamples.setBarcodeTypeExample()
barcodeGeneratorExamples.backColorExample()
barcodeGeneratorExamples.barColorExample()
barcodeGeneratorExamples.fontExample()
