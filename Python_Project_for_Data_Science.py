#                                      Python Project for Data Science

#                               Extracting Stock Data Using a Python Library
#
#import yfinance as yf
#import pandas as pd
#Using the yfinance Library to Extract Stock Data
#Using the Ticker module we can create an object that will allow us to access functions to extract data.
#To do this we need to provide the ticker symbol for the stock,
# here the company is Apple and the ticker symbol is AAPL.
#apple = yf.Ticker("AAPL")
#Now we can access functions and variables to extract the type of data we need. You can view them and what they represent here https://aroussi.com/post/python-yahoo-finance.
# If you're trying to run this in a command-line interface, you can use the wget command directly:
#!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

# alternative
#import requests

#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
#response = requests.get(url)

#with open("apple.json", "wb") as f:
#    f.write(response.content)

# Stock Info
#Using the attribute info we can extract information about the stock as a Python dictionary.
#import json
#with open('apple.json') as json_file:
#    apple_info = json.load(json_file)
    #print("Type:", type(apple_info))
    #print(apple_info)

#We can get the 'country' using the key country
#print(apple_info['country'])

#Extracting Share Price
# A share is the single smallest part of a company's stock that you can buy, the prices of these shares fluctuate over time.
# Using the history() method we can get the share price of the stock over a certain period of time.
# Using the period parameter we can set how far back from the present to get data.
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
#apple_share_price_data = apple.history(period="35y")

# The format that the data is returned in is a Pandas DataFrame.
# With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
#apple_share_price_data.head()
#print(apple_share_price_data.head())

#We can reset the index of the DataFrame with the reset_index function.
# We also set the inplace paramter to True so the change takes place to the DataFrame itself.
#apple_share_price_data.reset_index(inplace=True)

#We can plot the Open price against the Date:
#apple_share_price_data.plot(x="Date", y="Open")

#import matplotlib.pyplot as plt

# Assuming you have a DataFrame named apple_share_price_data
# If not, make sure you have the data loaded correctly

# Adding labels and title
#plt.xlabel("Date")
#plt.ylabel("Open Price")
#plt.title("Apple Stock Open Prices Over Time")

# Display the plot
#plt.savefig('apple_share_price_data_1.png')  # Save plot to a file

#Extracting Dividends
#Dividends are the distribution of a companys profits to shareholders.
# In this case they are defined as an amount of money returned per share an investor owns.
# Using the variable `dividends` we can get a dataframe of the data.
# The period of the data is given by the period defined in the 'history` function.
#print(apple.dividends)

#We can plot the dividends overtime:
#import matplotlib.pyplot as plt
#apple.dividends.plot()
#plt.savefig('apple_dividends_overtime_1.png')  # Save plot to a file


#                                       Exercise
#Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker
# symbol is AMD called; name the object amd.
#import yfinance as yf
#import pandas as pd
#Using the yfinance Library to Extract Stock Data
#Using the Ticker module we can create an object that will allow us to access functions to extract data.
#To do this we need to provide the ticker symbol for the stock,
# here the company is Apple and the ticker symbol is AAPL.
#amd = yf.Ticker("AMD")
#Now we can access functions and variables to extract the type of data we need. You can view them and what they represent here https://aroussi.com/post/python-yahoo-finance.
# If you're trying to run this in a command-line interface, you can use the wget command directly:
#!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json

# alternative
#import requests

#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
#response = requests.get(url)

#with open("amd.json", "wb") as f:
#    f.write(response.content)

# Stock Info
#Using the attribute info we can extract information about the stock as a Python dictionary.
#import json
#with open('amd.json') as json_file:
#    amd_info = json.load(json_file)
    #print("Type:", type(amd_info))
    #print(amd_info)

#We can get the 'country' using the key country
#print(amd_info['country'])

# Question 1 Use the key 'country' to find the country the stock belongs to,
# remember it as it will be a quiz question.
#print('Question 1 Use the key country to find the country the stock belongs to:', amd_info['country']) # United States

# Question 2 Use the key 'sector' to find the sector the stock belongs to,
# remember it as it will be a quiz question.
#print('Question 2 Use the key sector to find the sector the stock belongs to:', amd_info['sector']) # Technology

# Question 3 Obtain stock data for AMD using the history function, set the period to max.
# Find the Volume traded on the first day (first row). # 219600

# 1 Extracting (history function)
#amd_data = amd.history(period="100y") # 35y / 100y
#amd_data = amd.history(period="max") # max
#print(amd_data.head()) # 219600

# Find the Volume traded on the first day (first row)
#first_day_volume = amd_data.iloc[0]['Volume']
#print('Question 3 Volume traded on the first day (first row):', first_day_volume) # 219600.0



#                       Extracting Stock Data Using Web Scraping

#import pandas as pd
#import requests
#from bs4 import BeautifulSoup

# Using Webscraping to Extract Stock Data Example
# We will extract Netflix stock data https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html.

#Steps for extracting the data
#1 Send an HTTP request to the web page using the requests library.
#2 Parse the HTML content of the web page using BeautifulSoup.
#3 Identify the HTML tags that contain the data you want to extract.
#4 Use BeautifulSoup methods to extract the data from the HTML tags.
#5 Print the extracted data

# Step 1: Send an HTTP request to the web page
# You will use the request library for sending an HTTP request to the web page.
#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# You use the .text method for extracting the HTML content as a string in order to make it readable.
#data  = requests.get(url).text
#print(data)

# Step 2: Parse the HTML content
#Parsing the data using the BeautifulSoup library
#Note: To create a BeautifulSoup object in Python, you need to pass two arguments to its constructor:
#1 The HTML or XML content that you want to parse as a string.
#2 The name of the parser that you want to use to parse the HTML or XML content.
# This argument is optional, and if you don't specify a parser, BeautifulSoup
# will use the default HTML parser included with the library. here in this lab we are using "html5lib" parser.
#soup = BeautifulSoup(data, 'html5lib')

# Step 3: Identify the HTML tags
# You will create an empty data frame using the pd.DataFrame() function with the following columns:
# "Date", "Open", "High", "Low", "Close", "Volume"
#netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
#print(netflix_data) # Empty DataFrame

# Step 4: Use a BeautifulSoup method for extracting data
# We will use find() and find_all() methods of the BeautifulSoup object to
# locate the table body and table row respectively in the HTML.
#The find() method will return particular tag content.
#The find_all() method returns a list of all matching tags in the HTML.

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
#for row in soup.find("tbody").find_all('tr'):
#    col = row.find_all("td")
#    date = col[0].text
#    Open = col[1].text
#    high = col[2].text
#    low = col[3].text
#    close = col[4].text
#    adj_close = col[5].text
#    volume = col[6].text

    # Finally we append the data of each row to the table
#    netflix_data = netflix_data._append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    #print(netflix_data)

# Step 5: Print the extracted data
# We can now print out the data frame using the head() or tail() function.
#print('BeautifulSoup:\n', netflix_data.head())


#                           Extracting data using pandas library

#  pd.read_html(url) is a function provided by the pandas library in Python that is used to extract tables from HTML web pages.
#  It takes in a URL as input and returns a list of all the tables found on the web page.
#read_html_pandas_data = pd.read_html(url)

# Or you can convert the BeautifulSoup object to a string.
#read_html_pandas_data = pd.read_html(str(soup))

# Because there is only one table on the page, just take the first table in the returned list.
#netflix_dataframe = read_html_pandas_data[0]
#print('Panda:\n', netflix_dataframe.head())


#                       Exercise: use webscraping to extract stock data
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html.
# Save the text of the response as a variable named html_data.

# Step 1: Send an HTTP request to the web page
#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

# You use the .text method for extracting the HTML content as a string in order to make it readable.
#html_data  = requests.get(url).text
#print(data)

#Parse the html data using beautiful_soup.
# Step 2: Parse the HTML content

#soup = BeautifulSoup(html_data, 'html5lib')
#print(soup)

# Question 1: What is the content of the title attribute?
#print('Question 1 - content of the title attribute:', soup.find('title'))
# Question 1 - content of the title attribute: <title>Amazon.com, Inc. (AMZN) Stock Historical Prices &amp; Data - Yahoo Finance</title>

# Using BeautifulSoup, extract the table with historical share prices and store it into a data frame
# named amazon_data. The data frame should have columns Date, Open, High, Low, Close, Adj Close, and Volume.
# Fill in each variable with the correct data from the list col.

# You will create an empty data frame using the pd.DataFrame() function with the following columns:
#amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

#for row in soup.find("tbody").find_all("tr"):
#    col = row.find_all("td")
#    date = col[0].text
#    Open = col[1].tex
#    high = col[2].text
#    low = col[3].text
#    close = col[4].text
#    adj_close = col[5].text
#    volume = col[6].text

#    amazon_data = amazon_data._append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    #print(amazon_data)

# Step 5: Print the extracted data
# We can now print out the data frame using the head() or tail() function.
#print('BeautifulSoup:\n', amazon_data.head())

# Question 2: What are the names of the columns in the data frame?
#column_names = amazon_data.columns
#print("Question 2 - names of the columns in the data frame:", column_names)
#Question 2 - names of the columns in the data frame: Index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], dtype='object')

# Question 3: What is the Open of the last row of the amazon_data data frame?
#last_row_open = amazon_data.iloc[-1]['Open']
#print("Question 3 - Open of the last row of the amazon_data data frame:", last_row_open)
#Question 3 - Open of the last row of the amazon_data data frame: None


#       Hands-on Lab: Analyzing Historical Stock/Revenue Data and Building a Dashboard
#                       Extracting and Visualizing Stock Data

# Define a Function that Makes a Graph
# Question 1: Use yfinance to Extract Stock Data
# Question 2: Use Webscraping to Extract Tesla Revenue Data
# Question 3: Use yfinance to Extract Stock Data
# Question 4: Use Webscraping to Extract GME Revenue Data
# Question 5: Plot Tesla Stock Graph
# Question 6: Plot GameStop Stock Graph

#!pip install yfinance==0.1.67
#!mamba install bs4==4.10.0 -y
#!pip install nbformat==4.2.0
#!pip install plotly==5.17.0

#import yfinance as yf
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots

# Define Graphing Function
# In this section, we define the function make_graph. You don't have to know how the function works,
# you should only care about the inputs. It takes a dataframe with stock data
# (dataframe must contain Date and Close columns), a dataframe with revenue data
# (dataframe must contain Date and Revenue columns), and the name of the stock.

#def make_graph(stock_data, revenue_data, stock):
#    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
#    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
#    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
#    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
#    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
#    fig.update_xaxes(title_text="Date", row=1, col=1)
#    fig.update_xaxes(title_text="Date", row=2, col=1)
#    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
#    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
#    fig.update_layout(showlegend=False,
#    height=900,
#    title=stock,
#    xaxis_rangeslider_visible=True)
#    fig.show()

#                   Question 1: Use yfinance to Extract Stock Data

# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker
# object. The stock is Tesla and its ticker symbol is TSLA.

#tesla = yf.Ticker("TSLA")

# Using the ticker object and the function history extract stock information and save it in a dataframe
# named tesla_data. Set the period parameter to max so we get information for the maximum amount of time.
#amd_data = amd.history(period="100y") # 35y / 100y
#amd_data = amd.history(period="max") # max
#print(amd_data.head()) # 219600
#tesla_data = tesla.history(period="35y")  # 35y / 100y
#tesla_data = tesla.history(period="max")    # max
#tesla_data['Date'] = pd.to_datetime(tesla_data['Date'])
#tesla_data.set_index('Date', inplace=True)  # Set 'Date' column as the index

#print(tesla_data.head())

# Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame and
# display the first five rows of the tesla_data dataframe using the head function.
# Take a screenshot of the results and code from the beginning of Question 1 to the results below.
#tesla_data.reset_index(inplace=True)
#print(tesla_data.head())

#               Question 2: Use Webscraping to Extract Tesla Revenue Data
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
#Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named html_data.
# Step 1: Send an HTTP request to the web page
#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# You use the .text method for extracting the HTML content as a string in order to make it readable.
#html_data  = requests.get(url).text
#print(html_data)

#Parse the html data using beautiful_soup.
# Step 2: Parse the HTML content

#soup = BeautifulSoup(html_data, 'html5lib')
#print(soup)

# Using BeautifulSoup or the read_html function extract the table with Tesla Revenue and store it into
# a dataframe named tesla_revenue. The dataframe should have columns Date and Revenue.
#tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
#print(tesla_revenue)

#tesla_revenue_table = soup.find('table')

# Initialize lists to store Date and Revenue data
#dates = []
#revenues = []

# Loop through the rows of the table
#for row in tesla_revenue_table.find_all('tr')[1:]:  # Start from the second row to skip headers
#    cols = row.find_all('td')
#    date = cols[0].text.strip()
#    revenue = cols[1].text.strip()
#    dates.append(date)
#    revenues.append(revenue)

# Create a DataFrame
#tesla_revenue = pd.DataFrame({'Date': dates, 'Revenue': revenues})

# Print the first few rows of the DataFrame
#print(tesla_revenue.head())


# Execute the following line to remove the comma and dollar sign from the Revenue column.
#tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")


# Execute the following lines to remove an null or empty strings in the Revenue column.
#tesla_revenue.dropna(inplace=True)

#tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
#print(tesla_revenue)


# Display the last 5 row of the tesla_revenue dataframe using the tail function.
# Take a screenshot of the results.
#print(tesla_revenue.tail())


#                   Question 3: Use yfinance to Extract Stock Data
#import yfinance as yf

# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a
# ticker object. The stock is GameStop and its ticker symbol is GME.
#GameStop = yf.Ticker("GME")

#Using the ticker object and the function history extract stock information and save it in a dataframe
# named gme_data. Set the period parameter to max so we get information for the maximum amount of time.
#gme_data = GameStop.history(period="max")
#print(gme_data.head())

# Reset the index using the reset_index(inplace=True) function on the gme_data DataFrame and display the
# first five rows of the gme_data dataframe using the head function.
# Take a screenshot of the results and code from the beginning of Question 3 to the results below.

#gme_data.reset_index(inplace=True)
#print(gme_data.head())


#                     Question 4: Use Webscraping to Extract GME Revenue Data
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup
# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html.
# Save the text of the response as a variable named html_data.
#url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# You use the .text method for extracting the HTML content as a string in order to make it readable.
#html_data  = requests.get(url).text
#print(html_data)

#Parse the html data using beautiful_soup.
#soup = BeautifulSoup(html_data, 'html5lib')
#print(soup)

# Using BeautifulSoup or the read_html function extract the table with GameStop Revenue and store it into a
# dataframe named gme_revenue. The dataframe should have columns Date and Revenue. Make sure the
# comma and dollar sign is removed from the Revenue column using a method similar to what you did in Question 2.

#GameStop_Revenue = pd.DataFrame(columns=["Date", "Revenue"])

#GameStop_Revenue_table = soup.find('table')

# Initialize lists to store Date and Revenue data
#dates = []
#revenues = []

# Loop through the rows of the table
#for row in GameStop_Revenue_table.find_all('tr')[1:]:  # Start from the second row to skip headers
#    cols = row.find_all('td')
#    date = cols[0].text.strip()
#    revenue = cols[1].text.strip()
#    dates.append(date)
#    revenues.append(revenue)

# Create a DataFrame
#GameStop_Revenue = pd.DataFrame({'Date': dates, 'Revenue': revenues})

#print(GameStop_Revenue.head())


#Display the last five rows of the gme_revenue dataframe using the tail function.
# Take a screenshot of the results.
#print(GameStop_Revenue.tail())


#                       Question 5: Plot Tesla Stock Graph

# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.
# The structure to call the make_graph function is make_graph(tesla_data, tesla_revenue, 'Tesla').
# Note the graph will only show data upto June 2021.

#make_graph(tesla_data, tesla_revenue, 'Tesla')


#                       Question 6: Plot GameStop Stock Graph

# Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.
# The structure to call the make_graph function is make_graph(gme_data, gme_revenue, 'GameStop').
# Note the graph will only show data upto June 2021.

#make_graph(gme_data, GameStop_Revenue, 'GameStop')









