
'''
Name: Carlos Amezian
Directory ID: camezian
Date: 11/2/2020
Assignment: Homework 3
'''

import sys
import argparse
import re


class Server:

    def __init__(self, path):
        """
        Opens the file specified by the path. Sets the words to attribute to a list
        of email object. 

        Args:
            path (string): the string representation of the path
        """        
        self.emails = []

        myline = open(str(path), "r", encoding="UTF-8").read()
        self.emails = [s for s in myline.split('End Email"\n"Message-ID') if s.strip('') != '']
        
        for x in self.emails:       
            self.messageid = re.findall(r"\<(.*)\>", x)
            # print(self.messageid[0])
            self.date = re.findall(r"(\D{3}\,\s\d{2}\s\D{3}\s\d{4})", x)
            # print(self.date)
            self.subject = re.findall(r"(?m)^Subject: (.+)$", x)
            # print(self.subject)
            self.sender = re.findall(r'From: ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)', x)
            # print(self.sender)
            self.receiver = re.findall(r'To: ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)', x)
            # print(self.receiver)
            self.body = re.findall(r'nsf(.*?)End', x)




class Email:

    def __init__(self, message_id, date, subject, sender, receiver, body):
        """
        Sets the parameters to a corresponding attribute

        Args:
            message_id (string): string with message id
            date (string): string representing the date
            subject (string): string representing the subject
            sender (string): string representing the sender email
            receiver (string): string representing the receiver email
            body (string): string representing the body of the email
        """
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body


def parse_args(parse_list):
    """
    Creates an isntance of ArgumentParser 

    Args:
        parse_list (list): list of string that holds the name of the file

    Returns:
        str: the string of the path
    """    
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
    """
    Creates and instance of the server class and prints the lenght of all the emails

    Args:
        path (str): the string with the file name
    """
    myserver = Server(path)
    print("The length of the emails is:", len(myserver.emails))


if __name__ == "__main__":
    ranvar = parse_args(sys.argv[1:])
    main(ranvar.path)
