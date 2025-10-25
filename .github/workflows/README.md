# GitHub Actions Configuration

Este diretório contém os workflows de CI/CD do projeto.

## 📋 Workflows Disponíveis

### `ci-pr-develop.yml`

Workflow de CI executado automaticamente em Pull Requests para a branch `develop`.

**Trigger:**
- Pull Request aberto para `develop`
- Push em PR aberto para `develop`
- PR reaberto

**Jobs:**

1. **🔍 Lint e Validação de Código**
   - Verifica formatação com Black
   - Verifica ordenação de imports com isort
   - Executa Flake8 para verificar qualidade do código

2. **🧪 Testes**
   - Executa testes com pytest
   - Gera relatório de cobertura

3. **📁 Validar Estrutura do Projeto**
   - Verifica se arquivos essenciais existem
   - Valida estrutura de diretórios
   - Garante integridade do projeto

4. **📝 Validar Prompts**
   - Valida sintaxe YAML dos prompts
   - Verifica campos obrigatórios
   - Valida estrutura dos prompts versionados

5. **📦 Verificar Dependências**
   - Tenta instalar todas as dependências
   - Verifica conflitos
   - Escaneia vulnerabilidades conhecidas com Safety

6. **📊 Resumo do CI**
   - Consolida resultados de todos os jobs
   - Exibe status final

## 🚀 Como Usar

### Criando um Pull Request

```bash
# Criar uma nova branch a partir da develop
git checkout develop
git pull origin develop
git checkout -b feature/minha-feature

# Fazer suas modificações
git add .
git commit -m "feat: adiciona nova funcionalidade"

# Push da branch
git push origin feature/minha-feature

# Criar PR no GitHub para develop
# O CI será executado automaticamente
```

### Configurações Locais para Lint

Para verificar o código localmente antes de fazer commit:

```bash
# Instalar ferramentas de lint
pip install black isort flake8 mypy

# Formatar código
black src/ --line-length 100

# Ordenar imports
isort --profile black src/

# Verificar lint
flake8 src/ --max-line-length=100 --extend-ignore=E203,W503
```

### Pre-commit Hook (Recomendado)

Instale pre-commit para executar verificações automaticamente:

```bash
pip install pre-commit

# Criar .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        args: [--line-length=100]

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: [--profile=black]

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=100, --extend-ignore=E203,W503]
EOF

# Instalar hooks
pre-commit install
```

## 📊 Status do CI

O status do CI aparecerá no PR:
- ✅ **Verde**: Todas as verificações passaram
- ❌ **Vermelho**: Uma ou mais verificações falharam
- 🟡 **Amarelo**: CI em execução

## 🔧 Solução de Problemas

### Erro de formatação Black

```bash
# Corrigir automaticamente
black src/ --line-length 100
```

### Erro de imports (isort)

```bash
# Corrigir automaticamente
isort --profile black src/
```

### Erro de lint (Flake8)

Corrija manualmente os problemas apontados ou configure exceções no `.flake8`:

```ini
[flake8]
max-line-length = 100
extend-ignore = E203, W503
exclude = venv/, __pycache__/, .git/
```

### Testes falhando

```bash
# Executar testes localmente
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=src --cov-report=html
```

### Prompts inválidos

Valide o YAML localmente:

```python
import yaml

with open('prompts/v1.0.0/prompt.yaml', 'r') as f:
    data = yaml.safe_load(f)
    print("✅ YAML válido")
```

## 🔒 Secrets Necessários

Caso precise configurar secrets no GitHub Actions:

1. Acesse: `Settings > Secrets and variables > Actions`
2. Adicione secrets necessários:
   - `GOOGLE_API_KEY` (se necessário para testes)

## 📚 Referências

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python in GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

