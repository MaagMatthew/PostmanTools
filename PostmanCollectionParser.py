# CREATED BY: Matthew Maag
# Date: 8/14/2020

# Purpose: Runs through a JSON collection and pulls the requested APIs, and returns a new JSON collection

import sys, getopt, json

def main(argv):
    inputFile = 'apis.txt'
    outputFile = 'output.json'
    jsonFile = 'AdvancedMD.Testing.AdvancedMD.Testing.API.Postman.HealthChecks.postman_collection.json'

    helpOut = """
    Postman Collection Parser takes a Postman collection JSON and returns a collection JSON with only the tests specified in
    a text file input.
    Example Input:
        -i  --ifile <inputfile>
        -j  --json <Postman Collection JSON>
        -o  --ofile <outputfile>
    """
    try:
        opts, args = getopt.getopt(argv, "hj:o:i:", ["ifile=","ofile=","json="])
    except getopt.GetoptError:
        print("Invalid input:\n", helpOut)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpOut)
            sys.exit(2)
        elif opt in ('-i', '--ifile'):
            inputFile = arg
        elif opt in ('-j', '--json'):
            jsonFile = arg    
        elif opt in ('-o', '--ofile'):
            outputFile = arg
    
    inFile = open(inputFile)
    inJSON = open(jsonFile)
    jsonData = json.loads(inJSON.read())
    inFileList = inFile.read().split("\n")
    nameList = jsonData["item"]
    output = {}
    output["info"] = jsonData["info"]
    output["event"] = jsonData["event"]
    output["variable"] = jsonData["variable"]
    output["protocolProfileBehavior"] = jsonData["protocolProfileBehavior"]
    output["item"] = []

    for file in inFileList:
        for i in range(len(nameList)):
            if(file == nameList[i]["name"]):
                output["item"].append(nameList[i])

    outputFileData = json.dumps(output)
    outputFileWriter = open(outputFile, "w")
    outputFileWriter.write(outputFileData)
    outputFileWriter.close()


    
if __name__ == "__main__":
    main(sys.argv[1:])