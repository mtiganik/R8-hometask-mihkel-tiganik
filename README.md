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
This is my solution. It contains pagination so it is possible to get 2nd,3rd... pages aswell. Default output is together with index and comment count. Title is taken from input as was requested it is whether title or story as was requested. Articles that do not have comments they are taken away. 
API calls have made asynchronous. With `singlePageJSON` method every page entry is reduced to `title` and `num_comments` objects within asynchronous tasks so overload issues have been taken into account.

This program mainly uses native Python Libraries, but it also have `aiohttp`, so you might need to download this aswell  

Solution for this hometask is run by:  
``` python main.py --list```

You can also run this with arguments `--help` or `-h`, `--list`, `--no_comments`. Default `--page` is 1 and `--per_page` is 10, but you can change them.  

For example command:  
`python main.py --page 2 --per_page 7`

will give output:  
```
ID      Title                                                   Comments
8       Don't Fly During Ramadan                                961
9       SpaceX’s Falcon Heavy successfully launches             872
10      macOS High Sierra: Anyone can login as “root” with e... 813
11      Chrome 69 will keep Google Cookies when you tell it ... 810
12      Paradise Papers: Dear Tim Cook                          791
13      Pardon Snowden                                          781
14      How Uber Used Secret “Greyball” Tool to Deceive Auth... 764
```

There are also tests in this project. To run tests:  
``` python -m unittest ```
