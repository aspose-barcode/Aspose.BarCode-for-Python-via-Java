import os
import base64
from asposebarcode import Assist

pythonLicensePath = "../resources/license/Aspose.BarCode.Python.Java-1.lic"
results_root = "../resources/generated/"
test_data_root = "../resources/input/"

def set_license():
    if (os.path.exists(pythonLicensePath)):
        try:
            license = Assist.License()
            license.setLicense(pythonLicensePath)
        except:
            print("Exception occurred\nLicense was not installed.")
    else:
            print("Path " + pythonLicensePath + " is not correct\nLicense was not installed.")


def save_image(base_64_str, path):
    try:
        print("Will be saved to : " + path)
        f = open(path, 'wb+')
        image_bytes = base64.b64decode(base_64_str)
        f.write(image_bytes)
        f.close()
        return os.path.exists(path)
    except Exception as ex:
        print('Failed to upload to ftp: ' + str(ex))


def check_path(path):
    if (is_exists(path)):
        print("Path " + path + " exists")
    else:
        print("Path " + path + " doesn't exist")

def is_exists(file_path):
    if (os.path.exists(file_path)):
        return True
    else:
        return False


def load_image_base64_from_path(filePath):
    try:
        image_file = open(filePath, "rb")
        image_data_binary = image_file.read()
        return (base64.b64encode(image_data_binary)).decode('ascii')
    except Exception as ex:
        print('Failed to upload to ftp: ' + str(ex))


