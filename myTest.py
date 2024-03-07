from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the URL
url = "https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text

    # Use BeautifulSoup to parse the fetched HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <code> tags with a 'data-class' attribute that contains '23'
    codes = soup.find_all('code', attrs={'data-class': lambda x: x and '23' in x})

    url = ''
    for code in codes:
        # Within each <code> tag, find <div> with 'data-tag' attribute ending in '93'
        divs = code.find_all('div', attrs={'data-tag': lambda x: x and x.endswith('93')})
        for div in divs:
            # Within each <div>, find <span> with 'data-id' attribute containing '21'
            spans = div.find_all('span', attrs={'data-id': lambda x: x and '21' in x})
            for span in spans:
                # Within each <span>, find <i> tag with class 'char' and extract 'value'
                char_tag = span.find('i', class_='char')
                if char_tag and 'value' in char_tag.attrs:
                    url += char_tag['value']
    print(url)
else:
    print('Failed to retrieve the page')
