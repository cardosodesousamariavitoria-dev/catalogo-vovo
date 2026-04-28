import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Enxovais da Vovó",
    page_icon="🛏️",
    layout="wide"
)

telefone = "5563984996508"

# 🎨 ESTILO
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff4f6 0%, #ffffff 100%);
}

h1 {
    text-align: center;
    color: #7a2438;
    font-size: 44px !important;
    font-weight: 800 !important;
}

p, span, div {
    color: #241418 !important;
}

h3 {
    color: #7a2438 !important;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #ffffff;
    border-radius: 18px;
    box-shadow: 0 4px 14px rgba(122, 36, 56, 0.12);
    padding: 12px;
}

.stButton > button, .stLinkButton > a {
    background-color: #25D366 !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 10px 18px !important;
}

img {
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# 🏷️ CABEÇALHO
st.markdown("""
<div style="text-align:center; margin-bottom: 20px;">
    <h1>🛏️ Enxovais da Vovó</h1>
    <p style="font-size:20px;">
        Conforto, qualidade e carinho em cada peça 💖
    </p>
</div>
""", unsafe_allow_html=True)

st.success("💳 Pix e dinheiro | 📲 Pedido direto pelo WhatsApp")

# 📦 PRODUTOS ORGANIZADOS
produtos = [
    {
        "nome": "Jogo de Lençol Casal com Elástico",
        "preco": 130.00,
        "descricao": "Lençol + 2 fronhas | Macio e confortável",
        "imagem": "lencol1.jpg",
        "tamanho": "Casal",
        "cores": "Floral rosa",
        "disponivel": False
    },

    # TOALHAS
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Alta absorção e toque macio",
        "imagem": "toalha1.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "Vermelha",
        "disponivel": True
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Macia e confortável",
        "imagem": "toalha2.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "Azul escuro",
        "disponivel": True
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Toque suave",
        "imagem": "toalha3.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "Azul claro",
        "disponivel": True
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Conforto no dia a dia",
        "imagem": "toalha4.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "Verde",
        "disponivel": True
    },

    # LENÇOL SOLTEIRO
    {
        "nome": "Jogo de Lençol Solteiro com Elástico",
        "preco": 100.00,
        "descricao": "Lençol + 1 fronha",
        "imagem": "lencolsolteiro.jpg.jpeg",
        "tamanho": "1,30m x 2,40m",
        "cores": "Floral rosa",
        "disponivel": True
    },

    # LENÇÓIS
    {
        "nome": "Lençol para Cobrir",
        "preco": 100.00,
        "descricao": "Leve e confortável",
        "imagem": "lencol1.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Cinza",
        "disponivel": True
    },
    {
        "nome": "Lençol para Cobrir",
        "preco": 100.00,
        "descricao": "Macio e agradável",
        "imagem": "lencol2.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Verde com folhas",
        "disponivel": True
    },
    {
        "nome": "Lençol para Cobrir",
        "preco": 100.00,
        "descricao": "Conforto garantido",
        "imagem": "lencol3.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Rosa com bolinhas",
        "disponivel": True
    },

    # EDREDOM
    {
        "nome": "Edredom",
        "preco": 160.00,
        "descricao": "Quentinho e confortável",
        "imagem": "edredom.jpg.jpeg",
        "tamanho": "Grande",
        "cores": "Rosa com flores",
        "disponivel": True
    },

    # MANTA
    {
        "nome": "Manta",
        "preco": 160.00,
        "descricao": "Ideal para dias frios",
        "imagem": "manta.jpg.jpeg",
        "tamanho": "Grande",
        "cores": "Marrom e cinza",
        "disponivel": True
    },

    # PANO
    {
        "nome": "Pano de Prato",
        "preco": 20.00,
        "descricao": "Resistente e útil no dia a dia",
        "imagem": "Pano de prato.jpg.jpeg",
        "tamanho": "Padrão",
        "cores": "Estampado",
        "disponivel": True
    },
]

# 🧱 GRID
cols = st.columns(3)

for i, produto in enumerate(produtos):
    with cols[i % 3]:
        with st.container(border=True):

            try:
                st.image(f"imagens/{produto['imagem']}", use_container_width=True)
            except:
                st.warning("Imagem não encontrada")

            st.subheader(produto["nome"])
            st.markdown(f"✨ {produto['descricao']}")
            st.write(f"📏 {produto['tamanho']}")
            st.write(f"🎨 {produto['cores']}")

            preco = f"R$ {produto['preco']:.2f}".replace(".", ",")
            st.markdown(f"### 💰 {preco}")

            if produto["disponivel"]:
                st.success("Disponível")

                mensagem = f"""Olá! Tenho interesse:

Produto: {produto['nome']}
Cor: {produto['cores']}
Preço: {preco}"""

                link = f"https://wa.me/{telefone}?text={quote(mensagem)}"
                st.link_button("📲 Comprar no WhatsApp", link)

            else:
                st.error("Indisponível")
                st.button("Indisponível", disabled=True, key=i)

st.write("---")
st.write("💖 Atendimento via WhatsApp")

