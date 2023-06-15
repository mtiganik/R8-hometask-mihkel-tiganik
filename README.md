## Hometask for R8

### Problem:
There is a service that returns a list of articles in the form of json
https://jsonmock.hackerrank.com/api/articles?page={page_number}
Where `{page_number}` is an integer indicating the page whose articles you want to query.
Each query returns information in the form of json:
+ “page” - the page number whose data is currently being returned
+ “per_page” - number of articles per page
+ “total” - the total number of articles on all pages
+ “total_pages” - the total number of pages containing articles
+ “data” - an array in the form of json of objects that contain information about articles (title, url,
author, num_comments, story_id, story_title, story_url, parent_id, created_at)
---
For example, the following query returns a list of the first page:
https://jsonmock.hackerrank.com/api/articles?page=1

### Implement
Write a Python script that finds and returns the titles of the ten articles with the most comments
`(num_comments)` in descending order of number of comments over all pages. The title of the
article is the `title` field value in the article information, if there is no `title` field value, then the
`story_title` field value, if both field values are missing than ignore such an article and select the
article with the most comments next.

## Solution
Here is my solution. Added pagination so it is possible to get 2nd,3rd... pages aswell. Output is just a list of strings containing article titles/story titles as was requested. Articles that do not have comments they are taken away. 
API calls have made asynchronous. With `singlePageJSON` method every page entry is reduced to `title` and `num_comments` objects within asynchronous tasks so overload issues have been taken into account.

To run this program:
``` python main.py ```

To run tests:
``` python -m unittest ```
