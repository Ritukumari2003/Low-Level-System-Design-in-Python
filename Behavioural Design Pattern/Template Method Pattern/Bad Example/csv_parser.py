# Problem : Repetition of same methods again and again 

class CSVParser:
    def parse(self):
        self.openFile()

        # Specific logic/code for parsing the file 
        print("Parsing the CSV file..")

        self.closeFile()

    def openFile(self):
        print("Opening the file")
    
    def closeFile(self):
        print("Closing the file")

class JSONParser:
    def parse(self):
        self.openFile()

        # Specific logic/code for parsing the file 
        print("Parsing the JSON file..")

        self.closeFile()

    def openFile(self):
        print("Opening the file")
    
    def closeFile(self):
        print("Closing the file")

csvparser = CSVParser()
csvparser.parse()

jsonparser = JSONParser()
jsonparser.parse()