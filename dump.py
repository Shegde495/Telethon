from telethon import TelegramClient
import asyncio
from telethon.tl.types import InputPhoto
from dotenv import load_dotenv
import os
from datetime import datetime
import datetime
load_dotenv()
# Set up the Telegram client
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
client = TelegramClient('session_name', api_id, api_hash)

file_path = 'D:/Python/'

print(client.download_media(InputPhoto(id=5831237309658410983,access_hash=4225054679292238613,file_reference=b'\x02l>i\xfc\x00\x00e7d\x1d8AR\x7fn+\xe2\x8d\xbbO\x12\xa1<\x85\x87jMu'),file_path))

# async def main():
#     # Connect to the Telegram server
#     await client.connect()

#     # Define the photo dictionary
#     photo_dict = {'_': 'Photo', 'id': 5831237309658410983, 'access_hash': 4225054679292238613, 'file_reference': b'\x02l>i\xfc\x00\x00e7d\x1d8AR\x7fn+\xe2\x8d\xbbO\x12\xa1<\x85\x87jMu', 'date': datetime.datetime(2023, 3, 24, 5, 27, 24, tzinfo=datetime.timezone.utc), 'sizes': [{'_': 'PhotoStrippedSize', 'type': 'i', 'bytes': b'\x01\x12(\xa5\x83\x8f\xbbG>\x82\x9e\xa4\xfa\xd2\xe0\xfa\x9a`G\xcf\xa0\xa3\x9fAR`\xfa\x9a?\xe0F\x80"\xc1\xf4\xa2\x9e~\xb9\xa2\x80\x12\x8a(\xa0\x02\x8a(\xa0\x02\x8a(\xa0\x0f'}, {'_': 'PhotoSize', 'type': 'm', 'w': 320, 'h': 146, 'size': 8697}, {'_': 'PhotoSize', 'type': 'x', 'w': 729, 'h': 333, 'size': 25973}], 'dc_id': 4, 'has_stickers': False, 'video_sizes': []}

#     # Download the photo
#     download_file(photo_dict)

#     # Disconnect from the Telegram server
#     await client.disconnect()

# # Run the main function
# asyncio.run(main())
