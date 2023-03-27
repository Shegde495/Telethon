from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerUser, InputPeerEmpty,PeerChannel
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from dotenv import load_dotenv
import os
import codecs, json
import datetime
from datetime import datetime,timedelta,timezone
import pathlib
from convert import dateconversion
  

load_dotenv()

api_id=os.getenv('API_ID')
api_hash=os.getenv('API_HASH')


client = TelegramClient('session_name', api_id, api_hash)
client.start()

user_input_channel = input("enter entity(telegram URL or entity id):")

if user_input_channel.isdigit():
    entity = PeerChannel(int(user_input_channel))
else:
    entity = user_input_channel
    

user_entity = client.get_entity(entity)
offset_id = 0
limit = 100
all_messages = []
total_messages = 0
total_count_limit = 0
msg=0
li=[]
diction={}
while True:        
        #print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
        history = client(GetHistoryRequest(
            peer=user_entity,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=msg, 
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            msg=message.id
            date=message.date
            #print(date)
            current_date=datetime.utcnow()
            message_date=date
            message_date_naive = datetime.fromisoformat(str(message_date))
            message_date_aware = message_date_naive.replace(tzinfo=tkimezone.utc)
            current_date_aware = datetime.now(timezone.utc)
            if current_date_aware - message_date_aware < timedelta(hours=48):
                offset_id = messages[len(messages) - 1].id
                all_messages.append(message.to_dict())
                li.append(date)
                flag=1
            else:
                flag=0
        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            print("Limit reached")
            break
        if flag==0:
            break
        
        
print(type(message))

# search=input("enter the search element : ")
# print()
# print("######### Searched By  #########")
# print()
# all=[]
# for i in all_messages:
#     li=[]
#     if search.upper() == str(i['message']).upper() or search.upper() in str(i['message']).upper():
#         from_id=i['from_id']
#         if from_id==None:       
#             print("Message : ",i['message'])
#             Date=dateconversion(i['date'])
#             print("Date : ", Date)
#             print("Views :", i['views'])
#             li.extend([i['message'],Date,i['views']])
#             print("Username : " ,str(user_entity.username))
#             if i['media'] is not None:
#                 media_file = client.download_media(i['media'])    
#                 if i['media']['_']=='MessageMediaPhoto':
#                     li.append(i['media']['_'])
#             print()
#             all.append(li)
#         else:
#             print("Message : ",i['message'])
#             Date=dateconversion(i['date'])
#             print("Date : ", Date)
#             print("Views :", i['views'])
#             li.extend([i['message'],Date,i['views']])
#             user=client.get_entity(i['from_id']['user_id'])
#             print("Name : " ,str(user.first_name),'',str(user.last_name))
#             if i['media'] is not None:
#                 media_file = client.download_media(message.media)    
#                 if i['media']['_']=='MessageMediaPhoto':
#                     li.append(i['media']['_'])
#             print()
#             all.append(li)
           
#     else:
#         continue
        

# empty_json = []
# with open('messages.json', 'w') as f:
#     json.dump(empty_json, f)
    
# with codecs.open('messages.json', 'w', 'utf8') as f:
#     f.write(json.dumps(all, sort_keys = True, ensure_ascii=False))

     
