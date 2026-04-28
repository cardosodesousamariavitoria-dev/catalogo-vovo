import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Enxovais da Vovó",
    page_icon="🛏️",
    layout="wide"
)

telefone = "5563984996508"

st.markdown("""
<style>
.stApp {
    background-color: #fff7f8;
}
.titulo {
    text-align: center;
    color: #9b3f57;
    font-size: 46px;
    font-weight: 800;
}
.subtitulo {
    text-align: center;
    color: #5c2d35;
    font-size: 20px;
    margin-bottom: 25px;
}
.card {
    background-color: white;
    padding: 18px;
    border-radius: 20px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.10);
    margin-bottom: 25px;
}
.preco {
    color: #b83250;
    font-size: 28px;
    font-weight: 800;
}
.info {
    background-color: #ffe3ea;
    padding: 14px;
    border-radius: 14px;
    text-align: center;
    color: #7a2e43;
    font-size: 18px;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>🛏️ Enxovais da Vovó</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Conforto, qualidade e carinho em cada peça 💖</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='info'>💳 Pagamento via Pix e dinheiro | 📲 Pedido direto pelo WhatsApp</div>",
    unsafe_allow_html=True
)

produtos = [
    {
        "nome": "Jogo de Lençol Casal com elástico Floral",
        "preco": 130.00,
        "descricao": "Lençol + 2 fronhas",
        "imagem": "lencol1.jpg",
        "tamanho": "Casal",
        "cores": "Floral rosa",
        "disponivel": False
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Toalha grande e macia",
        "imagem": "toalha1.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "vermelha",
        "disponivel": True
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Toalha grande e macia",
        "imagem": "toalha2.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "azul escuro",
        "disponivel": True
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Toalha grande e macia",
        "imagem": "toalha3.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "azul claro",
        "disponivel": True
    },
    {
        "nome": "Toalha de Banho",
        "preco": 70.00,
        "descricao": "Toalha grande e macia",
        "imagem": "toalha4.jpg.jpeg",
        "tamanho": "75cm x 1,50m",
        "cores": "verde",
        "disponivel": True
    },
    {
        "nome": "Jogo de Lençol de solteiro com elástico Floral",
        "preco": 100.00,
        "descricao": "Lençol + 1 fronha",
        "imagem": "lencolsolteiro.jpg.jpeg",
        "tamanho": "1,30m x 2,40m",
        "cores": "Floral rosa",
        "disponivel": True
    },
    {
        "nome": "Lençol de virol (cobrir)",
        "preco": 100.00,
        "descricao": "Lençol",
        "imagem": "lencol1.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Cinza",
        "disponivel": True
    },
    {
        "nome": "Lençol de virol (cobrir)",
        "preco": 100.00,
        "descricao": "Lençol",
        "imagem": "lencol2.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Verde com folhas marrons",
        "disponivel": True
    },
    {
        "nome": "Lençol de virol (cobrir)",
        "preco": 100.00,
        "descricao": "Lençol",
        "imagem": "lencol3.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Rosa com bolinha",
        "disponivel": True
    },
    {
        "nome": "Lençol de virol (cobrir)",
        "preco": 100.00,
        "descricao": "Lençol",
        "imagem": "lencol4.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Verde com listras pretas",
        "disponivel": True
    },
    {
        "nome": "Lençol de virol (cobrir)",
        "preco": 100.00,
        "descricao": "Lençol",
        "imagem": "lencol5.jpg.jpeg",
        "tamanho": "1,80m x 2,40m",
        "cores": "Rosa tropical",
        "disponivel": True
    },
    {
        "nome": "Edredom",
        "preco": 160.00,
        "descricao": "Edredom",
        "imagem": "edredom.jpg.jpeg",
        "tamanho": "Grande",
        "cores": "Rosa com flores",
        "disponivel": True
    },
    {
        "nome": "Manta",
        "preco": 160.00,
        "descricao": "Manta",
        "imagem": "manta.jpg.jpeg",
        "tamanho": "Grande",
        "cores": "Marrom, cinza e branca",
        "disponivel": True
    },
    {
        "nome": "Pano de prato",
        "preco": 20.00,
        "descricao": "Pano de prato",
        "imagem": "Pano de prato.jpg.jpeg",
        "tamanho": "Padrão",
        "cores": "Brancos com estampas",
        "disponivel": True
    },
]

cols = st.columns(3)

for i, produto in enumerate(produtos):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        try:
            st.image(f"imagens/{produto['imagem']}", use_container_width=True)
        except:
            st.warning("Imagem não encontrada")

        st.markdown(f"### {produto['nome']}")
        st.write(produto["descricao"])
        st.write(f"📏 **Tamanho:** {produto['tamanho']}")
        st.write(f"🎨 **Cor/estampa:** {produto['cores']}")

        preco_formatado = f"R$ {produto['preco']:.2f}".replace(".", ",")
        st.markdown(f"<div class='preco'>{preco_formatado}</div>", unsafe_allow_html=True)

        if produto["disponivel"]:
            st.success("✅ Em estoque")

            mensagem = f"""Olá! Tenho interesse neste produto:

Produto: {produto['nome']}
Descrição: {produto['descricao']}
Tamanho: {produto['tamanho']}
Cor/estampa: {produto['cores']}
Preço: {preco_formatado}

Pode me passar mais informações?"""

            link = f"https://wa.me/{telefone}?text={quote(mensagem)}"

            st.link_button("📲 Pedir no WhatsApp", link)
        else:
            st.error("❌ Indisponível no momento")
            st.button("Indisponível", disabled=True, key=f"ind_{i}")

        st.markdown("</div>", unsafe_allow_html=True)

st.write("---")
st.markdown(
    "<p style='text-align:center;'>📲 Atendimento direto pelo WhatsApp | Feito com carinho 💖</p>",
    unsafe_allow_html=True
)


