from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Claves de acceso a Text Analytics
key = ""
endpoint = ""

# Crea una instancia del cliente de Text Analytics
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Texto de ejemplo
text = "No llames, no volvere contigo, me fuiste infiel"

# Detecta el sentimiento del texto
result = client.analyze_sentiment(documents=[text])[0]

# Muestra el resultado
print("Texto: ", text)
print("Sentimiento: ", result.sentiment)
print("Puntuación positiva: ", result.confidence_scores.positive)
print("Puntuación negativa: ", result.confidence_scores.negative)
print("Puntuación neutral: ", result.confidence_scores.neutral)
