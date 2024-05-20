import pandas as pd
import re
from bs4 import BeautifulSoup

# First, read the data
# df = pd.readcsv('')

# Since I don't have the access to database, created for example.
data = {
    'Device_Type': ['AXO145', 'TRU151', 'ZOD231', 'YRT236', 'LWR245'],
    'Stats_Access_Link': [
        '<url>https://xcd32112.smart_meter.com</url>',
        '<link>http://tXh67.dia_meter.com</link>',
        '<link>ssl://yT5495_.smart_meter.com</link>',
        '<url>https://ret323_TRu.crown.com</url>',
        '<url>luwr3243.celcius.com</url>'
    ]
}

# creating dataframe
df = pd.DataFrame(data)

# Function to remove XML tags
def remove_xml_tags(text):
    return BeautifulSoup(text, 'html.parser').get_text()

# Defining the pattern
pattern = re.compile(r'[a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+')

# Function to extract the URL part
def extract_url(access_link):
    # Remove XML tags
    clean_link = remove_xml_tags(access_link)
    # Search for the URL part
    match = pattern.search(clean_link)
    if match:
        return match.group(0)
    return None

# Apply the function to the DataFrame
df['Extracted_URL'] = df['Stats_Access_Link'].apply(extract_url)

# Display the DataFrame
print(df)
print(df['Extracted_URL'])