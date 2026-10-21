
import streamlit as st
import pandas as pd
import joblib


# =====================================================
# CONFIGURAÇÃO
# =====================================================

st.set_page_config(
    page_title="Perfil Literário",
    page_icon="📖",
    layout="centered"
)


# =====================================================
# CARREGAMENTO DOS ARQUIVOS
# =====================================================

modelo = joblib.load(
    "modelo_kmeans_livros.pkl"
)

colunas_modelo = joblib.load(
    "colunas_modelo.pkl"
)

livros = pd.read_csv(
    "livros_com_perfis.csv"
)

books_meta = pd.read_csv(
    "books.csv"
)

livros = livros.merge(
    books_meta[
        [
            "book_id",
            "small_image_url",
            "image_url",
            "average_rating",
            "original_publication_year"
        ]
    ],
    on="book_id",
    how="left"
)


# =====================================================
# PERFIS
# =====================================================

nomes_clusters = {
    0: "Clássicos & Literatura Canônica",
    1: "Ficção Histórica",
    2: "Fantasia",
    3: "Ficção Contemporânea",
    4: "Mistério, Crime & Thriller",
    5: "Young Adult",
    6: "Romance",
    7: "Horror & Ficção Sombria",
    8: "Ficção Científica"
}


descricoes_clusters = {
    0: (
        "Você se aproxima de obras clássicas e consagradas, histórias que "
        "atravessaram gerações e continuam relevantes pela força de seus "
        "temas, personagens e conflitos."
    ),

    1: (
        "Você demonstra afinidade com narrativas que transportam o leitor "
        "para outros períodos e exploram acontecimentos, costumes e conflitos "
        "marcados pelo contexto histórico."
    ),

    2: (
        "Mundos imaginários, magia, criaturas extraordinárias e grandes "
        "jornadas tendem a chamar sua atenção. Seu perfil combina com histórias "
        "que expandem os limites da realidade."
    ),

    3: (
        "Seu perfil se aproxima de histórias ligadas à vida cotidiana, "
        "relações humanas, conflitos pessoais e experiências reconhecíveis "
        "no mundo contemporâneo."
    ),

    4: (
        "Mistérios, investigações, crimes, segredos e tensão narrativa aparecem "
        "com força nas suas preferências. Você tende a gostar de histórias "
        "que mantêm perguntas abertas até as últimas páginas."
    ),

    5: (
        "Descobertas pessoais, amadurecimento, relações intensas e grandes "
        "mudanças fazem parte do seu perfil. Fantasia, romance e aventura "
        "também costumam dividir espaço nessas histórias."
    ),

    6: (
        "Relacionamentos, emoções e conflitos afetivos têm bastante peso nas "
        "suas preferências. Seu perfil se aproxima de histórias em que os "
        "vínculos entre personagens ocupam o centro da narrativa."
    ),

    7: (
        "Atmosferas inquietantes, acontecimentos perturbadores, suspense e "
        "elementos sobrenaturais aparecem com força nas suas escolhas. "
        "Seu perfil combina com narrativas mais sombrias e intensas."
    ),

    8: (
        "Tecnologia, futuros possíveis, sociedades alternativas, espaço e "
        "especulação científica chamam sua atenção. Seu perfil gosta de usar "
        "a imaginação para explorar possibilidades além do presente."
    )
}


# =====================================================
# ESTILO
# =====================================================

st.markdown(
    """
    <style>

    .block-container {
        max-width: 920px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    .stApp,
    .stApp p,
    .stApp span,
    .stApp div,
    .stApp label,
    .stApp button,
    .stApp input {
        font-family: "Trebuchet MS", "Segoe UI", Arial, sans-serif !important;
    }

    .stApp p {
        color: #352727 !important;
        line-height: 1.6;
    }

    .stApp label {
        color: #2B2020 !important;
        font-weight: 500 !important;
    }

    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4 {
        font-family: "Trebuchet MS", "Segoe UI", Arial, sans-serif !important;
        color: #4D0E13 !important;
    }

    .stApp h1 {
        font-size: 3rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.04em !important;
        line-height: 1.05 !important;
    }

    .stApp h2 {
        font-weight: 700 !important;
    }

    .stApp h3 {
        font-weight: 650 !important;
    }

    [data-testid="stCaptionContainer"] {
        color: #795653 !important;
        font-weight: 500 !important;
    }

    [data-testid="stCaptionContainer"] p {
        color: #795653 !important;
    }

    [data-testid="stMetricLabel"] {
        color: #6F4D4A !important;
        font-weight: 600 !important;
    }

    [data-testid="stMetricValue"] {
        color: #4D0E13 !important;
        font-weight: 700 !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #D8C4AC !important;
        border-radius: 18px !important;
        background-color: #F5EAE3 !important;
    }

    div[data-baseweb="slider"] {
        color: #4D0E13 !important;
    }

    /* BOTÃO — CORRIGIDO */

    div.stButton > button {
        background-color: #4D0E13 !important;
        color: #EEE4DA !important;
        border: 1px solid #4D0E13 !important;
        border-radius: 12px !important;
        padding: 0.85rem 1.2rem !important;
        font-weight: 700 !important;
        width: 100% !important;
        transition: 0.2s !important;
    }

    div.stButton > button p,
    div.stButton > button span,
    div.stButton > button div {
        color: #EEE4DA !important;
        font-weight: 700 !important;
    }

    div.stButton > button:hover {
        background-color: #68181F !important;
        color: #FFFFFF !important;
        border-color: #68181F !important;
    }

    div.stButton > button:hover p,
    div.stButton > button:hover span,
    div.stButton > button:hover div {
        color: #FFFFFF !important;
    }

    hr {
        border-color: #D8C4AC !important;
        opacity: 0.85 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# CABEÇALHO
# =====================================================

with st.container(border=True):

    st.caption("DESCUBRA SEU PERFIL DE LEITURA")

    st.title("Que tipo de história te encontra primeiro?")

    st.write(
        "Seu gosto por leitura vai além de um gênero favorito. "
        "Conte o que costuma prender sua atenção e o modelo "
        "identificará o perfil literário que mais se aproxima "
        "das suas preferências."
    )


# =====================================================
# RESUMO TÉCNICO
# =====================================================

st.write("")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Perfis possíveis",
        "9"
    )

with m2:
    st.metric(
        "Livros analisados",
        "9.402"
    )

with m3:
    st.metric(
        "Características",
        "13"
    )

st.divider()


# =====================================================
# QUESTIONÁRIO
# =====================================================

st.subheader("Suas preferências")

st.write(
    "Para cada afirmação, escolha um valor entre **0 e 5**. "
    "Não existem respostas certas ou erradas."
)

st.caption(
    "0 = não combina comigo  ·  5 = combina muito comigo"
)

st.write("")


q1 = st.slider(
    "Quanto você gosta de histórias ambientadas em mundos diferentes do nosso, com magia ou elementos extraordinários?",
    0, 5, 0
)

q2 = st.slider(
    "Quanto um relacionamento amoroso influencia sua vontade de continuar uma história?",
    0, 5, 0
)

q3 = st.slider(
    "Quanto você gosta de acompanhar personagens jovens descobrindo quem são e encontrando seu lugar no mundo?",
    0, 5, 0
)

q4 = st.slider(
    "Você gosta de narrativas envolvendo investigações, segredos, pistas ou acontecimentos que precisam ser desvendados?",
    0, 5, 0
)

q5 = st.slider(
    "Quanto você se interessa por histórias ambientadas em outras épocas ou relacionadas a acontecimentos históricos?",
    0, 5, 0
)

q6 = st.slider(
    "Quanto você gosta de histórias sobre tecnologia, futuros possíveis, espaço ou sociedades diferentes da nossa?",
    0, 5, 0
)

q7 = st.slider(
    "Quanto você gosta de elementos sobrenaturais, criaturas inexplicáveis ou acontecimentos fora do comum?",
    0, 5, 0
)

q8 = st.slider(
    "Quanto você prefere histórias próximas da vida real, centradas em relações, cotidiano e conflitos pessoais?",
    0, 5, 0
)

q9 = st.slider(
    "Quanto você gosta de histórias sombrias, perturbadoras ou capazes de provocar medo e tensão?",
    0, 5, 0
)

q10 = st.slider(
    "Quanto você aprecia obras antigas ou consagradas que continuam sendo lidas ao longo das gerações?",
    0, 5, 0
)

q11 = st.slider(
    "Quanto você gosta de jornadas, exploração, perigos e personagens enfrentando grandes desafios?",
    0, 5, 0
)

q12 = st.slider(
    "Quanto você gosta de histórias aceleradas, tensas e cheias de reviravoltas?",
    0, 5, 0
)

q13 = st.slider(
    "Quanto você se interessa por histórias envolvendo crimes, criminosos ou investigação policial?",
    0, 5, 0
)

st.write("")


# =====================================================
# BOTÃO
# =====================================================

clicou = st.button(
    "Descobrir meu perfil literário →",
    type="primary"
)


# =====================================================
# RESULTADO
# =====================================================

if clicou:

    respostas = [
        q1, q2, q3, q4, q5, q6, q7,
        q8, q9, q10, q11, q12, q13
    ]

    soma = sum(respostas)

    if soma == 0:

        st.warning(
            "Antes de continuar, marque pelo menos uma preferência."
        )

    else:

        respostas_normalizadas = [
            valor / soma
            for valor in respostas
        ]

        entrada = pd.DataFrame(
            [respostas_normalizadas],
            columns=colunas_modelo
        )

        cluster = int(
            modelo.predict(entrada)[0]
        )

        perfil = nomes_clusters[cluster]
        descricao = descricoes_clusters[cluster]

        st.write("")
        st.divider()


        # =====================================================
        # PERFIL
        # =====================================================

        with st.container(border=True):

            st.caption(
                "SEU PERFIL LITERÁRIO"
            )

            st.header(
                perfil
            )

            st.write(
                descricao
            )

            entrada_series = (
                entrada.iloc[0]
                .sort_values(
                    ascending=False
                )
            )

            principais = (
                entrada_series
                .head(3)
                .index
                .tolist()
            )

            nomes_exibicao = {
                "fantasy": "Fantasia",
                "romance": "Romance",
                "young_adult": "Young Adult",
                "mystery": "Mistério",
                "historical_fiction": "Ficção histórica",
                "science_fiction": "Ficção científica",
                "paranormal": "Paranormal",
                "contemporary": "Contemporâneo",
                "horror": "Horror",
                "classics": "Clássicos",
                "adventure": "Aventura",
                "thriller": "Thriller",
                "crime": "Crime"
            }

            principais_texto = " · ".join(
                nomes_exibicao[item]
                for item in principais
            )

            st.caption(
                "Traços que mais pesaram nas suas respostas: "
                + principais_texto
            )

        st.write("")


        # =====================================================
        # RECOMENDAÇÕES
        # =====================================================

        st.subheader(
            "Talvez sua próxima leitura esteja aqui"
        )

        st.write(
            "Estes livros estão entre os mais próximos "
            "do centro do perfil identificado pelo modelo."
        )

        livros_cluster = livros[
            livros["cluster"] == cluster
        ].copy()

        centro = modelo.cluster_centers_[cluster]

        livros_cluster["distancia"] = (
            (
                livros_cluster[
                    colunas_modelo
                ].values
                - centro
            ) ** 2
        ).sum(axis=1)

        recomendacoes = (
            livros_cluster
            .sort_values(
                "distancia"
            )
            .head(3)
        )

        cards = st.columns(
            3,
            gap="medium"
        )

        for coluna, (_, livro) in zip(
            cards,
            recomendacoes.iterrows()
        ):

            with coluna:

                with st.container(
                    border=True
                ):

                    imagem = livro[
                        "image_url"
                    ]

                    if pd.notna(
                        imagem
                    ):

                        st.image(
                            imagem,
                            use_container_width=True
                        )

                    st.markdown(
                        f"**{livro['title']}**"
                    )

                    st.caption(
                        str(
                            livro["authors"]
                        )
                    )

                    detalhes = []

                    if pd.notna(
                        livro[
                            "average_rating"
                        ]
                    ):

                        detalhes.append(
                            "★ "
                            + f"{float(livro['average_rating']):.2f}"
                        )

                    if pd.notna(
                        livro[
                            "original_publication_year"
                        ]
                    ):

                        detalhes.append(
                            str(
                                int(
                                    livro[
                                        "original_publication_year"
                                    ]
                                )
                            )
                        )

                    if detalhes:

                        st.write(
                            " · ".join(
                                detalhes
                            )
                        )

        st.write("")

        st.caption(
            "As recomendações são exemplos representativos "
            "do agrupamento e não constituem um sistema "
            "tradicional de recomendação individual."
        )
