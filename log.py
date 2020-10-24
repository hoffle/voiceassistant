##
## Log System
##
## Personal Assistent
## by Hoffle

import logging

def log(filename):
    logging.basicConfig(filename=filename, level=logging.DEBUG)
