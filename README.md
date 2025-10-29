# 🤖 Agent Code Reviewer

Agente inteligente de revisão de código com IA, usando LangChain e Google Gemini. Fornece análise rigorosa e detalhada sobre segurança, performance, qualidade, boas práticas e manutenibilidade através de uma API REST.

## 📋 Sobre o Projeto

Este projeto implementa um **Agente Revisor de Código Sênior** com inteligência artificial que realiza análise completa de código em 5 dimensões principais:

### 🔐 1. Segurança
- Vulnerabilidades conhecidas (OWASP Top 10)
- Validação de entrada e sanitização de dados
- Exposição de informações sensíveis
- Autenticação e autorização

### ⚡ 2. Performance
- Complexidade algorítmica
- Uso eficiente de memória
- Identificação de gargalos
- Otimizações recomendadas

### 📝 3. Qualidade do Código
- Legibilidade e clareza
- Aderência aos padrões de código
- Nomenclatura adequada
- Estrutura e organização

### ✅ 4. Boas Práticas
- Princípios SOLID
- Design patterns apropriados
- Tratamento de erros
- Testabilidade

### 🔧 5. Manutenibilidade
- Acoplamento e coesão
- Duplicação de código
- Facilidade de modificação
- Escalabilidade

## 🎯 Características

- ✅ API REST com FastAPI
- ✅ Agente de IA usando LangChain + Google Gemini
- ✅ Prompts gerenciados via LangSmith (pull_prompt)
- ✅ Análise contextual configurável
- ✅ Suporte a múltiplas linguagens
- ✅ Resposta estruturada e detalhada
- ✅ Logs detalhados de processamento

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone <seu-repositorio>
cd ver_prompt_ia_project
```

### 2. Crie um ambiente virtual

```bash
# Criar ambiente virtual na raiz do projeto
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Modelo LLM
LLM_MODEL=gemini-pro
GOOGLE_API_KEY=sua-chave-google-ai-aqui

# LangSmith - Pull do Prompt
LANGSMITH_API_KEY=sua-chave-langsmith-aqui
LANGSMITH_PROMPT_NAME=prompt_padrao_pr_revisor:ce5c6278

# Servidor
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
```

**Como obter a Google API Key:**
1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie uma nova API Key
3. Copie e cole no arquivo `.env`

**Como obter a LangSmith API Key:**
1. Acesse [LangSmith](https://smith.langchain.com/)
2. Crie uma conta ou faça login
3. Vá em Settings > API Keys
4. Crie uma nova API Key
5. Copie e cole no arquivo `.env`

**Configurar o Prompt no LangSmith:**
- O sistema usa `client.pull_prompt()` para buscar o prompt do LangSmith
- Configure o nome do prompt na variável `LANGSMITH_PROMPT_NAME`
- O formato é: `nome_do_prompt:commit_hash` (ex: `prompt_padrao_pr_revisor:ce5c6278`)
- Se não configurado, usa o prompt padrão definido no código

> 📝 Veja mais detalhes em [ENV_CONFIG.md](ENV_CONFIG.md)

## 🎯 Uso

### Iniciando o servidor

```bash
# A partir da raiz do projeto
python -m src.main

# Ou usando uvicorn diretamente
uvicorn src.api.server:app --reload --host 0.0.0.0 --port 8000
```

O servidor estará disponível em: `http://localhost:8000`

### Documentação da API

Acesse a documentação interativa:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📡 API Endpoints

### POST /revisor

Endpoint principal para revisão de código com IA.

**Parâmetros da requisição:**

| Campo | Tipo | Obrigatório | Padrão | Descrição |
|-------|------|-------------|---------|-----------|
| `diff` | string | Sim | - | Diff do código a ser revisado |
| `pr_title` | string | Não | null | Título do Pull Request |
| `pr_description` | string | Não | null | Descrição do PR |
| `language` | string | Não | "Python" | Linguagem de programação |
| `repo_rules` | string | Não | "Seguir boas práticas..." | Regras do repositório |
| `security_level` | string | Não | "high" | Nível de segurança (high/medium/low) |
| `review_focus` | string | Não | "all" | Foco da revisão (all/security/performance/quality) |

**Exemplo com cURL:**

```bash
curl -X POST "http://localhost:8000/revisor" \
  -H "Content-Type: application/json" \
  -d '{
    "diff": "diff --git a/auth.py b/auth.py\nindex abc123..def456\n--- a/auth.py\n+++ b/auth.py\n@@ -5,7 +5,8 @@\n def authenticate(username, password):\n-    query = f\"SELECT * FROM users WHERE username='\''{username}'\'' AND password='\''{password}'\''\"\n+    query = \"SELECT * FROM users WHERE username=? AND password=?\"\n+    result = db.execute(query, (username, hash_password(password)))",
    "pr_title": "Fix SQL Injection vulnerability",
    "language": "Python",
    "security_level": "high",
    "review_focus": "security"
  }'
```

**Exemplo com Python:**

```python
import requests

response = requests.post(
    "http://localhost:8000/revisor",
    json={
        "diff": "diff --git a/file.py...",
        "pr_title": "Refatora autenticação",
        "language": "Python",
        "repo_rules": "Seguir PEP 8 e OWASP Top 10",
        "security_level": "high",
        "review_focus": "all"
    }
)

result = response.json()
print(f"Status: {result['status']}")
print(f"Versão do Prompt: {result['prompt_version']}")
print(f"\n{result['review']}")
```

**Resposta de Sucesso (200 OK):**

```json
{
  "status": "success",
  "message": "Revisão concluída com sucesso",
  "diff_received": true,
  "diff_size": 256,
  "review": "**RESUMO EXECUTIVO:**\n- Avaliação geral: Aprovado com ressalvas\n...\n\n**ISSUES CRÍTICOS:**\n- [CRITICAL] SQL Injection corrigido...",
  "pr_title": "Fix SQL Injection vulnerability",
  "language": "Python",
  "prompt_version": "v1.0.0"
}
```

### GET /health

Health check do serviço.

```bash
curl http://localhost:8000/health
```

**Resposta:**

```json
{
  "status": "healthy",
  "service": "PR Reviewer Agent",
  "version": "1.0.0",
  "prompt_version": "v1.0.0",
  "llm_model": "gemini-pro"
}
```

### GET /

Informações básicas da API e endpoints disponíveis.

## 📁 Estrutura do Projeto

```
ver_prompt_ia_project/
├── venv/                        # Ambiente virtual (não versionar)
├── src/                        # Código fonte
│   ├── __init__.py
│   ├── main.py                 # Script para iniciar servidor
│   ├── agent/                  # Agente de IA
│   │   └── agent_pr_revisor.py # Lógica do agente com LangChain + LangSmith
│   └── api/                    # API REST
│       ├── __init__.py
│       ├── models.py           # Modelos Pydantic
│       └── server.py           # Servidor FastAPI
├── test_api.py                 # Script de teste da API
├── examples_curl.sh            # Exemplos com cURL
├── requirements.txt            # Dependências Python
├── ENV_CONFIG.md              # Documentação das variáveis de ambiente
├── .env                        # Variáveis de ambiente (não versionar)
├── .gitignore
└── README.md                   # Este arquivo
```

## 🔍 Formato da Resposta do Agente

O agente fornece análises estruturadas seguindo o formato:

### RESUMO EXECUTIVO
- Avaliação geral (Aprovado/Aprovado com ressalvas/Requer mudanças)
- Principais pontos de atenção

### ISSUES CRÍTICOS (se houver)
- `[CRITICAL]` Descrição do problema e impacto
- Solução recomendada
- Exemplo de código corrigido

### MELHORIAS RECOMENDADAS
- `[PERFORMANCE]` Sugestões de otimização
- `[SECURITY]` Recomendações de segurança
- `[QUALITY]` Melhorias de qualidade
- `[MAINTAINABILITY]` Sugestões de manutenibilidade

### PONTOS POSITIVOS
- Aspectos bem implementados
- Boas práticas identificadas

### PRÓXIMOS PASSOS
- Lista priorizada de ações recomendadas

## 🎨 Variáveis do Prompt

O prompt suporta as seguintes variáveis de contexto:

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `code_diff` | Diff do código | `diff --git a/...` |
| `language` | Linguagem de programação | `Python`, `JavaScript` |
| `repo_rules` | Regras do repositório | Guidelines, padrões |
| `security_level` | Nível de rigor | `high`, `medium`, `low` |
| `review_focus` | Foco da revisão | `all`, `security`, `performance` |

## 🛠️ Tecnologias

- **Python 3.10+**: Linguagem base
- **FastAPI**: Framework web moderno e rápido
- **Uvicorn**: Servidor ASGI de alta performance
- **LangChain**: Framework para aplicações com LLM
- **LangSmith**: Gerenciamento e versionamento de prompts
- **Google Gemini**: Modelo de IA (via langchain-google-genai)
- **Pydantic**: Validação de dados

## 📦 Gerenciamento de Prompts com LangSmith

Os prompts são gerenciados centralizadamente no **LangSmith** e carregados via `client.pull_prompt()`:

### Como funciona:

1. **Prompts no LangSmith**: Os prompts são criados e versionados no LangSmith Hub
2. **Pull do Prompt**: O sistema faz pull automático do prompt usando o LangSmith Client
3. **Versionamento**: Cada prompt tem um commit hash único (ex: `ce5c6278`)
4. **Configuração**: Define-se o prompt via variável de ambiente `LANGSMITH_PROMPT_NAME`

### Para usar um prompt diferente:

```bash
# Formato: nome_do_prompt:commit_hash
export LANGSMITH_PROMPT_NAME=prompt_padrao_pr_revisor:ce5c6278
python -m src.main
```

### Vantagens:
- ✅ Versionamento centralizado
- ✅ Fácil rollback entre versões
- ✅ Compartilhamento de prompts entre projetos
- ✅ Histórico completo de mudanças
- ✅ Colaboração em equipe

## 🧪 Testes

### Script de teste Python

Execute o script de teste que faz 3 requisições de exemplo:

```bash
python test_api.py
```

### Exemplos com cURL

```bash
# Tornar executável
chmod +x examples_curl.sh

# Ver os exemplos
cat examples_curl.sh
```

## 🔐 Segurança

- Configure `GOOGLE_API_KEY` em um arquivo `.env` (nunca commite chaves no Git)
- Use `security_level=high` para análises críticas
- O agente identifica vulnerabilidades OWASP Top 10
- Certificados SSL customizados podem ser configurados

## 🐛 Troubleshooting

### Erro: Module 'uvicorn' not found

```bash
# Ative o venv e instale as dependências
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: GOOGLE_API_KEY not configured

```bash
# Configure a chave no .env
echo "GOOGLE_API_KEY=sua-chave-aqui" >> .env
```

### Erro: Falha ao carregar prompt do LangSmith

```bash
# Configure a chave do LangSmith no .env
echo "LANGSMITH_API_KEY=sua-chave-aqui" >> .env

# Configure o nome do prompt
echo "LANGSMITH_PROMPT_NAME=prompt_padrao_pr_revisor:ce5c6278" >> .env

# Verifique se o prompt existe no LangSmith Hub
# Acesse: https://smith.langchain.com/
```

## 📝 Logs

O servidor exibe logs detalhados no console:

```
============================================================
📝 Nova requisição de revisão
============================================================
   Título: Fix SQL Injection
   Linguagem: Python
   Tamanho do diff: 256 caracteres
   Nível de segurança: high
   Foco: security
============================================================

🤖 Processando revisão com IA...
✅ Revisão concluída com sucesso!
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 🙋‍♂️ Suporte

Para dúvidas, problemas ou sugestões:
- Consulte a documentação em `/docs`
- Veja exemplos em `test_api.py` e `examples_curl.sh`
- Acesse seus prompts no [LangSmith Hub](https://smith.langchain.com/)
- Verifique as variáveis de ambiente em `ENV_CONFIG.md`

---

**Desenvolvido com ❤️ usando LangChain, LangSmith, Google Gemini e FastAPI**

*Melhore a qualidade e segurança do seu código com análises inteligentes!*
