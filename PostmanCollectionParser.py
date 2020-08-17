# CREATED BY: Matthew Maag
# Date: 8/14/2020

# Purpose: Runs through a JSON collection and pulls the requested APIs, and returns a new JSON collection

import sys, getopt, json

def main(argv):
    # Default File Names
    inputFile = 'apis.txt'
    outputFile = 'output.json'
    jsonFile = 'postman_collection.json'

    # Help Message in case something gets messed up, or if they request help messages.
    helpOut = """
    Postman Collection Parser takes a Postman collection JSON and returns a collection JSON with only the tests specified in
    a text file input.
    Example Input:
        -i  --ifile <inputfile>
        -j  --json <Postman Collection JSON>
        -o  --ofile <outputfile>
    """

    #Gets the values of each Command Line argument
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
    
    # Gets the data from those files
    inFile = open(inputFile)
    inJSON = open(jsonFile)
    jsonData = json.loads(inJSON.read())
    inFileList = inFile.read().split("\n")
    nameList = jsonData["item"]
    output = {}

    # Gets the header information
    output["info"] = jsonData["info"]
    output["item"] = []

    for file in inFileList:
        for i in range(len(nameList)):
            if(file == nameList[i]["name"]):
                output["item"].append(nameList[i])

    # Gets the footer information
    output["event"] = jsonData["event"]
    output["variable"] = jsonData["variable"]
    output["protocolProfileBehavior"] = jsonData["protocolProfileBehavior"]

    # Writes the data out to the output file
    outputFileData = json.dumps(output)
    outputFileWriter = open(outputFile, "w")
    outputFileWriter.write(outputFileData)
    outputFileWriter.close()


    
if __name__ == "__main__":
    main(sys.argv[1:])