import requests
import json
from config import subscription_key, endpoint

# Configurar la solicitud
analyze_url = endpoint + 'vision/v3.0/analyze'

# Configurar los parámetros de la solicitud
params = {'visualFeatures': 'Categories,Description,Color'}
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}

# Función para obtener las etiquetas de una imagen
def get_image_tags(image_url):
    # Cargar la imagen desde la web
    image_data = requests.get(image_url).content

    # Enviar la solicitud
    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)

    # Analizar la respuesta
    response.raise_for_status()
    analysis = response.json()

    # Devolver las etiquetas encontradas
    return analysis['description']['tags']

# URLs de las dos imágenes a comparar
image1_url = 'https://media.licdn.com/dms/image/D4D03AQEI5aKzAD2J2w/profile-displayphoto-shrink_800_800/0/1680821070094?e=1686787200&v=beta&t=9rghMU6wf0Qzg47z8qgU7RRwPbCSVQ5Gr9s9Bw4lBVw'
image2_url = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg'

# Obtener las etiquetas de cada imagen
image1_tags = get_image_tags(image1_url)
image2_tags = get_image_tags(image2_url)

# Comparar las etiquetas encontradas
common_tags = set(image1_tags).intersection(set(image2_tags))
print('Etiquetas comunes encontradas en ambas imágenes:')
print(common_tags)