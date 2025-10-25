# 🚀 Guia de Contribuição e CI/CD

## 📋 Workflow de Desenvolvimento

### 1. Criar uma Feature Branch

```bash
# Atualizar develop
git checkout develop
git pull origin develop

# Criar nova branch
git checkout -b feature/nome-da-feature
```

### 2. Fazer Modificações

Desenvolva sua feature seguindo as boas práticas:

- ✅ Escreva código limpo e documentado
- ✅ Adicione testes se aplicável
- ✅ Siga os padrões de código (PEP 8)
- ✅ Atualize a documentação se necessário

### 3. Verificar Localmente

Antes de fazer commit, execute as verificações:

```bash
# Formatar código
black src/ --line-length 100

# Ordenar imports
isort --profile black src/

# Verificar lint
flake8 src/ --max-line-length=100 --extend-ignore=E203,W503

# Executar testes
pytest tests/ -v
```

### 4. Commit e Push

```bash
# Adicionar arquivos
git add .

# Commit com mensagem descritiva
git commit -m "feat: adiciona nova funcionalidade X"

# Push da branch
git push origin feature/nome-da-feature
```

### 5. Criar Pull Request

1. Acesse o repositório no GitHub
2. Clique em "Pull Request"
3. Selecione `develop` como branch de destino
4. Preencha título e descrição
5. Clique em "Create Pull Request"

**O CI será executado automaticamente! 🎉**

## 🤖 CI/CD - GitHub Actions

### Trigger

O CI é executado automaticamente quando:
- ✅ Um PR é aberto para `develop`
- ✅ Há um push em um PR aberto
- ✅ Um PR é reaberto

### Jobs Executados

#### 1. 🔍 Lint e Validação de Código
- Verifica formatação (Black)
- Verifica ordenação de imports (isort)
- Executa análise estática (Flake8)

#### 2. 🧪 Testes
- Executa suite de testes com pytest
- Valida funcionalidades

#### 3. 📁 Validar Estrutura
- Verifica arquivos essenciais
- Valida estrutura de diretórios
- Garante integridade do projeto

#### 4. 📝 Validar Prompts
- Valida sintaxe YAML
- Verifica campos obrigatórios
- Valida versionamento

#### 5. 📦 Verificar Dependências
- Tenta instalar dependências
- Verifica conflitos
- Escaneia vulnerabilidades (Safety)

#### 6. 📊 Resumo
- Consolida resultados
- Exibe status final

### Status do CI

No Pull Request você verá:

- ✅ **Verde**: Todas as verificações passaram - PR pode ser mergeado
- ❌ **Vermelho**: Verificações falharam - corrija os problemas
- 🟡 **Amarelo**: CI em execução - aguarde

## 🛠️ Ferramentas de Lint

### Instalar ferramentas

```bash
pip install black isort flake8 mypy safety
```

### Black (Formatação)

```bash
# Verificar
black --check src/ --line-length 100

# Corrigir automaticamente
black src/ --line-length 100
```

### isort (Imports)

```bash
# Verificar
isort --check-only --profile black src/

# Corrigir automaticamente
isort --profile black src/
```

### Flake8 (Lint)

```bash
# Executar verificação
flake8 src/ --max-line-length=100 --extend-ignore=E203,W503
```

## 🔧 Pre-commit Hooks

Recomendamos usar pre-commit para executar verificações automaticamente:

```bash
# Instalar pre-commit
pip install pre-commit

# Instalar hooks
pre-commit install

# Executar manualmente
pre-commit run --all-files
```

Os hooks configurados:
- ✅ Black (formatação)
- ✅ isort (imports)
- ✅ Flake8 (lint)
- ✅ Trailing whitespace
- ✅ End of file fixer
- ✅ YAML validation
- ✅ JSON validation
- ✅ Detect private keys

## 📝 Padrões de Commit

Use mensagens de commit descritivas seguindo Conventional Commits:

```bash
# Features
git commit -m "feat: adiciona endpoint de validação"

# Correções
git commit -m "fix: corrige validação de diff vazio"

# Documentação
git commit -m "docs: atualiza README com exemplos"

# Refatoração
git commit -m "refactor: melhora estrutura do agente"

# Testes
git commit -m "test: adiciona testes para API"

# CI/CD
git commit -m "ci: adiciona workflow de deploy"
```

## 🐛 Solução de Problemas no CI

### Erro: "Black formatting check failed"

```bash
# Corrigir localmente
black src/ --line-length 100
git add .
git commit -m "style: aplica formatação black"
git push
```

### Erro: "Imports not sorted"

```bash
# Corrigir localmente
isort --profile black src/
git add .
git commit -m "style: ordena imports"
git push
```

### Erro: "Flake8 issues found"

Leia os erros e corrija manualmente, ou ignore regras específicas no `.flake8`:

```ini
[flake8]
extend-ignore = E203, W503, E501
```

### Erro: "YAML validation failed"

Valide o YAML localmente:

```bash
python -c "import yaml; yaml.safe_load(open('prompts/v1.0.0/prompt.yaml'))"
```

### Erro: "Dependencies installation failed"

Verifique conflitos no `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 📊 Cobertura de Testes

Para gerar relatório de cobertura localmente:

```bash
# Instalar coverage
pip install pytest-cov

# Executar com cobertura
pytest tests/ --cov=src --cov-report=html

# Abrir relatório
open htmlcov/index.html  # Mac
xdg-open htmlcov/index.html  # Linux
```

## 🔒 Secrets no GitHub Actions

Se precisar adicionar secrets (como API keys para testes):

1. Vá em: `Settings > Secrets and variables > Actions`
2. Clique em "New repository secret"
3. Adicione:
   - Nome: `GOOGLE_API_KEY`
   - Valor: sua chave

## 📚 Referências

- [GitHub Actions](https://docs.github.com/en/actions)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Black Code Style](https://black.readthedocs.io/)
- [PEP 8](https://pep8.org/)
- [Pre-commit](https://pre-commit.com/)

## ✅ Checklist antes do PR

- [ ] Código formatado (Black)
- [ ] Imports ordenados (isort)
- [ ] Sem erros de lint (Flake8)
- [ ] Testes passando (pytest)
- [ ] Documentação atualizada
- [ ] Commit messages seguem padrão
- [ ] Branch atualizada com develop
- [ ] Descrição clara no PR

---

**Dúvidas?** Consulte a [documentação completa](README.md) ou abra uma issue! 🚀

