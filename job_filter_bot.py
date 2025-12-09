import os
import re
from telethon import TelegramClient, events

# --- CONFIGURACIÓN ---
# Usa variables de entorno para seguridad (recomendado para deployment)
# O valores por defecto para desarrollo local
api_id = int(os.getenv('API_ID', '23002451'))
api_hash = os.getenv('API_HASH', '57526374f7d847472ac30c4ec396afb4')

# Lista de canales a escuchar (pueden ser @username o enlaces de invitación)
# IMPORTANTE: Tu cuenta debe estar unida a estos canales.
# Agrega más canales separados por comas, ejemplo:
# target_channels = ['@JScript_jobs', '@otro_canal', '@canal_trabajos']
target_channels = [
    '@JScript_jobs',
    '@Frontend_Jobs',
    '@Remoteit',
    # Agrega más canales aquí:
    # '@nombre_canal_2',
    # '@nombre_canal_3',
]

# Palabras clave a buscar (puedes añadir más)
keywords = ['react', 'react native', 'frontend', 'javascript', 'desarrollador', 'developer']

# --- INICIO DEL CLIENTE ---
client = TelegramClient('job_checker_session', api_id, api_hash)

print("🤖 Bot iniciado. Escuchando ofertas...")

@client.on(events.NewMessage(chats=target_channels))
async def handler(event):
    # Convertimos el texto a minúsculas para facilitar la búsqueda
    text = event.raw_text.lower()
    
    # Lógica de filtrado
    # Usamos regex word boundaries (\b) para evitar falsos positivos 
    # (ej: que no detecte "reaction" si buscas "react")
    found_keywords = []
    for k in keywords:
        # \b asegura que sea la palabra exacta o rodeada de espacios/puntuación
        if re.search(r'\b' + re.escape(k) + r'\b', text):
            found_keywords.append(k)

    if found_keywords:
        print(f"✅ Oferta encontrada en {event.chat.title}")
        
        # Crear un mensaje resumen
        summary = "**🎯 OFERTA DETECTADA**\n"
        summary += f"**Palabras clave:** {', '.join(found_keywords)}\n"
        summary += f"**Origen:** {event.chat.title}\n"
        summary += "-----------------------\n"
        
        # Enviar a tus "Mensajes Guardados" (Saved Messages)
        await client.send_message('me', summary)
        
        # Reenviar el mensaje original para tener todo el contexto/enlaces
        await client.forward_messages('me', event.message)

# Iniciar el cliente
client.start()
client.run_until_disconnected()

