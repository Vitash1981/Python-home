import csv, json
parser = argparse.ArgumentParser()
parser.add_argument('-csv')
parser.add_argument('-json')
ns = parser.parse_args(sys.argv[1:])

csvFilePath = "user_details.csv"
jsonFilePath = "user_details.json"


data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    fieldnames = [0]
    for csvRow in csvReader:
         user_id = csvRow['user_id']
         data[user_id] = csvRow
         data[user_id]["password"] = "NULL"
         with open('jsonFilePath','w') as jsonFile:
            jsonFile.write(json.dumps(data, indent = 4))
