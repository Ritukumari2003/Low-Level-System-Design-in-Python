from csv_parser import CSVParser
from json_parser import JSONParser

json_parser = JSONParser()
json_parser._parse()
print()
csv_parser = CSVParser()
csv_parser._parse()