# 🎡 Jogo Double (Roleta de Cassino) em PyQt6

Um projeto de simulação do popular jogo de roleta de cassino "Double" (Vermelho, Preto e Branco), desenvolvido em **Python** utilizando a biblioteca **PyQt6** para a interface gráfica (GUI).

Este projeto é uma excelente demonstração de:
* Desenvolvimento de GUI moderna com PyQt6.
* Implementação de animações baseadas em `QTimer`.
* Lógica de gerenciamento de estado (saldo, aposta, histórico).
* Uso do módulo `random` para simulação de probabilidades.

---

## 🎲 Regras e Probabilidades

O jogo baseia-se em três cores com diferentes probabilidades e pagamentos. Seu saldo inicial é de **100 fichas**.

| Cor | Multiplicador | Probabilidade (Peso) | Descrição |
| :---: | :-----------: | :-------------------: | :-------- |
| 🔴 **Vermelho** | **x2** | 48% (9.6/20 slots) | Acertando, o pagamento é de 2x a aposta. |
| ⚫ **Preto** | **x2** | 48% (9.6/20 slots) | Acertando, o pagamento é de 2x a aposta. |
| ⚪ **Branco** | **x14** | 4% (0.8/20 slots) | Resultado de alto risco e alto retorno. Pagamento de 14x a aposta. |

> **Nota:** O código utiliza `random.choices(..., weights=[48, 48, 4])` para simular as probabilidades de forma justa.

---

## 🚀 Como Executar (Passo a Passo)

Para rodar o jogo, você precisa ter o Python 3.x e a biblioteca PyQt6 instalada.

### 1. Clonar o Repositório

```bash
git clone [https://github.com/MATH2211/jogo_cassino.git](https://github.com/MATH2211/jogo_cassino.git)
cd jogo_cassino
2. Configuração do Ambiente
Recomendamos o uso de um ambiente virtual (venv):

Bash

# Cria e ativa o ambiente virtual (Exemplo para PowerShell/Windows)
python -m venv venv
.\venv\Scripts\Activate
3. Instalação de Dependências
Instale a biblioteca PyQt6:

Bash

(venv) PS> pip install PyQt6
4. Iniciar o Jogo
Com o ambiente virtual ativado, execute o arquivo principal:

Bash

(venv) PS> py main.py
🛠 Arquivos do Projeto
Arquivo/Pasta	Descrição
main.py	Contém a classe principal (JanelaPrincipal), toda a lógica do jogo, e o ponto de entrada (if __name__ == '__main__':) para iniciar a aplicação.
venv/	Pasta do ambiente virtual. (Ignorada pelo Git)
__pycache__/	Pasta de cache do Python. (Ignorada pelo Git)
.gitignore	Arquivo que lista pastas e arquivos a serem excluídos do versionamento (ex: venv/).
👤 Autor
[MATH2211] - Desenvolvedor

Conexão
