# 🌍 Crescimento Populacional — País A vs País B (Versão Simples)

Mini‑projeto em **Python** para calcular em **quantos anos** a população do **País A** ultrapassa (ou iguala) a do **País B**, considerando **taxas anuais de crescimento** constantes.

Feito para **ensino médio**: linguagem direta e foco em **entrada de dados**, **laços (`while`)**, **aritmética com porcentagem** e **saída formatada**.

---

## 🎯 Objetivo Educacional
- Reforçar o fluxo **entrada → processamento → saída**.
- Praticar conversão para `int`/`float` e porcentagens.
- Usar um **laço `while`** com condição de parada.
- Interpretar resultados e discutir **cenários de crescimento**.

---

## 📝 Enunciado (adaptado ao mundo real)
O Ministério do Planejamento deseja estimar quando o **País A** alcançará o **País B** em população.  
Sabemos que:
- População inicial do **País A**: `80.000` habitantes; **taxa anual**: `3%`
- População inicial do **País B**: `200.000` habitantes; **taxa anual**: `1,5%`

**Tarefa:** Faça um programa que **calcule e escreva** o **número de anos** necessários para que a população do **País A** ultrapasse **ou** iguale a do **País B**, **mantidas as taxas de crescimento**.

> **Versão didática**: o programa também permite **digitar valores** diferentes para simular outros cenários.

---

## 🔎 Exemplo de execução (com os valores do enunciado)
```
=== Crescimento Populacional: País A vs País B ===

Deseja usar os valores padrão do enunciado? (s/n): s

Após 63 anos, A alcança/ultrapassa B.
População final estimada:
- País A: 207,892 habitantes
- País B: 206,312 habitantes
```

> Observação: os números finais são **estimativas** por ano (sem casas decimais nos habitantes).

---

## 💻 Como executar

**Pré‑requisito:** Python **3.8+**

1) Clone este repositório ou baixe os arquivos.
```bash
git clone https://github.com/seu-usuario/projeto-fabrica-5.git
cd projeto-fabrica-5
```

2) No terminal, rode:
```bash
python projeto-fabrica-5.py
```
> **Windows:** se `python` não funcionar, tente `py projeto-fabrica-5.py`.

---

## 🧠 Conceitos trabalhados
- Entrada com `input()` e conversão para `int`/`float`
- Porcentagens e crescimento composto anual
- Estruturas de repetição (`while`)
- Condição de impossibilidade (quando A nunca alcança B)
- Formatação de números

---

## 🚀 Extensões sugeridas
- Mostrar a **evolução ano a ano** (tabela).
- Parar quando a diferença for menor que um **limiar** (ex.: 100 hab.).
- Salvar o histórico em `.csv`.
- Considerar **taxas variáveis** por período.

---

## 📂 Estrutura
```
projeto-fabrica-5/
├─ projeto-fabrica-5.py
└─ README.md
```

---

## 📝 Licença
Este projeto está sob licença **MIT** — use e adapte à vontade. ✨
