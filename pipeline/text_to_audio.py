# text_audio.py
import asyncio
import edge_tts

OUTPUT_FILE = "test.mp3"

async def generate_audio(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(OUTPUT_FILE)

def generate_audio_sync(text, voice):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(generate_audio(text, voice))
    loop.close()
