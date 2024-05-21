# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"H52y000","system":"readv2"},{"code":"14B5.00","system":"readv2"},{"code":"H52..00","system":"readv2"},{"code":"H52y100","system":"readv2"},{"code":"H52z.00","system":"readv2"},{"code":"98427.0","system":"readv2"},{"code":"2486.0","system":"readv2"},{"code":"36017.0","system":"readv2"},{"code":"27821.0","system":"readv2"},{"code":"9101.0","system":"readv2"},{"code":"1550.0","system":"readv2"},{"code":"5131.0","system":"readv2"},{"code":"53808.0","system":"readv2"},{"code":"23766.0","system":"readv2"},{"code":"70492.0","system":"readv2"},{"code":"28695.0","system":"readv2"},{"code":"J93","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pneumothorax-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pneumothorax---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pneumothorax---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pneumothorax---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
