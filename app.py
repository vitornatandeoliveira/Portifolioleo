import streamlit as st

# ====================================
# CONFIGURAÇÃO
# ====================================
st.set_page_config(
    page_title="Estudos de Algoritmos",
    layout="wide",
    page_icon="📘"
)

# CSS atualizada — mais escuro
st.markdown("""
    <style>
    body {
        background-color: #0A0A0A;
    }
    .sidebar .sidebar-content {
        background-color: #0A0A0A !important;
    }
    .main {
        background-color: #101010;
    }
    h1, h2, h3, p, li, label {
        color: #C9C9C9 !important;
    }
    .css-1d391kg, .css-1avcm0n {
        color: #C9C9C9 !important;
    }
    .card {
        padding: 20px;
        background-color: #151515;
        border-radius: 12px;
        box-shadow: 0px 0px 8px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)


# ====================================
# CONTROLE DE NAVEGAÇÃO
# ====================================
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go_to(page):
    st.session_state.page = page


# ====================================
# SIDEBAR
# ====================================
st.sidebar.title("📘 Menu de Conteúdos")
st.sidebar.markdown("---")

menu_items = {
    "Home": "🏠 Início",
    "Decisão e Repetição": "🔁 Decisão e Repetição",
    "Vetores e Matrizes": "📊 Vetores e Matrizes",
    "Funções e Bibliotecas": "📚 Funções e Bibliotecas",
    "Registros": "🗂️ Registros",
    "Arquivos em Disco": "💾 Arquivos em Disco",
    "Recursividade": "🌀 Recursividade",
    "Big O": "📈 Complexidade (Big O)",
    "APIs externas": "🌐 Uso de APIs externas",
}

for key, label in menu_items.items():
    if st.sidebar.button(label, use_container_width=True):
        go_to(key)

st.sidebar.markdown("---")
st.sidebar.write("Feito por Vitor • Portfólio")


# ====================================
# PÁGINAS — CONTEÚDOS COMPLETOS
# ====================================

# ---------- HOME ----------
def home():
    st.title("📘 Plataforma de Estudos – Algoritmos e Programação")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("""
    Este projeto foi desenvolvido em Streamlit para demonstrar domínio em:
    - Algoritmos
    - Análise de Complexidade
    - Estrutura de Dados
    - Recursividade
    - Vetores e Matrizes
    - Manipulação de Arquivos
    - APIs reais

    Explore o menu ao lado e veja exemplos reais + testes interativos.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- DECISÃO E REPETIÇÃO ----------
def decisao():
    st.title("🔁 Estruturas de Decisão e Repetição")
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📌 Estruturas de Decisão (if/elif/else)")
    st.write("""  
    A tomada de decisão permite executar um bloco de código dependendo de uma condição.
    """)

    st.code("""
x = 10

if x > 5:
    print("Maior que 5")
else:
    print("Menor ou igual a 5")
""")

    st.subheader("📌 Estruturas de Repetição (for/while)")
    st.code("""
for i in range(1, 6):
    print("Número:", i)

contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1
""")

    st.subheader("🧪 Teste interativo")
    numero = st.number_input("Digite um número:", value=5)
    if st.button("Testar"):
        st.write(f"O dobro de {numero} é {numero * 2}")

    st.subheader("📝 Exercício")
    st.write("""
    Crie um programa que peça 5 números ao usuário e exiba:
    - A soma total  
    - O maior valor  
    - A média  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- VETORES ----------
def vetores():
    st.title("📊 Vetores e Matrizes")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("Vetores são listas de valores. Matrizes são listas de listas.")

    st.code("""
vetor = [10, 20, 30]

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
""")

    st.subheader("🧪 Teste interativo — Soma de Vetor")
    valores = st.text_input("Digite valores separados por vírgula:", "1,2,3,4")
    if st.button("Somar"):
        lista = [int(x) for x in valores.split(",")]
        st.write("Soma =", sum(lista))

    st.subheader("📝 Exercício")
    st.write("""
    Faça um programa que recebe uma matriz 3x3 e retorna a soma da diagonal principal.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- FUNÇÕES ----------
def funcoes():
    st.title("📚 Funções e Bibliotecas")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.code("""
def soma(a, b):
    return a + b
""")

    st.subheader("🧪 Teste interativo")
    a = st.number_input("A:")
    b = st.number_input("B:")
    if st.button("Somar"):
        st.write("Resultado =", a + b)

    st.subheader("📝 Exercício")
    st.write("Crie uma função que recebe uma lista e retorna o menor número.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- REGISTROS ----------
def registros():
    st.title("🗂️ Registros (Structs)")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("Em Python usamos classes para simular registros.")

    st.code("""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
""")

    st.subheader("🧪 Teste interativo")
    nome = st.text_input("Nome:")
    idade = st.number_input("Idade:", value=18)
    if st.button("Criar Pessoa"):
        st.write(f"Pessoa criada: {nome}, {idade} anos")

    st.subheader("📝 Exercício")
    st.write("Crie um registro que guarda nome, notas e calcula a média automática.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- ARQUIVOS ----------
def arquivos():
    st.title("💾 Arquivos em Disco")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.code("""
with open("dados.txt", "w") as f:
    f.write("Olá mundo!")
""")

    st.subheader("🧪 Teste")
    texto = st.text_input("Texto para salvar:")
    if st.button("Salvar arquivo"):
        with open("saida.txt", "w") as f:
            f.write(texto)
        st.success("Arquivo salvo como 'saida.txt'")

    st.subheader("📝 Exercício")
    st.write("Crie um programa que leia um arquivo e conte quantas linhas ele possui.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- RECURSIVIDADE ----------
def recursividade():
    st.title("🌀 Recursividade")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.code("""
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)
""")

    st.subheader("🧪 Teste")
    n = st.number_input("Calcular fatorial de:", value=5)
    def fatorial(n):
        if n <= 1:
            return 1
        return n * fatorial(n-1)

    if st.button("Calcular"):
        st.write("Resultado =", fatorial(n))

    st.subheader("📝 Exercício")
    st.write("Crie uma função recursiva que soma os números de 1 a N.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- BIG O ----------
def big_o():
    st.title("📈 Complexidade (Big O)")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("""
    Big O mede o quanto um algoritmo cresce conforme o tamanho da entrada aumenta.

    Exemplos:
    - O(1): constante  
    - O(n): linear  
    - O(n²): quadrática  
    - O(log n): logarítmica  
    """)

    st.code("""
# O(n)
for i in range(n):
    print(i)
""")

    st.subheader("📝 Exercício")
    st.write("Classifique a complexidade do algoritmo: dois loops aninhados.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- APIs ----------
def apis():
    st.title("🌐 Uso de APIs Externas")
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.code("""
import requests

r = requests.get("https://api.github.com/users")
print(r.json())
""")

    st.subheader("🧪 Teste API")
    if st.button("Consultar API pública"):
        import requests
        r = requests.get("https://api.agify.io/?name=vitor")
        st.write(r.json())

    st.subheader("📝 Exercício")
    st.write("Crie um programa que consulta uma API de clima e exibe a temperatura atual.")

    st.markdown("</div>", unsafe_allow_html=True)


# ====================================
# ROTEAMENTO
# ====================================
pages = {
    "Home": home,
    "Decisão e Repetição": decisao,
    "Vetores e Matrizes": vetores,
    "Funções e Bibliotecas": funcoes,
    "Registros": registros,
    "Arquivos em Disco": arquivos,
    "Recursividade": recursividade,
    "Big O": big_o,
    "APIs externas": apis
}

pages[st.session_state.page]()
