import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    """
    Gera uma senha aleatória com base nas opções fornecidas.

    Parâmetros:
        tamanho (int): Comprimento da senha (padrão: 12).
        usar_maiusculas (bool): Incluir letras maiúsculas na senha.
        usar_minusculas (bool): Incluir letras minúsculas na senha.
        usar_numeros (bool): Incluir dígitos de 0 a 9 na senha.
        usar_simbolos (bool): Incluir símbolos (!@#$ etc.) na senha.

    Retorna:
        str: Uma senha aleatória gerada com os critérios escolhidos.
    """
    caracteres = ''

    # Adiciona os tipos de caracteres conforme a escolha do usuário
    if usar_maiusculas:
        caracteres += string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if usar_minusculas:
        caracteres += string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    if usar_numeros:
        caracteres += string.digits           # 0123456789
    if usar_simbolos:
        caracteres += string.punctuation      # !@#$%&*()_+ etc.

    if not caracteres:
        return "Erro: Selecione pelo menos um tipo de caractere."

    # Gera a senha aleatória com os caracteres disponíveis
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    # Interface de terminal simples
    print("=== Gerador de Senhas ===")

    # Coleta de informações do usuário
    tamanho = int(input("Tamanho da senha: "))
    usar_maiusculas = input("Usar letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Usar letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Usar números? (s/n): ").lower() == 's'
    usar_simbolos = input("Usar símbolos? (s/n): ").lower() == 's'

    # Geração da senha com base nas opções do usuário
    senha_gerada = gerar_senha(
        tamanho,
        usar_maiusculas,
        usar_minusculas,
        usar_numeros,
        usar_simbolos
    )

    # Exibição do resultado
    print(f"\nSenha gerada: {senha_gerada}")
