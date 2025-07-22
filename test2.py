import re
import argparse
import sys

class Server:

    def __init__(self, path):
        self.emails = []

        myline = open(str(path), "r").read()

        self.emails = [s for s in myline.split('End Email') if s.strip('') != '']
        # print(len(self.emails))


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
    # myarg.add_argument('message_id', type=str, help='a string that represents the messages id')
    # myarg.add_argument('date', type=str, help='string representing the date')
    # myarg.add_argument('subject', type=str, help='string representing the subject of the mail')
    # myarg.add_argument('sender', type=str, help='string email of the sender')
    # myarg.add_argument('receiver', type=str, help='string email of the receiver')
    # myarg.add_argument('body', type=str, help= 'the body text of the email')
    args = myarg.parse_args(parse_list)
    return args


def main(path):
    myserver = Server(path)
    print("The length of the emails is:", len(myserver.emails))


if __name__ == "__main__":
    ranvar = parse_args(sys.argv[1:])
    main(ranvar.path)

    # print(ranvar.path)
