# import json
# from bs4 import BeautifulSoup

# def extract_emails_and_sname_from_json(json_data):
#     soup = BeautifulSoup(json_data, 'html.parser')
    
#     email_elements = soup.find_all(attrs={'email': True})
    
    
#     data = []
#     for element in email_elements:
#         email = element['email']
        
       
#         # Try to find a sname within the parent <td> of the email element
#         sname_span = element.find_parent('td').find('span')
#         sname = sname_span.get_text(strip=True) if sname_span else ''
        
#         data.append({'email': email, 'sname': sname})
    
#     return data

# # Replace 'your_file_path.json' with the actual path to your JSON file
# file_path = r'C:\Users\Pirate\Downloads\scraped.json'

# with open(file_path, 'r', encoding='utf-8') as file:
#     json_data = file.read()

# # Extract all email addresses and sname from the HTML content in the JSON
# result_data = extract_emails_and_sname_from_json(json_data)

# # Print the extracted email addresses and sname
# for item in result_data:
#     print(f"Email: {item['email']}, Sender_Name: {item['sname']}")

import json
from bs4 import BeautifulSoup

def extract_emails_and_sname_from_json(json_data):
    soup = BeautifulSoup(json_data, 'html.parser')
    
    email_elements = soup.find_all(attrs={'email': True})
    
    
    data = []
    for email_element in email_elements:
        print("0: ",email_element,">")
        email = email_element['email']
        
        
        # Find the corresponding timestamp for the current email element
       
        timestamp_span = email_element.find_next('span',{'title': True, 'aria-label': True})
        #timestamp_span_ = timestamp_span.replace(","," ")
        print("1: ",timestamp_span)
        
        timestamp = timestamp_span.get('aria-label', '') if timestamp_span else ''
        print("2: ",timestamp)
        
        # Try to find a sname within the parent <td> of the email element
        sname_span = email_element.find_parent('td').find('span')
        print("3: ",sname_span)
        sname = sname_span.get_text(strip=True) if sname_span else ''
        print("4: ",sname)
        
        data.append({'email': email, 'sname': sname, 'timestamp': timestamp})
        break
    
    return data

# Replace 'your_file_path.json' with the actual path to your JSON file
file_path = r'C:\Users\Pirate\Downloads\scraped.json'

with open(file_path, 'r', encoding='utf-8') as file:
    json_data = file.read()

# Extract all email addresses, sender names, and timestamps from the HTML content in the JSON
result_data = extract_emails_and_sname_from_json(json_data)

# Print the extracted email addresses, sender names, and timestamps
for item in result_data:
    print(f"Email: {item['email']}, Sender_Name: {item['sname']}, Timestamp: {item['timestamp']}")












