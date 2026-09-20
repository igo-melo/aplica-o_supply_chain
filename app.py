import streamlit as st

def check_password():
    """Retorna True se o utilizador e a palavra-passe estiverem corretos."""
    
    def password_entered():
        """Valida as credenciais introduzidas pelo utilizador."""
        user = st.session_state.get("username", "")
        password = st.session_state.get("password", "")
        
        # Procura as credenciais definidas no ficheiro secrets.toml
        credentials = st.secrets.get("credentials", {})
        
        if user in credentials and password == credentials[user]:
            st.session_state["password_correct"] = True
            # Limpa as variáveis da memória por motivos de segurança
            del st.session_state["password"]
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # 1. Se o utilizador já estiver autenticado, permite o acesso
    if st.session_state.get("password_correct", False):
        return True

    # 2. Se não estiver autenticado, exibe o ecrã de login
    st.title("🔒 Acesso Restrito - Organização")
    
    st.text_input("Utilizador", key="username")
    st.text_input("Palavra-passe", type="password", key="password")
    st.button("Entrar", on_click=password_entered)

    # Exibe mensagem de erro se a autenticação falhar
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Utilizador ou palavra-passe incorretos.")

    return False

# --- CONTEÚDO PRINCIPAL DA APLICAÇÃO ---
if check_password():
    st.title("📊 Painel Interno da Empresa")
    st.success("Autenticação efetuada com sucesso!")
    st.write("Bem-vindo ao sistema exclusivo da organização.")

    # Botão para terminar a sessão
    if st.button("Sair (Logout)"):
        st.session_state["password_correct"] = False
        st.rerun()
