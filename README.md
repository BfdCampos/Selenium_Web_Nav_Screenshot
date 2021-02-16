# Paysafe Project:
## Using Selenium with Python to go to specific websites, navigate the site and take screenshots

This is a simple programme to go to specific websites that are used by the team daily to compare our service's prices. 

The sites in use often contained hidden HTML elements so BeautifulSoup was a difficult choice as this package cannot navigate a webpage.

Selenium is a great alternative with awesome features like "send keys" and "find element(s) by" a certain HTML tag.

The result of running this interface-less programme is a a series of screenshots of pre-written, hard coded sites and instructions.

### Future Developments:

In the future I would like to create a programme that takes a country pair, for a certain amount and add's this to the list of screenshots to take. *- Priority Low*

Further in, I could use an AI algorithm to look for similar traits on all comparison sites such as "Amount" and "Send country", allowing for there to be a programme where you can add any website and country pair (with amount) to get a screenshot **and** raw data saved as CSV and hence manipulated in a spreadsheet app. *- Priority Very Low*