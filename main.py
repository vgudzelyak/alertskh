from datetime import datetime, timezone
from asyncio import sleep
from telethon import TelegramClient

api_id = 'your_api_id'
api_hash = 'your_api_hash'
source_channel = 'air_alert_ua'
alerts_channel = 'some_channel'
region_name = 'Харківська'
log_file = 'alertskh.log'
message_id_file = 'sent_id.txt'

client = TelegramClient('notificationbotua', api_id, api_hash)

async def main():
    while True:
        try:
            with open(message_id_file, 'r') as file:
                raw_value = file.read()
                if raw_value:
                    sent_id = int(raw_value)
                else:
                    sent_id = 0
            messages = await client.get_messages(source_channel, limit=5, offset_id=0)
            for message in messages:
                if (datetime.now(timezone.utc) - datetime.strptime(str(message.date), '%Y-%m-%d %H:%M:%S+00:00').replace(tzinfo=timezone.utc)).seconds < 120:
                    if region_name in message.message and sent_id != message.id:
                        metadata = await client.get_entity(alerts_channel)
                        await client.send_message(entity=metadata, message=message.message)
                        with open(message_id_file, 'w') as file:
                            file.write(str(message.id))
                        with open(log_file, 'a') as file:
                            file.write(f'\n{datetime.now()} {message.message}')
            await sleep(60)
        except Exception as error:
            with open(log_file, 'a') as file:
                file.write(f'\n{datetime.now()} {error}')

client.start()
client.loop.run_until_complete(main())