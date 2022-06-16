import dotenv
import os
import json
import asyncio
from telethon import TelegramClient, events

dotenv.load_dotenv()
client = TelegramClient('anon', os.getenv('api_id'), os.getenv('api_hash'))
client.start()

async def out_dir(filename):
    """Вывод специализаций и направлений из json"""
    with open(filename, encoding='utf 8') as f:
        directs = json.load(f)
    return json.loads(json.dumps(directs, indent=4, sort_keys=True, ensure_ascii=False).replace("'", '"'))



@client.on(events.NewMessage([-1001588379468, -1001732996590]))
async def main(event):
    words = await out_dir('cfg.json')
    for nm in words["Words"]:
        if nm in event.text:
            for i in words["Names"]:
                print(f"Message was sent to @{i}: {nm}")
                await client.send_message(i, event.message)

client.run_until_disconnected()
