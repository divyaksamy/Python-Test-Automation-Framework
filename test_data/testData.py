import utilities.read_json as RJ
import os


def testData(attribute):
    testDataPath = os.path.abspath("/Users/karthickdhivya/Documents/GitHub/Python-Test-Automation-Framework/test_data/test_data.json")
    testDataJsonFile = RJ.readJson(testDataPath)
    return testDataJsonFile[attribute]