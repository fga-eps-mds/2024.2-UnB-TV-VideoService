from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

from utils.constants import PORTUGUESE_STOP_WORDS

from utils.model import Catalog

from utils.get_videos import find_all_videos, videos_to_dataframe
from utils.categorize_videos import categorize_videos

# Calcula similaridade dos vídeos a partir da distância dos cossenos (cosine distance)
def calculate_similarity(df):
    tfidf = TfidfVectorizer(stop_words=PORTUGUESE_STOP_WORDS)
    tfidf_matrix = tfidf.fit_transform(df['Descrição'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

if __name__ == "__main__":
    catalog = Catalog()
    videos = find_all_videos()
    
    if videos:
        # Categorização dos vídeos
        categorize_videos(videos, catalog)
        
        # Cria e salva o DataFrame com os vídeos
        df = videos_to_dataframe(videos)
        df.to_csv('../src/recommendation_model/df_videos.csv')

        cosine_sim = calculate_similarity(df)

        with open('../src/recommendation_model/cosine_similarity.pkl', 'wb') as f:
            pickle.dump(cosine_sim, f)
    else:
        print("Nenhum vídeo encontrado.")