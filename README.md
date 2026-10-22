# Perfil Literário com K-means

**Objetivo**

Este projeto foi desenvolvido com o objetivo de aplicar uma técnica de aprendizado de máquina não supervisionado para identificar padrões entre livros e formar grupos com características literárias semelhantes.

A partir desses agrupamentos, foi criada uma aplicação em Streamlit na qual o usuário informa suas preferências de leitura. As respostas são processadas pelo modelo, que identifica o cluster mais próximo e apresenta o perfil literário correspondente, além de alguns livros representativos daquele agrupamento.

**Aplicação publicada**

A aplicação está disponível pelo Streamlit no seguinte endereço:

https://perfil-literario-kmeans-3dvbfq7pktmg9tpk6m7z8p.streamlit.app

**Repositório do projeto**

O código e os arquivos utilizados na aplicação estão disponíveis no GitHub:

https://github.com/carolzita-11/perfil-literario-kmeans

**Dataset**

Foi utilizado o dataset público goodbooks-10k, disponível em:

https://github.com/zygmuntz/goodbooks-10k

O dataset contém informações sobre aproximadamente 10 mil livros, incluindo autores, avaliações e tags associadas às obras.

Para a construção dos perfis literários foram utilizadas as relações entre livros e tags. Após a preparação dos dados, 9.402 livros apresentaram informações compatíveis com as características selecionadas para o modelo.

As características consideradas foram fantasia, romance, young adult, mistério, ficção histórica, ficção científica, paranormal, ficção contemporânea, horror, clássicos, aventura, thriller e crime.

**Modelo de Machine Learning**

Foi utilizado o algoritmo K-means, uma técnica de aprendizado não supervisionado utilizada para agrupar elementos com características semelhantes.

Foram testados diferentes valores de K entre 3 e 12. A avaliação foi realizada por meio do Silhouette Score e pela análise da interpretabilidade dos grupos formados.

O melhor resultado foi obtido com K igual a 9, com Silhouette Score aproximado de 0,491.

A partir da análise dos centroides e dos livros mais próximos de cada agrupamento, os nove clusters foram interpretados como Clássicos e Literatura Canônica, Ficção Histórica, Fantasia, Ficção Contemporânea, Mistério, Crime e Thriller, Young Adult, Romance, Horror e Ficção Sombria e Ficção Científica.

**Funcionamento da aplicação**

A interface foi desenvolvida utilizando Streamlit.

O usuário responde a 13 perguntas utilizando valores de 0 a 5, indicando o quanto cada característica combina com suas preferências de leitura.

Antes da classificação, as respostas são normalizadas para manter uma representação compatível com os dados utilizados no treinamento do modelo.

Em seguida, o sistema utiliza o modelo K-means previamente treinado para identificar o centroide mais próximo da entrada fornecida.

Como resultado, são apresentados o perfil literário identificado, uma descrição do perfil, algumas características de maior peso nas respostas e três livros representativos do agrupamento.

O treinamento do modelo não ocorre durante o uso da aplicação. O sistema utiliza apenas o modelo já treinado para realizar a inferência.

**Testes**

Foram realizados cinco casos de teste.

Três testes utilizaram entradas válidas com preferências bem definidas e resultaram nos perfis Fantasia, Romance e Mistério, Crime e Thriller.

Um teste utilizou uma entrada inválida, com todos os valores iguais a zero. Nesse caso, o sistema impediu a classificação e apresentou uma mensagem solicitando que pelo menos uma preferência fosse informada.

Também foi realizado um teste de fronteira, no qual todas as preferências receberam o mesmo valor. Nesse cenário, o sistema classificou a entrada como Horror e Ficção Sombria, selecionando matematicamente o centroide mais próximo mesmo sem uma característica dominante.

Os valores utilizados nos testes e os respectivos resultados estão registrados no arquivo casos_de_teste.txt.

**Limitações**

O sistema possui algumas limitações relacionadas principalmente ao dataset utilizado.

O goodbooks-10k representa um catálogo de um período anterior ao desenvolvimento deste projeto. Por esse motivo, livros mais recentes podem não estar presentes na base.

As tags utilizadas para representar os livros dependem das informações disponíveis no próprio dataset e não abrangem necessariamente todas as características possíveis de uma obra.

As imagens das capas são obtidas por URLs presentes na base. Algumas podem apresentar baixa resolução ou estar indisponíveis.

Além disso, os livros apresentados ao usuário correspondem aos exemplares mais representativos de cada cluster e não constituem um sistema completo de recomendação personalizada.

**Arquivos do projeto**

O arquivo app.py contém a aplicação desenvolvida em Streamlit.

O arquivo modelo_kmeans_livros.pkl contém o modelo K-means treinado.

O arquivo colunas_modelo.pkl armazena a ordem das características utilizadas pelo modelo.

O arquivo livros_app.csv contém os livros processados, seus respectivos clusters e os metadados utilizados pela aplicação.

O arquivo requirements.txt apresenta as bibliotecas e versões necessárias para execução da aplicação.

O arquivo casos_de_teste.txt registra as entradas e os resultados dos casos de teste.

O arquivo dataset_instrucoes.txt apresenta a origem e as instruções para obtenção do dataset utilizado.

O código utilizado para preparação dos dados, treinamento, comparação dos valores de K e avaliação do modelo foi desenvolvido separadamente em notebook.

**Execução**

Para executar o projeto localmente, é necessário instalar as dependências disponíveis no arquivo requirements.txt.

Após a instalação das dependências, a aplicação pode ser iniciada por meio do comando:

streamlit run app.py

**Tecnologias utilizadas**

O projeto foi desenvolvido utilizando Python, Pandas, Scikit-learn, Joblib, Streamlit, Google Colab e GitHub.

**Identificação**

Projeto desenvolvido individualmente por Caroline Eleno Mateus para a disciplina Tópicos Avançados em Inteligência Artificial.
