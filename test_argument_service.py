from unittest import TestCase
from unittest.mock import MagicMock, patch
from argument_service import getArgs, getDefaults

import getopt

class TestArgumentGetter(TestCase):
    
    def testWrongArgumentRaises(self):
        args = ['--some','random','args']
        self.assertRaises(getopt.GetoptError, getArgs, args)
    
    def testInvalidPageCntRaises(self):
        args = ['--page', 'abc']
        self.assertRaises(ValueError, getArgs, args )
    
    def testListChangesResult(self):
        args = ['--list', '-p','3','--per_page','5']
        expected = {'page':3,'per_page': 5, 'no_comment':False,'list':True}
        self.assertEqual(expected,getArgs(args))
    
    def testCommentChanges(self):
        args = ['--page','2','-t','3','--no_comments']
        excpected = {'page':2,'per_page':3,'no_comment':True,'list':False}
        self.assertEqual(excpected,getArgs(args))
