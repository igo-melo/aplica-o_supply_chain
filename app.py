import streamlit as st
import pandas as pd

def check_password():
    """Retorna True se o utilizador e a palavra-passe estiverem corretos."""
    
    def password_entered():
        """Valida as credenciais introduzidas pelo utilizador."""
        user = st.session_state.get("username", "")
        password = st.session_state.get("password", "")
        
        credentials = st.secrets.get("credentials", {})
        
        if user in credentials and password == credentials[user]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.title("🔒 Acesso Restrito - Organização")
    
    st.text_input("Utilizador", key="username")
    st.text_input("Palavra-passe", type="password", key="password")
    st.button("Entrar", on_click=password_entered)

    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Utilizador ou palavra-passe incorretos.")

    return False

# --- CONTEÚDO PRINCIPAL DA APLICAÇÃO ---
if check_password():
    
    # Menu lateral para informações e encerramento de sessão
    with st.sidebar:
        st.write("👤 **Utilizador Autenticado**")
        st.write("Acesso: Nível Geral")
        st.divider()
        if st.button("Sair (Logout)"):
            st.session_state["password_correct"] = False
            st.rerun()

    # Cabeçalho Principal
    st.title("📊 Painel Executivo - Vendas e Estoque")
    st.caption("Acompanhamento de desempenho em tempo real para a organização.")
    
    # ---------------------------------------------------------
    # 1. INDICADORES CHAVE (KPIs)
    # ---------------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Faturamento Total", value="R$ 145.800", delta="+12.5%")
    col2.metric(label="Total de Vendas", value="1.240 un", delta="+4.2%")
    col3.metric(label="Itens em Estoque", value="850 un", delta="-2.1%")
    col4.metric(label="Ticket Médio", value="R$ 117,58", delta="+1.8%")

    st.divider()

    # ---------------------------------------------------------
    # 2. DADOS FICTÍCIOS DE VENDAS E ESTOQUE
    # ---------------------------------------------------------
    dados_vendas = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "Vendas (R$)": [18000, 22000, 21000, 25000, 28000, 31800]
    }).set_index("Mês")

    dados_estoque = pd.DataFrame({
        "Categoria": ["Eletrónicos", "Acessórios", "Vestuário", "Calçados", "Outros"],
        "Quantidade": [250, 400, 120, 50, 30]
    }).set_index("Categoria")

    # ---------------------------------------------------------
    # 3. ORGANIZAÇÃO EM ABAS COM GRÁFICOS E TABELAS
    # ---------------------------------------------------------
    aba_vendas, aba_estoque = st.tabs(["📈 Desempenho de Vendas", "📦 Gestão de Estoque"])

    with aba_vendas:
        st.subheader("Evolução do Faturamento (Últimos 6 meses)")
        st.line_chart(dados_vendas)
        
        st.subheader("Detalhamento do Faturamento Mensal")
        st.dataframe(dados_vendas, use_container_width=True)

    with aba_estoque:
        st.subheader("Nível de Estoque por Categoria")
        st.bar_chart(dados_estoque)
        
        st.subheader("Resumo do Inventário")
        st.dataframe(dados_estoque, use_container_width=True)