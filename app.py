from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

@app.post("/webhook/")
async def webhook(request:Request):

    data = await request.json()
    chat_id = data.get('data').get('key').get('remoteJid')
    message = data.get('data').get('message').get('conversation')

    if chat_id and message and not '@g.us' in chat_id:
        print('Grupo Não, apenas contato direto')      
    else: 
        print('BLACKCAT')
    return {'status': 'ok'}
    

