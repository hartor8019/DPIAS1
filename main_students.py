import pandas as pd
import os

# Cargar el archivo CSV
# Asumiendo que el archivo CSV está en la misma carpeta que 'src'
import os
os.chdir('C:/Users/USUARIO/proyectosem1')
df = pd.read_csv('src/IMDB top 1000.csv')
#df = pd.read_csv("/src/IMDB top 1000.csv")

# TODO: mostrar los primeros 5 registros de dataframe
print(df.head())

#Usando Sentence Transformer para crear embeddings
from sentence_transformers import SentenceTransformer  # Import the class
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Visualizo los nombre de las columnas
print(df.columns)

embeddings = model.encode(df['Title'],batch_size=64,show_progress_bar=True)

df['embeddings'] = embeddings.tolist()

## Calculando la similitud usando la métrica de similitud por coseno

def compute_similarity(example, query_embedding):
    embedding = example['embeddings'] 
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity  


## Ejecuntando la búsqueda 

from sentence_transformers import util

def search_by_multiple_fields(df, query, fields=['Title', 'Genre']):
  """
  Busca en un DataFrame por múltiples campos.

  Args:
    df: El DataFrame de películas.
    query: La consulta de búsqueda.
    fields: Una lista de los nombres de los campos a buscar.

  Returns:
    Un DataFrame ordenado por similitud.
  """

  query_embedding = model.encode([query])[0]

  df['combined_text'] = df[fields].apply(lambda x: ' '.join(x.dropna()), axis=1)
  # Apply the compute_similarity function to each row of the DataFrame
  df['similarity'] = df.apply(lambda row: compute_similarity(row, query_embedding), axis=1) 
  return df.sort_values(by='similarity', ascending=False)

# Ejemplo de uso:
results = search_by_multiple_fields(df, 'time travel sci-fi', fields=['Title', 'Genre'])
#print(results.head()['Title'])

#Imprimiendo el resultado de la busqueda
print(results.head()[['Title', 'Genre']])

