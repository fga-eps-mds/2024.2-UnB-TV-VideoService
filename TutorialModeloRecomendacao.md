# Tutorial de como atualizar o modelo de recomendação de vídeos

Este é um tutorial sobre como atualizar os arquivos necessários para o funcionamento do modelo de recomendação. **Este tutorial deve ser executado sempre que novos vídeos forem adicionados ao catálogo da UnBTV.**

## 1. Instalar pendências

É necessário instalar algumas bibliotecas em Python para a criação do modelo:

```pip install pandas==1.5.0```

## 2. Atualizar o modelo

Para atualizar o modelo, é necessário executar o arquivo que produz o modelo (cosine_similarity.pkl) e o DataFrame de vídeos (df_videos.csv):

```python3 recomendation_model/renew_model.py```

Assim, os novos vídeos serão adicionados no DataFrame de busca, além de também serem usados no cálculo de similaridade.