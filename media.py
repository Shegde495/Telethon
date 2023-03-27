from telethon import TelegramClient, sync, types
from telethon.tl.functions.messages import GetHistoryRequest,GetMessagesRequest
from telethon.tl.types import InputMessagesFilterPhotos
from dotenv import load_dotenv
load_dotenv()
import os

# create a TelegramClient instance
api_id = os.getenv('API_ID')# your api id
api_hash = os.getenv('API_HASH')# your api hash
client = TelegramClient('session_name', api_id, api_hash)

# connect to the Telegram server
client.start()

# define the channel username or ID
channel = 'https://t.me/ChatGPT_OpenAi'


messages = client(GetHistoryRequest(
    peer=channel,
    limit=10, # number of messages to retrieve
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0,
    #filter=InputMessagesFilterPhotos(), # filter only photo messages
    ))
    
# loop through each message and download the media file
for message in messages.messages:
    # check if the message has media
    if message.media:
        #print(message.media)
        # download the media file
        media_file = client.download_media(message.media)     
        # print the file path
        print('File Path:', media_file)






# get the messages from the channel
# messages = client(GetMessagesRequest(
#     peer=channel,
#     limit=10,  # number of messages to retrieve
#     filter=types.InputMessagesFilterPhotos(),  # filter only photo messages
# ))

# # loop through each message and download the media file
# for message in messages:
#     # check if the message has media
#     if message.media:
#         # download the media file
#         media_file = client.download_media(message.media)
        
#         # print the file path
#         print('File Path:', media_file)
