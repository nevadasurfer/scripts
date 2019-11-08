#!/usr/bin/python
from validator_collection import validators, checkers

checkers.is_url('http://www.stackoverflow.com')
# Returns True

checkers.is_url('not a valid url')
# Returns False

#value = validators.url('http://www.stackoverflow.com')
# value set to 'http://www.stackoverflow.com'

#value = validators.url('not a valid url')
# raises a validator_collection.errors.InvalidURLError (which is a ValueError)
