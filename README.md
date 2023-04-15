#Comparación de etiquetas entre dos imágenes
Este script compara las etiquetas de dos imágenes obtenidas mediante el servicio de reconocimiento de imágenes de Azure Cognitive Services. Las etiquetas son palabras clave que describen el contenido de la imagen y se obtienen mediante la API analyzede Azure.

#Requisitos
Pitón 3.x
Librería requestsinstalada. Puedes instalarla mediante el comando pip install requests.
Una cuenta de Azure Cognitive Services con la suscripción activa y la API de reconocimiento de imágenes habilitada. Debes tener una clave de suscripción ( subscription_key) y el endpoint correspondiente ( endpoint).

#How to use
Asigna la clave de suscripción y el endpoint a las variables subscription_keyy endpoint, respectivamente, en el archivo config.py.
Asigna las URL de las dos imágenes que quieres comparar a las variables image1_urle image2_url, respectivamente, en el script.
Ejecuta el script en la terminal mediante el comando python comparison_script.py.

#Resultado
El script imprimirá en la terminal las etiquetas comunes encontradas en ambas imágenes.

#Aviso de privacidad
Ten en cuenta que las imágenes que se envían a Azure Cognitive Services para su análisis pueden contener información personal y sensible. Asegúrese de tener el consentimiento del propietario de la imagen antes de utilizar este script. Además, si desea mantener la privacidad de sus credenciales de Azure, asegúrese de que el archivo config.pyno sea visible públicamente.





