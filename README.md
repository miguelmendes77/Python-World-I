# Python World I

Exercícios e anotações dos meus primeiros estudos em Python, organizados por aula. Cada pasta tem o código de explicação da aula (`testN.py`, com comentários) e os desafios práticos (`testN-challengeM.py`).

## Conteúdo

| Pasta | Assunto | Desafios |
|---|---|---|
| `aula-01` | Introdução e o Zen do Python (`import this`) | – |
| `aula-02` | `print`, concatenação, variáveis e `input` | 3 |
| `aula-03` | Tipos de dados e conversão (`int`, `float`, `str`) | 4 |
| `aula-04` | Operadores aritméticos, precedência e `format` | 12 |
| `aula-05` | Módulos: `math`, `random` e `pygame` | 8 |
| `aula-06` | Manipulação de strings (fatiamento, `upper`, `lower`, `replace`, `find`) | 6 |
| `aula-07` | Condições (`if`/`else`) | 10 |
| `aula-08` | Cores no terminal com códigos ANSI | – |

## Como executar

Requer Python 3. Para rodar qualquer exercício:

```bash
python aula-04/test4-challenge1.py
```

O desafio 8 da `aula-05` usa a biblioteca `pygame` para tocar um arquivo de áudio que está na própria pasta. Instale com `pip install pygame` e rode o script de dentro da pasta `aula-05`, pois o caminho do áudio é relativo:

```bash
cd aula-05
python test5-challenge8.py
```
