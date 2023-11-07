import csv
import json
import requests


file = open("Testing.csv", "w", newline='')
header = ['Site', 'Title', 'URL', 'Author', 'Date']
writer = csv.writer(file)
writer.writerow(header)

out_rows = 0



base_url = ('https://www.googleapis.com/customsearch/v1?key=AIzaSyBK3_cOE7ZnTKL7QBVFJoLQL-rBuRzeRvc&cx=e6e23df52086e4ed7&q=Owain%20Doull&sort=date:r:20230101:20231104')

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


file.close()




print(f"OK! Published file with {out_rows} articles.")

with open("Testing.json", "w") as json_file:
    json.dump(response_dict, json_file, indent=2)





