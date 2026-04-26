import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Catálogo da Vovó",
    page_icon="🛏️",
    layout="wide"
)

telefone = "5563984996508"

st.title("🛏️ Catálogo de Cama, Mesa e Banho")
st.write("Escolha seu produto e peça direto pelo WhatsApp 💚")

#st.info("🛌 Temos opção de adicionar lençol (para se cobrir) + R$ 100,00")
st.success("💳 Pix e dinheiro")

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
        "imagem": "Edredon.jpg.jpeg",
        "tamanho": "Grande",
        "cores": "Rosa com flores",
        "disponivel": True
    },
    {
        "nome": "Manta",
        "preco": 160.00,
        "descricao": "Manta",
        "imagem": "Manta.jpg.jpeg",
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

cols = st.columns(2)

for i, produto in enumerate(produtos):
    with cols[i % 2]:
        with st.container(border=True):
            try:
                st.image(f"imagens/{produto['imagem']}", use_container_width=True)
            except:
                st.warning("Imagem não encontrada")

            st.subheader(produto["nome"])
            st.write(produto["descricao"])

            st.write(f"📏 Tamanho: {produto['tamanho']}")
            st.write(f"🎨 Cor: {produto['cores']}")
            st.markdown(f"### 💰 R$ {produto['preco']:.2f}".replace(".", ","))

            if produto["disponivel"]:
                st.success("✅ Em estoque")

                total = produto["preco"]

                mensagem = f"""Olá! Quero comprar:

Produto: {produto['nome']}
Descrição: {produto['descricao']}
Tamanho: {produto['tamanho']}
Cor: {produto['cores']}
Preço: R$ {produto['preco']:.2f}
Total: R$ {total:.2f}""".replace(".", ",")

                link = f"https://wa.me/{telefone}?text={quote(mensagem)}"

                st.link_button("📲 Pedir no WhatsApp", link)
            else:
                st.error("❌ Indisponível no momento")
                st.button("Indisponível", disabled=True, key=f"ind_{i}")

st.write("---")
st.write("📲 Atendimento direto pelo WhatsApp")
