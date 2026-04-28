import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Enxovais da Vovó",
    page_icon="🛏️",
    layout="wide"
)

telefone = "5563984996508"

# 🎨 ESTILO (cores corrigidas)
st.markdown("""
<style>
.stApp {
    background-color: #fff7f8;
}

/* TÍTULO */
.titulo {
    text-align: center;
    color: #7a1f35;
    font-size: 46px;
    font-weight: 800;
}

/* SUBTÍTULO */
.subtitulo {
    text-align: center;
    color: #3a1f24;
    font-size: 20px;
    margin-bottom: 25px;
}

/* CARD */
.card {
    background-color: white;
    padding: 18px;
    border-radius: 20px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.12);
    margin-bottom: 25px;
}

/* TEXTO */
.card p {
    color: #1a1a1a !important;
}

/* NOME DO PRODUTO */
.card h3 {
    color: #2b0d14 !important;
    font-weight: 700;
}

/* PREÇO */
.preco {
    color: #c1121f;
    font-size: 28px;
    font-weight: 800;
}

/* INFO */
.info {
    background-color: #ffd6e0;
    padding: 14px;
    border-radius: 14px;
    text-align: center;
    color: #4a1c27;
    font-size: 18px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# 🏷️ TÍTULO
st.markdown("<div class='titulo'>🛏️ Enxovais da Vovó</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Conforto, qualidade e carinho em cada peça 💖</div>", unsafe_allow_html=True)

# 📢 INFO
st.markdown(
    "<div class='info'>💳 Pagamento via Pix e dinheiro | 📲 Pedido direto pelo WhatsApp</div>",
    unsafe_allow_html=True
)

# 📦 PRODUTOS
produtos = [
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Toalha grande, macia e super confortável",
        "imagem": "toalha1.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "Vermelha",
        "disponivel": True
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Alta absorção e toque suave",
        "imagem": "toalha2.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "Azul escuro",
        "disponivel": True
    },
    {
        "nome": "Lençol de Virol",
        "preco": 100.00,
        "descricao": "Ideal para se cobrir, tecido leve e confortável",
        "imagem": "lencol1.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Cinza",
        "disponivel": True
    },
    {
        "nome": "Edredom",
        "preco": 160.00,
        "descricao": "Super quentinho e macio",
        "imagem": "edredon.jpg.jpeg",
        "tamanho": "Grande",
        "cores": "Rosa com flores",
        "disponivel": True
    },
    {
        "nome": "Manta",
        "preco": 160.00,
        "descricao": "Perfeita para dias frios",
        "imagem": "manta.jpg.jpeg",
        "tamanho": "Grande",
        "cores": "Marrom e cinza",
        "disponivel": True
    },
]

# 🧱 LAYOUT
cols = st.columns(3)

for i, produto in enumerate(produtos):
    with cols[i % 3]:
        with st.container(border=True):

            try:
                st.image(f"imagens/{produto['imagem']}", use_container_width=True)
            except:
                st.warning("Imagem não encontrada")

            st.markdown(f"### {produto['nome']}")
            st.write(produto["descricao"])
            st.write(f"📏 **Tamanho:** {produto['tamanho']}")
            st.write(f"🎨 **Cor:** {produto['cores']}")

            preco = f"R$ {produto['preco']:.2f}".replace(".", ",")
            st.markdown(f"<div class='preco'>{preco}</div>", unsafe_allow_html=True)

            if produto["disponivel"]:
                st.success("✅ Em estoque")

                mensagem = f"""Olá! Tenho interesse neste produto:

Produto: {produto['nome']}
Tamanho: {produto['tamanho']}
Cor: {produto['cores']}
Preço: {preco}

Pode me passar mais informações?"""

                link = f"https://wa.me/{telefone}?text={quote(mensagem)}"
                st.link_button("📲 Pedir no WhatsApp", link)
            else:
                st.error("❌ Indisponível")
                st.button("Indisponível", disabled=True, key=f"ind_{i}")


