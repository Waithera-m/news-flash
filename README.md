# News-Flash
#### The web application allows users to view news articles from different sources, April 26, 2020 
#### By **Waithera-m**
## Description
News-Flash is a simple flask application that uses the news api to get news sources, headlines, and topical articles. The site allows users to view source specific articles. Users can also use provided links to read full articles, which are published on different news sites.
## Setup/Installation Requirements
To use the application, users need internet access and web browsers, preferably  Chrome, Safari, and Firefox.
## Set-Up a Local Project
To set up a local project:
* Fork the repository
* Clone the repository using the git clone command
* Activate a virtual environment
* Install Python, preferably versions 3.6 and later
* Install flask and bootstrap
## Known Bugs
* None at the moment.
## Behavior Driven Development (BDD)
|Behavior                |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads |Users scroll | Users see different sources and top headlines|
|The landing page loads|Users click on view articles link|Users are directed to source page, which displays articles unique to each source|
|Source page loads|Users click on read full article link|Users are directed to the sites where the articles are published|
|The landing page loads|Users click on visit news site button|Users are directed to sources' websites|
|The landing page loads|Users click on read full article link|Users are directed to the sites where the articles are published|
|The landing page loads|Users use the navbar to naviagate to coronavirus page|Users see coronavirus-related articles|
|The landing page loads|Users use the navbar to naviagate to about page|Users see details regarding what the site does|
## Technologies Used
* HTML - HTML dictates the structure of webpages.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Python 3.8.2 - The language was used to create classes, testcases, and functions to retrieve data 
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) -  Flask is a Python microframework.The framework's templates were used to refactor code and promote code maintenance. Inbuilt filters,classes, and methods were used to initialize the application and extensions and loop through and display api response lists and different views. 
## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creator via this email address: njihiamary11@gmail.com
## Demo
You can view changes made to the website by visiting this working live demo: 
### License
*MIT*
MIT License Copyright (c) 2020 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) 2020 **Waithera-m**