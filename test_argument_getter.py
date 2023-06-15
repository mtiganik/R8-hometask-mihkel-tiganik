from unittest import TestCase
from unittest.mock import patch
import asyncio

from argument_getter import getArgs

class TestFilterByComments(TestCase):

    def testNoArgsGiveDefaultValues