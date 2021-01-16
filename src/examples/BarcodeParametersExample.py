from asposebarcode import Generation
import TestAssist as ta

class BarcodeParametersExample:
 def setParametersExample(self):
        print("---\nbarcodeParametersExample")
        ta.set_license()
        newCodeText = "UPDATED_NEW"
        barColor = "#0C3925"
        autoSizeMode = Generation.AutoSizeMode.NEAREST
        barCodeHeight = 91
        barCodeWidth = 133
        barHeight = 1
        barcodeGenerator = Generation.BarcodeGenerator(Generation.EncodeTypes.CODE_128, "1234567891")
        baseGenerationParameters = barcodeGenerator.getParameters()
        barcodeParameters = baseGenerationParameters.getBarcode()
        barcodeGenerator.setCodeText(newCodeText)
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
        path_to_save =  ta.results_root + "barcodeParametersExample.png"
        barcodeGenerator.save(path_to_save, "PNG")
        print("Image was saved to " + path_to_save)


barcodeParametersExample = BarcodeParametersExample()
barcodeParametersExample.setParametersExample()

