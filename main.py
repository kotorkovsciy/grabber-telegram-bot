import dotenv
import os
import json
from telethon import TelegramClient, events

dotenv.load_dotenv()
client = TelegramClient('anon', os.getenv('api_id'), os.getenv('api_hash'))
client.start()


with open('cfg.json', encoding='utf 8') as f:
    directs = json.load(f)
words = json.loads(json.dumps(directs, indent=4, sort_keys=True,
                   ensure_ascii=False).replace("'", '"'))


@client.on(events.NewMessage(words["Chat_IDs"]))
async def main(event):
    for nm in words["Words"]:
        if nm in event.text:
            for i in words["Names"]:
                print(f"Message was sent to @{i}: {nm}")
                await client.send_message(i, event.message)

client.run_until_disconnected()
