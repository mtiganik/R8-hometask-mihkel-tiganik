from unittest import TestCase
from unittest.mock import patch
import asyncio

from services.comment_filter_service import filterByComment, singlePageJSON, createDTO, getUrls
from test_models import page1, resultsFirstPage10ForPage, dataToCreateDTOMethod, firstPageTake5Res, secondPageTake3Res

class TestFilterByComments(TestCase):
    
    def testSinglePageJSON(self):
        # fromMethod = asyncio.run(singlePageJSON(page1['data']))
        fromMethod = singlePageJSON(page1['data'])
        self.assertEqual(len(fromMethod),9)
    
    def testCreateDTO(self):
        firstPageTake5 = createDTO(dataToCreateDTOMethod, page=1, per_page=5)
        secondPageTake3 = createDTO(dataToCreateDTOMethod, page=2, per_page=3)
        self.assertEqual(firstPageTake5, firstPageTake5Res)
        self.assertEqual(secondPageTake3, secondPageTake3Res)
    
    def testGetUrls(self):
        url = "example.com"
        pageCnt = 3
        expectedRes = ["example.com?page=1","example.com?page=2", "example.com?page=3"]
        self.assertEqual(getUrls(url, pageCnt), expectedRes)

    def testFullApiCall(self):
        url = 'https://jsonmock.hackerrank.com/api/articles'
        result = asyncio.run(filterByComment(url, page=1, per_page=10))
        self.assertEqual(result, resultsFirstPage10ForPage)




