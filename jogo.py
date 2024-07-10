def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
  
    for linha in tabuleiro:
        if all(s == jogador for s in linha):
            return True


    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True

   
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(all(c != " " for c in linha) for linha in tabuleiro)

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input(f"Jogador {jogador_atual}, digite a linha (0-2): "))
        coluna = int(input(f"Jogador {jogador_atual}, digite a coluna (0-2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Espaço já ocupado. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar()
