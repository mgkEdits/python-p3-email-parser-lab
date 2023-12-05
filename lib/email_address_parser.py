# your code goes here!

import re

class EmailAddressParser:
    regex_mail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Use regular expression to find email addresses in the input string
        address_list = re.split(r'[,\s]+', self.email_addresses)

        mail_addresses = set()
        for address in address_list:
            if self.regex_mail.fullmatch(address):
                mail_addresses.add(address)

        # Remove duplicates and sort alphabetically
        unique_addresses = sorted(list(mail_addresses))

        return unique_addresses
