
# 🤖 Oráculo

Aplicação web feita com [Streamlit](https://streamlit.io/) que oferece login de usuários e navegação personalizada. Ideal para dashboards internos, ferramentas de análise ou sistemas que exigem autenticação.

## 🔧 Funcionalidades

- Menu lateral com boas-vindas personalizadas
- Interface limpa com menus ocultos

## 🚀 Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/oraculo.git
cd oraculo
```

### 2. Instale as dependências

Crie um ambiente virtual e instale os pacotes:

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install streamlit streamlit-authenticator PyYAML streamlit-option-menu
```

### 3. Configure o `config.yaml`

Crie um arquivo `config.yaml` com as credenciais:

```yaml
credentials:
  usernames:
    usuario1:
      name: João da Silva
      password: $2b$12$exemplodesenhaCriptografada

cookie:
  name: oraculo_cookie
  key: segredo_cookie
  expiry_days: 30
```

💡 Para gerar senhas criptografadas:

```python
import streamlit_authenticator as stauth
print(stauth.Hasher(['sua_senha']).generate())
```

### 4. Execute o app

```bash
streamlit run app.py
```

## 📁 Estrutura

```
.
├── app.py                 # Código principal do app
├── config.yaml            # Configurações de autenticação
├── paginas/
│   └── oraculo.py         # Página inicial (módulo principal)
├── requirements.txt       # Dependências (opcional)
└── README.md              # Instruções do projeto
```

## 🛡️ Requisitos

- Python 3.8+
- streamlit
- streamlit-authenticator
- PyYAML
- streamlit-option-menu

---

Desenvolvido com ❤️ usando Streamlit.
