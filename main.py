import datetime
from telethon import TelegramClient, events

api_id = 'your_api_id'
api_hash = 'your_api_hash'
source_channel = 'air_alert_ua'
alerts_channel = 'some_channel'

client = TelegramClient('alertskh', api_id, api_hash)
@client.on(events.NewMessage(chats=source_channel))

async def my_event_handler(event):
    with open('alertskh.log', 'a') as file:
        file.write(f'{datetime.datetime.now()} New message received')
    if 'Харківська' in event.raw_text:
        metadata = await client.get_entity(alerts_channel)
        await client.send_message(entity=metadata, message=event.raw_text)

client.start()
client.run_until_disconnected()