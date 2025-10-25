from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import Client
import os
import ssl

load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context

# Inicializar LLM
llm = ChatGoogleGenerativeAI(model=os.getenv("LLM_MODEL"), temperature=0.0)


def load_prompt_from_langsmith(prompt_name: str = None) -> PromptTemplate:
    """
    Carrega o prompt do LangSmith usando pull_prompt.
    
    O nome do prompt pode ser fornecido como argumento ou através da 
    variável de ambiente LANGSMITH_PROMPT_NAME.
    Se não definido, usa 'prompt_padrao_pr_revisor' como padrão.
    
    Args:
        prompt_name: Nome do prompt no LangSmith. Se None, usa variável de ambiente.
        
    Returns:
        PromptTemplate carregado do LangSmith
        
    Raises:
        Exception: Se houver erro ao buscar o prompt do LangSmith
    """
    # Obter nome do prompt da variável de ambiente ou usar padrão
    if prompt_name is None:
        prompt_name = os.getenv("LANGSMITH_PROMPT_NAME", "prompt_padrao_pr_revisor:ce5c6278")
    
    try:
        # Inicializar o client do LangSmith
        client = Client()
        
        # Fazer pull do prompt do LangSmith
        prompt = client.pull_prompt(prompt_name)
        
        print(f"✅ Prompt carregado com sucesso do LangSmith!")
        print(f"   Nome: {prompt_name}")
        
        return prompt
        
    except Exception as e:
        raise Exception(
            f"Erro ao carregar prompt do LangSmith: {e}\n"
            f"Prompt solicitado: {prompt_name}\n"
            f"Verifique se o prompt existe no LangSmith e se as credenciais estão configuradas."
        )


# Carregar o prompt do LangSmith
prompt_template = load_prompt_from_langsmith()


def review_code(
    code_diff: str,
    language: str = "Python",
    repo_rules: str = "Seguir boas práticas de código limpo e PEP 8",
    security_level: str = "high",
    review_focus: str = "all"
) -> str:
    """
    Revisa código usando o prompt versionado.
    
    Args:
        code_diff: Diff do código a ser revisado
        language: Linguagem de programação
        repo_rules: Regras específicas do repositório
        security_level: Nível de segurança (high, medium, low)
        review_focus: Foco da revisão (all, security, performance, quality)
        
    Returns:
        Análise completa do código
    """
    # Formatar o prompt com as variáveis
    formatted_prompt = prompt_template.format(
        code_diff=code_diff,
        language=language,
        repo_rules=repo_rules,
        security_level=security_level,
        review_focus=review_focus
    )
    
    # Enviar para o LLM
    response = llm.invoke(formatted_prompt)
    
    return response.content