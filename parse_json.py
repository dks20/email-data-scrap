def extract_emails_and_sname_from_json(json_data):
    
    dataarray= json_data.split("<tr class")
    
    vcount=0
    Record = 1
    for email_element in dataarray:
        
        if(vcount <= 2):
          print(vcount)
          vcount = vcount+1
          continue
        else:
          print("Record No-",Record)
          index01 = email_element.find('email=')  
          index02 = email_element.find('name',index01)  
          print("Senders e-mail :",email_element[(index01+8):(index02-3)] )
          index01 = index02  
          index02 = email_element.find('\"',index01+8)  
          print("Senders name :",email_element[(index01+7):(index02-1)] )
          index01 = email_element.find('data-legacy-thread-id',index02)
          index01 = email_element.find('\">',index01)
          index02 = email_element.find('</span>',index01+8)  
          print("Subject :",email_element[(index01+2):(index02)] )
          index01 = email_element.find('title',index02)
          index02 = email_element.find('\"',index01+8)
          print("Time :",email_element[(index01+8):(index02-1)] )
          print("\n")
          
        Record += 1
        vcount += 1
        
    
file_path = r'C:\Users\Pirate\Downloads\scraped.json'

with open(file_path, 'r', encoding='utf-8') as file:
    json_data = file.read()


extract_emails_and_sname_from_json(json_data)













