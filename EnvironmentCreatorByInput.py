# CREATED BY: Matthew Maag
# Date: 8/14/2020

# Purpose: Runs through a JSON collection and pulls the requested APIs, and returns a new JSON collection

import sys, getopt, json

def main(argv):

    print("What is the name of the environment:")
    envName = input()
    envVarNames = []
    envVarValues = []
    enabledList = []
    cont = True
    while(cont):
        print("Enter the name of the environment variable: ")
        envVarNames.append(input())
        print("Enter the value of the environment variable: ")
        envVarValues.append(input())
        print("Type E if the variable is enabled, or press enter: ")
        if(input().upper() == "E"):
            enabledList.append(True)
        else:
            enabledList.append(False)
        print("Type X to finish, or press enter: ")
        if(input().upper() == "X"):
            cont = False
    
    output = {}
    output["name"] = envName
    output["values"] = []
    output["_postman_variable_scope"] = "environment"
    for i in range(len(envVarNames)):
        keyValuePair = {}
        keyValuePair["key"] = envVarNames[i]
        keyValuePair["value"] = envVarValues[i]
        keyValuePair["enabled"] = enabledList[i]
        output["values"].append(keyValuePair)

    # Writes the data out to the output file
    outputFile = envName + ".postman_environment.json"
    outputFileData = json.dumps(output)
    outputFileWriter = open(outputFile, "w")
    outputFileWriter.write(outputFileData)
    outputFileWriter.close()


    
if __name__ == "__main__":
    main(sys.argv[1:])