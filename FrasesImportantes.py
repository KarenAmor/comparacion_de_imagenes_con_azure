from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Configurar las credenciales y el cliente del servicio de Text Analytics
key = ""
endpoint = ""
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Definir el texto para analizar
text = "En biología, una flor es la estructura reproductiva característica de las plantas angiospermas. Consiste en una serie de hojas modificadas que rodean los órganos reproductores, como los estambres y el pistilo. Las flores pueden tener diversas formas, tamaños y colores, y su función principal es la reproducción sexual mediante la producción y dispersión de semillas. Las flores también pueden ser importantes en la polinización, ya sea por el viento, el agua o los animales, como los insectos y los pájaros"
# Llamar a la función para extraer las frases clave
response = client.extract_key_phrases(documents=[text])[0]

# Imprimir las frases clave identificadas
if not response.is_error:
    print("Frases clave:")
    for phrase in response.key_phrases:
        print("\t", phrase)
else:
    print(response.id, response.error)
