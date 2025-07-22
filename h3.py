import sys
import argparse
import re


class Server:

    def __init__(self, path):      
        self.emails = []
        myline = open(str(path), "r", encoding="UTF-8").read()
        self.emails = [s for s in myline.split('End Email"\n"Message-ID') if s.strip('') != '']
        
        for x in self.emails:       
            self.messageid = re.findall(r"\<(.*)\>", x)

            self.date = re.findall(r"(\D{3}\,\s\d{2}\s\D{3}\s\d{4})", x)

            self.subject = re.findall(r"(?m)^Subject: (.+)$", x)

            self.sender = re.findall(r'From: ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)', x)

            self.receiver = re.findall(r'To: ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)', x)

            self.body = re.findall(r'nsf(.*?)End', x)




class Email:

    def __init__(self, message_id, date, subject, sender, receiver, body):

        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body


def parse_args(parse_list):

    myarg = argparse.ArgumentParser(description="The list of arguments")

    myarg.add_argument('path', type=str, help='the path to the text file')

    args = myarg.parse_args(parse_list)

    return args


def main(path):

    myserver = Server(path)
    print("The length of the emails is:", len(myserver.emails))


if __name__ == "__main__":
    ranvar = parse_args(sys.argv[1:])
    main(ranvar.path)
