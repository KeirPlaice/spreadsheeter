import csv
import json
import requests
import tempfile
import streamlit as st

st.title('Spreadsheeter')

st.header('Turn your Google Custom Search results into a spreadsheet in an instant')

API=st.text_input(
        "What is your API key?",
        "Fill in your API key",
        key="APIplaceholder",
    )




ID=st.text_input(
        'What is your Google Custom Search Engine ID?',
        "Fill your Google Custom Search Engine ID",
        key="IDplaceholder",
    )

QUERY=st.text_input(
        'What is your query?',
        "Write your query",
        key="QUERYplaceholder",
    )
STARTDATE=st.text_input(
        'From which date would you like to search?',
        "Fill in your start date, y/m/d, e.g 20230131",
        key="STARTDATEplaceholder",
    )

ENDDATE=st.text_input(
        'Up to which date would you like to search?',
        "Fill in your end date, y/m/d, e.g 20231231",
        key="ENDDATEplaceholder",
    )


base_url='https://www.googleapis.com/customsearch/v1?key='+(API)+'&cx='+(ID)+'&q='+(QUERY)+'&sort=date:r:'+(STARTDATE)+':'+(ENDDATE)


if API!= 'Fill in your API key' and ID!= 'Fill your Google Custom Search Engine ID' and QUERY!= 'Write your query' and STARTDATE!= 'Fill in your start date, y/m/d, e.g 20230131' and ENDDATE!= 'Fill in your end date, y/m/d, e.g 20231231':

    @st.cache_data
    
    tempfile = open("Testing.csv", "w", newline='')
    header = ['Site', 'Title', 'URL', 'Author', 'Date']
    writer = csv.writer(file)
    writer.writerow(header)

    out_rows = 0

    for i in range(1,100,10):
        if i == 1:
            url = base_url
        else:
            url = base_url + f"&start={i}"
        print(url)


        response = requests.get(url)
        response_dict = response.json()


        for item in response_dict.get('items', []):
            title = item.get('title', '')
            url = item.get('link', '')

            author = item.get('pagemap', {}).get('metatags', [{}])[0].get('author', '')
            date = item.get('pagemap', {}).get('metatags', [{}])[0].get('article:published_time', '')
            site = item.get('pagemap', {}).get('metatags',[{}])[0].get('og:site_name','')

            data = [site, title, url, author, date]
            writer.writerow(data)
            out_rows += 1


    tempfile.close()



with open('testing.csv') as f:
    st.download_button('Download CSV', f, 'Results.csv')




    














